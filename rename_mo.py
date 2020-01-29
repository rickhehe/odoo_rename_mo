import psycopg2
import pandas as pd

# you may need to config your own con
from connections import live

def row_gen():

    df = pd.read_csv(r'input\trial.csv')
    for i in df.itertuples():
        rename(i.ID, i.name)

def rename(id_, name):

    cursor = live.cursor()

    cursor.execute(f"""
        update mrp_production
          set name = '{name}'
        where id=1
    """)

    live.commit()

def main():
    row_gen()

if __name__ == '__main__':
    main()
