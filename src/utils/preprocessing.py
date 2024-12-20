from src.utils.utils import *
import pandas as pd
import ast

def import_and_preprocess_population(path):
    # Load the population data
    df_population = pd.read_csv(path)

    # Preprocess the columns as needed
    df_population = df_population.rename(columns={"Country Name":"originLabel"})
    df_population = df_population.drop(columns=["Indicator Name", "Indicator Code", "Unnamed: 66"])

    # Keep our countries of choice
    df_population = df_population[df_population['Country Code'].isin(country_code_mapping.keys())]
    df_population["originLabel"] = df_population["Country Code"].map(country_code_mapping)

    # Drop the country code and return
    df_population = df_population.drop(columns="Country Code")
    return df_population

def import_and_preprocess_gdp(path):
    # Load the GDP data
    df_gdp = pd.read_csv(path)

    # Preprocess the columns as needed
    df_gdp = df_gdp.rename(columns={"Country Name":"originLabel"})
    df_gdp = df_gdp.drop(columns=["Code", "Unnamed: 65"])

    # Rename the column to match our countries names
    df_gdp.loc[df_gdp.originLabel == "United States", 'originLabel'] = "United States of America"
    df_gdp.loc[df_gdp.originLabel == "Hong Kong SAR, China", 'originLabel'] = "Hong Kong"
    df_gdp.loc[df_gdp.originLabel == "Korea, Rep.", 'originLabel'] = "South Korea"

    # Keep our countries of choice and return
    df_gdp = df_gdp[df_gdp['originLabel'].isin(countries)]
    df_gdp = df_gdp.fillna(0)
    return df_gdp

def import_domestic_international_and_merge(path, df_movies_path):
    # Reload the movies data
    df_movies = pd.read_csv(df_movies_path)

    # Load the domestic and international data
    df_domestic_international = pd.read_csv(path)

    # Preprocess the columns as needed
    df_domestic_international = df_domestic_international.rename(columns={"items": "item"})

    df_movies["originLabel"] = df_movies["originLabel"].replace("People's Republic of China", "China")

    # Merge the movies data to have boxoffice domestic and international
    merged_df = pd.merge(df_domestic_international, df_movies, on="item", how='inner')
    merged_df = merged_df.drop(columns=["pub_date", "title_year", "Wikipedia_movie_ID", "Freebase_movie_ID", "Runtime"])

    # Combine to keep only 1 title
    df = merged_df.copy()
    df["Title"] = df["title_x"].combine_first(df["title_y"])
    df = df.drop(columns=["title_x", "title_y"])

    # Combine to keep only the good genres
    df["Genre"] = df["Genre_x"].combine_first(df["Genre_y"])
    df = df.drop(columns=["Genre_x", "Genre_y"])

    # Keep our countries of choice 
    df = df.loc[df['originLabel'].isin(countries)]

    # Threshold on the worlwide boxoffice to keep only the "true" scraped values (with a margin of 0.2) and return
    df = df[(df['domestic'] + df['international']) / df['worldwide'] >= 0.8]
    df = df[(df['domestic'] + df['international']) / df['worldwide'] <= 1.2]
    return df

def preprocess_movies_for_genres_analysis(data):
    df_movies_preprocessed = data.dropna(subset=["Genre_x", "Genre_y"], how="all")

    # Combine the two columns into one, keeping the non-NaN value
    df_movies_preprocessed["Genre"] = df_movies_preprocessed["Genre_x"].combine_first(df_movies_preprocessed["Genre_y"])

    # Drop the old columns if they are no longer needed
    df_movies_preprocessed = df_movies_preprocessed.drop(columns=["Genre_x", "Genre_y"])
    df_movies_preprocessed["Genre"] = df_movies_preprocessed["Genre"].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith("[") else [x] if isinstance(x, str) else x
    )

    # Use the explode method to split the list elements into separate rows
    df_movies_preprocessed = df_movies_preprocessed.explode("Genre", ignore_index=True)

    df_movies_preprocessed = df_movies_preprocessed[df_movies_preprocessed.originLabel.isin(countries)]

    # Assign "counts" column if missing and return
    df_movies_preprocessed["counts"] = 1 

    return df_movies_preprocessed

def preprocess_movies_for_genres_analysis_second_plot(df_movies):
    # Preprocess the data
    df_movies['Genre_x'] = df_movies['Genre_x'].fillna(df_movies['Genre_y'])
    df_movies['Genre_y'] = df_movies['Genre_y'].fillna(df_movies['Genre_x'])
    df_movies['Genre_x'] = df_movies['Genre_x'].fillna("Unknown")
    df_movies['Genre_y'] = df_movies['Genre_y'].fillna("Unknown")
    df_movies_genre = df_movies[~((df_movies['Genre_x'] == "Unknown") & (df_movies['Genre_y'] == "Unknown"))]
    df_movies_genre['Genre_y'] = df_movies_genre['Genre_y'].apply(
        lambda x: x.split(',') if isinstance(x, str) else x
    )

    # Split genres further if they have slashes (e.g. 'Action/Adventure' -> ['Action', 'Adventure'])
    df_movies_genre['Genre'] = df_movies_genre['Genre_y'].apply(
        lambda x: [item.strip() for genre in x for item in genre.split('/') if item.strip()] if isinstance(x, list) else x
    )

    # Clean the genres in each list, handling extra spaces, quotes, and brackets
    df_movies_genre['Genre'] = df_movies_genre['Genre'].apply(
        lambda x: [
            g.replace("[", "").replace("]", "").replace("'", "").replace('"', "").strip() 
            for g in x
        ] if isinstance(x, list) else []
    )
    df_movies_exploded = df_movies_genre.explode('Genre')

    # Get top 12 genres
    top_genres = (
        df_movies_exploded['Genre']
        .value_counts()
        .head(12)
        .index
    )

    # Proceed with the grouping and proportion calculation
    genre_trends = (
        df_movies_exploded.groupby(['Year', 'Genre'])
        .size()
        .reset_index(name='Count')
    )

    # Calculate total movies per year for proportions
    total_movies_per_year = (
        df_movies_exploded.groupby('Year').size().reset_index(name='TotalMovies')
    )

    # Merge and calculate proportions
    genre_trends = genre_trends.merge(total_movies_per_year, on='Year')
    genre_trends['Proportion'] = genre_trends['Count'] / genre_trends['TotalMovies']

    # Filter only for top genres and return
    return genre_trends[genre_trends['Genre'].isin(top_genres)]