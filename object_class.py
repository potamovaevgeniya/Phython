class Person():
        def __init__(self,name="",summ=0):
         self.name=name    
         self.summ=summ
         print("Создан пользователь ",self.__str__())
        def __str__(self):
          return self.name + " имеет " + str(self.summ) + " рублей"

person1=Person()
person1.name="Саша"
person1.summ=700

person2=Person("Вася",900)



