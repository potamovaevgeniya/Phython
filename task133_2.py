import random
mass1=[]
mass2=[]
mass = [random.randint(0, 100) for i in range(5)]
print (mass)
for i in mass:
    if i>=50:
       mass1.append(i)
    elif i<50:
        mass2.append (i)
print (f"До 50: {sum(mass2)/len (mass2)}")
print (f"После 50: {sum(mass1)/len(mass1)}")