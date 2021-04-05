import sqlite3

connection = sqlite3.connect('census.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS destiny(province_or_teritory TEXT,population integer, Land_area Real)")

cursor.execute("INSERT INTO  destiny VALUES('Newfoundland and Labrador', 512930 ,370501.69)")
cursor.execute("INSERT INTO  destiny VALUES('Prince Edward Island' ,135294 ,5684.39)")
cursor.execute("INSERT INTO  destiny VALUES('Nova Scotia', 908007, 52917.43)")
cursor.execute("INSERT INTO  destiny VALUES('New Brunswick', 729498, 71355.67)")
cursor.execute("INSERT INTO  destiny VALUES('Quebec' ,7237479 ,1357743.08)")
cursor.execute("INSERT INTO  destiny VALUES('Ontario ',11410046 ,907655.59)")
cursor.execute("INSERT INTO  destiny VALUES('Manitoba',1119583 ,551937.87)")
cursor.execute("INSERT INTO  destiny VALUES('Saskatchewan', 978933, 586561.35)")
cursor.execute("INSERT INTO  destiny VALUES('Alberta' ,2974807, 639987.12)")
cursor.execute("INSERT INTO  destiny VALUES('British Columbia',3907738, 926492.48)")
cursor.execute("INSERT INTO  destiny VALUES('Yukon Territory' ,28674, 474706.97)")
cursor.execute("INSERT INTO  destiny VALUES('Northwest Territories', 37360 ,1141108.37)")
cursor.execute("INSERT INTO  destiny VALUES('Nunavut', 26745 ,1925460.18)")


connection.commit()
cursor.execute('SELECT  * FROM destiny')

print("all:",cursor.fetchall())

cursor.execute('SELECT population FROM destiny')
print('population:',cursor.fetchall())

cursor.execute('SELECT province_or_teritory,population FROM destiny where population >1000000')
print("population more than 1 milion:",cursor.fetchall())

cursor.execute('SELECT province_or_teritory,population FROM destiny where population < 1000000 or population>5000000')
print("პროვინციები, რომლებშიც 1 მილიონზე ნაკლები ან 5 მილიონზე მეტი ადამიანი ცხოვრობს",cursor.fetchall())



cursor.execute('SELECT province_or_teritory,population FROM destiny WHERE land_area >  200000')
print('land area <200000:',cursor.fetchall())

cursor.execute('SELECT province_or_teritory,population ,  population/land_area FROM DESTINY')
print('mosaxleobis simchidrove:',cursor.fetchall())

