import matplotlib.pyplot as plt


class Plot:
    def hist(self, dataset, column_name):
        plt.hist(dataset[column_name])
        plt.show()