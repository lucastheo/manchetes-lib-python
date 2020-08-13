import requests
import datetime
import json


class MostCited:
    @classmethod
    def __init__(self , HEADERS = None):
        self.__keys = ( datetime.datetime.now() , None )
        if HEADERS != None: self.HEADERS = HEADERS
        else:               self.HEADERS = { "user-email":"lucastheo.g.a@gmail.com"}
    @classmethod
    def __get_keys(self):
        if self.__keys[ 1 ] == None or self.__keys[ 0 ] + datetime.timedelta(minutes=5) < datetime.datetime.now():
            var = requests.get(  self.__url_key() , headers= self.HEADERS  ).text            
            self.__keys = json.loads( var )
        return self.__keys
    @classmethod
    def keys_tuples( self ):
        out = list()
        keys = self.__get_keys()
        for url in keys:
            for date in keys[url]:
                out.append( ( url , date ) )
        return out
                
    @classmethod
    def keys(self):
        return self.__get_keys()
    @classmethod
    def find( self, url = None , date = None ):
        if url != None and date != None:
            api_url = self.__url_find_by_url_by_date( url, date )
        elif url == None and date == None:
            api_url = self.__url_find()
        elif url != None: 
            api_url = self.__url_find_by_url( url )
        else:
            api_url =self.__url_find_by_date( date )
        var = requests.get(  api_url , headers= self.HEADERS  ).text
        return json.loads( var )
    @staticmethod
    def __domain():
        return "http://54.173.240.207:8080"
    @staticmethod
    def __url_key():
        return f"{MostCited.__domain()}/data/query/most_cited_keys?data=True&url=True"
    @staticmethod
    def __url_find():
        return f"{MostCited.__domain()}/data/query/most_cited_by"
    @staticmethod
    def __url_find_by_url( url:str):
        return f"{MostCited.__domain()}/data/query/most_cited_by?url=__url__".replace('__url__' , url ) 
    @staticmethod
    def __url_find_by_date( date:str ):
        return f"{MostCited.__domain()}/data/query/most_cited_by?data=__date__".replace('__date__' , date )
    @staticmethod
    def __url_find_by_url_by_date( url:str , date:str ):
        return f"{MostCited.__domain()}/data/query/most_cited_by?data=__date__&url=__url__".replace('__url__' , url ).replace('__date__' , date ) 