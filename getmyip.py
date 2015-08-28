__author__ = 'chaoswow'

import ipgetter

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class IPman:
    MYIP = "/home/chaoswow/my_ip"
    # WEBIP = "/home/chaoswow/web_ip"

    def getMyIp(self):
        ip = ipgetter.myip()
        print(ip)
        return ip

    def readMyFile(self, path):
        try:
            with open(path, 'r') as f:
                r = f.read()
                print(r)
                return r
        except IOError as err:
            print("Erreur de type Input/Output dans la methode readMyFile \n", err)

    def writeMyFile(self, path, webip):
        try:
            with open(path, 'w') as f:
                f.write(webip)
        except IOError:
            print("Erreur de type Input/Output dans la methode writeMyFile")

    def sendMail(self, newIP):
        fromaddr = "EMAIL OF EXPEDITOR"
        toaddr = "DESTINATION EMAIL"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "IP address has been changed"

        partialbody = "Mail automatique : \n"
        body = partialbody + newIP
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "YOUR PASSWORD")
        text = msg.as_string()
        try:
            server.sendmail(fromaddr, toaddr, text)
        except smtplib.SMTPException as err:
            print(err)
        except:
            print("Erreur d'envoi")

        server.quit()


webIp = IPman().getMyIp()  # Get IP from web
r = IPman().readMyFile(IPman.MYIP)  # Read IP in file

""" On compare l'adresse ip obtenue et celle qu'on a inscrit """
if r == webIp:
    print("No diff")
if r != webIp:
    print("There are diff !  /!\\")
    IPman().sendMail(webIp)
    IPman().writeMyFile(IPman.MYIP, webIp)
#print(type(r))



# IPman().writeMyFile(IPman.MYIP, webIp)
