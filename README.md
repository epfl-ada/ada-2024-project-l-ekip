# Globalisation of Cinema: A Comparative Study of National Film Industries
This project explores the evolution of global cinema through an analysis of regional and international film industries, focusing on how economic and demographic shifts have influenced box office performance. By examining significant historical events, we aim to reveal their impact on audience behaviors and the development of local film industries. The study investigates domestic and international box office trends, revealing variations across countries and the interaction between regional preferences and global patterns. Furthermore, it examines the progression of film genres over time, highlighting the impact of important historical events on the cinematographic industry. 

## Website Link
https://titi1000.github.io/ada-website/

## Authors
Hana Salvetová, Quentin Chappuis, Louis Martins, Kelu Huang and Nour Guermazi.
## How to use the dataset?
1. Download the data [here](https://www.cs.cmu.edu/~ark/personas/)
2. Create a folder `dataset/` at the root of the repo
3. Unzip the data you downloaded in the dataset folder
## Research questions
1. How have economic and population shifts influenced box office revenues in regional and global film industries over the last century?
2. How have significant historical events of the last century shaped the development and success of cinema in different countries?
3. How do domestic and international box office trends vary by country, and how do these trends reflect differences in genre popularity? 
## Additional datasets 
To enrich our analysis and provide a more comprehensive understanding of global cinema trends, we integrated several external datasets: 
### Economic Data
- **GDP Growth Data**: Global GDP growth data to understand the economic context of a region and its impact on the film industry.
    [Download](https://www.kaggle.com/datasets/sazidthe1/world-gdp-growth)


### Demographic Data
- **World Population**: world_population.csv – Includes population data by country, which is essential for normalizing box office data and understanding audience size.
    [Download](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)


### Box Office Data 
- **Box Office**: Additional data on box office scrapped from "Box Office Mojo" and "The Numbers" 
 	[Box Office Mojo](https://www.boxofficemojo.com/)  
 	[The Numbers](https://www.the-numbers.com/)

### Datasets Description

The provided dataset contains movie metadata (e.g., release dates, box office revenue) and character metadata (e.g., actor names, ethnicity). 
<br>
To provide a broader economic and demographic context, we supplement this with external datasets:

- **Economic data**:  GDP for correlation analysis with box office revenue

- **Demographic data**: Population figures to better understand audience size and regional market characteristics.

- **Box office data**: An indicator on films success in terms of cinema entry sales.

### Methods

- **Data selection**: We identified relevant economic, demographic, and movie metadata to address research questions on global cinema trends. 

- **Data collection**: we downloaded datasets from Kaggle in .csv format, (inflation, population data) and we scrapped global and local box office revenues from "Box Office Mojo" and "The Numbers" to account for the high percentage of missing box office value in the CMU movie metadata dataset. We also completed those by scrapping Wikidata (the data are in query.csv). Finally for scrapping the domestic and international box office data, we used the GPT API.

- **Data preprocessing**: Cleaning and merging datasets to create a unified data frame including columns standardizartion, filling missing values, removing irrelevant data but also data cleaning/normalization ensuring textual consistency (for example using a uniform naming convention for "China"). This improves data quality and avoids issues like duplicates caused by different representations of the same entity. 

- **Visualization and analysis**: 
Our analysis employs a combination of statistical techniques, machine learning, and advanced visualizations to investigate the globalization of cinema and its driving factors. Specifically, we focus on the following approaches:
We used Python visualization libraries, such as Matplotlib, Seaborn, and Plotly, to explore and communicate insights effectively. Key visualizations include:
    1. Pie charts to analyze the proportions of domestic versus international revenue for different countries, highlighting regional preferences. <br>
    2. Time-series analysis with line plots to track trends in genre popularity, regional box office revenue, and the impact of significant historical events on filmmaking. <br>
    3. Correlation analysis using a heatmap to examine how economic and demographic factors influence the success of local films and Hollywood blockbusters. <br>
    4. To complement the correlation analysis we used regression models and clustering techniques to predict revenue using the same demographic and economic data used for correlation analysis.<br>
    5. We also performed some statistical tests (e.g., Kolmogorov-Smirnov tests)for we compared pre- and post-COVID box office performance for selected countries, assessing the significance of observed differences.

- **Country selection**: To determine the most impactful countries in the film industry (and also avoiding analysis of countries with nearly no data), we selected nations from each region of the world, ensuring a minimum of one per region. Our selection focused on countries with the highest box office revenues, making them the most relevant for our study.

### Organization within the team

- **Hana** took care of the data cleaning and preprocessing. She ensured the datasets are ready for analysis by removing irrelevant data, filling missing values, and standardizing columns across datasets. She also worked on data visualization with Quentin.

- **Louis** handled the mathematical methods, focusing on statistical analysis such as hypothesis testing to assess the significance of observed trends and relationships in the data, helping to validate our findings and strengthen the conclusions drawn from the research.

- **Quentin** developed extensive visualization methods tailored to each research question, using tools like matplotlib and seaborn to create heatmaps, box plots, and line charts that illustrate trends and patterns across various datasets.

- **Kelu** synthesized all results into coherent findings. He prepared the final data story by collating insights from each analysis phase and ensuring they are clearly communicated.

- **Nour** led the writing of the data story, focusing on articulating the project's findings and implications. She also developed the website representing the project.

### Architecture of the project
```tree
└───ada-2024-project-l-ekip
    │   .gitignore
    │   README.md
    │   requirements.txt
    │   results.ipynb
    │
    ├───data
    │       Cleaned_Final_Dataset.csv
    │       CMU_clead_ready_to_merge.csv
    │       CMU_Other_dataset.csv
    │       Cumulative_Movie_Production_Data.csv
    │       dataset_with_domestic_boxoffice.csv
    │       df_movies_preprocessed.csv
    │       events.csv
    │       Final_Dataset.csv
    │       genres.csv
    │       query.csv
    │       world_gdp_2.csv
    │       world_population_2.csv
    │
    └───src
        ├───data
        │       boxoffice_api_request.ipynb
        │       dataset_creation.ipynb
        │
        ├───models
        │       models.py
        │
        ├───scripts
        │       mojoboxoffice_scraper.ipynb
        │       scrapingthenumbers.ipynb
        │
        └───utils
                preprocessing.py
                utils.py
```