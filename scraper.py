#!/usr/bin/python
import pprint
import re

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
            pprint.pprint(list_of_lists)
