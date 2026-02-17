import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data=pd.read_csv("Amazon Sales data.csv")
data= pd.DataFrame(data= data)

st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

image = Image.open('logo.png')

col1, col2 = st.columns([0.9, 3])

with col1:
    st.markdown("<div style='margin-top:30px;'>", unsafe_allow_html=True)
    st.image("logo.png", width=90)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(
        "<h1 style='margin-top:20px;'>Amazon Sales Dashboard</h1>",
        unsafe_allow_html=True
    )



    
st.markdown("---")   
   
col1,col2,col3,col4 =st.columns(4)

with col1:
    st.subheader("Total Profit")
    profit=data['Total Profit'].sum()
    st.markdown(f"<h3 style='color: red;'>${profit:,.0f}",unsafe_allow_html=True)



with col2:
 st.subheader("Total Sales")
 sale=data['Total Revenue'].sum()
 st.markdown(f"<h3 style='color: red;'>${sale:,.0f}</h3>",unsafe_allow_html=True)

with col3:
 st.subheader("Total Units")
 sold=data['Units Sold'].sum()
 st.markdown(f"<h3 style='color: red;'>${sold:,.0f}</h3>",unsafe_allow_html=True)

with col4:
    st.subheader("Total Cost")
    
    # Calculate the value
    cost = data['Total Cost'].sum()
    
    # Use HTML to style the number
    # f-string: {cost:,.0f} adds commas
    st.markdown(f"<h3 style='color: red;'>${cost:,.0f}</h3>", unsafe_allow_html=True)

st.markdown("---")
# Which regions have the highest total sales revenue?
chart1,chart2=st.columns(2)

higest_sales= data.groupby(data['Region'])['Total Revenue'].sum()
Avg_Price_Cost = (
        data
        .groupby('Item Type')[['Unit Price', 'Unit Cost']]
        .mean()
        .reset_index()
    )
with chart1:

    higest_sales = (
        higest_sales
        .reset_index()
        .sort_values('Total Revenue', ascending=False)
    )
    
    fig, ax = plt.subplots()
    st.subheader("Higest Sales Revenue")
    ax.bar(higest_sales['Region'], higest_sales['Total Revenue'])

    plt.xticks(rotation=45, ha='right')
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

    st.pyplot(fig)

with chart2:
    fig, ax = plt.subplots()
    st.subheader("Average unit price and unit cost for each item type")

    Avg_Price_Cost.set_index('Item Type').plot(
        kind='bar',
        ax=ax
    )

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    st.pyplot(fig)
    
view1, view2=st.columns(2)

with view1:
    with st.expander("Higest Sales"):
        higest_sales=data.groupby(data['Region'])['Total Revenue'].sum()
        st.dataframe(higest_sales)
        csv=higest_sales.to_csv(index=False).encode('utf-8')
        st.download_button(
            'Download Data',
            data=csv,
            file_name='Higest Sales',
            mime='text/csv',
            help="Click here to download data"
        )
    
with view2:
    with st.expander("Average Unit sold and cost"):
        Avg_Price_Cost = (
        data
        .groupby('Item Type')[['Unit Price', 'Unit Cost']]
        .mean()
        .reset_index()
    )
        st.dataframe(Avg_Price_Cost)      
        csv=Avg_Price_Cost.to_csv(index=False).encode('utf-8')
        st.download_button(
            'Download Data',
            data=csv,
            file_name='Avg_Price_Cost',
            mime='text/csv',
            help='click here to download data'
        )  
st.markdown("---")

# Which country has the highest total profit?
col3 = st.columns(1)[0]   # extract the first column

with col3:

    group_data = (
        data.groupby('Country')['Total Profit']
        .sum()
        .sort_values(ascending=False)
    )

    sns.set_style("darkgrid")

    fig, ax = plt.subplots(figsize=(15, 5))

    sns.barplot(
        x=group_data.index,
        y=group_data.values,
        ax=ax
    )

    plt.xticks(rotation=90)

    ax.set_title("Country With Highest Total Profit")
    ax.set_xlabel("Country")
    ax.set_ylabel("Total Profit")

    plt.tight_layout()

    st.pyplot(fig)

st.markdown("---")

# How does the sales channel affect the order priority distribution?
col1,col2=st.columns(2)
data['Order Date'] = pd.to_datetime(
    data['Order Date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)

data['Ship Date'] = pd.to_datetime(
    data['Ship Date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)



with col1:
    table_data = (
        data
        .groupby('Sales Channel')['Order Priority']
        .value_counts()
        .unstack(fill_value=0)
    )

    st.dataframe(table_data, use_container_width=True)
    
st.markdown("---")

# What is the average order processing time (duration between order and ship dates) for each sales channel?

with col2:

    data['Order Date'] = pd.to_datetime(
        data['Order Date'],
        format='mixed',
        dayfirst=True,
        errors='coerce'
    )

    data['Ship Date'] = pd.to_datetime(
        data['Ship Date'],
        format='mixed',
        dayfirst=True,
        errors='coerce'
    )

    data['Processing Time'] = (
        data['Ship Date'] - data['Order Date']
    ).dt.days

    Avg_Processing_Time = (
        data.groupby('Sales Channel')['Processing Time']
        .mean()
        .round(2)
        .reset_index(name='Avg Processing Days')
    )

    st.dataframe(Avg_Processing_Time, use_container_width=True)

st.markdown("---")

# Which item types have the highest and lowest total sales?
chart4=st.columns(1)[0]
group_item_type= data.groupby(data['Item Type'])['Total Revenue'].sum()

highest_sales_revenue_item_type= group_item_type.idxmax()
lowest_sales_revenue_item_type= group_item_type.idxmin()

print("{'Highest Sales Revenue By Item Type':", highest_sales_revenue_item_type, "\n'Lowest Sales Revenue By Item Type':", lowest_sales_revenue_item_type, "}")

with chart4:
    st.subheader("Item types have the higest and lowes sales")
    fig, ax = plt.subplots(figsize=(10, 5))

    # Base scatter
    ax.scatter(
        group_item_type.index,
        group_item_type.values,
        s=200
    )

    # Highlight Max
    max_index = group_item_type.idxmax()
    ax.scatter(
        max_index,
        group_item_type[max_index],
        s=250,
        color='green',
        edgecolor='black',
        label='Max'
    )

    # Highlight Min
    min_index = group_item_type.idxmin()
    ax.scatter(
        min_index,
        group_item_type[min_index],
        s=250,
        color='red',
        edgecolor='black',
        label='Min'
    )

    plt.xticks(rotation=45)
    ax.legend()

    plt.tight_layout()

    st.pyplot(fig)

st.markdown("---")

# How does the order priority vary across different regions?
chart5=st.columns(1)[0]
Diff_regions_by_order_priority= data.groupby(data['Region'])['Order Priority'].value_counts()

with chart5:

    Diff_regions_by_order_priority = (
        data.groupby('Region')['Order Priority']
        .value_counts()
        .reset_index(name='Order Priority Count')
    )
    
    st.subheader("Order priority very across different region")
    fig, ax = plt.subplots(figsize=(10, 5))

    sns.barplot(
        data=Diff_regions_by_order_priority,
        x='Region',
        y='Order Priority Count',
        hue='Order Priority',
        ax=ax
    )

    plt.xticks(rotation=90)

    # Optional custom y ticks (only if small counts)
    ax.set_yticks(np.arange(
        0,
        Diff_regions_by_order_priority['Order Priority Count'].max() + 5,
        5
    ))

    plt.tight_layout()

    st.pyplot(fig)

st.markdown("---")
     
# What is the distribution of unit prices for each item type?
chart6,chart7=st.columns(2)
unit_price_and_item_type_distribution= data.groupby(data['Item Type'])['Unit Price'].sum().reset_index(name= 'Unit Price')

Highest_avg_unit_price_for_sales_channel= data.groupby(data['Sales Channel']) ['Unit Price'].mean().reset_index(name= 'new')


with chart6:
    st.subheader("Distribution of unit prices for each item type")
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        unit_price_and_item_type_distribution['Unit Price'],
        labels=unit_price_and_item_type_distribution['Item Type'],
        autopct='%1.1f%%'
    )

    ax.axis('equal')  # Keep circle shape

    st.pyplot(fig)

# Which sales channel has the highest average unit price?
with chart7:
    st.subheader("Sales channel has the higest average unit price")
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        Highest_avg_unit_price_for_sales_channel['new'],
        labels=Highest_avg_unit_price_for_sales_channel['Sales Channel'],
        autopct='%1.1f%%',
        startangle=90
    )

    ax.axis('equal')  # Keep circle shape

    st.pyplot(fig)

