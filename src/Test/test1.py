import pandas as pd
import numpy as np

if __name__ == '__main__':
    ratings_1 = pd.read_csv("../../../data/ml-latest-small/ratings_1.csv")
    print(ratings_1.head(2))

    ratings_2 = pd.read_csv("../../../data/ml-latest-small/ratings_2.csv")
    print(ratings_2.head(2))

    movies = pd.read_csv("../../../data/ml-latest-small/movies.csv")
    print(movies.head(2))

    links = pd.read_csv("../../../data/ml-latest-small/links.csv")
    print(links.head(2))

    print(len(ratings_1))
    print(len(ratings_2))

    ratings_info = ratings_1.append(ratings_2, ignore_index=True)
    print(ratings_info.shape)

    print(ratings_info.tail())

    # movies 包含的不重复的 movieId 个数
    print(len(movies.movieId.unique()))
    # links 包含的不重复的 movieId 个数
    print(len(links.movieId.unique()))
    # movies 和 links 交集中包含的不重复的 movieId 个数
    print(len(np.intersect1d(movies.movieId.unique(), links.movieId.unique())))

    movies_info = movies.merge(links, how="inner", on="movieId")
    print(movies_info.shape)


    print(movies_info.head())

    # ratings_info 包含的不重复的 movieId 个数# rating
    print(len(ratings_info.movieId.unique()))
    # movies_info 包含的不重复的 movieId 个数
    print(len(movies_info.movieId.unique()))
    # ratings_info 和 movies_info 交集中包含的不重复的 movieId 个数
    print(len(np.intersect1d(ratings_info.movieId.unique(), movies_info.movieId.unique())))

    data = ratings_info.merge(movies_info, how="left", on="movieId")
    print(data.shape)


    print(data.head())

    data.to_csv("../../../data/ml-latest-small/user_for_movie_ratings_summary_test.csv", index=False)

    frame = [ratings_1, ratings_2]
    ratings_info2 = pd.concat(frame)

    print(ratings_info2)

    ratings_info3 = ratings_info2.set_index("movieId").join(movies_info.set_index("movieId"))
    print("----------------------------------------------------")
    print(ratings_info3)


