import sqlite3
import pandas as pd

cxn = sqlite3.connect('db.sqlite3')
wb = pd.read_excel('Клиенты_import.xlsx', sheet_name='ЮЛ')
wb.columns = ['ID', 'product', 'art', 'price']
wb.to_sql(name='main_client', con=cxn, if_exists='replace', index=True)
cxn.commit()
cxn.close()
