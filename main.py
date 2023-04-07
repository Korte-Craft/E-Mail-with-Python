import smtplib

# Bejelentkezés az e-mail fiókunkba
email_address = input("YOU E-MAIL ADRESS: ")
password = input("YOUR PASSWORD: ")
smtp_server = input("SMTP SERVER: ")
smtp_port = input("SMTP PORT: ")  # SMTP szerver portja (általában 587)

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_address, password)

# Elküldjük az e-mailt
from_email = email_address
to_email = input("TO: ")
subject = input("SUBJECT: ")
body = input("BODY: ")

message = f"Subject: {subject}\n\n{body}"

server.sendmail(from_email, to_email, message)

# Bezárjuk a kapcsolatot
server.quit()
