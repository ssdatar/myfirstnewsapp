import csv
import re

with open('static/civic-art.csv', 'r') as csv_in:
  with open('static/art.csv', 'w') as csv_out:

    reader = csv.reader(csv_in)
    headers = next(reader)
    headers += ['x', 'y']
    writer = csv.writer(csv_out)
    writer.writerow(headers)

    for row in reader:
      # Capture coordinates from the geometry column
      temp = re.search('\[(.*?)\]', row[7]).group().replace('[','').replace(']','').split(',')
      row.append(float(temp[0]))
      row.append(float(temp[1]))
      writer.writerow(row)