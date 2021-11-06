from numpy import dtype, mod
import Data
import Analysis
import Pretreatment
import Model

data = Data.Data()
analysis = Analysis.Analysis()

# データの結合及びデータフレーム化
dataframe = data.combine()
analysis.analyse(dataframe)

# 視覚化
#analysis.hist(dataset, data.salary_min)
#analysis.hist(dataset, data.salary_max)

# 前処理
pretreatment = Pretreatment.Pretreatment()
# 欠損値の補正
dataframe.replace({data.salary_min: {0: dataframe[data.salary_min].median()}})
dataframe.replace({data.salary_max: {0: dataframe[data.salary_max].median()}})
# 0埋め
pretreatment.fill_none(dataframe, data.pass_rank, "")
pretreatment.fill_none(dataframe, data.occupation, "")

# ダミー変数化
pass_rank_df = pretreatment.get_one_hot_vector(dataframe, data.pass_rank)
#print(pass_rank_df)

occupation_df = pretreatment.get_one_hot_vector(dataframe, data.occupation)
#print(occupation_df)

enviroment_df = pretreatment.get_one_hot_vector(dataframe, data.environment)
#print(enviroment_df)

framework_df = pretreatment.get_one_hot_vector(dataframe, data.framework)
#print(framework_df)

dataframe = pretreatment.merge_dummies(dataframe, pass_rank_df, occupation_df, enviroment_df, framework_df)
data.output_csv(dataframe)

# 年収予測
model = Model.Model()

# ターゲット変数と特徴量を作成する
target_col = data.salary_min
exclude_cols = [data.salary_min, data.salary_max, data.offer_id, data.company_name, data.pass_rank, data.occupation, data.location, data.environment, data.framework]
model.supervised_learn(dataframe, target_col, exclude_cols)

del data
del analysis
del pretreatment
del model