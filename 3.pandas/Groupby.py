filepath = os.path.abspath("C:\Users\Auxo User\Documents\DataSet\Weather.csv")
data = pd.read_csv(filepath, index_col='Date', parse_dates=True)