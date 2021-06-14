import requests
import os, csv
import shutil

filename = 'riseattire.csv'

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

    print("TOTAL ROWS:  %d"%(csvreader.line_num))

print("Field names are: " + ", ".join(field for field in fields))

os.mkdir('tmp')     # create a temp dir real quick

print("Downloading images...")

d = 0       # set a counter so we can see how many images we downloaded
for img in range(len(rows)):

    url = rows[img][24]         # field 24 is the URL for Shopify images
    if len(url) > 15:           # make sure we're actually getting a URL
        response = requests.get(url, stream=True)
        fn = url.rsplit('/', 1)[-1]     # grab the image name (everything after the slash)
        jpg = fn.split('?', 1)[0]       # strip off the ?=v34refsdfa ID crap from the JPG
        with open('tmp/' + jpg, 'wb') as out_file:      # append the TMP dir & save the file
            shutil.copyfileobj(response.raw, out_file)
        del response
        d = d + 1


print("Downloaded %d images", d)
