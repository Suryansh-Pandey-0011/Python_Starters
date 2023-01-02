'''file=open("C:/PythonPrograms/Files/textfile1.txt","r")'''
'''print(file.read(5))'''
'''for i in range(4):
    print(file.readline().strip())'''
'''file2=open("C:/PythonPrograms/Files/textfile2.txt","a+")
file2.write("Python is a coding language\n")
file2.writelines(["Hello\n","Python is a coding language\n"])
file2.seek(5)
print(file2.read())
file2.close()'''
'''f=open("C:/PythonPrograms/Files/reversedFile.txt","r")
l=f.readlines()
for i in l:
    print(i[::-1].strip())
