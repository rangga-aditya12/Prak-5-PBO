class Movie:
    def __init__(self, title, release_year, director, order):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.order = order

    def display_info(self):
        print(f"Film favorit ke-{self.order}:")
        print(f"Judul: {self.title}")
        print(f"Tahun Rilis: {self.release_year}")
        print(f"Sutradara: {self.director}")

# List untuk menyimpan objek Movie
daftar_film = []

# Data film favorit
film_data = [
    {"title": "Joker", "release_year": 2019, "director": "Todd Philips"},
    {"title": "The Batman", "release_year": 2022, "director": "Matt Reeves"},
    {"title": "Oppenheimer", "release_year": 2023, "director": "Christopher Nolan"},
    {"title": "evangelion 3.0+1.0 thrice upon a time", "release_year": 2022, "director": "Hideaki Ano"},
    {"title": "Suzume", "release_year": 2023, "director": "Makoto Shinkai"}
]

# Memasukkan data film ke dalam daftar_film
for i, data in enumerate(film_data, start=1):
    movie = Movie(data["title"], data["release_year"], data["director"], i)
    daftar_film.append(movie)

# Menampilkan informasi film
print("----------ELKOM 2----------")
for film in daftar_film:
    film.display_info()
    print("==============")