#!/usr/bin/python
import pprint
import re

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


valign = re.compile(' valign="top"><td bgcolor="#e3e3e3"><b>(.*)</b></td><td bgcolor="#e3e3e3"><b>(.*)</b></td><td bgcolor="#e3e3e3"><b>(.*)</b></td><td colspan="1" bgcolor="#e3e3e3" width="45%">(.*)</td><td bgcolor="#e3e3e3" width="25%" align="right"><A HREF="(.*)">(.*)</A></td></tr>')
td_colspan = re.compile('<td colspan="2">(.*)</td>')
td_i = re.compile('><td colspan="3" /><td><i>(.*)</i></td></tr>')

deposits_html = open("deposits.html","r")

for line in deposits_html:
    if line.startswith("<?xml"):
            e3e3e3 = line.split('<tr')
            del e3e3e3[0:5]
            list_of_lists = []
            for i in xrange(0, len(e3e3e3), 4):
                first = valign.findall(e3e3e3[i])[0]
                second = td_colspan.findall(e3e3e3[i+1])[0]
                third = td_i.findall(e3e3e3[i+2])[0]
                list_of_lists.append((first, second, third))
                d = Deposit((first, second, third))
                print d.legislature
            # pprint.pprint(list_of_lists[4])
            z = Deposit(list_of_lists[4])
            
            print z.text
            
