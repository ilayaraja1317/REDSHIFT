#import psycopg2
import redshift_connector

conn = redshift_connector.connect(
                host="rsdevops.cj9lbag2g8ix.us-east-1.redshift.amazonaws.com",
                database="dev",
                user="awsuser",
                password="Admin12345"
)

cur = conn.cursor()

cur.execute("select * from category")
rows = cur.fetchall()
print(rows)
conn.close()
