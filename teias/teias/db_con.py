import sqlite3

conn=sqlite3.connect("tutorial.db")
c=conn.cursor()

#I created personel tabel for teiaş
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS personel (ID REAL,AD TEXT, SOYAD TEXT,TEL REAL)')

#ı inserted value to personel
def data_entry(ad,soyad,tel):
    c.execute('SELECT ID FROM personel')
    data=c.fetchall()
    ıd=len(data)+1
    c.execute("INSERT INTO personel (ID,AD,SOYAD,TEL) VALUES(?,?,?,?)",
              (ıd,ad,soyad,tel))
    conn.commit()
    c.close()
    conn.close()



data_entry("selahattin","aksoy",2323)
