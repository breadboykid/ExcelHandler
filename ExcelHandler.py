import pandas as pd

class ExcelHandler():
    def __init__(self, filename):
        self.filename = filename
        self.excel_data = self.getFileData()

    def getFileData(self):
        return pd.read_excel(self.filename)

    def getDataByColumnName(self, column_name):
        return self.excel_data[column_name]

    def getDataListByColumnName(self, column_name):
        return self.excel_data[column_name].values

    def getRowByColumnNameAndValue(self, column_name, column_value):
        return self.excel_data.loc[self.excel_data[column_name] == column_value]