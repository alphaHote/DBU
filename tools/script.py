import pandas as pd
import json   as js

# Excel = pd.read_excel('excel\\spectacles.xlsx',sheet_name='spectacles')
# Json = js.loads(Excel.to_json(orient='records'))
# # print(Json)
# # print(type(Json))
# # for student in Json:
# #     print(student["nom"])
# out_file = open("json\\spectacles.json", "w")
# js.dump(Json, out_file, indent = 2)
# out_file.close()

df=pd.read_json('data\\json\\new_data.json')
for col in df.columns:
    print(col)

# for ligne in df.to_records():
#     print(ligne)


# print(df['address'])
