import numpy as np
import matplotlib.pyplot as plt
import Data

data = Data.Data()

# データの結合及びデータフレーム化
dataset = data.combine()
del data

print(dataset.head(5))

print('Number of Rows: %i   Number of Columns: %i' % dataset.shape)
print(dataset.describe())

plt.hist(dataset['salary_min'])
plt.show()

plt.hist(dataset['salary_max'])
plt.show()