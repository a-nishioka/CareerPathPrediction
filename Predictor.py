import Data
import Analysis
import Pretreatment
import pandas as pd

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
environment_ele_list = pretreatment.get_element_list(dataset, data.environment)
enviroment_unique_list = pretreatment.get_unique_list(environment_ele_list)

enviroment_frame_dummy = pretreatment.get_dummy_mat(dataset, enviroment_unique_list, data.environment)
enviroment_frame_df = pd.DataFrame(enviroment_frame_dummy, columns=enviroment_unique_list)
enviroment_frame_df.drop(columns="", inplace=True)

framework_ele_list = pretreatment.get_element_list(dataset, data.framework)
framework_unique_list = pretreatment.get_unique_list(framework_ele_list)

del data
del analysis
del pretreatment