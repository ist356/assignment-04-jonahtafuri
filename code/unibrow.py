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
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to display", cols, default=cols)
    final_df = df[selected_cols]
    if st.toggle("Filter data"):
        stcols = st.columns(3)
        
        text_cols = pl.get_columns_of_type(df, 'object')
        filter_col = stcols[0].selectbox("Get values of: ", text_cols)
        if filter_col:
            vals = pl.get_unique_values(df, filter_col)
            val = stcols[1].selectbox("Select value to filter: ", vals)
            final_df = df[df[filter_col] == val][selected_cols]
        else:
            final_df = df[selected_cols]
    st.dataframe(final_df)
    st.dataframe(final_df.describe())

