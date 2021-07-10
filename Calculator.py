# Main Libraries
from tkinter import*
import time

tic = time.perf_counter()
#%% Functions

def btnClick(num): #-> gets the pressed key
    global operator
    operator = operator + str(num)
    text_Input.set(operator)

def btnClearDisplay(): #-> clears display
    global operator
    operator = ''
    text_Input.set('')

def btnEqualsInput(): #-> gets the operation val
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=''


#%% Main Objects
cal = Tk()
cal.title('Calculator')
operator = ''
text_Input = StringVar()

#%% Display Objects:

txtDisplay = Entry(cal,font=('arial', 12, 'bold'),
                   fg='lime',textvariable=text_Input,bd = 30,insertwidth=4,bg = 'black',
                   justify='right').grid(columnspan=4)

#-----------------------------------#
# Keys:

keys_general = list(range(0,10))
for i in range(0,4):   #-> keys 7,8,9 and '+' operator
    while i<3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text=str(i+7),bg='gray',command = lambda i=i+7:btnClick(i)).grid(row=1,column=i)
        break
    if i == 3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text='+',bg='gray',command = lambda:btnClick('+')).grid(row=1,column=i)
del i


for i in range(0,4):   #-> keys 4,5,6 and '-' operator
    while i<3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text=str(i+4),bg='gray',command = lambda i=i+4:btnClick(i)).grid(row=2,column=i)
        break
    if i == 3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text='-',bg='gray',command = lambda:btnClick('-')).grid(row=2,column=i)
del i


for i in range(0,4):   #-> keys 1,2,3 and '*' operator
    while i<3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text=str(i+1),bg='gray',command = lambda i=i+1:btnClick(i)).grid(row=3,column=i)
        break
    if i == 3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text='*',bg='gray',command = lambda:btnClick('*')).grid(row=3,column=i)
del i


keys = ['0','C','=','/']
for i in range(0,4):   #-> keys 0,C and '/','=' operators
    while i<3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text=keys[i],bg='gray',command = lambda i=i:btnClick(keys[i])).grid(row=4,column=i)
        if i == 1:
            key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text=keys[i],bg='gray',command = btnClearDisplay).grid(row=4,column=i)
        elif i == 2:
            key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text=keys[i],bg='gray',command = btnEqualsInput).grid(row=4,column=i)
        break
    if i == 3:
        key = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial', 12, 'bold'),
                     text=keys[i],bg='gray',command = lambda:btnClick('/')).grid(row=4,column=i)
del i

#%% Loop
cal.mainloop()

toc = time.perf_counter()

print('\n')
print('-'*75)
print('Elapsed time (seconds):', toc-tic)
print('\n')
#--------------------------------------------------------------------End.