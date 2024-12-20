import pandas as pd
from scipy.stats import spearmanr, ks_2samp
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures


# Linear regression for each country over the gdp and the population data for each year
def lin_reg(countries, data):
    r2_scores = []

    # Iterate through each country and calculate R² score
    for _, country in enumerate(countries):
        # Filter data for the current country
        country_data = data[data['originLabel'] == country]

        # Independent variables: GDP and Population
        X = country_data[['GDP', 'Population']]
        y = country_data['TotalWorldwideRevenue']

        # Add polynomial terms
        poly = PolynomialFeatures(degree=2, include_bias=False)
        X_poly = poly.fit_transform(X)

        # Fit the regression model
        model = LinearRegression()
        model.fit(X_poly, y)

        # Predict movie revenue
        y_pred = model.predict(X_poly)

        # Calculate R² value
        r2 = r2_score(y, y_pred)
        r2_scores.append({"Country": country, "R² Score": r2})
        print(f'R² score for {country}: {r2}')
    
    # Return the r2 scores for each country
    return r2_scores

# Calculate the spearman correlation for each country between the worlwide revenue and the GDP and the worldwide revenue and the population
def spearman_corr(countries, data):
    results = []

    for country in countries:
        country_data = data[data['originLabel'] == country]

        if len(country_data) > 1:  # Ensure sufficient data points
            corr_gdp, _ = spearmanr(country_data['TotalWorldwideRevenue'], country_data['GDP'])
            corr_population, _ = spearmanr(country_data['TotalWorldwideRevenue'], country_data['Population'])
            results.append({'Country': country, 'Movies - GDP': corr_gdp, 'Movies - Population': corr_population})

    # Convert results to DataFrame and return
    return pd.DataFrame(results)


# KS test for each country
def ks_test(countries, data):
    countries_list = []
    test_stats = []
    p_values = []

    # Run the KS test for each country and collect results
    for country in countries:
        country_data = data[data['originLabel'] == country]
        pre_covid_country = country_data[country_data['Year'].isin([2017, 2018, 2019])]['worldwide']
        post_covid_country = country_data[country_data['Year'].isin([2020, 2021, 2022])]['worldwide']
        
        if len(pre_covid_country) > 1 and len(post_covid_country) > 1:
            k_stat, p_value = ks_2samp(pre_covid_country, post_covid_country, alternative='less')
            countries_list.append(country)
            test_stats.append(k_stat)
            p_values.append(p_value)

    # Create a DataFrame for ease of plotting and return it
    dataframe = pd.DataFrame({
        'Country': countries_list,
        'Test Statistic': test_stats,
        'P-value': p_values
    })
    
    return dataframe