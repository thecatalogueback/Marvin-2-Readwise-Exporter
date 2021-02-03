# Python3
## version 03-02-2021a
# Marvin Export to Readwise

import csv, sys, json

def ReadwiseExporter(MarvinCsv, ExportCsv):
  rows = []
  with open(MarvinCsv) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row.get('HighlightText') or row.get('EntryText'):
        rows.append(row)

  print(json.dumps(rows)) # DEBUG

  with open(ExportCsv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Highlight', 'Title', 'Author', 'URL', 'Note', 'Location'])
    for row in rows:
      if row.get('HighlightText') or row.get('EntryText'): # Valid Entry
        if not row.get('HighlightText') and row.get('EntryText'):
          row['HighlightText'] = 'VOCAB: ' + row.get('EntryText') # ASSUMES is Highlighted Vocab
          row['EntryText'] = '' # Clear Entry Text as not to get duplicate
        writer.writerow([
          row['HighlightText'].replace('\n', '    '),
          row['Title'].replace('\n', '    '),
          row['Author'].replace('\n', '    '),
          '',
          row['EntryText'].replace('\n', '    '),
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
