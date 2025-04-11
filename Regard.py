# import pyodbc as db
from IPython.display import display
import pandas as pd
import requests

def regard():
    url = 'https://www.regard.ru/api/price/regard_price_100425_8.xlsx'
    try:
        r = requests.get(url, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        print(e)
        raise SystemExit(e)

    with open('./price.xlsx', 'wb') as f:
        f.write(r.content)

    latest_file = './price.xlsx'

    Regard_excel = pd.read_excel(latest_file) #, nrows=100)
    # display(Regard_excel.to_string())

    Reg_excel = Regard_excel[['Unnamed: 5', 'Unnamed: 6']]
    not_null_mask = Reg_excel.notnull().all(axis=1)
    Reg_excel = Reg_excel[not_null_mask]

    Reg_excel.rename(columns={'Unnamed: 5': 'Name', 'Unnamed: 6': 'Price'}, inplace=True)

    Regard_CPU = Reg_excel[Reg_excel['Name'].str.contains(r'Процессор[ \w()]{0,}')].reset_index(drop=True)
    Regard_GPU = Reg_excel[Reg_excel['Name'].str.contains(r'Видеокарта[ \w()]{0,}')].reset_index(drop=True)
    # Regard_GPU.reset_index(drop=True, inplace=True)

    display(Regard_CPU.to_string())
    display(Regard_GPU.to_string())

    # Fin_recordset = []

    # for row in Reg_excel.itertuples(index=False):
    #     Fin_recordset.append(row)

    # Fin_recordset = list(Reg_excel.itertuples(index=False, name=None))


    # conn = db.connect(''
    #                   'driver={ODBC Driver 18 for SQL Server};'
    #                   'SERVER=sqlserver;'
    #                   'database=Scrapper;'
    #                   'uid=sa;'
    #                   'pwd=Qwerty11;'
    #                   'encrypt=no;'
    #                   'TrustServerCertificate=yes;')
    #
    # query = '''
    # insert into dbo.Regard
    # (name,price)
    # values
    # (?, ?)
    # '''

    # print(Fin_recordset[100])

    # cursor = conn.cursor()
    # cursor.executemany(query, Fin_recordset)
    # cursor.commit()
    #
    # # print(cursor.fetchall())
    #
    # cursor.close()
    # conn.close()