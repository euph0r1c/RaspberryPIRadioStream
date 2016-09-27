import json
import sqlite3

rows_to_json = list()
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute("SELECT ID, NAME, IMAGE_URL FROM homestream_stream")
rows = c.fetchall()

for row in rows:
    print(row)
    t = (row[0], row[1], row[2])
    rows_to_json.append(t)

j = json.dumps(rows_to_json)
with open("homestream_stream.js", 'wb') as stream_js:
    stream_js.write(j)
c.close()


c = conn.cursor()
rows_to_json = list()

c.execute("SELECT ID, NAME, URL, STREAM_ID, IMAGE_URL, NB_PLAYS FROM homestream_radiochannel")
rows = c.fetchall()

for row in rows:
    t = (row[0], row[1], row[2], row[3], row[4], row[5])
    rows_to_json.append(t)

j = json.dumps(rows_to_json)
with open("homestream_radiochannel.js", 'wb') as stream_js:
    stream_js.write(j)
c.close()



