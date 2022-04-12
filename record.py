import sqlite3
import pandas as pd

con=sqlite3.connect('action_time_record.db')
cur=con.cursor()
# con.execute('''CREATE TABLE record (time single, work_property integer) ''')
con.execute('''INSERT INTO record VALUES (1649773897.0977066, 1)''')
cur.execute('''SELECT * FROM record''')
print(cur.fetchall())
con.commit()
# con.close()

df=pd.read_sql('''select * from record''', con=con)
df.to_csv('record.csv')
df.to_sql('test2',con=con)
cur.execute('''SELECT name FROM sqlite_master WHERE type='table' ''')
print(cur.fetchall())
print(df)
con.close()
