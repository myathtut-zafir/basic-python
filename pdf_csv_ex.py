import csv
import PyPDF2
import re

data=open('find_the_link.csv',encoding='utf-8')

csv_data=csv.reader(data)
data_lines=list(csv_data)
link_str=''
for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]
    # print(data[row_num])

print(link_str)

f=open('Find_the_Phone_Number.pdf','rb')
pdf_reader=PyPDF2.PdfReader(f)
pattern=r'\d{3}.\d{3}.\d{4}'
all_text=''

for n in range(len(pdf_reader.pages)):
    page=pdf_reader.pages[n]
    page_text=page.extract_text()
    all_text=all_text+' '+page_text

print(all_text)
print(re.findall(pattern,all_text))

for match in re.finditer(pattern,all_text):
    print(match)





