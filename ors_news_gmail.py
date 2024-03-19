# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class Gmail:
    def __init__(self):
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_port = 465
        self.smpt = smtplib.SMTP_SSL(self.gmail_smtp, self.gmail_port)
        print(self.smpt)

        self.my_id = "bnkrisk"
        self.my_password = "ayaqddtjfuwprlih"   # wlwnfltmzm1!
        self.smpt.login(self.my_id, self.my_password)

    def sendmail(self, receiver="", sender="", filepath="", filename=""):
        msg = MIMEMultipart()
        msg["Subject"] = f"(금융지주)운영리스크 크롤링 파일 첨부"
        msg["From"] = f"bnkrisk"
        msg["To"] = f"makens@naver.com"

        content = "첨부파일 테스트"
        content_part = MIMEText(content, "plain")
        msg.attach(content_part)

        filepath = os.getcwd() + "/" + "crawling_result/"  # 첨부파일 경로
        filename = "RESULT.xlsx"

        with open(filepath + filename, 'rb') as send_file:
            attachment = MIMEApplication(send_file.read())
            # 첨부파일의 정보를 헤더로 추가
            attachment.add_header('Content-Disposition', 'attachment', filename=filename) # 수신자 메일 표시 파일명
            msg.attach(attachment)


        to_mail = "makens@naver.com"
        self.smpt.sendmail(self.my_id, to_mail, msg.as_string())
        self.smpt.quit()


gmail = Gmail()
gmail.sendmail()
