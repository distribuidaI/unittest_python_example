import datetime
import time
import random

class SendMailClass():

    def send_mail(self, message):
        print ("Conectando con servidor...")
        time.sleep(5)
        print("Esto debería mandar realmente un mail -> " + message)



class OneService():

    def __init__(self, send_mail_service):
        self.bussiness_done = False
        self.mail_service = send_mail_service

    def make_things_and_get_result(self):

        self.mail_service.send_mail("1er servicio")

    def __make_real_things(self):
        return random.randrange(0, 1000)


class AnotherMoreComplexService():

    def __init__(self, mail_service, one_service):
        self.mail_service = mail_service
        self.first_service = one_service

    def make_complex_bussiness(self):
        number = self.first_service.make_things_and_get_result()
        self.__make_real_magic(number)
        self.mail_service.send_mail("2do servicio")

    def __make_real_magic(self, number):
        self.magical_number = number * 2

    def get_magical_number(self):
        return self.magical_number





