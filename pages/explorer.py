from pygwalker.api.streamlit import StreamlitRenderer
import streamlit as st

from modules import initialize_state


def main():
    st.set_page_config(page_title="explorer", layout="wide")
    initialize_state()

    # データを読み込めている場合はpygwalkerを起動
    if st.session_state.data is not None:
        explorer = StreamlitRenderer(
            st.session_state.data, spec=st.session_state.pyg_spec
        )
        explorer.explorer()
    else:
        st.write("pygwalkerを起動するにはデータをロードしてください")


if __name__ == "__main__":
    main()
