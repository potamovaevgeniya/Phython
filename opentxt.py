#Загрузка файла txt
file=open("my.txt","r")
contents=file.read()
print(contents)
file.close()