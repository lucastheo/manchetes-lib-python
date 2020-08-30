import requests
import datetime
import json


class Subject:
    @classmethod
    def __init__(self , HEADERS = None):
        self.__subject = ( datetime.datetime.now() , None )
    @classmethod
    def __get_subjects(self):
        if self.__subject[ 1 ] == None or self.__subject[ 0 ] + datetime.timedelta(minutes=5) < datetime.datetime.now():
            var = requests.get(  self.__url_subject() ).text            
            self.__subject = json.loads( var )
        return self.__subject
    @classmethod
    def subject(self):
        return self.__get_subjects()
    @staticmethod
    def __domain():
        return "http://localhost:8080"
        #return "http://54.173.240.207:8080"
    @staticmethod
    def __url_subject():
        return f"{Subject.__domain()}/data/query/subject"