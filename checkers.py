stroka=" +"
mas=[]
poleigri=[]
for i in range(8):#генерация массива с клетками
    mas=[]
    for z in range(8):
       if (z+i)%2==1  and i<3:  #черные(вверхние) шашки
           mas.append("че")
       elif(z+i)%2==1 and i>4:
           mas.append("бе")
       else:
           mas.append("  ")
    poleigri.append(mas)
for i in range(8):
    stroka=stroka+"--+"
def pole():   #функция для генерации поля
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
print(poleigri)    
pole()        
c=input("  ")

        
    
  
