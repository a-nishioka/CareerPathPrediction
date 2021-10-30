from matplotlib import pyplot
import Plot
import StringOperation


class Analysis:
    plot = Plot.Plot()
    so = StringOperation.StringOperation()

    def __init__(self):
        self.pyplot = Plot.Plot()
        self.so = StringOperation.StringOperation()

    def __del__(self):
        del self.pyplot
        del self.so

    def analyse(self, dataset):
        self.head(dataset, 5)
        print("------------------------------")
        self.get_datanum(dataset)
        print("------------------------------")
        self.describe(dataset)
        print("------------------------------")
        self.so.check_blank(dataset)
        print("------------------------------")
        self.so.check_zero(dataset)
        print("------------------------------")

    def head(self, dataset, num):
        print(dataset.head(num))

    def get_datanum(self, dataset):
        print('Number of Rows: %i   Number of Columns: %i' % dataset.shape)

    def describe(self, dataset):
        print(dataset.describe())

    def hist(self, dataset, column_name):
        self.pyplot.hist(dataset, column_name)

    def check_blank(self, dataset):
        self.so.check_blank(dataset)

    def check_zero(self, dataset):
        self.so.check_zero(dataset)