import streamlit as st
import pandas as pd

st.title("Data elements")
st.write("This demo app shows the different data elements that are possible.")

data = pd.read_parquet("data.parquet.gzip")

st.caption("st.dataframe()")
st.dataframe(data)

st.caption("st.table()")
st.table(data.sort_values("install_year", ascending=False).head(2))

st.caption("st.metric")
waccp_2020 = data[data.install_year == 2020.0].shape[0]
waccp_2019 = data[data.install_year == 2019.0].shape[0]
st.metric("Number of new Water Access Points", waccp_2020, delta=waccp_2020-waccp_2019)

st.caption("st.json()")
st.json({
    'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
})