class Person():
        Nurslind=list()
        def __init__(self,name="",summ=0):
         self.name=name    
         self.summ=summ
         print("Создан пользователь ",self.__str__())
        def __str__(self):
          return self.name + " имеет " + str(self.summ) + " рублей"

person1=Person("Саша",700)
person2=Person("Вася",900)

class Nurslind():
        def __init__(self,view="",name="", age="",owner="", callnumber=""):
         self.view=view
         self.name=name
         self.age=age
         self.owner=owner
         self.callnumber=callnumber
         print("Новый клиент ",self.__str__())
        def __str__(self):
          return self.view + self.name + self.age +" лет" + " хозяин " + self.owner + self.callnumber

nurslind1=Nurslind("собака"," Буся"," 5"," Юлия"," +79631524477")