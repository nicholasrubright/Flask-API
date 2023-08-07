from src.models.movie import Movie
class MovieService:
    movieSchema = Movie.Schema()

    def getMovies(self):
        test_1 = Movie(1, "test title")
        test_2 = Movie(2, "another test")
        movies = [test_1, test_2]
        return self.movieSchema.dump(movies, many=True)
