# work just like tables's column or like a column in a table, it is 1D array which holds data of any type
import pandas as pd
prashant=[1,7,2,5,6]
prashant_new=pd.Series(prashant)
print(prashant_new)

# labeling / accessing the values from indexing - label can be use to access specified value
print(prashant_new[3])

#with create label you can create your own name labels

prashant_new=pd.Series(prashant,index=["a","b","c","d","e"])
print(prashant_new)

print("value at 'e' is ", prashant_new["e"])

# can also use key or value like dictionary while creating a series

# here we will create a simple pandas series from dictionary
myDict={"name":"Prashant","Country":"India","Age":25,"Role":"Data Engineer"}
myDict_new=pd.Series(myDict)
print(myDict_new)

# now we will create a series with using name and country

myDict_new=pd.Series(myDict_new,index=("name","Country"))
print(myDict_new)
