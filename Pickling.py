import pickle
L1=[1,2,3,4,5,6,'a','b']
f=open("C:/PythonPrograms/Files/pickle.txt","wb")
pickle.dump(L1,f)
f.close()
f2=open("C:/PythonPrograms/Files/pickle.txt","rb")
d=pickle.load(f2)
print(d)
