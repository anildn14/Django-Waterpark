import sqlite3
conn = sqlite3.connect('db.sqlite3')
print "conn :",conn
c = conn.cursor()
print "\nc :",c
c.execute('SELECT * FROM water_park_park_details')
print "\nc.fetchall() :",c.fetchall()

c.execute("PRAGMA table_info(water_park_park_details)")
print "\nc.fetchall() :",c.fetchall()

c.execute('SELECT * FROM water_park_park_details')
print c.description
op=c.fetchone()
print "\nop :",op
print "\nc.fetchall() :",c.fetchall()
# print "column names :",op.keys()
print "\n"
for row in c.execute('SELECT * FROM water_park_park_details'):
	print "row :",row

c.execute("SELECT * FROM water_park_park_details")
col_name_list = [x[0] for x in c.description]
print "\ncol_name_list :",col_name_list



c.execute("INSERT INTO water_park_park_details VALUES (6,'hello','hello','9:00 AM to 7:30 PM','https://www.esselworld.in/travel/home','999.99',0,0,'americanpie_70VgToI_HtS93ol.jpg')")
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()














# https://docs.python.org/2/library/sqlite3.html
# https://www.daniweb.com/programming/software-development/threads/124403/sqlite3-how-to-see-column-names-for-table