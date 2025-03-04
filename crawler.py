import requests
import pandas as pd
import time
from datetime import datetime

# === 需填寫的選項 ===
URL_LIST = ["https://luz.tcd.gov.tw/web/default.aspx"]  # 測試網址清單
FREQUENCY = 5  # 請求頻率 (秒)

# 特殊 Header (如需要請填寫)
HEADERS = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

# 設定報告存放路徑（容器內部）
REPORT_PATH = "/app/logs"

def fetch_status(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "content_length": len(response.content)
        }
    except requests.RequestException as e:
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "status_code": "ERROR",
            "error": str(e)
        }

def main():
    start_time = time.time()
    log_data = []

    while time.time() - start_time < 1 * 60:  # 20 分鐘執行時間
        for url in URL_LIST:
            result = fetch_status(url)
            log_data.append(result)
            print(result)  # 即時顯示 Log

        time.sleep(FREQUENCY)  # 控制爬取頻率

    # 產生帶有時間戳記的檔名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"crawler_report_{timestamp}.csv"
    report_filepath = f"{REPORT_PATH}/{report_filename}"

    # 產出報告
    df = pd.DataFrame(log_data)
    df.to_csv(report_filepath, index=False)
    print(f"報告已儲存：/logs/{report_filename}")

if __name__ == "__main__":
    main()
