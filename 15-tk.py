'''
Игра Пятнашки
'''

from tkinter import *
from random import *
from tkinter.messagebox import *
from time import sleep

def printa(a):
    '''
    Отладочная функция выводит список кнопок
    '''
    for i in range(4):
        for j in range(4):
            print(a[i+1][j+1]["text"],end=" ")
        print()    

def click(ev):
    '''
    Обработка клика:
    Если вохможно, меняем кнопки местами
    r0,c0 - координаты "пустой" ячейки
    '''
    
    global a,r0,c0,flag
    # Узнаем по какой кнопке кликнули
    r=ev.widget.grid_info()["row"]
    c=ev.widget.grid_info()["column"]
    
    if ((abs(r-r0)==1 and c==c0) or 
       (abs(c-c0)==1 and r==r0)):
        a[r][c].grid(row=r0,column=c0)
        a[r0][c0].grid(row=r,column=c)
        a[r][c],a[r0][c0]=a[r0][c0],a[r][c]
        r0,r=r,r0
        c0,c=c,c0
        #printa(a)
    else:
        a[r][c].bell()   
         
    if check() and flag:
        finish()    

def start():
    '''
    Перемешиваем кнопки путем генерации нажатий 
    на случайно выбранную кнопку
    '''
    global a,r0,c0
    flag=False
    for i in range(500):
        x,y=randint(1,4),randint(1,4)
        a[x][y].event_generate("<Button-1>")
        #sleep(1)
        a[x][y].after(1,a[x][y].event_generate("<ButtonRelease-1>"))
    flag=True    



def start1():
    '''
    Второй вариант премешивания кнопок
    '''
    
    global a,r0,c0
    
    tmp=[[0]*5 for i in range(5)]
    k=1
    for i in range(1,5):
        for j in range(1,5):
            tmp[i][j]=k%16
            k+=1
    r0=4
    c0=4
    for i in range(500):
        x,y=randint(1,4),randint(1,4)
        if ((abs(x-r0)==1 and y==c0) or 
            (abs(y-c0)==1 and x==r0)):
                tmp[x][y],tmp[r0][c0]=tmp[r0][c0],tmp[x][y]
                r0,x=x,r0
                c0,y=y,c0
    
    for i in range(1,5):
        for j in range(1,5):
            for x in range(1,5):
                for y in range(1,5):
                    if a[x][y]["text"]==str(tmp[i][j]):
                        a[x][y].grid(row=i,column=j)
                        a[i][j].grid(row=x,column=y)
                        a[i][j],a[x][y]=a[x][y],a[i][j]
    



def check():
    '''
    Проверка успешного окончания игры
    (все кнопки в нужном порядке)
    '''
    k=1
    for i in range(1,5):
        for j in range(1,5):
            if a[i][j]["text"]!=str(k%16):return False
            k+=1
    return True

def finish():
    '''
    Обработка окончания игры
    '''
    showinfo("15", "Complete!")


root = Tk()
root.title("15")

# Создаем двумерный список кнопок( индексы 0 не используются) 
a=[[None]*5 for i in range(5)]
for i in range(4):
    for j in range(4):
        a[i+1][j+1]=Button(root,text=str((4*i)+j+1),
                           width=10,height=4,bg="red")
        a[i+1][j+1].grid(row=i+1,column=j+1)
        a[i+1][j+1].bind('<Button-1>',click)
        
# Делаем "пустую" ячейку
a[4][4]["bg"]="white"
a[4][4]["fg"]="white"
a[4][4]["text"]="0"
r0=4
c0=4


# Кнопка START
b=Button(root,text='START',command=start,height=7,width=20)
b.grid(row=5,columnspan=4)
#Надо ли отслеживать окончание игры
flag=False
root.mainloop()
