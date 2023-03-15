import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache(persist=True)
def load_airbnb_data():
    return pd.read_excel('/home/hatta/Dokumen/streamlit/airbnb_ready.xlsx')

@st.cache(persist=True)
def load_geojson():
    with open("/home/hatta/Dokumen/streamlit/singapore_geojson.json") as f:
        return json.load(f)

def show_Notes():
    st.title("Notes")
    st.write("This is the Notes page.")

    # Load Airbnb data (example data)
    airbnb_data = load_airbnb_data()

    # Load Singapore GeoJSON
    sg_geojson = load_geojson()

    # Create a choropleth map of Airbnb listings in Singapore
    fig = px.choropleth_mapbox(
        airbnb_data,
        geojson=sg_geojson,
        locations='neighbourhood',
        color='price',
        color_continuous_scale="Viridis",
        range_color=(0, 500),
        mapbox_style='carto-positron',
        zoom=11,
        center={'lat': 1.3521, 'lon': 103.8198},
        opacity=0.5
    )

    # Show the map
    st.plotly_chart(fig)
