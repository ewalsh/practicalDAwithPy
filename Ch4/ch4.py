import pandas as pd

product_data = {
    'product a': [13, 20, 0, 10],
    'product b': [10, 30, 17, 20],
    'product c': [6, 9, 10, 0]
}

purch_data = pd.DataFrame(product_data, index=['Ronny', 'Bobby','Ricky','Mike'])



print(purch_data.loc['Ronny'])
