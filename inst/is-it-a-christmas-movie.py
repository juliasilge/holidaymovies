# %% Set up ✨
import pandas as pd
import seaborn as sns
from calendar import month_name
import requests
headers = {'User-Agent': 'julia.silge@posit.co'}


# %% Make my function 🛠️
def wikipedia_by_month(wikipedia_page):
    url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{wikipedia_page}/monthly/2018010100/2023123100'
    resp = requests.get(url, headers = headers)
    data = resp.json()
    df = pd.DataFrame(data['items'])
    df = df[['article', 'timestamp', 'views']]
    df['timestamp'] = pd.to_datetime(df['timestamp'], format = '%Y%m%d%H')
    df['month'] = pd.DatetimeIndex(df['timestamp']).month_name()
    df['month'] = pd.Categorical(df['month'], categories = month_name[1:])
    return df


# %% Get the monthly page views 📆
wonderful_life = wikipedia_by_month('It%27s_a_Wonderful_Life')
home_alone = wikipedia_by_month('Home_Alone')


# %% Make a plot 🍿
movies = pd.concat([wonderful_life, home_alone, die_hard])
movies = movies.groupby(['month', 'article'], as_index=False, observed=True)['views'].sum()
sns.barplot(movies, x = 'views', y = 'month', hue = 'article')

