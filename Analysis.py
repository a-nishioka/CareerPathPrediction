import Plot
import StringOperation
import DFOperation

class Analysis:
    plot = Plot.Plot()
    so = StringOperation.StringOperation()
    dfo = DFOperation.DFOperation()

    def __init__(self):
        self.pyplot = Plot.Plot()
        self.so = StringOperation.StringOperation()
        self.dfo = DFOperation.DFOperation()

    def __del__(self):
        del self.pyplot
        del self.so
        del self.dfo

    def analyse(self, dataframe):
        self.head(dataframe, 5)
        print("------------------------------")
        self.get_datanum(dataframe)
        print("------------------------------")
        self.describe(dataframe)
        print("------------------------------")
        self.dfo.check_none(dataframe)
        print("------------------------------")
        self.dfo.check_blank(dataframe)
        print("------------------------------")        

    def head(self, dataframe, num):
        print(dataframe.head(num))

    def get_datanum(self, dataframe):
        print('Number of Rows: %i   Number of Columns: %i' % dataframe.shape)

    def describe(self, dataframe):
        print(dataframe.describe())

    def hist(self, dataframe, column_name):
        self.pyplot.hist(dataframe, column_name)