#https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html
import tabula
#print(help(tabula.read_pdf))
pdf_path ='data02.pdf'

#dfs = tabula.read_pdf(pdf_path, columns=[47, 147, 256, 310, 375, 431, 504], guess=False, pages=1)
dfs = tabula.read_pdf(pdf_path, columns=[47, 310], guess=False, pages=1)
df = dfs[0].drop(["Unnamed: 0"], axis=1)
print(df)

df.to_csv('ok02.csv')