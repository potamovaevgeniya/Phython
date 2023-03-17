#Викторина по фактам  (список)
print("Добро пожаловать на виторину по интересным фактам")

questions=["Есть ли атмосфера у солнца?","Является ли светлячок жуком?","Есть ли у Марса магнитное поле?", "Является ли органом кожа человека?","Кто может дольше обходиться без воды: жираф или верблюд?"]

answers=["Да","Да","Нет","Да","Жираф"]

score=0

for i in range (answers):    
    for j in questions:
      print(questions[i])
      answers=input("Ваш ответ: ")
        if answers==answers[j]:
          print("Верно")
          score +=20
        else:
          print("Неверно")

#for i in answers:
    #for j in questions:
        #print(questions[i])
        #answers=input("Ваш ответ: ")
        #if answers==answers[i]:
          #print("Верно")
          #score +=20
        #else:
          #print("Неверно")

print("Вы набрали " + str(score) + " баллов")
if score>=80:
   print("Вы молодец!")
elif score<80 and score>=50:
   print("Немного не хватило сил")
else:
   print("Вам есть куда стремиться")