###########
# This document shows an example of the final app
# that was made from the ground up during
# the workshop
##########
import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_parquet('data.parquet.gzip')

st.title("Water Access Points in Africa")
st.sidebar.title("Sidebar")
st.sidebar.write("")
country = st.sidebar.selectbox("Select the country you wish to analyse:",
                     ["All"] + list(data.country_name.unique()))
if country != "All":
    data = data[data.country_name == country].copy()


st.header("Dataset")
st.write("The data is collected from the Water Point Data Exchange (WPDx). The WPDx is the global platform for sharing water point data. The WPDx Data Standard was designed by a wide range of stakeholders from across sectors and around the world. The core attributes included in the standard are already being collected by governments, researchers, and organizations around the world. Note that only certain columns are included in the dataset here and a sample was taken.")

filter1, _, filter2 = st.columns([4,1,4])
with filter1:
    water_sources = st.multiselect(
         'Filter based on water source',
            data.water_source.unique())
    apply_filter_ws = st.checkbox('Apply water source filter?')
    water_source_filter = data.water_source.apply(lambda x: x in water_sources)
    
with filter2:
    water_techs = st.multiselect(
         'Filter based on water tech',
            data.water_tech.unique())
    apply_filter_wt = st.checkbox('Apply water tech filter?')
    water_tech_filter = data.water_tech.apply(lambda x: x in water_techs)


    
if apply_filter_ws:
    data = data[water_source_filter].copy()
if apply_filter_wt:
    data = data[water_tech_filter].copy()

st.write(data.head(100))

st.header("Overall Visualization")

variable_selected = st.selectbox(
    "Wich variable do you wish to visualize?",
    ("water_source", "water_tech")
)

fig = px.scatter_geo(data,
                    lat='lat_deg',
                    lon='lon_deg',
                    color=variable_selected,
                    opacity=0.5,
                    hover_name="country_name",
                    hover_data=[variable_selected],
                    title="Geographic location of selected Water Access Points",
                    labels={ # replaces default labels by column name
                        "lat_deg": "Latitude",
                        "lon_deg": "Longitude",
                        "water_source": "Water Source",
                        "water_tech": "Water Tech"
                    },
                    template="simple_white",
                    scope="africa",
                    projection="mercator")
st.plotly_chart(fig)

data_counts = data.groupby(variable_selected, as_index=False).agg('count')[['row_id', variable_selected]]
data_counts.sort_values("row_id", inplace=True)
fig = px.bar(data_counts, x="row_id", y=variable_selected, orientation='h',
            title="Number of Water Access Points per {}".format(variable_selected.replace("_", " ")),
            template="simple_white",
            labels={ # replaces default labels by column name
                "row_id": "Number of Water Access Points",
                "water_source": "Water Source",
                "water_tech": "Water Tech"
            })

st.plotly_chart(fig)

data_over_time = data.groupby("install_year", as_index=False).agg("count")[["install_year", "row_id"]]
fig = px.line(data_over_time.tail(25), x="install_year", y="row_id", 
              title='New Water Access Points over time',
              template="simple_white",
              labels={ 
                        "install_year": "Year",
                        "row_id": "Number of Water Access Points installed"
                    },)
st.plotly_chart(fig)