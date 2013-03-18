import os
black=12 #кол-во шашек
white=12
stroka=" +"+8*"--+"
mas=[]  #масив одной строки поля
poleigri=[] #массив клеток поля
n=1 #номер хода
c=0# константа для белых -1 для черных 1 ,нужна потому что белые ходят вверх п черные вниз
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
    global black
    global white
    global n
    if n%2==1:
        rev="че"   #rev хранит противоположный цвет нашей шашки
        rev2="ДЧ"
    else:
        rev="бе"
        rev2="ДБ"
    pass
    if (int(st[1])==int(st[3])+2 or int(st[1])==int(st[3])-2 )and(ord(st[0])==ord(st[2])+2 or ord(st[0])==ord(st[2])-2):
        d1=int(ord(st[2])+(ord(st[0])-ord(st[2]))/2)
        d2=int(int(st[3])+(int(st[1])-int(st[3]))/2)
        if poleigri[8-int(st[1])][ord(st[0])-65]==("бе") or poleigri[8-int(st[1])][ord(st[0])-65]==("че"): #если шашка
            if  ((poleigri[8-d2][d1-65]==rev)or (poleigri[8-d2][d1-65]==rev2)):
                eat=1
                if poleigri[8-int(st[1])][ord(st[0])-65]==("бе"):
                    black=black-1
                else:
                    white=white-1
                poleigri[int(8-int(st[3])-(int(st[1])-int(st[3]))/2)] [int(ord(st[2])+(ord(st[0])-ord(st[2]))/2-65)]="  "
                poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
                poleigri[8-int(st[1])][ord(st[0])-65]="  "
                try:    
                    if   ((poleigri[8-int(st[3])+1][ord(st[2])-65+1]==(rev or rev2)and poleigri[8-int(st[3])+2][ord(st[2])-65+2]=="  ")
                       or (poleigri[8-int(st[3])+1][ord(st[2])-65-1]==(rev or rev2)and poleigri[8-int(st[3])+2][ord(st[2])-65-2]=="  ")
                       or (poleigri[8-int(st[3])-1][ord(st[2])-65+1]==(rev or rev2)and poleigri[8-int(st[3])-2][ord(st[2])-65+2]=="  ")
                       or (poleigri[8-int(st[3])-1][ord(st[2])-65-1]==(rev or rev2)and poleigri[8-int(st[3])-2][ord(st[2])-65-2]=="  ")):
                       pole()
                       print("ешь еще раз")
                       xod(1,st)
                  
                except IndexError:
                    pass
        elif poleigri[8-int(st[1])][ord(st[0])-65]==("ДБ" or "ДЧ"): #если дамка
            pass  
        else:  
            pass
    
       
    return eat
def pole():   #функция для генерации поля
    print("Осталось "+str(black)+" черных")
    print("Осталось "+str(white)+" белых")
    os.system('cls')
    for i in range(8):
        print("  "+chr(ord("A")+i),end="") #нумерация сверху
    print("\n"+stroka)
    for i in range(1,9):
        print(str(9-i),end="") #нумерация сбоку
        print("|",end="")    
        for z in range(8):
            print(poleigri[i-1][z][0:2]+"|",end="") #из массива клеток получаем состояние клетки
        print(str(9-i)+"\n"+stroka) #нумерация сбоку 2
    for i in range(8):
        print("  "+chr(ord("A")+i),end="") #нумерация снизу
    print()
def xod(f,stold): #если f=1 то только есть
    global n, black, white
    if n%2==1:
        igrok="белые"
        c=-1
    else:
        igrok="черные"
        c=1
    while 1: 
        while 1:  #цикл проверки правильности ввода хода
            st=input("Ходят "+igrok+"\n" ) #ход шашки
            st=st.strip() #убираем лишние пробелы в начале строки и в конце
            if st=="gameover" and igrok=="белые":
                print("Белые сдаются")
                white=0
                break
            elif st=="gameover" and igrok=="черные":
                print("Черные сдаются")
                black=0
                break
            try:              #Проверяем правильность введенных данных
                if (f==0 or (f==1 and st[0:1]==stold[2:3])):
                    if(1<=int(st[1])<=8 and 1<=int(st[3])<=8)and ((65<=ord(st[0])<=72 and 65<=ord(st[2])<=72))and len(st)<5:
                        break
                    else: 
                         print("Нет такой позиции на доске")
                else:
                    print("Ешь той шашкой которой ел до этого")            
            except (IndexError , ValueError) :
                    print("Вы ничего не ввели,или ввели не правильно")
            #Проверяем возможность хода 
        if black==0 or white==0:
            break
        if  (n%2==1 and poleigri[8-int(st[1])][ord(st[0])-65]==("бе"))or(n%2==0 and poleigri[8-int(st[1])][ord(st[0])-65]==("че")):#если ход своей фигурой
            if  poleigri[8-int(st[3])][ord(st[2])-65]==("  "):#проверка на занятость клетки
                if (int(st[1])==int(st[3])+c)and(ord(st[0])==ord(st[2])+1 or ord(st[0])==ord(st[2])-1)and f==0:#если ход по диагонали
                    poleigri[8-int(st[3])][ord(st[2])-65]=poleigri[8-int(st[1])][ord(st[0])-65]
                    poleigri[8-int(st[1])][ord(st[0])-65]="  "
                    if  n%2==0 and int(st[3])==1:     # если дошел до конца поля то дамка
                        poleigri[8-int(st[3])][ord(st[2])-65]="ДЧ"
                    elif n%2==1 and int(st[3])==8:
                        poleigri[8-int(st[3])][ord(st[2])-65]="ДБ"
                    break
                elif Eatme(st)==1: #КУШАТЬ
                     if  n%2==0 and int(st[3])==1:     # если дошел до конца поля то дамка
                        poleigri[8-int(st[3])][ord(st[2])-65]="ДЧ"
                     elif n%2==1 and int(st[3])==8:
                        poleigri[8-int(st[3])][ord(st[2])-65]="ДБ"
                     break
                else:
                   print("Данный ход невозможен")
                   
            else:
                print("Данная клетка занята")
        else:
             print("Играйте своими фигурами")
            

while 1:
    if black==0:
        print("Белые выиграли")
        break
    elif white==0:
        print("Черные выиграли")
        break
    pole()
    xod(0,"")
    n=n+1
