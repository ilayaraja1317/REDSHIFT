import sys
#import psycopg2

#import psycopg2
import redshift_connector

conn = redshift_connector.connect(
                host="rsdevops.cj9lbag2g8ix.us-east-1.redshift.amazonaws.com",
                database="dev",
                user="awsuser",
                password="Admin12345"
)

cur = conn.cursor()
cur.execute(open("test.sql", "r").read())
conn.commit()
rows = cur.fetchall()
print(rows)
print("Done")

conn.close()

