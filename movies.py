import sqlite3

def query_movies():
    con = sqlite3.connect('bond_movies.db')
    cur = con.cursor()

    cur.execute('''
        SELECT Year, Movie, Bond'
        FROM movies
        WHERE Year < 1980
                ''')
    
    results = cur.fetchall()
    for year, movie, bond in results:
        print(f"In {year}, the movie '{movie}' starred the Bond actor '{bond}'.")
    con.close()

def main():
    query_movies()

if __name__ == "__main__":
    main()