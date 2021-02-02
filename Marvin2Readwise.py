# Python3
# Marvin Export to Readwise

import csv, sys, json

def ReadwiseExporter(MarvinCsv, ExportCsv):
  rows = []
  with open(MarvinCsv) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      rows.append(row)

  #print(json.dumps(rows)) # DEBUG

  with open(ExportCsv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Highlight', 'Title', 'Author', 'URL', 'Note', 'Location'])
    for row in rows:
      if not row.get('HighlightText'):
        row['HighlightText'] = 'NOTE: ' + row.get('EntryText')
      writer.writerow([
        row['HighlightText'].replace('\n', ''),
        row['Title'].replace('\n', ''),
        row['Author'].replace('\n', ''),
        '',
        row['EntryText'].replace('\n', ''),
        ''
      ])

  print('...Done')

if __name__ == "__main__":

  try:
    marvin = sys.argv[1]
    readwise = sys.argv[2]
    ReadwiseExporter(marvin, readwise)
  except:
    print('HOW TO USE:\npython Marvin2Readwise.py "MarvinJournal.csv" "Highlights.csv"')
