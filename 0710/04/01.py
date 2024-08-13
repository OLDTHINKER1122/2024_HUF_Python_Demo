#https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html
import tabula


pdf_path ='data01.pdf'

dfs = tabula.read_pdf(pdf_path,encoding='Big5',stream=True)
# read_pdf returns list of DataFrames
print(len(dfs))
print(dfs[0])

# set pages option
dfs = tabula.read_pdf(pdf_path, pages=3, encoding='Big5',stream=True)
print(dfs[0])


# pass pages as string
dfs =tabula.read_pdf(pdf_path, pages="1,3", encoding='Big5',stream=True)
print(dfs)

# extract all pages
dfs =tabula.read_pdf(pdf_path, pages="all", encoding='Big5',stream=True)
print(dfs)

# set area option
dfs = tabula.read_pdf(pdf_path, area=[0,80,180,500], encoding='Big5',pages=2)
print(dfs[0])


#convert_into
tabula.convert_into(pdf_path, "data01.json", output_format="json", stream=True,pages='all')
tabula.convert_into(pdf_path, "data01.csv", output_format="csv", stream=True,pages='all')