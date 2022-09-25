import sqlite3

con=sqlite3.connect("scrape.db")
c=con.cursor()
tab="""create table flip(sno number(20),title varchar(100), desc varchar(2000),stars number(2),dat_p DATE,dat DATE);"""
c.execute(tab)
con.commit()
con.close()