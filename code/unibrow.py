'''
Solution unibrow.py
'''
# It consists of 3 inputs:

# - upload a file in Excel (XLSX), Comma-Separared, with Header (CSV), or Row-Oriented Json (JSON) into a dataframe
# - select which columns to display from the dataframe
# - build a fiter on the dataframe based on a text column and one of the values in the column.

# And 2 outputs:

# - the dataframe with column / row filters applied.
# - the describe of the dataframe (to see statistics for the numerical columns)

import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")



uploaded_file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])
if uploaded_file is not None:
    # Get the file name
    file_name = uploaded_file.name
    st.write(f"You uploaded: {file_name}")
    
    file_type = pl.get_file_extension(file_name)
    df = pl.load_file(uploaded_file, file_type)
    st.dataframe(df)
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to display", cols, default=cols)
    if selected_cols:
        st.dataframe[selected_cols]

