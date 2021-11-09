## pandas basic methods to study dataset #
- head()
- tail()
- shape
- dtype
- astype
- isnull
- dropna
- fillna

- pd.__version__
- pd.io.excel.xlsx['openpyxl']
- pd.set_option("xlsx","openpyxl")
-  above both options does not work :
-  currently have to specify engine in pd.read_excel itself
-  “openpyxl” supports newer Excel file formats
-  link:https://stackoverflow.com/questions/60288732/pandas-read-excel-returns-pendingdeprecationwarning
-  engine has been specified to deal with warning