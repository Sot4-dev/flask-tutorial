# Dockerfile
# ベースイメージとして公式のPythonイメージを使用
FROM python:3.11-slim 
# 環境変数を設定
ENV PYTHONUNBUFFERED 1
#　作業ディレクトリを設定
WORKDIR /app
# 依存ライブラリ定義fileをコンテナにコピー
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# アプリケーションのソースコードをコンテナにコピー
COPY . . 
# ポートを開放
EXPOSE 5000
#コンテナ起動時に実行されるコマンドを指定
CMD ["flask","--app", "flaskr", "run", "--host=0.0.0", "--debug"]
