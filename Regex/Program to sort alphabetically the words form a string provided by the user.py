import regex as re
string=input("enter the string  ")
Regex1=re.compile(r'\w*')
m1=Regex1.search(string)
print(sorted(str(m1.group())))
