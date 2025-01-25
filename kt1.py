import random;
connection = random.randint(0,1)
email=input("Введите почту: ")
if connection==True:
    while connection==True:
        if "@" and "." in email:
            print("Ваша почта принята, аккаунт зарегистрирован")
            break
        else:
            print("Ваша почта недействительна, повторите попытку")
            break
else: 
    print("Отсутствует подключение к интернету. Повторите попытку!")