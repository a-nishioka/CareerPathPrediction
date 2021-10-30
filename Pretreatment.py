import numpy as np
import pandas as pd
from pandas.core.construction import array


class Pretreatment:

    def __init__(self):
        return

    def __del__(self):
        return

    def fill_none_with_blank(self, dataframe, column_name, text):
        for i in range(len(dataframe[column_name])):
            if(dataframe[column_name][i] is None):
                s = None
                dataframe[column_name][i] = s or ""

    def get_one_hot_vector(self, dataset, column_name):
        element_list = self.get_element_list(dataset, column_name)
        unique_list = self.get_unique_list(element_list)
        for each in unique_list:
            print(each)
        frame_dummy = self.get_dummy_mat(dataset, unique_list, column_name)
        data_frame = pd.DataFrame(frame_dummy, columns=unique_list)
        data_frame.drop(columns="", inplace=True)
        return data_frame

    def get_element_list(self, dataset, column_name):
        all_element_list = ",".join(dataset[column_name])
        element_list = str(all_element_list).split(",")
        all_element_list = [element.strip() for element in element_list]
        return all_element_list

    def get_unique_list(self, text_array):
        return list(set(text_array))

    def get_dummy_mat(self, dataset, unique_list, col_name):
        dummy_mat = np.zeros((dataset.shape[0],  len(unique_list)))

        for i, row in enumerate(dataset[col_name]):
            tmp = row.split(",")
            for one in tmp:
                one = one.strip()
                if one in unique_list:
                    idx = unique_list.index(one)
                    dummy_mat[i, idx] = 1
        return dummy_mat
