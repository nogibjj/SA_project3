import sqlite3
import pandas as pd

con = sqlite3.connect("spotify_songs.db")
df = pd.read_csv("songs_normalize.csv")
df.to_sql("spotify_songs", con, if_exists='replace', index=False)
con.commit()
con.close()
