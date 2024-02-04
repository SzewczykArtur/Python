from bs4 import BeautifulSoup
import requests
import sqlite3


class MusicData:
    """
    This class need to get a date. Next create a dictionary with top 100 musics that day.
    """
    def __init__(self, date):
        self.date = date

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                     '(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        accept_language = 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'
        self.headers = {
            'User-Agent': user_agent,
            'Accept-Language': accept_language
        }

    def get_data(self):
        # Create a string with link to website Billboard with specific date.
        url = f"https://www.billboard.com/charts/hot-100/{self.date}"

        response = requests.get(url=url, headers=self.headers)
        status = response.status_code
        if status == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Get all songs
            music_data = soup.select('li ul li h3')
            songs = [song.getText().strip() for song in music_data]
            # Create a list o artists
            artists_data = soup.find_all('span',
                                       class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                              "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                              "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
            first_artist = soup.find('span', class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                                    "u-line-height-normal@mobile-max u-letter-spacing-0021 "
                                                    "lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 "
                                                    "u-max-width-230@tablet-only u-font-size-20@tablet")
            artists = [artist.getText().strip() for artist in artists_data]
            artists = [first_artist.getText().strip()] + artists

            # Create a list with top 100 music that day
            data = []
            for i in range(len(artists)):
                song_info = {'Place on the list': i+1, 'Artiste': artists[i], 'Song': songs[i]}
                data.append(song_info)
            # print(data)
            return {self.date: data}
        else:
            return "Something is wrong. Please contact with us or try later."


class Database:

    def __init__(self, date):
        # Date have to be in format "year-month-day"
        self.date = date

    def read_database(self):
        connection = sqlite3.connect("musics_data.sql")
        data = connection.execute("""
        SELECT "tabel_name" FROM "main"
        """)
        data_list = [data[0] for data in data.fetchall()]
        connection.commit()
        connection.close()

        return data_list

    def check_data(self):
        name = f'Top_100_best_songs_of_{self.date}'
        # print(self.read_database()[0])
        # Check if music for this day was checked already
        if self.read_database() == [] or name not in self.read_database():
            # If no, create new tabel, add data, fill main tabel and return this data
            music_data = MusicData(self.date).get_data()[self.date]

            connection = sqlite3.connect('musics_data.sql')
            connection.execute(f"""
            CREATE TABLE "{name}" (id INTEGER PRIMARY KEY AUTOINCREMENT, ranking INTEGER, song TEXT, artiste TEXT)
            """)
            for data in music_data:
                try:
                    connection.execute(f"""
                    INSERT INTO "{name}" ("ranking", "song", "artiste") 
                    VALUES ("{data['Place on the list']}","{data['Song']}", "{data['Artiste']}")
                    """)
                    print("Hi")
                except sqlite3.OperationalError as e:
                    connection.execute(f"""
                    INSERT INTO "{name}" ("ranking", "song", "artiste") 
                    VALUES ("{data['Place on the list']}","------", "-------")
                    """)
                connection.commit()
            connection.commit()
            connection.close()

            # Add new row to main tabel
            connection = sqlite3.connect('musics_data.sql')
            connection.execute(f"""
            INSERT INTO "main" ("tabel_name","date")
            VALUES ("{name}", "{self.date}")
            """)
            connection.commit()
            connection.close()

            connection = sqlite3.connect("musics_data.sql")
            data = connection.execute(f"""
                                    SELECT * FROM "{name}"
                                    """)
            songs_data = data.fetchall()
            connection.commit()
            connection.close()
            return songs_data
        else:
            # If so, return data for this day
            connection = sqlite3.connect("musics_data.sql")
            data = connection.execute(f"""
                        SELECT * FROM "{name}"
                        """)
            data_list = data.fetchall()
            connection.commit()
            connection.close()
            return data_list


test = Database('2023-12-12').check_data()
print(test)
