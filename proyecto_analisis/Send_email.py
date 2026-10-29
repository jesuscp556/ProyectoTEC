import smtplib

content="Prueba en clase \n"
datos = ["Christian","18"]
content = content + str(datos)

mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='ps6005.tec@gmail.com'
recipient='greudazifreppau-7148@yopmail.com'
mail.login('ps6005.tec@gmail.com','erdl efrz ktcx vjtm')

header='To:'+recipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()