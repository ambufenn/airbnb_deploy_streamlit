# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import requests
# import io
# import seaborn as sns
# import folium


# def shorten_categories(categories, cutoff):
#     categorical_map = {}
#     for i in range(len(categories)):
#         if categories.values[i] >= cutoff:
#             categorical_map[categories.index[i]] = categories.index[i]
#         else:
#             categorical_map[categories.index[i]] = 'Other'
#     return categorical_map

# @st.cache
# def load_data():
#     url = 'https://github.com/ambufenn/airbnb_deploy_streamlit/raw/c5f2fc89bc601ae64acbc3aa9f214454a27ad4a2/airbnb_ready.xlsx'
#     r = requests.get(url)
#     df = pd.read_excel(io.BytesIO(r.content))
#     df = df[["neighbourhood_group", "neighbourhood", "minimum_nights", "room_type", "price"]]

#     neighbourhood_group_map = shorten_categories(df.neighbourhood_group.value_counts(), 400)
#     df['neighbourhood_group'] = df['neighbourhood_group'].map(neighbourhood_group_map)
#     df = df[df["price"] <= 250]
#     df = df[df["price"] >= 50]
#     df = df[df['neighbourhood_group'] != 'Other']
#     return df

# df = load_data()


# def show_explorepage():
#     st.title("judul coba")


# # >.......................1
#     st.write(
#         """### Stack Overflow """)

#     data = df["neighbourhood_group"].value_counts()

#     fig1, ax1 = plt.subplots()
#     ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
#     ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

#     st.write("""#### Number of Data from different places""")

#     st.pyplot(fig1)


# # ......................................2
    
#     st.write(
#         """
#     ####judul tes3
#     """
#     )

#     data = df.groupby(["neighbourhood_group"])["price"].mean().sort_values(ascending=True)
#     st.bar_chart(data)




# # ..................................3

#     st.write(
#         """
#     ####judul tes4
#     """
#     )

#     data = df.groupby(["minimum_nights"])["price"].mean().sort_values(ascending=True)
#     st.line_chart(data)

# # >>>>>>>>>>>>>>4
#     st.write(
#     """
#     #### Price Trend by Neighbourhood Group
#         """
#     )

#     # menentukan rentang harga
#     bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

#     # menghitung jumlah listing pada setiap rentang harga
#     hist = pd.cut(df['price'], bins=bins).value_counts(sort=False)

#     # membuat diagram distribusi harga
#     plt.bar(hist.index.astype(str), hist.values)
#     plt.xticks(rotation=45)
#     plt.xlabel('Rentang Harga (SGD)')
#     plt.ylabel('Jumlah Listing')
#     plt.title('Distribusi Harga Listing Airbnb di Singapura')
#     plt.show()











# # ...........................
#     st.write(
#     """
#     #### Price Trend by Neighbourhood Group
#         """
#     )

#     fig, ax = plt.subplots(1, 1, figsize=(12, 7))
#     df.boxplot('price', 'neighbourhood_group', ax=ax)
#     ax.set_title('Price Trend by Neighbourhood Group')
#     ax.set_xlabel('Neighbourhood Group')
#     ax.set_ylabel('Price')
#     plt.xticks(rotation=90)
#     st.pyplot(fig)
# # ...................













import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
import seaborn as sns
import folium
from sklearn import linear_model
import plotly.graph_objects as go


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


@st.cache
def load_data():
    url = 'https://github.com/ambufenn/airbnb_deploy_streamlit/raw/c5f2fc89bc601ae64acbc3aa9f214454a27ad4a2/airbnb_ready.xlsx'
    r = requests.get(url)
    df = pd.read_excel(io.BytesIO(r.content))
    df = df[["neighbourhood_group", "neighbourhood", "minimum_nights", "room_type", "price"]]

    neighbourhood_group_map = shorten_categories(df.neighbourhood_group.value_counts(), 400)
    df['neighbourhood_group'] = df['neighbourhood_group'].map(neighbourhood_group_map)
    df = df[df["price"] <= 250]
    df = df[df["price"] >= 50]
    df = df[df['neighbourhood_group'] != 'Other']
    return df


df = load_data()


def show_explorepage():
    st.title("Airbnb Analytics Exploration")

    # 1
    st.write(
        """### """)
    data = df["neighbourhood_group"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.write("""#### Airbnb distribution in Singapore region""")
    st.pyplot(fig1)

    # 2
    st.write('\n\n')
    st.write('\n\n')
    st.write("""#### Airbnb Price Distribution in Singapore region""")
    data = df.groupby(["neighbourhood_group"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)




    # st.write('\n\n')
    # st.write('\n\n')
    # st.write("""#### Airbnb price distribution by city""")
    # fig, ax = plt.subplots()
    # sns.set(style="whitegrid")
    # sns.boxplot(x="neighbourhood_group", y="price", data=df, ax=ax)
    # ax.set_xlabel("Neighbourhood Group")
    # ax.set_ylabel("Price")
    # ax.set_title("Price Trend by Neighbourhood Group")
    # plt.xticks(rotation=90)
    # st.pyplot(fig)

        # Add some space
    st.write('\n\n')

    # Add a title
    # st.write("""#### Airbnb price distribution by city""")

    # Create a scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x="price", y="neighbourhood_group", data=df, ax=ax)
    ax.set_xlabel("Price")
    ax.set_ylabel("Neighbourhood Group")
    ax.set_title("Price Distribution by Neighbourhood Group")

    # Show the plot in Streamlit
    st.pyplot(fig)

    # 3
    st.write('\n\n')
    st.write('\n\n')
    st.write("""#### Price correlation with minimum lease term requirements""")
    data = df.groupby(["minimum_nights"])["price"].mean().sort_values(ascending=True)
    st.line_chart(data)

    # 4
    st.write('\n\n')
    st.write('\n\n')
    st.write("""#### Price distribution based on rental amount""")
    # menentukan rentang harga
    bins = [0, 50, 
            100, 150, 200, 250, 300, 350, 400, 450, 500]

    # menghitung jumlah listing pada setiap rentang harga
    hist = pd.cut(df['price'], bins=bins).value_counts(sort=False)

    # membuat diagram distribusi harga
    fig, ax = plt.subplots()
    ax.bar(hist.index.astype(str), hist.values)
    ax.set_xticklabels(hist.index.astype(str), rotation=45)
    ax.set_xlabel('Price Range (SGD)')
    ax.set_ylabel('Listing Number')
    ax.set_title('Price distribution based on rental amount')
    st.pyplot(fig)

    st.write('\n\n')
    # st.write("""#### Price distribution based on rental amount""")

    # menentukan rentang harga
    bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

    # menghitung jumlah listing pada setiap rentang harga
    hist = pd.cut(df['price'], bins=bins).value_counts(sort=False)

    # membuat diagram distribusi harga
    fig = go.Figure(go.Funnel(
        y=hist.index.astype(str),
        x=hist.values,
        textinfo="value+percent previous",
        textposition='inside'
    ))
    fig.update_layout(
        title="Price distribution based on rental amount",
        xaxis_title="Listing Number",
        yaxis_title="Price Range (SGD)"
    )

    st.plotly_chart(fig)
        





    # 5
    st.write('\n\n')
    st.write('\n\n')
    st.write("""#### Pricing trends by room type""")
    fig, ax = plt.subplots()
    sns.boxplot(x="room_type", y="price", data=df, ax=ax)
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Price")
    st.pyplot(fig)
   
  

    # st.write(
    # """
    # #### 6.Price Trend by Neighbourhood Group
    # """
    # )
    # sns.set(style="whitegrid")
    # plt.figure(figsize=(15, 7))
    # sns.boxplot(x="room_type", y="price", data=df)
    # plt.xticks(rotation=90)
    # plt.title("Trend Harga pada Neighborhood")
    # plt.xlabel("Neighborhood")
    # plt.ylabel("Harga")
    # st.pyplot()

   


















    # st.write(
    #     """
    #     #### 7 Price Trend by Neighbourhood Group
    #     """
    # )

    # fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    # df.boxplot('price', 'neighbourhood_group', ax=ax)
    # ax.set_title('Price Trend by Neighbourhood Group')
    # ax.set_xlabel('Neighbourhood Group')
    # ax.set_ylabel('Price')
    # plt.xticks(rotation=90)
    # st.pyplot(fig)



    st.write('\n\n')
    st.write(""" Kekurangan dari explore page ini:  """)
    st.markdown("map tidak muncul karena heavy loading, pemilihan jenis grafix mungkin belum sesuai penggunaanya, juga masih banyak grafix yang bisa di masukan ke page ini")
    st.write('\n\n')
    st.write("""created by fenira for dqlab""")
