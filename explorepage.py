import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    df=pd.read_excel('/home/hatta/Dokumen/streamlit/airbnb_ready.xlsx')
    df = df[["neighbourhood_group", "neighbourhood", "minimum_nights", "room_type", "price"]]

    neighbourhood_group_map = shorten_categories(df.neighbourhood_group.value_counts(), 400)
    df['neighbourhood_group'] = df['neighbourhood_group'].map(neighbourhood_group_map)
    df = df[df["price"] <= 250]
    df = df[df["price"] >= 50]
    df = df[df['neighbourhood_group'] != 'Other']
    return df

df = load_data()


def show_explorepage():
    st.title("judul coba")


# >.......................1
    st.write(
        """### Stack Overflow """)

    data = df["neighbourhood_group"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different places""")

    st.pyplot(fig1)


# ......................................2
    
    st.write(
        """
    ####judul tes3
    """
    )

    data = df.groupby(["neighbourhood_group"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)




# ..................................3

    st.write(
        """
    ####judul tes4
    """
    )

    data = df.groupby(["minimum_nights"])["price"].mean().sort_values(ascending=True)
    st.line_chart(data)

# >>>>>>>>>>>>>>4
    # st.write("""
    # ####ggg
    # """
    # )

  

    # fig, ax = plt.subplots(1,1, figsize=(12, 7))
    # df.boxplot('price', 'neighbourhood_group', ax=ax)
    # plt.suptitle('price trend neighbourhood_group')
    # plt.title('')
    # plt.ylabel('price')
    # plt.xticks(rotation=90)
    # plt.show()