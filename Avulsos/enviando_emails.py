import smtplib
# fonte: Insta led.ufba
email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()

remetente = "Email do Remetente"
senha = "Senha do email do remetente"
destinatario = "email do destinatário"

mensagem = "Siga o LED no Instagram!".encode('utf-8')

email.login(remetente, senha)
email.sendmail(remetente, destinatario, mensagem)
email.quit()