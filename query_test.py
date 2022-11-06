import sqlite3
import pandas as pd

#test spotify_songs.db was created and do a test query
con = sqlite3.connect("spotify_songs.db")
con_cur = con.cursor()
query = con_cur.execute("SELECT * FROM spotify_songs LIMIT 5")
for x in query.fetchall():
    print(x)

con.commit()
con.close()