import os
def Eatme(st):#Нужно кушать
    eat=0
    global black, white, n, rev, rev2
    if (int(st[1])==int(st[3])+2 or int(st[1])==int(st[3])-2 )and(ord(st[0])==ord(st[2])+2 or ord(st[0])==ord(st[2])-2):
        d1=int(ord(st[2])+(ord(st[0])-ord(st[2]))/2)
        d2=int(int(st[3])+(int(st[1])-int(st[3]))/2)
        if poleigri[8-int(st[1])][ord(st[0])-64]==("бе") or poleigri[8-int(st[1])][ord(st[0])-64]==("че"): #если шашка
            if  ((poleigri[8-d2][d1-64]==rev)or (poleigri[8-d2][d1-64]==rev2)):
                eat=1
                if poleigri[8-int(st[1])][ord(st[0])-64]==("бе"):
                    black=black-1
                else:
                    white=white-1
                poleigri[int(8-int(st[3])-(int(st[1])-int(st[3]))/2)] [int(ord(st[2])+(ord(st[0])-ord(st[2]))/2-64)]="  "
                poleigri[8-int(st[3])][ord(st[2])-64]=poleigri[8-int(st[1])][ord(st[0])-64]
                poleigri[8-int(st[1])][ord(st[0])-64]="  "
                if  n%2==0 and int(st[3])==1:     # если дошел до конца поля то дамка
                       poleigri[8-int(st[3])][ord(st[2])-64]="ДЧ"
                elif n%2==1 and int(st[3])==8:
                       poleigri[8-int(st[3])][ord(st[2])-64]="ДБ"
                try:    
                    if  (((poleigri[8-int(st[3])+1][ord(st[2])-64+1]==rev or poleigri[8-int(st[3])+1][ord(st[2])-64+1]==rev2)and poleigri[8-int(st[3])+2][ord(st[2])-64+2]=="  ")
                       or ((poleigri[8-int(st[3])+1][ord(st[2])-64-1]==rev or poleigri[8-int(st[3])+1][ord(st[2])-64-1]==rev2)and poleigri[8-int(st[3])+2][ord(st[2])-64-2]=="  ")
                       or ((poleigri[8-int(st[3])-1][ord(st[2])-64+1]==rev or poleigri[8-int(st[3])-1][ord(st[2])-64+1]==rev2)and poleigri[8-int(st[3])-2][ord(st[2])-64+2]=="  ")
                       or ((poleigri[8-int(st[3])-1][ord(st[2])-64-1]==rev or poleigri[8-int(st[3])-1][ord(st[2])-64-1]==rev2)and poleigri[8-int(st[3])-2][ord(st[2])-64-2]=="  ")):
                       pole()
                       print("ешь еще раз")
                       xod(1,st)
                except IndexError:
                    pass
                #ЕСТ ДАМКА!!!!    ЕСТ ДАМКА!!!!    ЕСТ ДАМКА!!!!
    if  (abs(ord(st[0])-ord(st[2]))==abs(int(st[1])-int(st[3])))and poleigri[8-int(st[1])][ord(st[0])-64]==("ДБ") or poleigri[8-int(st[1])][ord(st[0])-64]==("ДЧ") :#если ход по диагонали
        a=(ord(st[0])-ord(st[2]))/abs(ord(st[0])-ord(st[2])) #изменение по вертикале
        b=-(int(st[1])-int(st[3]))/abs(int(st[1])-int(st[3])) #изменение по горизонтале
        stroka=[]
        mestorev=-1# место шашки,которую будет есть дамка
        for i in range(1,abs(int(st[1])-int(st[3])+1)):
            if (poleigri[int(8-int(st[1])+a*i)][int(ord(st[0])-64+b*i)]==rev)or(poleigri[int(8-int(st[1])+a*i)][int(ord(st[0])-64+b*i)]==rev2):
                mestorev=i
            stroka.append(poleigri[int(8-int(st[1])+a*i)][int(ord(st[0])-64+b*i)])
            print(poleigri[int(8-int(st[1])+a*i)][int(ord(st[0])-64+b*i)])
        try:
            for i in range(20):  #УДАЛЯЕМ ПРОБЕЛЫ,ЕСЛИ кол-во оставшихся элементов =1 то ход возможен
                stroka.remove('  ')
        except ValueError:
            pass
        if len(stroka)==1 and (stroka[0]==rev) or (stroka[0]==rev2):
            eat=1
            if poleigri[8-int(st[1])][ord(st[0])-64]==("ДБ"):
                black=black-1
            else:
                white=white-1
            poleigri[int(8-int(st[1]))][int(ord(st[0]))-64]="  "
            poleigri[int(8-int(st[1])+a*mestorev)][int(ord(st[0])-64+b*mestorev)]="  "
            poleigri[8-int(st[3])][ord(st[2])-64]=poleigri[8-int(st[1])][ord(st[0])-64]
        else:
            eat=0
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
        for z in range(1,9):
            print(poleigri[i-1][z]+"|",end="") #из массива клеток получаем состояние клетки
        print(str(9-i)+"\n"+stroka) #нумерация сбоку 2
    for i in range(8):
        print("  "+chr(ord("A")+i),end="") #нумерация снизу
    print()
def xod(f,stold): #если f=1 то только есть
    global n, black, white, rev , rev2
    if n%2==1:
        igrok="белые"
        c=-1
        rev="че"   #rev хранит противоположный цвет нашей шашки
        rev2="ДЧ"
    else:
        igrok="черные"
        c=1
        rev="бе"
        rev2="ДБ"
    while 1: 
        while 1:  #цикл проверки правильности ввода хода
            st=input("Ходят "+igrok+"\n" ) #ход шашки
            st=st.strip() #убираем лишние пробелы в начале строки и в конце
            st=st.upper()
            if st=="GAMEOVER" and igrok=="белые":
                print("Белые сдаются")
                white=0
                break
            elif st=="GAMEOVER" and igrok=="черные":
                print("Черные сдаются")
                black=0
                break
            try:              #Проверяем правильность введенных данных
                if (f==0 or (f==1 and st[0:1]==stold[2:3])):
                    if(1<=int(st[1])<=8 and 1<=int(st[3])<=8)and ((64<=ord(st[0])<=72 and 64<=ord(st[2])<=72))and len(st)<5:
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
        if  (n%2==1 and ((poleigri[8-int(st[1])][ord(st[0])-64]==("бе"))or (poleigri[8-int(st[1])][ord(st[0])-64]==("ДБ"))))or(n%2==0 and ((poleigri[8-int(st[1])][ord(st[0])-64]==("че"))or(poleigri[8-int(st[1])][ord(st[0])-64]==("ДЧ")))):
             if  poleigri[8-int(st[3])][ord(st[2])-64]==("  "):#проверка на занятость клетки
                if (int(st[1])==int(st[3])+c)and(ord(st[0])==ord(st[2])+1 or ord(st[0])==ord(st[2])-1)and f==0:#если ход по диагонали
                    poleigri[8-int(st[3])][ord(st[2])-64]=poleigri[8-int(st[1])][ord(st[0])-64]
                    poleigri[8-int(st[1])][ord(st[0])-64]="  "
                    if  n%2==0 and int(st[3])==1:     # если дошел до конца поля то дамка
                        poleigri[8-int(st[3])][ord(st[2])-64]="ДЧ"
                    elif n%2==1 and int(st[3])==8:
                        poleigri[8-int(st[3])][ord(st[2])-64]="ДБ"
                    break
            #ХОДИТ ДАМКА!!!!!!!!!            #ХОДИТ ДАМКА!!!!!!!!!             #ХОДИТ ДАМКА!!!!!!!!!
                elif (poleigri[8-int(st[1])][ord(st[0])-64]=="ДБ")or(poleigri[8-int(st[1])][ord(st[0])-64]=="ДЧ"): #Ход дамки
                    if abs(ord(st[0])-ord(st[2]))==abs(int(st[1])-int(st[3])): #если ход по диагонали
                        b=-(ord(st[0])-ord(st[2]))/abs(ord(st[0])-ord(st[2])) #изменение по горизонтале
                        a=(int(st[1])-int(st[3]))/abs(int(st[1])-int(st[3])) #изменение по вертикале
                        xodDamki=1 #Если ходДамки равен 1 то на её пути нет препятствий
                        for i in range(1,abs(int(st[1])-int(st[3]))):
                            print(poleigri[int(8-int(st[1])+a*i)][int(ord(st[0])-64+b*i)])
                            if poleigri[int(8-int(st[1])+a*i)][int(ord(st[0])-64+b*i)]!="  ":
                                xodDamki=0
                                break
                        if xodDamki==1:
                            poleigri[8-int(st[3])][ord(st[2])-64]=poleigri[8-int(st[1])][ord(st[0])-64]
                            poleigri[8-int(st[1])][ord(st[0])-64]="  "
                            break
                        elif Eatme(st)==1:
                           break
                    else:
                        print("Данный ход невозможен для дамки")
                elif Eatme(st)==1: #КУШАТЬ ШАШКА
                    break
                else:
                   print("Данный ход невозможен")   
             else:
                print("Данная клетка занята")
        else:
             print("Играйте своими фигурами")
             #МЕНЮ ПРОГРАММЫ И ЗАПУСК ИГРЫ  МЕНЮ ПРОГРАММЫ И ЗАПУСК ИГРЫ!!!!!!!!!!!!!!!      
while 1:
    print("Вас приветствует программа шашки\nЕсли вы хотите сыграть наберите play\nдля того чтобы прочитать правила наберите rules\nдля выхода наберите exit")
    command=input()
    command=command.strip()
    if command=="play":
        print("Для того-чтобы сделать ход введите комманду вида A1B3,где A1 это фигура,которой вы ходите ,а B3 место куда вы хотите ходить,"
              "для того чтобы завершить игру наберите gameover \n УДАЧИ")
        black=12 #кол-во шашек
        white=12
        stroka=" +"+8*"--+"
        mas=[]  #масив одной строки поля
        poleigri=[] #массив клеток поля
        n=1 #номер хода
        c=0# константа для белых -1 для черных 1 ,нужна потому что белые ходят вверх ,а черные вниз
        for i in range(8):#генерация массива с клетками
            mas=[]
            mas.append("><")
            for z in range(8):
               if (z+i)%2==1  and i<3:  #черные(вверхние) шашки
                   mas.append("че")
               elif(z+i)%2==1 and i>4:  #белые(нижние) шашки
                   mas.append("бе")
               elif(z+i)%2==0:
                   mas.append("><")#пустое место
               else:
                   mas.append("  ")
            mas.append("><")
            poleigri.append(mas)
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
    elif command=="rules":
        print("rules")
    elif command=="exit":
        print("exit")
    else:
        print("нет такой комманды попробуйте ещё раз\n")

