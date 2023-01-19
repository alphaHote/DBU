
st=""
with open('json//database.json','r') as f:
    st+=f.read()
data=st.split("\n")
# new="["+ ",".join(data) +"]"
for rec in data[:500]:
    print(rec, end='')
    print()

# with open('json//new_data.json','w') as f:
#     f.write(new)


