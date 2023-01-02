i=0
while(i==0):
    n=input("vowel or 9 to quit: ")
    if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' or n=='U'):
        print("vowel")
    elif(n=='9'):
        break
    else:
        print("Not a Vowel")
