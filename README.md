# Globalization of Cinema: A Comparative Study of National Film Industries
This project explores the globalization of cinema through a comparative analysis of national film industries, examining the impact of economic, cultural, and demographic factors on local and international box office performance. By integrating movie metadata with relevant economic and demographic data, we aim to identify key trends influencing film performance across different markets, explore regional preferences, and assess the role of cultural elements such as local actors and themes in shaping commercial success. Our study also delves into the dynamics of global film distribution, highlighting the relationship between national cinemas and Hollywood's dominance. By analyzing patterns in genre popularity, audience engagement, and economic contexts, we provide insights into how regional and global industries have evolved over time. This research contributes to understanding global cultural exchanges and underscores the factors driving the enduring appeal of national cinemas amid globalization, enriching our knowledge of the global cinematic landscape.
## Authors
Hana Salvetová, Nour Guermazi, Kelu Huang, Louis Martins and Quentin Chappuis
## How to use the dataset?
1. Download the data [here](https://www.cs.cmu.edu/~ark/personas/)
2. Create a folder `dataset/` at the root of the repo
3. Unzip the data you downloaded in the dataset folder
## Research questions
1. How have regional and global film industries evolved over time? How shifts in economic, culture, technological and demographic context influenced the development in filmmaking?
2. How do films perform in terms of box office revenue both domestically and internationally? Which regions exhibit the highest preference for local films over global blockbusters, and why?
3. How have regional specificities, including culturally significant themes, genres, and the presence of local actors, evolved over time in comparison to global filmmaking trends? In what ways does the shifting popularity and influence of local actors impact the success of films within their domestic markets over time, and how does this dynamic affect their international appeal?
## Additional datasets
To enrich our analysis and provide a more comprehensive understanding of global cinema trends, we integrated several external datasets:
### Economic Data
- **Cost of Living**: cost-of-living_v2.csv – Contains data on average ticket prices and other living costs by country. 
  
[Download](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living)

- **Inflation Data (1970-2022)**: Global Dataset of Inflation.csv – Provides inflation rates globally, used to adjust box office revenue to constant dollars.

[Download](https://www.kaggle.com/datasets/belayethossainds/global-inflation-dataset-212-country-19702022)

- **Inflation Data (1915-1969)**: Historical inflation data for adjusting older revenues to current dollars.

[Link to the data](https://www.usinflationcalculator.com/inflation/historical-inflation-rates/)

- **GDP Growth Data**: Global GDP growth data to understand the economic context of a region and its impact on the film industry.

[Download](https://www.kaggle.com/datasets/sazidthe1/world-gdp-growth)


### Demographic Data
**World Population**: world_population.csv – Includes population data by country, which is essential for normalizing box office data and understanding audience size.
<br>
[Download](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)


### Box Office Data 
**Box Office**: Additional data on box office scrapped from "Box Office Mojo" and "The Numbers" 
<br>
 			[Box Office Mojo](https://www.boxofficemojo.com/)  
 			[The Numbers](https://www.the-numbers.com/)

### Datasets Description

The provided dataset contains movie metadata (e.g., release dates, box office revenue) and character metadata (e.g., actor names, ethnicity). 
<br>
To provide a broader economic and demographic context, we supplement this with external datasets:

- **Economic data**: average ticket prices, inflation rates, and GDP, essential for adjusting box office figures over 100 years of cinema history.

- **Demographic data**: population figures to better understand audience size and regional market characteristics.

- **Box office data**: an indicator on films success in terms of cinema entry sales.

### Methods

- **Data selection**: We identified relevant economic, demographic, and movie metadata to address research questions on global cinema trends.

- **Data collection**: we downloaded datasets from Kaggle in .csv format, (inflation, population data) and we scrapped global and local box office revenues from "Box Office Mojo" and "The Numbers" to account for the high percentage of missing box office value in the movie metadata dataset.

- **Data preprocessing**: cleaning and merging datasets to create a unified data frame, standardizing columns, filling missing values, and removing irrelevant data.

- **Mathematical adjustments**: applying normalization techniques, such as adjusting box office revenue for inflation, population size, and GDP per capita to allow meaningful comparisons.

- **Visualization**: using matplotlib and seaborn to create heatmaps, box plots, and line charts that reveal trends and patterns in box office success, genre popularity, and ticket prices across countries.

- **Country selection**: to determine the most impactful countries in the film industry, we selected nations from each region of the world, ensuring a minimum of two per region. Our selection focused on countries with the highest box office revenues, making them the most relevant for our study.

### Timeline

- **Week 1**: Detailed analysis of datasets, conduct data cleaning and pre processing 

- **Week 2**: Implement methods to answer proposed research questions 1

- **Week 3**: Implement methods to answer proposed research questions 2

- **Week 4**:  Implement methods to answer proposed research questions 3

- **Week 5**: Gather all results and synthesize our findings in the final version of the data story, publish it on GitHub.

### Organization within the team

- **Hana** will take care of the data cleaning and preprocessing. She will ensure the datasets are ready for analysis by removing irrelevant data, filling missing values, and standardizing columns across datasets.

- **Louis** will handle the mathematical methods, focusing on normalization and statistical analysis. He will integrate inflation data to adjust box office figures, allowing for accurate historical comparisons.

- **Quentin** will develop extensive visualization methods tailored to each research question. He will use tools like matplotlib and seaborn to create heatmaps, box plots, and line charts that illustrate trends and patterns across various datasets.

- **Kelu** will synthesize all results into coherent findings. He will prepare the final data story by collating insights from each analysis phase and ensuring they are clearly communicated.

- **Nour** will lead the writing of the data story, focusing on articulating the project's findings and implications. She will develop the website representing the project.
