import pandas as pd
import matplotlib.pyplot as plt

years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103,101,99,100,100,95,95,96,93,90]
movie_dict = {'years':years,'durations':durations}

durations_df = pd.DataFrame(movie_dict) #create dataframe
print(durations_df)

plt.plot(years,durations)
plt.title('Netflix Movie Durations 2011-2020')
plt.show() 


netflix_df = pd.read_csv("netflix_data.csv") # Read in the CSV as a DataFrame

print(netflix_df.iloc[:5]) # Print the first five rows of the DataFrame

netflix_df_movies_only = netflix_df[netflix_df["type"]=="Movie"] # Subset the DataFrame for type "Movie"


netflix_movies_col_subset = netflix_df_movies_only.loc[:,["title","country","genre","release_year","duration"]]

print(netflix_movies_col_subset.iloc[:5])# Print the first five rows of the DataFrame

short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"]<60]#list of short movies
print(short_movies.iloc[:20])

colors = []

for i, row in netflix_movies_col_subset.iterrows(): # Iterate over rows of netflix_movies_col_subset
    if row["genre"]=="Children" :
        colors.append("red")
    elif row["genre"]=="Documentaries" :
        colors.append("blue")
    elif row["genre"]=="Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")
fig = plt.figure(figsize=(12,8))

#Scatter Plot
plt.scatter(netflix_movies_col_subset["release_year"],netflix_movies_col_subset["duration"],c=colors)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()





