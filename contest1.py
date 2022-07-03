
import redshift_connector

conn = redshift_connector.connect(
                host="rsdevops.cj9lbag2g8ix.us-east-1.redshift.amazonaws.com",
                database="dev",
                user="awsuser",
                password="Admin12345"
)

cur = conn.cursor()

cur.execute("create table products (id int not null identity(1, 1),product_name varchar(150) not null,price decimal(12,2) not null,status varchar(25) not null default 'ACTIVE',close_date date null)")
rows = cur.fetchall()
print(rows)
conn.close()

