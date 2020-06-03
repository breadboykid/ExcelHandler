import ExcelHandler as eh

#instantiate class with excel filename variable
excel_file = eh.ExcelHandler('filename.xlsx')
#get list by column name, in this case 'Hospitals'
hospital_list = excel_file.getDataListByColumnName('Hospitals')

#example code use in library
#get second row from excel file
print(excel_file.excel_data.iloc[2])

print()
#get all rows with column name 'Hospitals' of value 'North Middlesex Hospital'
print(excel_file.getRowByColumnNameAndValue('Hospitals', 'North Middlesex Hospital'))

print()
#get hospital name with a given institute number
print('Hospital name with institute number 15324: ')
print(excel_file.getRowByColumnNameAndValue('Institute Number', 15324)['Hospitals'].iloc[0])

print()
print(excel_file.getDataListByColumnName('Hospitals'))