s=input ("Введите строку")
s1=""
for c in s:
    if c == "а":
        s1 += "б"
    elif c=="б":
        s1+="а" 
    elif c=="А":
        s1+="Б"
    elif c=="Б":
        s1+="А" 
    elif c=="C":
        s1+="с"
    else:
        s1+="с" 
print (s1)    