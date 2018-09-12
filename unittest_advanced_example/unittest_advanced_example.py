import datetime
import time

class SendMailClass():

    def send_mail(self, message):
        print ("Conectando con servidor...")
        time.sleep(5)
        print("Esto debería mandar realmente un mail -> " + message)



class LogicClass():

    def __init__(self, send_mail_service):
        self.bussiness_done = False
        self.mail_service = send_mail_service

    def is_business_done(self):
        return self.bussiness_done

    def make_some_bussiness(self):
        self.__make_the_bussiness()
        self.mail_service.send_mail("Negocio hecho el día " + str(datetime.date.today()))

    def __make_the_bussiness(self):
        self.bussiness_done = True


if __name__ == '__main__':
    mail_service = SendMailClass()
    logicObject = LogicClass(mail_service)
    logicObject.make_some_bussiness()


