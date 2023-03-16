import streamlit as st
import pickle
import numpy as np
import requests
import io



@st.cache(allow_output_mutation=True)
def load_model():
    url = 'https://github.com/ambufenn/airbnb_deploy_streamlit/raw/c5f2fc89bc601ae64acbc3aa9f214454a27ad4a2/saved_steps.pkl'
    r = requests.get(url)
    data = pickle.load(io.BytesIO(r.content))
    return data

data = load_model()

regressor = data["model"]
le_place_group = data["le_place_group"]
le_place = data["le_place"]


def show_predpage():
    st.title("judul 1")

    st.write("""### judul2""")

    States = (
       "North Region", "Central Region", "West Region", "East Region", "North-East Region"
    )

    Town = (
        'Tampines', 'Novena', 'Pasir Ris', 'Kallang', 'Outram', 'Hougang',
       'Serangoon', 'Toa Payoh', 'Woodlands', 'Queenstown', 'Geylang',
       'Jurong East', 'Bedok', 'Downtown Core', 'Jurong West', 'Punggol',
       'Tanglin', 'Newton', 'River Valley', 'Museum', 'Clementi',
       'Marine Parade', 'Sembawang', 'Western Water Catchment', 'Rochor',
       'Bukit Timah', 'Singapore River', 'Yishun', 'Bukit Batok',
       'Lim Chu Kang', 'Bukit Merah', 'Sungei Kadut', 'Bishan',
       'Sengkang', 'Choa Chu Kang', 'Bukit Panjang',
    )

    place_group = st.selectbox("le_place_group", States)
    place = st.selectbox("le_place", Town)

    harga_pred = st.slider("kategori_tes", 0, 550, 3)

    ok = st.button("kategori_price")
    if ok:
        x = np.array([[place_group, place, harga_pred ]])
        x[:, 0] = le_place_group.transform(x[:,0])
        x[:, 1] = le_place.transform(x[:,1])
        x = x.astype(float)

        price = regressor.predict(x)
        st.subheader(f"The estimated price is ${price[0]:.2f}")
