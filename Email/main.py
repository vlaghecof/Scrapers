import smtplib, ssl


#
# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "automateemailtestcv@gmail.com"  # Enter your address
# receiver_email = "vladcofaru@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
# message = """\
# Subject: Hi there
#
# This message is sent from Python because im the baus.  \n
#
# Cu drag Vladi :*
# """
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "automateemailtestcv@gmail.com"  # Enter your address
#receiver_email =input("Please imput the sender here ") # "vladcofaru@gmail.com"  # Enter receiver address
receiver_emails ="vladcofaru@gmail.com"  # Enter receiver address
#receiver_emails = ["vladcofaru@yahoo.com","nicolae.cofaru@ulbsibiu.ro","ioana.cofaru@ulbsibiu.ro","ionutcofaru@yahoo.com","gabrielasas2007@yahoo.com"]  # Enter receiver address

#password = input("Type your password and press enter:")
password="cofaru123"
message = MIMEMultipart("alternative")
message["Subject"] = "Situatie azi testam heroku  "
message["From"] = sender_email


# Create the plain-text and HTML version of your message
text = """\
Data de 23-iulie-2020 
Numarul de cazuri de azi: 1112
Numar total  de teste: 1.030.692
Numar de teste azi: 21.419
Total in sibiu:  801
Cazuri sibiu  azi: 9
Procentul Cazurilor confirmate 5.19% 
-----------------------------------------------
Data de 22-iulie-2020 
Numarul de cazuri de azi: 1030 
Numar total  de teste: 1.009.273
Numar de teste azi: 24.877
Total in sibiu:  792 
Cazuri sibiu  azi: 13
Procentul Cazurilor confirmate 4.13% 
-----------------------------------------------
Data de 21-iulie-2020 
Numarul de cazuri de azi: 994 
Numarul total  de cazuri externate: 25586  
Numarul de externari de azi:  373 
Numar total  de teste: 984396
Numar de teste azi: 17204
Total in sibiu:  779 
Cazuri sibiu  azi: 9
Procentul Cazurilor confirmate 5.78% 
-----------------------------------------------


"""
print(text)
# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#     Ce faci  ? Am facut un sender de mail automat , because i can .<br>
#     Voiam sa testez cu tine , uite si o
#     <a href="https://www.youtube.com/watch?v=S68Sc_SoelY">melodie</a>
#     sa nu trimit mailu gol  <br>
# <br>
#     Cu drag Vladut :*
#     </p>
#   </body>
# </html>
# """

# Turn these into plain/html MIMEText objects
text='mesaj de test '
part1 = MIMEText(text, "plain")


# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)


# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    # for receiver in receiver_emails:
    #     # server.sendmail(sender_email, receiver, message.as_string())
    #     pass

    server.sendmail(sender_email, receiver_emails, message.as_string())
