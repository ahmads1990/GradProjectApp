import sqlite3
import pandas as pd

conn = sqlite3.connect('PatientDatabase') 
c = conn.cursor()
                   
c.execute('''
          SELECT
          *
          FROM patients
          ''')

df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
print (df)