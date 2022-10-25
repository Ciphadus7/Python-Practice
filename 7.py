names1 = ['John', 'Dan', 'Mary']
names2= ['tim', 'Steve', 'dan', 'john']

names1_lower = [n.lower() for n in names1]
names_in_both_lists = [name for name in names2 if name.lower() in names1.lower()]

print(names_in_both_lists)