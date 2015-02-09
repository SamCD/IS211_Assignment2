#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using built-in modules"""

import urllib2
import csv
import datetime
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

LOG_FILENAME = 'errors.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )
logging.getLogger('assignment2')


def downloadData(url):
    """Takes a URL as a string and opens it to retreive data.

    Args: url (string) - the url to be opened

    Ex; downloadData('http://www.myinfo.csv')
    > 
    """
    
    req = urllib2.Request(url)
    return urllib2.urlopen(req)


def processData(data):
    """Executes an operation on data gotten from a url

    Args: url (string) - the url containing the information

    Ex: processData('https://www.myinfo.csv')
       >
    """

    membdays = {}
    for j, i in enumerate(csv.reader(data)):
        try:
            bday = datetime.datetime.strptime(i[2],'%d/%m/%Y')
            membdays[i[0]] = (i[1], bday)
        except:
            logging.debug('Error processing line #{} for ID #{}'.format(j, i[0]))
    return membdays


def displayPerson(id,personData):
    """Displays information about an individual

    Args: id (int) - user ID
          personData (dict) - dictionary containing member info

    Ex: displayPerson(79, processData('http://s3.amazonaws.com/
                                       cuny-is211-spring2015/birthdays100.csv'))
       >'Person #79 is Donna Burgess with a birthday of 08/04/1964'
    """
    ID = str(id)
    if ID not in personData.keys():
        print 'No user found with that id'
    else:
        print 'Person {} is {} with a birthday of {}'.format(
                        id,
                        personData[ID][0],
                        datetime.datetime.strftime(personData[ID][1],
                                                   '%Y-%m-%d'))


def main():
    """Runs when the program is opened"""
    if args is False:
        break
    else:
        try:
            csvData = downloadData(args)
        except URLError:
            print 'Please try a different URL'
            raise
        else:
            personData = processData(csvData)
            ID = int(raw_input("Enter a user ID: "))
            if ID <= 0:
                break
            else:
                displayPerson(ID)
                main()

if __name__ == "__main__":
    main()
