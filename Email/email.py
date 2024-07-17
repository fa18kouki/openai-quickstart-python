# 使用するライブラリ
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime
import time

# .envファイルの読み込み
load_dotenv()

# 環境変数から必要な項目を取得
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')
SUBJECT = os.getenv('SUBJECT')
BODY = os.getenv('BODY')
SEND_INTERVAL = int(os.getenv('SEND_INTERVAL'))  # 送信間隔（秒）

def send_email():
    # メールの設定
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_ADDRESS
    msg['Subject'] = SUBJECT

    # メールの本文
    msg.attach(MIMEText(BODY, 'plain'))

    # GmailのSMTPサーバーに接続
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # TLSで暗号化する
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # ログイン
        server.send_message(msg)  # メールを送信
        print(f"{datetime.now()}: メールを送信しました")

# 定期的にメールを送信するためのループ
while True:
    send_email()  # メールを送信する関数を呼び出す
    time.sleep(SEND_INTERVAL)  # 指定された間隔で待機する

# .envファイルの項目:
# EMAIL_ADDRESS=あなたのメールアドレス
# EMAIL_PASSWORD=あなたのメールパスワード
# RECIPIENT_ADDRESS=受信者のメールアドレス
# SUBJECT=メールの件名
# BODY=メールの本文
# SEND_INTERVAL=送信間隔（秒）
