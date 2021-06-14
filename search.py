import requests
import os, csv
import shutil

filename = 'riseattire.csv'

term = input("Product Title to search for:  ")

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)



items_list = []

for img in range(len(rows)):

    title = rows[img][1]        # name of product
    url = rows[img][24]         # field 24 is the URL for Shopify images
    price = rows[img][19]       # field 19 is the PRICE
    fn = url.rsplit('/', 1)[-1]
    jpg = fn.split('?', 1)[0]
    if term in title:
        print(title + " : " + price + " : " + jpg[:-4])
        items_list.append(title + " : " + price + " : " + jpg[:-4])