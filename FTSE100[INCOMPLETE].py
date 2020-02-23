# IGNORE THIS SCRIPT AS IT HASNT BEEN ADAPTIVE FOR ITS PURPOSE IN THIS SCRIPT... USING AS TEMPLATE.

import pandas as pd
import requests
import urllib.request
import urllib
import os
import time
from bs4 import BeautifulSoup
import csv
import re

# for FTSE 100 index
pages = [1, 2, 3, 4, 5, 6]
#pages = [1,2]
#output_file = r'\\Galileo\Public\Legal Intelligence\Customer Segmentation\BA\Ad Hoc Reports & Requests\2019\201909 - September\DAI-2093 - Kenneth Ume - Market Product Penetration Data Request - REPORT\ftse_100_list.xlsx'
output_file = r"./FTSE100/ftse100_list.xlsx"
lst=[]
for page in pages:
    url = r'https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-indices-constituents.html?index=UKX&page={}'.format(
        page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    table = soup.find('table',{'class':'table_dati'})
    table_rows = table.findAll('tr')
    l=[]
    for tr in table_rows:
        td=tr.findAll('td')
        row = list(filter(lambda r: r != '""', [tr.text.strip() for tr in td]))

        url_name = tr.find('a')
        link = r'http://www.londonstockexchange.com' + url_name.attrs['href']
        response = requests.get(link)
        soup = BeautifulSoup(response.text,"html.parser")
        t = soup.find('h1',{'class':'tesummary'})
        name = t.text.strip()

        if name != 'FTSE 100':
            ticker = re.search(r'.*\s', name)
            name = name.replace(ticker.group(),"").strip()
            row.append(name)

        while("" in row):
            row.remove("")

        l.append(row)
    lst.extend(l)
FTSE = [e for e in lst if e!=[]]
df=pd.DataFrame(FTSE,columns=['Code','Name','Cur','Price','+/-','%+/-','Full Name'])
df.to_csv(output_file, index=False, encoding = 'utf-8-sig')
df.to_excel(output_file, index=False)
#print(df)


# for top 200 law firms
#output_file_2 = r'\\Galileo\Public\Legal Intelligence\Customer Segmentation\BA\Ad Hoc Reports & Requests\2019\201909 - September\DAI-2093 - Kenneth Ume - Market Product Penetration Data Request - REPORT\law_firm_list.xlsx'
output_file_2 = r"./FTSE100/lawfirm_list.xlsx"
lst_2 = []
url = r'https://www.thelawyer.com/top-200-uk-law-firms/'
response = requests.get(url)
soup2 = BeautifulSoup(response.text, "html.parser")
table2 = soup2.find('tbody')
#print(table2)
table_rows2 = table2.findAll('tr')
a = []
for tr2 in table_rows2:
    td2 = tr2.findAll('td')
    row2 = [tr2.text.strip() for tr2 in td2]
    while("" in row2):
        row2.remove("")
    a.append(row2)
law = [x for x in a if x != []]
head = law[0]
del law[0]
df2 = pd.DataFrame(law,columns=head)
#print(df2)
df2.to_csv(output_file_2, index=False, encoding='utf-8-sig') #avoid ()shown as funny characters
df2.to_excel(output_file_2, index=False)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# for full stock list on London Stock Exchange
#pages = range(1,1199)
#pagegs=[1,2]
#output_file_full = r'\\Galileo\Public\Legal Intelligence\Customer Segmentation\BA\Ad Hoc Reports & Requests\2019\201909 - September\DAI-2093 - Kenneth Ume - Market Product Penetration Data Request - REPORT\ftse_list.xlsx'
#lst_full = []

#for page in pages:
 #   url = r'https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/prices-search/stock-prices-search.html?nameCode=&page={}'.format(page)
  #  response = requests.get(url)
   # soup_full = BeautifulSoup(response.text, "html.parser")
    #print(soup_full)
    #table_full = soup_full.find('table', {'class': 'table_dati'})
    #print(table_full)
    #table_rows_full = table_full.findAll('tr')
    #print(table_rows_full)
#    full_row = []
 #   for tr_full in table_rows_full:
  #      td_full = tr_full.findAll('td')
   #     row_full = list(filter(lambda tr_full: tr_full != "", [tr_full.text.strip() for tr_full in td_full]))

    #    full_row.append(row_full)

    #lst_full.extend(full_row)

#FTSE_full = [foo for foo in lst_full if foo != []]
#df = pd.DataFrame(FTSE_full, columns=['Code', 'Name', 'Cur', 'Price', '+/-', '%+/-'])
#df.to_csv(output_file_full, index=False, encoding = 'utf-8-sig', float_format = None, sep = ',', quoting = csv.QUOTE_ALL)
#df.to_excel(output_file_full, index = False)


