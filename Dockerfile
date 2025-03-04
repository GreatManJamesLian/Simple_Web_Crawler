# 使用 Python 官方基礎映像
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 複製當前目錄內的所有檔案到容器
COPY . /app

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 執行 Python 爬蟲腳本
CMD ["python", "crawler.py"]
