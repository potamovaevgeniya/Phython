#Загрузка файла txt
file=open("my.txt","r",encoding="UTF-8")
contents=file.read()
print(contents)
file.close()