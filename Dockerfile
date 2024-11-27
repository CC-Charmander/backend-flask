# ベースイメージの指定 (Python)
FROM public.ecr.aws/lambda/python:3.9

# 必要な依存関係をコピー
COPY requirements.txt /var/task/

# 依存関係のインストール
RUN pip install --no-cache-dir -r /var/task/requirements.txt -t /var/task/

# Flaskアプリケーションをコピー
COPY . /var/task/

# ポート番号の指定
EXPOSE 8000

# Flaskアプリケーションの起動
CMD ["lambda_handler.lambda_handler"]