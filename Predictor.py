import Data
import Analysis
import Pretreatment

data = Data.Data()
analysis = Analysis.Analysis()

# データの結合及びデータフレーム化
dataset = data.combine()
analysis.analyse(dataset)

# 視覚化
#analysis.hist(dataset, data.salary_min)
#analysis.hist(dataset, data.salary_max)

# ダミー変数化
pretreatment = Pretreatment.Pretreatment()
enviroment_df = pretreatment.get_one_hot_vector(dataset, data.environment)
print(enviroment_df)

framework_df = pretreatment.get_one_hot_vector(dataset, data.framework)
print(framework_df)

del data
del analysis
del pretreatment