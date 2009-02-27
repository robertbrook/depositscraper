#!/usr/bin/python
import pprint
import re
import unittest
import csv

class Deposit:
  def __init__(self, aTuple):
    self.number = aTuple[0][0]
    self.legislature = aTuple[0][1]
    self.date_deposited = aTuple[0][2]
    self.department = aTuple[0][3]
    self.text = aTuple[1]
    self.download_link = aTuple[0][4]
    self.download_text = aTuple[0][5]
    self.associated_legislation = aTuple[2]

re_details = re.compile(' valign="top"><td bgcolor="#e3e3e3"><b>(.*)</b></td><td bgcolor="#e3e3e3"><b>(.*)</b></td><td bgcolor="#e3e3e3"><b>(.*)</b></td><td colspan="1" bgcolor="#e3e3e3" width="45%">(.*)</td><td bgcolor="#e3e3e3" width="25%" align="right"><A HREF="(.*)">(.*)</A></td></tr>')
re_text = re.compile('<td colspan="2">(.*)</td>')
re_associated_legislation = re.compile('><td colspan="3" /><td><i>(.*)</i></td></tr>')

deposits_html = open("deposits.html","r")
csv_writer = csv.writer(open('deposits.csv', 'w'), quoting=csv.QUOTE_ALL)

for line in deposits_html:
    if line.startswith("<?xml"):
            e3e3e3 = line.split('<tr')
            del e3e3e3[0:5]
            for i in xrange(0, len(e3e3e3), 4):
                details = re_details.findall(e3e3e3[i])[0]
                deposit_number = details[0]
                deposit_legislature = details[1]
                deposit_date = details[2]
                deposit_source = details[3]
                deposit_link = details[4]
                deposit_file = details[5]
                text = re_text.findall(e3e3e3[i+1])[0]
                associated_legislation = re_associated_legislation.findall(e3e3e3[i+2])[0]
                csv_writer.writerow([deposit_number, deposit_legislature, deposit_date, deposit_source, deposit_link, deposit_file, text, associated_legislation])



            
