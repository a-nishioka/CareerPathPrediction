

from numpy import e


class DFOperation:
    def check_none(self, dataframe):
        print("check_none")
        for col in dataframe.columns:
            print(col, dataframe[col].isnull().sum())

    def check_blank(self, dataframe):
        print("check_blank")
        for column in dataframe.columns:
            blank_data = []
            for each in dataframe[column]:
                if(each == ""):
                    blank_data = each
            print(column, len(blank_data))