import requests

for i in range(0,36):
  base_url='https://censusindia.gov.in/2011census/C-16/DDW-C16-STMT-MDDS-'+str(i).zfill(2)+'00.XLSX'
  r=requests.get(base_url)
  with open(str(i).zfill(2)+'.xlsx','wb') as file:
    file.write(r.content)