import csv
data=open('example.csv',encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
# print(data_lines[1])

for line in data_lines[:5]: #[:5] start to 5
    print(line)

print(data_lines[10][3]) # email

file_to_output=open('to_save_file.csv',mode='w',newline='')
csv_writer=csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','bm','c'])
csv_writer.writerows([['a','bm','c'],['aa','bma','ca'],['acc','bmcc','ccc']])
file_to_output.close()

data=open('to_save_file.csv',encoding='utf-8')
cs_data=csv.reader(data)
print(list(cs_data))
