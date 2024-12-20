import pandas as pd


### EVENTS
# Events that we chose DataFrame
events_df = pd.DataFrame({
    'Event': ['COVID-19', 'New Wave Movement', 'World War 1', 'World War 2', 'Digital Revolution and CGI', 'Baby Boom', 'Post-Colonial'],
    'StartYear': [2019, 1959, 1914, 1939, 1990, 1946, 1945],
    'EndYear': [2021, 1974, 1918, 1945, 2000, 1965, 1964]
})

# Function to determine active event for a given year
def get_event_for_year(year):
    active_events = events_df[(events_df['StartYear'] <= year) & (events_df['EndYear'] >= year)]
    if not active_events.empty:
        return ', '.join(f"{row['Event']}" for _, row in active_events.iterrows())
    return "No significant events for this year"


### MAPPINGS

# Mapping of countries to their continent
countries_by_continent = {
    "Africa": [
        "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", 
        "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", 
        "Congo", "Djibouti", "Egypt", "Equatorial Guinea", 
        "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", 
        "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", 
        "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", 
        "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", 
        "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
        "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", 
        "Zimbabwe"
    ],
    "Asia": [
        "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", 
        "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", 
        "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", 
        "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", 
        "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", 
        "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", 
        "Syria", "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan", 
        "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen", "Hong Kong"
    ],
    "Europe": [
        "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", 
        "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Estonia", 
        "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", 
        "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", 
        "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", 
        "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", 
        "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", 
        "Switzerland", "Ukraine", "United Kingdom", "Vatican City", "Turkey"
    ],
    "North America": [
        "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", 
        "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", 
        "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", 
        "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", 
        "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States of America"
    ],
    "South America": [
        "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", 
        "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
    ],
    "Oceania": [
        "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", 
        "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", 
        "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
    ]
}

# Function to map country to continent
def map_continent(continent, mapping):
    for broad_continent, specific_country in mapping.items():
        if continent in specific_country:
            return broad_continent
    return None 

# Country code mapping for our preprocessing
country_code_mapping = {"USA": "United States of America", "CAN": "Canada", "DEU": "Germany",
                        "GBR": "United Kingdom", "FRA": "France", "AUS": "Australia",
                        "JPN": "Japan", "CHN": "China", "HKG": "Hong Kong", 
                        "IND": "India", "KOR": "South Korea", "ZAF": "South Africa", 
                        "MEX": "Mexico", "NGA": "Nigeria", "ARG": "Argentina"}

### SELCTION OF COUNTRIES

# Our selection of countries for the analysis  
countries = ["United States of America", "Canada", "Germany", "United Kingdom", 
             "France", "Australia", "Japan", "China", 
             "Hong Kong", "India", "South Korea", "South Africa", "Mexico", 
             "Nigeria", "Argentina"]


### COLORMAPS (colormaps for plotly plots)

continent_colors = {
    'Africa': 'limegreen',
    'Asia': 'orange',
    'Europe': 'dodgerblue',
    'North America': 'violet',
    'Oceania': 'red',
    'South America': 'teal'
}

colormap_boxoffice = {
    "United States of America": "#1f77b4",
    "Canada": "#ff7f0e",
    "Germany": "#2ca02c",
    "United Kingdom": "#d62728",
    "France": "#9467bd", 
    "Australia": "#8c564b",
    "Japan": "#e377c2",
    "China": "#7f7f7f",
    "Hong Kong": "#bcbd22",
    "India": "#17becf", 
    "South Korea": "#e6550d",
    "South Africa": "#636363",
    "Mexico": "#98df8a",
    "Nigeria": "#ff9896", 
    "Argentina": "#c5b0d5" 
}
