import pandas as pd
import numpy as np

def transform_to_graph(stock_data, index_data):
  """
  Transforms stock time series data to a graph time series data.

  Args:
    stock_data: A Pandas DataFrame of stock data, with columns for ticker, date, and price.
    index_data: A Pandas DataFrame of index data, with columns for index name, date, and value.

  Returns:
    A Pandas DataFrame of graph data, with columns for source, target, date, and weight.
  """

  # Create a dictionary of stock tickers to indices.

  index_map = {}
  for index in index_data.itertuples():
    index_map[index.ticker] = index.index_name

  # Create a graph data frame.

  graph_data = pd.DataFrame()
  for stock in stock_data.itertuples():
    # Add an edge from the stock to the index.
    graph_data = graph_data.append({
      "source": stock.ticker,
      "target": index_map[stock.ticker],
      "date": stock.date,
      "weight": 1.0,
    }, ignore_index=True)

  return graph_data

# Example usage.

stock_data = pd.DataFrame({
  "ticker": ["AAPL", "GOOG", "MSFT"],
  "date": ["2023-07-31", "2023-07-31", "2023-07-31"],
  "price": [150.0, 200.0, 250.0],
})

index_data = pd.DataFrame({
  "ticker": ["NIFTY50", "BANKNIFTY"],
  "index_name": ["NIFTY50", "BANKNIFTY"],
  "date": ["2023-07-31", "2023-07-31"],
  "value": [10000.0, 20000.0],
})

graph_data = transform_to_graph(stock_data, index_data)

print(graph_data)