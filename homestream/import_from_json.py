import psycopg2
import json

conn_string = "host='localhost' dbname='homestreamdb' user='euphoric' password='ab140299'"
# print the connection string we will use to connect
print("Connecting to database\n	->%s" % (conn_string))

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()


stream_data = open('homestream_stream.js')
data = json.load(stream_data)
stream_data.close()

data_to_insert = [(item[0], item[1], item[2]) for item in data]
cursor.executemany("""INSERT INTO homestream_stream (id, name, image_url) VALUES(%s, %s, %s)""", data_to_insert)
print("homestream_stream is OK")

radiochannel_data = open('homestream_radiochannel.js')
data = json.load(radiochannel_data)
radiochannel_data.close()

data_to_insert = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in data]
cursor.executemany("""INSERT INTO homestream_radiochannel (ID, NAME, URL, STREAM_ID, IMAGE_URL, NB_PLAYS) VALUES(%s, %s, %s, %s, %s, %s)""",
                   data_to_insert)
print("homestream_radiochannel is OK")
cursor.execute("COMMIT")
cursor.close()
