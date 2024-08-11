import PyPDF2

data=open('Working_Business_Proposal.pdf','rb')
pdf_reader=PyPDF2.PdfReader(data)
# print(len(pdf_reader.pages))

p1=pdf_reader.pages[1]
p1_text=p1.extract_text()
# print(p1_text)
data.close()

data=open('Working_Business_Proposal.pdf','rb')
pdf_reader=PyPDF2.PdfReader(data)

first=pdf_reader.pages[1]
pdf_writer=PyPDF2.PdfWriter()
pdf_writer.add_page(first)
new_file=open('new_file.pdf','wb')
pdf_writer.write(new_file)
new_file.close()


data=open('Working_Business_Proposal.pdf','rb')
pdf_text=[]
pdf_reader=PyPDF2.PdfReader(data)
for key in range(len(pdf_reader.pages)):
    page=pdf_reader.pages[key]
    pdf_text.append(page.extract_text)

print(pdf_text)
