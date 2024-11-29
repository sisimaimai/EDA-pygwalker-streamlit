# EDA-pygwalker-streamlit

BigQueryからデータを取得してpygwalkerでごにょごにょできるEDAツール的なもの

## usage

1. gcloudのADCを取得します
    ```sh
    gcloud auth application-default login
    ```

2. venvなりで環境構築して起動します
    ```sh
    # よしなにvenvなりを切る
    python -m venv .venv
    source .venv/bin/activate.sh

    # ライブラリ周りのインストール
    pip install -r requirements.txt

    # 起動
    streamlit run main.py
    ```
