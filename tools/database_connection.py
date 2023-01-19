import pandas as pd
import sqlite3
import os


def from_sql_to_xlsx(db_name:str, xlsx_name:str,table_name:str):
    con = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * from "+table_name, con)
    # print(df.head())
    df.to_excel(xlsx_name)
    con.close()  

def from_xlsx_to_sql(db_name:str, xlsx_name:str,table_name:str):
    database = db_name
    conn = sqlite3.connect(database)
    # df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3'], 'location' : ['location 1', 'location 2', 'location 3']})
    df = pd.read_excel(xlsx_name)
    # print(df.head())
    df.to_sql(name=table_name, con=conn)
    conn.close()

# from_sql_to_xlsx("inventory.db","housni.xlsx","productmovements")
# from_xlsx_to_sql("housni_2.db","housni.xlsx","MVTPRODUIT")
# from_sql_to_xlsx("housni_2.db","housni8TRY.xlsx","MVTPRODUIT")

html_beg="""
<!DOCTYPE html>
<html>
\t<head>
\t\t<style>
\t\t\t#tableau {font-family: Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;}
\t\t\t#tableau td, #tableau th {border: 1px solid #ddd;padding: 8px;}
\t\t\t#tableau tr:nth-child(even){background-color: #f2f2f2;}
\t\t\t#tableau tr:hover {background-color: #ddd;}
\t\t\t#tableau th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #22427C;color: white;}
\t\t</style>
<link rel="stylesheet" href="barre_verticale.css">
<link rel="stylesheet" href="style_button_hover.css">
\t</head>


\t<body>
<div class="w3-sidebar w3-light-grey w3-bar-block" style="width:10%">
  <h3 class="w3-bar-item">Menu</h3>
  <a href="#" class="w3-bar-item w3-button"><button class="button button2">Shadow on Hover</button></a>
  <a href="#" class="w3-bar-item w3-button">Link 2</a>
  <a href="#" class="w3-bar-item w3-button">Link 3</a>
</div>
\t\t<table id="tableau">
"""

html_end="</table></body></html>"

def xlsx_to_html( xlsx_name:str,sheetName:str):
    if sheetName!="":
        df=pd.read_excel(xlsx_name,sheet_name=sheetName)
    else:
        df=pd.read_excel(xlsx_name)
    

    column_names=df.columns
    html="\n<tr>\n"
    for col in column_names:
        html+="\t<th>"+col+"</th>\n"
    html+="</tr>\n"


    for row in df.iloc:
        html+="<tr>\n"
        i=0
        for col in column_names:
            # print("*"*i,row[i])
            html+="\t<td>"+str(row[i])+"</td>\n"
            i+=1
        html+="</tr>\n"

    return html


source=".\\data\\excel\\housni.xlsx"
result=".\\data\\html\\housni.html"
html_=xlsx_to_html(source,"")

with open(result,"w") as f:
    f.write(html_beg+html_+html_end)

os.startfile(result)


