import streamlit as st
import pandas as pd
from google.cloud import bigquery


def get_data(query: str) -> pd.DataFrame:
    print("クエリ", query)
    client = bigquery.Client()
    return client.query_and_wait(query).to_dataframe()


def initialize_state():
    # 各データの初期化
    if "data" not in st.session_state:
        st.session_state.data = None
    if "pyg_spec" not in st.session_state:
        st.session_state.pyg_spec = ""
