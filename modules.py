import streamlit as st
import polars as pl
from google.cloud import bigquery


def get_data(query: str) -> pl.DataFrame:
    print("クエリ", query)
    client = bigquery.Client()
    return pl.from_arrow(client.query_and_wait(query).to_arrow())


def initialize_state():
    # 各データの初期化
    if "data" not in st.session_state:
        st.session_state.data = None
    if "pyg_spec" not in st.session_state:
        st.session_state.pyg_spec = ""
