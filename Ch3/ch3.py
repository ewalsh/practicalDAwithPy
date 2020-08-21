import numpy as np
import os

# print(os.listdir("./data"))

temp_array = []

with open('./data/AAPL_stock_price_example.csv', 'r') as input_file:
    # load all data into a var
    lines = input_file.readlines()
    # loop over records
    for line in lines:
        for raw_value in line.rsplit(',')[1:]:
            value = raw_value.replace("\n", "").replace("\r", "")
            temp_array.append(value)

temp_array = np.delete(temp_array, 0)
price_arr = temp_array.astype(float)
print(price_arr[0])
