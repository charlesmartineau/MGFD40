#%%
import pandas as pd

raw_data = pd.read_csv('assignment/tickers/raw_data.csv').dropna(subset=['Symbol'])
# %%
allowed_countries = ['United States', 'China', 'Japan', 'Canada', 'United Kingdom', 'Germany', 'Switzerland', 'France', 'South Korea', 'Hong Kong', 'Taiwan']
raw_data = raw_data[raw_data['country'].isin(allowed_countries)]

market_cap = raw_data.sort_values('marketcap', ascending=False).reset_index(drop=True)
market_cap = market_cap.head(1200)
market_cap['decile'] = pd.qcut(
    market_cap['marketcap'].rank(method='first', ascending=False),
    10,
    labels=range(1, 11)
)
# %%
num_students = 120
samples = {}
for d in range(1, 11):
    group   = market_cap[market_cap['decile'] == d]
    replace = len(group) < num_students
    samples[d] = group.sample(n=num_students, replace=replace, random_state=42)

# Build assignment table so each student gets one ticker from each decile
assignments = pd.DataFrame({'Student': range(1, num_students+1)})
for d in range(1, 11):
    assignments[f'Ticker {d}'] = samples[d]['Symbol'].tolist()

# Save the assignment grid
assignments.to_csv('assignment/tickers/student_assignments.csv', index=False)

# %%
long_df = assignments.melt(id_vars='Student', var_name='Decile', value_name='Symbol')
info_map = market_cap.set_index('Symbol')[['Name','marketcap','country']].to_dict('index')
long_df['Company Name']       = long_df['Symbol'].map(lambda s: info_map.get(s, {}).get('Name', ''))
long_df['Market Cap']  = long_df['Symbol'].map(lambda s: info_map.get(s, {}).get('marketcap', ''))
long_df['Country']    = long_df['Symbol'].map(lambda s: info_map.get(s, {}).get('country', ''))
long_df = long_df.drop(columns=['Student', 'Decile']).rename(columns={'Symbol': 'Ticker'})
long_df.to_csv('assignment/tickers/stock_ticker_details.csv', index=False)
# %%
