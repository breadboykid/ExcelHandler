import ExcelHandler as eh

#instantiate class with excel filename variable
excel_file = eh.ExcelHandler('filename.xlsx')
#get list by column name, in this case 'Hospitals'
hospital_list = excel_file.getDataListByColumnName('Hospitals')

##
## code use in library
##

#get second row from excel file
second_row_excel_file = excel_file.excel_data.iloc[2]

#get all rows with column name 'Hospitals' of value 'North Middlesex Hospital'
nmh_row_data = excel_file.getRowByColumnNameAndValue('Hospitals', 'North Middlesex Hospital')


#get hospital name with a given institute number
hosptal_by_institute_number =  excel_file.getRowByColumnNameAndValue('Institute Number', 15324)['Hospitals'].iloc[0]

print('-----------------------------')
print(second_row_excel_file)
print('-----------------------------')
print(nmh_row_data)
print('-----------------------------')
print('Hospital name with institute number 15324: \n', hosptal_by_institute_number)
print('-----------------------------')
print(hospital_list)
