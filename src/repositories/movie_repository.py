class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        return db.session.query(Movie).all()

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return db.session.query(Movie).filter_by(id=movie_id).first()

    def create_movie(self, title, director, rating):
        def create_movie(self, title, director, rating):
    new_movie = Movie(title=title, director=director, rating=rating)
    db.session.add(new_movie)
    db.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return db.session.query(Movie).filter(Movie.title.ilike(f'%{title}%')).all()


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
