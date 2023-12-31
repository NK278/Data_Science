favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]

book_movie_pairs = list(zip(favorite_books, favorite_movies))

for pair in book_movie_pairs:
    print(pair)
