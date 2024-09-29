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

# TODO Write code here to complete the unibrow.py

