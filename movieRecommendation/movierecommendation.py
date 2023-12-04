import requests
import random

# TMDb API key
api_key = "yourapikey"

def search_movie(movie_name):
    # Search for a movie by name using TMDb API
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            # Return the first found movie
            return data["results"][0]
    return None

def find_similar_movie(genre, keywords):
    # Find a movie similar to the user-input movies based on genre and keywords
    discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}&with_keywords={keywords}"
    response = requests.get(discover_url)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            # Return the first found similar movie
            return data["results"][0]
    return None

def recommend_random_movie(min_rating):
    # Get a random movie with IMDb rating equal to or above the specified minimum rating
    discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&vote_average.gte={min_rating}&sort_by=popularity.desc"
    response = requests.get(discover_url)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            # Return a random movie
            return random.choice(data["results"])
    return None

# Get movie genres based on user input and provide a recommendation
def movie_recommendation():
    # Prompt the user to enter three movie names
    movie_names = [input(f"Movie {i+1} name: ") for i in range(3)]
    genres = set()

    # Retrieve movie genres based on user-input movie names
    for movie_name in movie_names:
        movie_info = search_movie(movie_name)
        if movie_info:
            genres.update(movie_info.get("genre_ids", []))

    if len(genres) > 0:
        # Recommend a movie based on the common genre of user-input movies
        common_movie = find_similar_movie(list(genres), "")
        if common_movie:
            print("\nRecommendation based on the common genre of user-input movies:")
            print(f"Movie Title: {common_movie['title']}")
            print(f"Genre: {common_movie['genre_ids']}")
            print(f"Overview: {common_movie['overview']}")
        else:
            print("\nNo common movie recommendation found. Providing a random movie recommendation:")
            genre = list(genres)[0] if len(genres) == 1 else ""
            random_movie = recommend_random_movie(genre)
            if random_movie:
                print(f"Movie Title: {random_movie['title']}")
                print(f"Genre: {random_movie['genre_ids']}")
                print(f"Overview: {random_movie['overview']}")
            else:
                print("No other movie recommendation available.")
    else:
        print("\nGenres of the user-input movies could not be found. Providing a random movie recommendation:")
        random_movie = recommend_random_movie("")
        if random_movie:
            print(f"Movie Title: {random_movie['title']}")
            print(f"Genre: {random_movie['genre_ids']}")
            print(f"Overview: {random_movie['overview']}")
        else:
            print("No other movie recommendation available.")

# Main menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Get Movie Recommendation by Entering Movie Names")
        print("2. Get Random Movie Recommendation with IMDb Rating 8 or Above")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            movie_recommendation()

        elif choice == "2":
            min_rating = 8.0
            random_movie = recommend_random_movie(min_rating)
            if random_movie:
                print(f"\nRandom movie recommendation with IMDb rating {min_rating} or above:")
                print(f"Movie Title: {random_movie['title']}")
                print(f"Genre: {random_movie['genre_ids']}")
                print(f"Overview: {random_movie['overview']}")
            else:
                print("No other movie recommendation available.")

        elif choice == "3":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Call the main menu
if __name__ == "__main__":
    main_menu()
