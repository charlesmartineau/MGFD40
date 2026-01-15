#%%
import pandas as pd
import yfinance as yf
from tqdm import tqdm

raw_data = pd.read_csv('assignment/tickers/raw_data.csv').dropna(subset=['Symbol'])

allowed_countries = ['United States', 'Canada']
raw_data = raw_data[raw_data['country'].isin(allowed_countries)]

market_cap = raw_data.sort_values('marketcap', ascending=False).reset_index(drop=True)
market_cap = market_cap.head(1000)
# %%
def process_data():
    valid_tickers = []
    print("Checking 10-year price history for each ticker...")
    for _, row in tqdm(market_cap.iterrows(), total=len(market_cap)):
        ticker = row['Symbol']
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="10y")
            if not hist.empty and (hist.index.min().year <= pd.Timestamp.now().year - 10):
                valid_tickers.append(row)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    valid_market_cap = pd.DataFrame(valid_tickers)
    valid_market_cap.to_csv('assignment/tickers/processed_data.csv', index=False)

#%%
def main():
    valid_market_cap = pd.read_csv('assignment/tickers/processed_data.csv')
    valid_market_cap['decile'] = pd.qcut(
        valid_market_cap['marketcap'].rank(method='first', ascending=False),
        10,
        labels=range(1, 11)
    )

    num_students = 128
    samples = {}
    for d in range(1, 11):
        group = valid_market_cap[valid_market_cap['decile'] == d]
        replace = len(group) < num_students
        samples[d] = group.sample(n=num_students, replace=replace, random_state=42)

    assignments = pd.DataFrame({'Student': range(1, num_students + 1)})
    for d in range(1, 11):
        assignments[f'Ticker {d}'] = samples[d]['Symbol'].tolist()

    # %%
    long_df = assignments.melt(id_vars='Student', var_name='Decile', value_name='Symbol')
    long_df = long_df.drop_duplicates(subset=['Symbol'])
    info_map = market_cap.set_index('Symbol')[['Name','marketcap','country']].to_dict('index')
    long_df['Company Name']       = long_df['Symbol'].map(lambda s: info_map.get(s, {}).get('Name', ''))
    long_df['Market Cap']  = long_df['Symbol'].map(lambda s: info_map.get(s, {}).get('marketcap', ''))
    long_df['Country']    = long_df['Symbol'].map(lambda s: info_map.get(s, {}).get('country', ''))
    long_df = long_df.drop(columns=['Student', 'Decile']).rename(columns={'Symbol': 'Ticker'})
    long_df.to_csv('assignment/tickers/stock_ticker_details.csv', index=False)
    print("Stock ticker details saved")
    # %%
    students = pd.read_csv('assignment/tickers/students.csv')[['StudentID', 'Student Name']]
    assignments = pd.concat([students.reset_index(drop=True), assignments.reset_index(drop=True)], axis=1)
    assignments = assignments.drop(columns=['Student'])
    assignments.to_csv('assignment/tickers/student_assignments.csv', index=False)
    print("Student assignments saved")

if __name__ == "__main__":
    # process_data()
    main()