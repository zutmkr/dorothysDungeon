# -*- coding: utf-8 -*-
import logging
from time import sleep
from itertools import islice

logging.basicConfig(filename='error_logs/errors.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)


def rysuj_animacja_ciag(adres, s):
    try:
        fp = open(adres, encoding="utf8")
        for i, line in enumerate(fp):
            print(line, end='')
            sleep(s)
        fp.close()
    except Exception as e:
        logger.error(e)             
        fp.close()
      
    
def draw(adres):
    try:
        with open(adres, encoding="utf8") as file:
            print(file.read())  
            file.close() 
    except Exception as e:
        logger.error(e)        
        file.close()    
        
        
def rysuj_oddo(adres,od,do):
    try:
        with open(adres, encoding="utf8") as file:
            lines = islice(file, od, do)
            for line in lines:
                print(line)
            file.close()
    except Exception as e:
        logger.error(e)
        file.close()
            
     
    
