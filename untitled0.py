# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 02:35:45 2019

@author: adars
"""

import tkinter as tk
import tkinter.messagebox
m=tk.Tk()
l = list()
l1 = list()
n =8
import random
for i in range(n):
    l.append([])
    l1.append([])
    for j in range(n):
        l[i].append(0)
        l1[i].append('-')
bno =8
for i in range(bno):
    xi = random.randint(0, n - 1)
    yi = random.randint(0, n - 1)
    l[xi][yi] = 'b'


for x in range(n):
    for y in range(n):
        if x + 1 < n and l[x][y] == 'b' and l[x + 1][y] != 'b':  # Modification
            l[x + 1][y] += 1
        if x - 1 >= 0 and l[x][y] == 'b' and l[x - 1][y] != 'b':
            l[x - 1][y] += 1
        if x + 1 < n and y + 1 < n and l[x][y] == 'b' and l[x + 1][y + 1] != 'b':
            l[x + 1][y + 1] += 1
        if x - 1 >= 0 and y + 1 < n and l[x][y] == 'b' and l[x - 1][y + 1] != 'b':
            l[x - 1][y + 1] += 1
        if x + 1 < n and y - 1 >= 0 and l[x][y] == 'b' and l[x + 1][y - 1] != 'b':
            l[x + 1][y - 1] += 1
        if x - 1 >= 0 and y - 1 >= 0 and l[x][y] == 'b' and l[x - 1][y - 1] != 'b':
            l[x - 1][y - 1] += 1
        if y + 1 < n and l[x][y] == 'b' and l[x][y + 1] != 'b':
            l[x][y + 1] += 1
        if y - 1 >= 0 and l[x][y] == 'b' and l[x][y - 1] != 'b':
            l[x][y - 1] += 1
global c
c =0
#global win
#win = True
for i in range(n):
    for j in range(n):
        if l[i][j] == 'b':
            c += 1
#global flag
#flag=True
"""def display():
    global flag
    if flag==True:
        flag=False
        wid.configure(color='light blue',text='mine'):
    else:
        flag=True
        wid.configure(color='orange',text='mine')
   """
import sys
def display1(event,p,q):
        global c
        win=True
        bt[p][q].configure(bg='red')
        l1[p][q]='M'
        c=c-1
        lab1.configure(text='FLAGS= ' + str(c))
def display2(event,p,q):
            win=True
            if l[p][q] == 'b':
                bt[p][q].configure(bg='yellow')
                tk.messagebox.showinfo("l","YOU LOSE!!!")
                sys.exit(1)

            elif l[p][q] == 0:
                 recur(p,q)



            else:
                l1[p][q] = l[p][q]
                bt[p][q].configure(bg='grey',text=str(l1[p][q]))
            for i in range(n):
                for j in range(n):
                    if l1[i][j]=='-':
                        if l[i][j]=='b':
                            win=win and True
                        else:
                            win=win and False
            if win:
                tk.messagebox.showinfo('w','YOU WIN!!!')
                sys.exit(0)

bt=list()
for i in range(n):
    bt.append([])
    for j in range(n):
        bt[i].append((tk.Button(m,bg='green',width=5,height=5)))
for i in range(n):
    for j in range(n):
        bt[i][j].grid(row=i*5,column=j*5)
lab1 = tk.Label(m, fg='dark green')
lab1.grid(row=n * 5, column=n * 5)
for p in range(n):
    for q in range(n):
      bt[p][q].bind("<Button-1>",lambda event,p=p,q=q :display2(event,p,q))
      bt[p][q].bind("<Button-3>",lambda event,p=p,q=q :display1(event,p,q))
#wid=tk.Button(m,bg='orange',width=5,height=5,command=display)
#wid.grid(row=(n+1)*5,column=(n+1)*5)
def recur(x, y):

    if x >= 0 and y >= 0 and x < n and y < n :
        l1[x][y] =l[x][y]
        bt[x][y].configure(bg='grey', text=str(l[x][y]))



    if x+1<n:
        if l[x + 1][y] != 'b' and l1[x + 1][y] == '-':
            if l[x + 1][y] != 0:
                l1[x + 1][y] = l[x + 1][y]
                bt[x+1][y].configure(bg='grey',text=str(l[x+1][y]))

            else:
                l1[x+1][y] = 0
                bt[x+1][y].configure(bg='grey')
                recur(x + 1, y)
    if x> 0:
        if l[x - 1][y] != 'b' and l1[x - 1][y] == '-':
            if l[x - 1][y] != 0:
                l1[x - 1][y] = l[x - 1][y]
                bt[x-1][y].configure(bg='grey',text=str(l[x-1][y]))
            else:
                l1[x-1][y] = 0
                bt[x - 1][y].configure(bg='grey')
                recur(x - 1, y)

    if x+1<n  and y+1<n:
        if l[x + 1][y + 1] != 'b' and l1[x + 1][y + 1] == '-':
            if l[x + 1][y + 1] != 0:
                l1[x + 1][y + 1] = l[x + 1][y + 1]
                bt[x + 1][y+1].configure(bg='grey', text=str(l[x + 1][y+1]))
            else:
                l1[x+1][y+1] = 0
                bt[x + 1][y+1].configure(bg='grey')
                recur(x + 1, y + 1)
    if x>0 and y+1<n:
        if l[x - 1][y + 1] != 'b' and l1[x - 1][y + 1] == '-':
            if l[x - 1][y + 1] != 0:
                l1[x - 1][y + 1] = l[x - 1][y + 1]
                bt[x - 1][y+1].configure(bg='grey', text=str(l[x - 1][y+1]))
            else:
                l1[x-1][y+1] = 0
                bt[x - 1][y+1].configure(bg='grey')
                recur(x - 1, y + 1)
    if x+1< n  and y>0:
        if l[x + 1][y - 1] != 'b' and l1[x + 1][y - 1] == '-':
            if l[x + 1][y - 1] != 0:
                l1[x + 1][y - 1] = l[x + 1][y - 1]
                bt[x + 1][y-1].configure(bg='grey', text=str(l[x + 1][y-1]))
            else:
                print('x',x,'y',y)
                l1[x+1][y-1] = 0
                bt[x + 1][y-1].configure(bg='grey')
                recur(x + 1, y - 1)
    if x>0 and y>0:
        if l[x - 1][y - 1] != 'b' and l1[x - 1][y - 1] == '-':
            if l[x - 1][y - 1] != 0:
                l1[x - 1][y - 1] = l[x - 1][y - 1]
                bt[x - 1][y-1].configure(bg='grey', text=str(l[x - 1][y-1]))
            else:
                l1[x-1][y-1] = 0
                bt[x - 1][y-1].configure(bg='grey')
                recur(x - 1, y - 1)
    if y+1< n:
        if l[x][y + 1] != 'b' and l1[x][y + 1] == '-':
            if l[x][y+1] != 0:
                l1[x][y + 1] = l[x][y + 1]
                bt[x][y+1].configure(bg='grey', text=str(l[x][y+1]))
            else:
                l1[x][y+1] = 0
                bt[x][y+1].configure(bg='grey')
                recur(x, y + 1)
    if y>0:
        if l[x][y - 1] != 'b' and l1[x][y - 1] == '-':
            if l[x][y - 1] != 0:
                l1[x][y - 1] = l[x][y - 1]
                bt[x][y-1].configure(bg='grey', text=str(l[x][y-1]))
            else:
                l1[x][y-1] = 0
                bt[x][y-1].configure(bg='grey')
                recur(x, y - 1)

    return

print(l)



m.mainloop()