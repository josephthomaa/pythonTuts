import pandas as pd
import dtale

unemp_county = pd.read_csv("archive/EQ010114.CSV")
print(unemp_county.head())
d = dtale.show(unemp_county)
d.open_browser()