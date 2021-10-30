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

# データ前処理
pretreatment = Pretreatment.Pretreatment()
environment_ele_list = pretreatment.get_element_list(dataset, data.environment)
enviroment_unique_list = pretreatment.get_unique_list(environment_ele_list)

framework_ele_list = pretreatment.get_element_list(dataset, data.framework)
framework_unique_list = pretreatment.get_unique_list(framework_ele_list)

for text in framework_unique_list:
    print(text)

del data
del analysis
del pretreatment