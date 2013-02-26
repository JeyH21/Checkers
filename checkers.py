import os
stroka=" +"+8*"--+"
mas=[]  #масив одной строки поля
poleigri=[] #массив клеток поля
for i in range(8):#генерация массива с клетками
    mas=[]
    for z in range(8):
       if (z+i)%2==1  and i<3:  #черные(вверхние) шашки
           mas.append("че")
       elif(z+i)%2==1 and i>4:  #белые(нижние) шашки
           mas.append("бе")
       elif(z+i)%2==0:
           mas.append("><")#пустое место
       else:
           mas.append("  ")
    poleigri.append(mas)
def pole():   #функция для генерации поля
    os.system('cls')
    for i in range(8):
        print("  "+chr(ord("A")+i),end="") #нумерация сверху
    print("\n"+stroka)
    for i in range(1,9):
        print(str(9-i),end="") #нумерация сбоку
        print("|",end="")    
        for z in range(8):
            print(poleigri[i-1][z]+"|",end="") #из массива клеток получаем состояние клетки
        print(str(9-i)+"\n"+stroka) #нумерация сбоку 2
    for i in range(8):
        print("  "+chr(ord("A")+i),end="") #нумерация снизу
def xod():
    while 1:    
        while 1:
            st=input("\nход н игрока ") #ход шашки
            st=st.strip() #убираем лишние пробелы в начале строки и в конце
            #Проверяем правильность введенных данных
            try:
                if (1<=int(st[1])<=8 and 1<=int(st[3])<=8)and ((65<=ord(st[0])<=72 and 65<=ord(st[2])<=72))and len(st)<5 :
                    break
                else:
                    print("Нет такой позиции на доске")
            except (IndexError , ValueError) :
                    print("Вы ничего не ввели,или ввели не правильно")
        if (int(st[1])==int(st[3])-1)and(ord(st[0])==ord(st[2])+1 or ord(st[0])==ord(st[2])-1) and poleigri[8-int(st[3])][ord(st[2])-65]=="  "and poleigri[8-int(st[1])][ord(st[0])-65]=="бе": #если ход по диагонали и клетка свободна то ходим
            poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
            poleigri[8-int(st[1])][ord(st[0])-65]="  "
            break
        else:
            print("Данный ход не возможен")
while 1:
    pole()
    xod()
    pole()        
    xod()
    pole()


        
    
  
