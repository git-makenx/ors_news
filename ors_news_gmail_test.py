# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


gmail_smtp = "smtp.gmail.com"
gmail_port = 465
smpt = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
print(smpt)

my_id = "bnkrisk"
my_password = "ayaqddtjfuwprlih"
smpt.login(my_id,my_password)

msg = MIMEMultipart()
msg["Subject"] = f"요청하신 데이터를 전달드립니다."
msg["From"] = f"bnkrisk"
msg["To"] = f"makens@naver.com"

content = "첨부파일 테스트"
content_part = MIMEText(content, "plain")
msg.attach(content_part)


RESULT_PATH = os.getcwd() + "/" + "crawling_result/"  #결과 저장할 경로
file_name = RESULT_PATH + "RESULT_20240308_071450_BNK.xlsx"

with open(file_name, 'rb') as result_file :
    attachment = MIMEApplication(result_file.read())
    #첨부파일의 정보를 헤더로 추가
    attachment.add_header('Content-Disposition','attachment', filename = "RESULT_20240308_071450_BNK.xlsx")
    msg.attach(attachment)



to_mail ="makens@naver.com"
smpt.sendmail(my_id,to_mail,msg.as_string())
smpt.quit()

