import os
import pandas as pd
from apyori import apriori

file = os.path.dirname(__file__)+'\\store_data.csv'
df = pd.read_csv(file, header=None)

records = [[item for item in row if not isinstance(item,float)] for row in df.values]
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3)
for rule in association_rules:
    items, support, ordered_stastistics = rule
    base, add, confidence, lift = ordered_stastistics[0]
    items, base, add= ', '.join(items), ', '.join(base), ', '.join(add)
    print(f'Support for {items} : {support}')
    print(f'Rule : {base} --> {add}')
    print(f'confidence : {confidence}')
    print(f'lift : {lift}')
