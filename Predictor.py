import Data
import Analysis

data = Data.Data()
analysis = Analysis.Analysis()

# データの結合及びデータフレーム化
dataset = data.combine()
analysis.analyse(dataset)

# 視覚化
analysis.hist(dataset, data.salary_min)
analysis.hist(dataset, data.salary_max)

# データ前処理

del data
del analysis