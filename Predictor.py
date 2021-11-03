import Data
import Analysis
import Pretreatment

data = Data.Data()
analysis = Analysis.Analysis()

# データの結合及びデータフレーム化
dataframe = data.combine()
analysis.analyse(dataframe)

# 視覚化
#analysis.hist(dataset, data.salary_min)
#analysis.hist(dataset, data.salary_max)

# ダミー変数化
pretreatment = Pretreatment.Pretreatment()
pretreatment.fill_none_with_blank(dataframe, data.pass_rank, "")
pass_rank_df = pretreatment.get_one_hot_vector(dataframe, data.pass_rank)
print(pass_rank_df)

pretreatment.fill_none_with_blank(dataframe, data.occupation, "")
occupation_df = pretreatment.get_one_hot_vector(dataframe, data.occupation)
print(occupation_df)

enviroment_df = pretreatment.get_one_hot_vector(dataframe, data.environment)
print(enviroment_df)

framework_df = pretreatment.get_one_hot_vector(dataframe, data.framework)
print(framework_df)

merged_df = pretreatment.merge_dummies(dataframe, pass_rank_df, occupation_df, enviroment_df, framework_df)
data.output_csv(merged_df)

del data
del analysis
del pretreatment