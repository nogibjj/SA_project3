import sqlite3
import click

@click.group()
def cli():
    pass

@click.command()
def songs_per_year():
    """
    Return how many songs were released each year
    """
    con = sqlite3.connect("spotify_songs.db")
    cursor = con.cursor()
    cursor.execute("SELECT year, COUNT(*) FROM spotify_songs GROUP BY year;")
    songs_year = cursor.fetchall()
    for year, year_occ in songs_year:
        if year_occ == 1: 
            print(f"In {year}, {year_occ} song was released.")
        else: 
            print(f"In {year}, {year_occ} songs were released.")

@click.command()
def most_songs_year():
    """
    Return which year had the most songs released
    """
    con = sqlite3.connect("spotify_songs.db")
    cursor = con.cursor()
    cursor.execute("SELECT year, MAX (songcount) FROM (SELECT year, COUNT(*) songcount FROM spotify_songs GROUP BY year);")
    songs_year = cursor.fetchall()
    max_songs = songs_year[0]
    print(f"The most songs released (based on this dataset) was in {max_songs[0]} with {max_songs[1]} songs.")

@click.command()
def num_artists(): 
    """
    Return the unique artists and count
    """
    con = sqlite3.connect("spotify_songs.db")
    cursor = con.cursor()
    cursor.execute("SELECT artist, COUNT(*) FROM spotify_songs GROUP BY artist;")
    unique_artists = cursor.fetchall()
    print("According to this dataset: ")
    for artist, num_songs in unique_artists:
        print(f"{artist} released {num_songs} songs")

@click.command()
def most_popular():
    """
    Return 10 most popular songs
    """
    con = sqlite3.connect("spotify_songs.db")
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT(song), artist, year FROM spotify_songs ORDER BY popularity DESC LIMIT 10;")
    most_pop_songs = cursor.fetchall()
    rank_idx = 1
    for song, artist, year in most_pop_songs:
        print(f"#{rank_idx}: {song} by: {artist} released in {year}")
        rank_idx += 1

@click.command()
def longest_songs():
    """
    Return the top 5 longest songs
    """
    con = sqlite3.connect("spotify_songs.db")
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT(song), artist, duration_ms FROM spotify_songs ORDER BY duration_ms DESC LIMIT 5;")
    most_pop_songs = cursor.fetchall()
    rank_idx = 1
    for song, artist, length in most_pop_songs:
        print(f"#{rank_idx}: {song} by: {artist} is {length / 1000} seconds long ({length / (1000*60):.2f} mins)")
        rank_idx += 1

cli.add_command(songs_per_year)
cli.add_command(most_songs_year)
cli.add_command(num_artists)
cli.add_command(most_popular)
cli.add_command(longest_songs)


if __name__ == '__main__':
    cli()