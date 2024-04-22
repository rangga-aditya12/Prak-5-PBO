class FilmFavorit:
    def __init__(self):
        self.daftar_film = []

    def tambah_film(self, film):
        self.daftar_film.append(film)

    def tampilkan_daftar(self):
        print("\n===========DAFTAR FILM FAVORIT===========")
        for i, film in enumerate(self.daftar_film, start=1):
            print(f"{i}.) {film}")

def main():
    # Membuat objek dari kelas FilmFavorit
    pengelola_film = FilmFavorit()

    # Meminta pengguna memasukkan lima film favorit
    for i in range(1, 6):
        film = input(f"Film favorit KE-{i}: ")
        pengelola_film.tambah_film(film)

    # Menampilkan daftar film favorit
    pengelola_film.tampilkan_daftar()

if __name__ == "__main__":
    main()
