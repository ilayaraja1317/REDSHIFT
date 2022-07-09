import sys
import redshift_connector

def rs_dep():
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

if __name__ == "__main__":

    rs_dep()
