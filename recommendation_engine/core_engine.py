import pandas as pd

TRAIN_FILE = '/Users/tenzin.worden/Download/recommendation_engine/train_5UKooLv.csv'
TEST_FILE = '/Users/tenzin.worden/Download/recommendation_engine/test_J1hm2KQ.csv'


def recommender():
    raw_data = pd.read_csv(TRAIN_FILE)
    required_columns = ['CustomerID', 'Quantity', 'InvoiceDate', 'UnitPrice', 'StockCode']
    raw_data = raw_data[required_columns]
    raw_data = raw_data[raw_data['Quantity'] > 0]
