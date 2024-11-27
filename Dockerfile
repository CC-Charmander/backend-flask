# ベースイメージの指定 (Python)
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要な依存関係をコピー
COPY requirements.txt /app/

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# Flaskアプリケーションをコピー
COPY . /app/

# ポート番号の指定
EXPOSE 5000

# Flaskアプリケーションの起動
CMD ["python", "app.py"]