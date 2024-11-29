import streamlit as st
from modules import get_data

from modules import initialize_state


def main():
    st.set_page_config(page_title="loader", layout="wide")
    initialize_state()

    # データのロード（BigQueryから）
    with st.form("loader"):
        query = st.text_area("クエリ（BigQueryから取得します）")
        file = st.file_uploader("pygwalkerのvisual spec JSON")

        submitted = st.form_submit_button("ロードする")
        if submitted:
            st.session_state.data = get_data(query)
            if file is not None:
                st.session_state.pyg_spec = file.read().decode("utf-8")
            st.write("ロードが完了したので、explorerを利用できます")


if __name__ == "__main__":
    main()
