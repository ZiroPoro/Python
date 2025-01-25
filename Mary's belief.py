#https://www.codewars.com/kata/58844a13aa037ff143000072/python
#For young = true, beautiful = true and loved = true, the output should be false.
#Young and beautiful people are loved according to Mary's belief.
#For young = true, beautiful = false and loved = true, the output should be true.
#Mary doesn't believe that not beautiful people can be loved.
def check(value):
    if value=="Да":
        value=True
        print(value)
    elif value=="Нет":
        value=False
        print(value)
    else:
        print("Попробуйте снова и введите корректное значение...")

young=input("Введите молод ли человек (Да или Нет): ")
check(young)
beautiful=input("Введите прекрасен ли человек (Да или Нет) : ")
check(beautiful)
loved=input("Введите любим ли человек (Да или Нет) : ")
check(loved)
if young==True and beautiful==True and loved==True:
    print("Young and beautiful people are loved according to Mary's belief")
elif young==True and beautiful==False and loved==True:
    print("Mary doesn't believe that not beautiful people can be loved")
else:
    print("Произошла ошибка!")
