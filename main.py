import streamlit as st


def main():
    st.set_page_config(page_title="top", layout="wide")

    st.markdown(
        """
## 使い方
1. `loader`タブから諸々データをロードする
2. `explorer`タブで、pygwalkerが使えるようになります

## セッションの保存と復帰
1. pygwalkerのCodeExportからJSONを保存します
2. 次回起動時に1.で保存したJSONをloaderでアップロードすると、前回の内容を復元できます（データはJSONに含まれないので、同じものをロードしてください）
        """.strip()
    )


if __name__ == "__main__":
    main()
