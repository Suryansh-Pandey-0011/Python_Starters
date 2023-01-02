"""ch=input("num: ")
if ch=='1' or ch=='2' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9' :
      print("character is a digit")
elif ch == '0':
      exit()
elif ch=='!' or ch=='@' or ch=='#' or ch=='$' or ch=='%' or ch=='^' or ch=='&' or ch=='*':
      print("character is neither alphabet  nor digit")
else:
      print("character is alphabet")"""
ch=ord(input("num: "))
if (ch>=33 and ch<=47) or (ch>=58 and ch<=64) or (ch>=91 and ch<=96) or (ch>=123 and ch<=126):
      print("character is neither alphabet  nor digit")
elif(ch>=49 and ch<=57):
      print("character is a digit")
elif (ch=='0'):
      exit()
else:
      print("character is alphabet")
