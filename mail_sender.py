import email, smtplib, ssl
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


path = r"***"
subject = "***"
body = "***"
sender_email = "***"
receiver_email = "***"
password = "***"

files = os.listdir(path)
files = [os.path.join(path, file) for file in files]
files = [file for file in files if os.path.isfile(file)]

# Создание составного сообщения и установка заголовка
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Если у вас несколько получателей

# Внесение тела письма
message.attach(MIMEText(body, "plain"))

# можно задать конкретный путь и тогда скрипт будет отправлять все файлы из этой папки:
# filename = 'C://sent/cisco_asw_cable_diagnostic/cisco_asw_cable_diagnostic_log-17-01-2022.txt'
# можно использовать функцию max, возвращающую файл, имеющий самую актуальную дату сохранения:
filename = "{}".format(max(files, key=os.path.getctime))

# Открытие файла в бинарном режиме
with open(filename, "rb") as attachment:
    # Заголовок письма application/octet-stream
    # Почтовый клиент обычно может загрузить это автоматически в виде вложения
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Шифровка файла под ASCII символы для отправки по почте
encoders.encode_base64(part)

# Внесение заголовка в виде пара/ключ к части вложения
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Внесение вложения в сообщение и конвертация сообщения в строку
message.attach(part)
text = message.as_string()

# Подключение к серверу при помощи безопасного контекста и отправка письма
context = ssl._create_unverified_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    print(max(files, key=os.path.getctime))
