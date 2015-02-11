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


def main():
    """Runs when the program is opened"""

    args = parser.parse_args()
    if args is False:
        SystemExit
    try:
        csvData = downloadData(args)
    except urllib2.URLError:
        print 'Please try a different URL'
        raise
    else:
        LOG_FILENAME = 'errors.log'
        logging.basicConfig(filename=LOG_FILENAME,
                            level=logging.DEBUG,
                            )
        logging.getLogger('assignment2')
        personData = processData(csvData)
        ID = int(raw_input("Enter a user ID: "))
        if ID <= 0:
            raise Exception('Program exited, value <= 0')
        else:
            displayPerson(ID)
            main()

    

def downloadData(url):
    """Takes a URL as a string and opens it to retreive data.

    Args: url (string) - the url to be opened

    Ex; downloadData('http://www.myinfo.csv')
    > 
    """

    return urllib2.urlopen(url)


def processData(data):
    """Executes an operation on data gotten from a url

    Args: url (string) - the url containing the information

    Ex: processData('https://www.myinfo.csv')
       >
    """

    membdays = {}
    for i in csv.reader(data):
        try:
            bday = datetime.datetime.strptime(i[2],'%d/%m/%Y')
            membdays[i[0]] = (i[1], bday)
        except:
            print 'NO'
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

if __name__ == '__main__':
    main()
