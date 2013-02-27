import os
damka=0
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
def Eatme(st):#Нужно кушать
    eat=0
    if poleigri[8-int(st[1])][ord(st[0])-65]=="бе":
        rev="че"   #rev хранит противоположный цвет нашей шашки
    else:
        rev="бе"
    pass
    if ((ord(st[0])-ord(st[2]) +int(st[1])-int(st[3]))%2==0)and (ord(st[0])!=ord(st[2])and int(st[1])!=int(st[3]))  :#Ecли статок ноль ,то ход лежит на диагоналях
        d1=int(ord(st[2])+(ord(st[0])-ord(st[2]))/2)
        d2=int(int(st[3])+(int(st[1])-int(st[3]))/2)
        if damka==0: #если шашка
           if poleigri[8-d2][d1-65]==rev and (int(st[1])==int(st[3])-2 or int(st[1])==int(st[3])+2)and(ord(st[0])==ord(st[2])+2 or ord(st[0])==ord(st[2])-2):
            eat=1
##              poleigri[8-d2] [d1-65]="  "
##              poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
##              poleigri[8-int(st[1])][ord(st[0])-65]="  ")
        else:  #если ДАМКА, пока не работает
            pass  
    return eat
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
    print()
def xod(KolHod):
    if KolHod%2==1:
        igrok="белые"
    else:
        igrok="черные"
    while 1:    
        while 1:
            st=input("Ходят "+igrok+"\n" ) #ход шашки
            st=st.strip() #убираем лишние пробелы в начале строки и в конце
            #Проверяем правильность введенных данных
            try:
                if (1<=int(st[1])<=8 and 1<=int(st[3])<=8)and ((65<=ord(st[0])<=72 and 65<=ord(st[2])<=72))and len(st)<5 :
                    break
                else:
                    print("Нет такой позиции на доскеSAADSADFDSAFDSAFDSA")
            except (IndexError , ValueError) :
                    print("Вы ничего не ввели,или ввели не правильно")
            #Проверяем возможность хода отдельно для белых и черных
        if KolHod%2==1 and poleigri[8-int(st[1])][ord(st[0])-65]=="бе":
            if(int(st[1])==int(st[3])-1)and(ord(st[0])==ord(st[2])+1 or ord(st[0])==ord(st[2])-1) and poleigri[8-int(st[3])][ord(st[2])-65]=="  "  :#если ход по диагонали и клетка свободна то ходим
                poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
                poleigri[8-int(st[1])][ord(st[0])-65]="  "
                break
            eat=Eatme(st)
            if eat==1:
                poleigri[int(8-int(st[3])-(int(st[1])-int(st[3]))/2)] [int(ord(st[2])+(ord(st[0])-ord(st[2]))/2-65)]="  "
                poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
                poleigri[8-int(st[1])][ord(st[0])-65]="  "
                break
            else:
                print("Данный ход невозможен")
        elif KolHod%2==0 and poleigri[8-int(st[1])][ord(st[0])-65]=="че":
            if(int(st[1])==int(st[3])+1)and(ord(st[0])==ord(st[2])+1 or ord(st[0])==ord(st[2])-1) and poleigri[8-int(st[3])][ord(st[2])-65]=="  ":#если ход по диагонали и клетка свободна то ходим
                poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
                poleigri[8-int(st[1])][ord(st[0])-65]="  "
                break
            eat=Eatme(st)
            if eat==1:
                poleigri[int(8-int(st[3])-(int(st[1])-int(st[3]))/2)] [int(ord(st[2])+(ord(st[0])-ord(st[2]))/2-65)]="  "
                poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
                poleigri[8-int(st[1])][ord(st[0])-65]="  "
                break
            else:
                print("Данный ход невозможен")
        else:
            print("Вы можете играть только своими фигурами")
    return KolHod
n=1
while 1:
    pole()
    xod(n)
    n=n+1
   
        
  
