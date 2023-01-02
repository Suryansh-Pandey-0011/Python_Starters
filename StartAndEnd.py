s=input("str: ")
if s.startswith("Python") and s.endswith("programming"):
    print("valid")
else:
    print("invalid")
print("character with min val:",min(s))
print("character with max val:",max(s))
