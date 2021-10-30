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