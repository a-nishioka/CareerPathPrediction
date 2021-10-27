import Data
import pandas as pd
import StringOperation

data = Data.Data()

# データの結合
rows = data.combine()
del data

# データフレーム化
new_result = [one for one in rows]
dataset = pd.DataFrame(new_result)
dataset.columns = ["offer_id", "company_name", "occupation",
                   "salary_min", "salary_max", "location", "environment", "framework"]
print(dataset.head(5))

# データ前処理
so = StringOperation.StringOperation()
dataset["occupation"].apply(so.normalize)
print(dataset.head(5))
