class Person():
        def __init__(self,name="",money=0):
         self.name=name    
         self.money=money
         print("Создан пользователь ",self.__str__())
        def __str__(self):
          return self.name + " имеет " + str(self.money) + " рублей"

person1=Person()
person1.name="Саша"
person1.money=700

person2=Person("Вася",900)
person2.money=500

