# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # Best Artworks of All Time
# ## Collection of Paintings of the 50 Most Influential Artists of All Time
# ### https://www.kaggle.com/ikarus777/best-artworks-of-all-time
# 
# I am going to solve the problem of recognizing a genre from a painting.
# Since this task is educational, I can afford some tricks associated with the formation of a new dataset and data preprocessing to make my life easier.

#%%
import pandas as pd


#%%
artists = pd.read_csv('../data/artists.csv')
artists.head()


#%%
artists = artists.drop(['bio', 'wikipedia', 'years'], 1)
artists = artists.sort_values(by=['paintings'])
artists = artists.reset_index(drop=True)


#%%
for i, row in artists.iterrows():
    artists.at[i, 'name'] = artists.at[i, 'name'].replace(" ", "_")
(artists.head())


#%%
# artists_by_nationality = artists.drop(['genre'], 1)
# artists_by_nationality = artists_by_nationality.drop_duplicates(subset='nationality', keep='last')
# for i, row in artists_by_nationality.iterrows():
#     nationalities = artists_by_nationality.at[i, 'nationality'].split(',')
#     artists_by_nationality = artists_by_nationality.drop(i)
#     for nationality in nationalities:
#         # find nationality in "nationality" column
#         if (artists_by_nationality['nationality'][artists_by_nationality['nationality'] == nationality].empty):
#             row.at['nationality'] = nationality
#             artists_by_nationality = artists_by_nationality.append(row)
# artists_by_nationality = artists_by_nationality.sort_values(by=['paintings']).drop_duplicates(subset=['nationality'], keep='last').drop_duplicates(subset=['name'], keep='last')
# (artists_by_nationality.reset_index(drop=True))


#%%
artists_by_genre = artists.drop(['nationality'], 1)
artists_by_genre = artists_by_genre.drop_duplicates(subset='genre', keep='last')
for i, row in artists_by_genre.iterrows():
    genres = artists_by_genre.at[i, 'genre'].split(',')
    artists_by_genre = artists_by_genre.drop(i)
    for genre in genres:
        # find genre in "genre" column
        if (artists_by_genre['genre'][artists_by_genre['genre'] == genre].empty):
            row.at['genre'] = genre
            artists_by_genre = artists_by_genre.append(row)
artists_by_genre = artists_by_genre.sort_values(by=['paintings']).drop_duplicates(subset=['genre'], keep='last').drop_duplicates(subset=['name'], keep='last')
artists_by_genre = artists_by_genre[artists_by_genre.paintings >= 100].reset_index(drop=True)
artists_by_genre

#%% [markdown]
# We have a dataset of 16 classes. From the classes we will choose 100 images for training and from the remaining 10 for validation.

#%%
import cv2 as cv

name_genre = dict(zip(artists_by_genre["name"].to_list(), artists_by_genre["genre"].to_list()))
for name, genre in name_genre.items():
    print(name , genre)

#%%
