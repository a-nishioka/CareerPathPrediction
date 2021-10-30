import numpy as np

class Pretreatment:

    def __init__(self):
        return

    def __del__(self):
        return

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
