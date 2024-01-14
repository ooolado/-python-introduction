# Set is {without key and value}
# it will not allow duplicate items, it will not maintain the order
# dictionary will have key, value in the curly braces

groceries = {"eggs", "milk", "veggies", "eggs"}

print(groceries)

registration = {"vamsi@jjtecj.com", "avi@gmail.com", "jespo@amazon.com", "avi@gmail.com"}

print(registration)

playlist = {"album1", "album5", "album9", "album9"}

print(playlist)

print(len(registration))

playlist.add("album20")

print(playlist)

marvel_movies = {"ironman", "spiderman", "black panther", "hulk"}

fav_movies = {"ironman", "black panther", "super man"}

combined_movies = marvel_movies.union(fav_movies)

print(combined_movies)

common_movies = marvel_movies.intersection(fav_movies)

print(common_movies)

for i in marvel_movies:  # iteration function
    print(i)
    
