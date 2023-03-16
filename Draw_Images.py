# -*- coding: utf-8 -*-
import logging
from time import sleep
from itertools import islice

logging.basicConfig(filename='error_logs/errors.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)


def rysuj_animacja_ciag(adres, s):
    """
    Displays an animation from a file, with a delay of s seconds between each line.
    
    Args:
        adres (str): The file path of the animation file.
        s (float): The delay in seconds between each line.
    """
    try:
        with open(adres, encoding="utf8") as file:
            for i, line in enumerate(file):
                print(line, end='')
                sleep(s)
            file.close()
    except Exception as e:
        logger.error(e)
        file.close()


def draw(adres):
    """
    Displays the contents of a file.
    
    Args:
        adres (str): The file path of the file to be displayed.
    """
    try:
        with open(adres, encoding="utf8") as file:
            print(file.read())
            file.close()
    except Exception as e:
        logger.error(e)
        file.close()  
        
        
def rysuj_oddo(adres: str, od: int, do: int) -> None:
    """
    Reads a text file from the given address and prints its lines from the specified start position (od)
    to the end position (do).

    Args:
        adres (str): The file path of the text file to be read.
        od (int): The starting line position to be read from.
        do (int): The ending line position to be read until.

    Returns:
        None
    """

    with open(adres, encoding="utf8") as file:
        try:
            # read only the specified range of lines from the file
            lines = islice(file, od, do)
            for line in lines:
                print(line)
            file.close()
        except Exception as e:
            logger.error(e)
            file.close()
            
     
    
