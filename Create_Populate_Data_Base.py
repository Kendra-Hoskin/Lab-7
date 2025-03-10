import sqlite3
import pandas as pd

def create_database():
    con = sqlite3.connect('bond_movies.db')
    cur = con.cursor()

    create_table_query = """ (Year INTEGER, Movie TEXT, Bond TEXT, Avg_User_IMDB REAL) """
    cur.execute(create_table_query)
    con.commit()
    con.close()

def populate_movies_table():
    bond_data_file = pd.read_cvs('jamesbond.csv')
    con = sqlite3.connect('bond_movies.db')
    cur = con.cursor()

    for row in bond_data_file.inertuples(index=False):
        cur.execute( ''' INSERT INTO movies (Year, Movies, Bond, Avg_User_IMDB) VALUES (?, ?, ?, ?)''' (row.Year, row.Movie, row.Bond, row.Avg_User_IMDB))
    con.commit()
    con.close()

def main():
    create_database()
    populate_movies_table()
    print("Datebase created and populated successfully!")

if __name__ == "__main__":
    main()