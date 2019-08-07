from tkinter import *

main=Tk()
aar=[]
nar=[]
gui=1
#gui=0 means check results are not reported to the gui but via the variable 'valeed' which is used in the algorithm to solve the puzzle
valeed=1
#Default value: The sudoku is valid.
entries=[]
workable=0

def read_entry_fields():

   for r in range(9):
      for c in range(9):
         a=0
         i=0
         i=r*9+c
         try:   
            a=int(entries[i].get()[0])       
         except IndexError:
            a=0
         except ValueError:
            a=0
         finally:
            aar.append(a)
         if (c==9) and (r==9):
            print(aar)
   print(aar)
# I need a copy of the initial entry to be able to decide which field was entered and which one not.
#    print (aar)

#   print("Zeile 1")
#   for r in range(8):
#     i=r*9+0
#     print (aar[i])

def check_sudoku():
   for c in range(9):
     check_row(c) 
   for r in range(9):
     check_col(r)
   check_blocks()

def check_blocks():

#Blocks in Sudoku:
#1  4   7
#2  5   8
#3  6   9
# Rows and Columns from 0 to 8 respectively
    print("Check blocks")
    for b in range(1,10,1):
        check_subblock(b)

def check_subblock(b):
    rl=0
    rh=2
    cl=0
    ch=2
    print ("Check block",b)
    if (b==1):
       rl=0
       rh=3
       cl=0
       ch=3
    elif (b==2):
       rl=3
       rh=6
       cl=0
       ch=3
    elif (b==3):
       rl=6
       rh=9
       cl=0
       ch=3
    elif (b==4):
       rl=0
       rh=3
       cl=3
       ch=6
    elif (b==5):
       rl=3
       rh=6
       cl=3
       ch=6
    elif (b==6):
       rl=6
       rh=9
       cl=3
       ch=6
    elif (b==7):
       rl=0
       rh=3
       cl=6
       ch=9
    elif (b==8):
       print ("Block 8")
       rl=3
       rh=6
       cl=6
       ch=9
       print (" Hier",rl,rh,cl,ch)
    elif(b==9):
       print("Block 9")
       rl=6
       rh=9
       cl=6
       ch=9
    print("Start Scan",rl, rh, cl,ch)       
    for r in range(rl,rh):
       for c in range(cl,ch):
          print("R=",r)
          print("C=",c)
          i=9*c+r
#          i=9*r+c
#          print("I=",i)
          v1=aar[i]
          print("Scan" ,r,c,v1)
#          if (r==rh) or (c==ch):
#           we are done
#            break
          for r1 in range(rl,rh):
             for c1 in range(cl,ch):
                if (r1==r) and (c1==c):
                    continue
                i1=9*c1+r1
#                i1=9*r1+c1
                v2=aar[i1]
                print("Check ag.",r1,c1,v2)
                if (v1==v2):
                   if (v1==0):
                      continue
                   else:
                      if (b==1):
                         print("Duplicate Block 1")
                         if (gui==1):
                            csg1.configure(fg="red")
                            csg2.configure(fg="red")
                            csg3.configure(fg="red")
                            msg1.configure(fg="red")
                            msg2.configure(fg="red")
                            msg3.configure(fg="red")
                         else:
                            valeed=0
                      elif(b==2):
                         print("Duplicate Block 2")
                         if (gui==1):
                            csg1.configure(fg="red")
                            csg2.configure(fg="red")
                            csg3.configure(fg="red")
                            msg4.configure(fg="red")
                            msg5.configure(fg="red")
                            msg6.configure(fg="red")                      
                         else:
                            valeed=0                         
                      elif(b==3):
                          print("Duplicate Block 3")
                          if (gui==1):
                            csg1.configure(fg="red")
                            csg2.configure(fg="red")
                            csg3.configure(fg="red")
                            msg7.configure(fg="red")
                            msg8.configure(fg="red")
                            msg9.configure(fg="red")
                          else:
                            valeed=0
                      elif(b==4):
                         print("Duplicate Block 4")
                         if (gui==1):
                            csg4.configure(fg="red")
                            csg5.configure(fg="red")
                            csg6.configure(fg="red")
                            msg1.configure(fg="red")
                            msg2.configure(fg="red")
                            msg3.configure(fg="red")
                         else:
                            valeed=0
                      elif(b==5):
                         print("Duplicate Block",b)
                         if (gui==1):
                            csg4.configure(fg="red")
                            csg5.configure(fg="red")
                            csg6.configure(fg="red")
                            msg4.configure(fg="red")
                            msg5.configure(fg="red")
                            msg6.configure(fg="red")
                         else:
                             valeed=0
                      elif(b==6):
                         print("Duplicate Block",b)
                         if (gui==1):
                            csg4.configure(fg="red")
                            csg5.configure(fg="red")
                            csg6.configure(fg="red")
                            msg7.configure(fg="red")
                            msg8.configure(fg="red")
                            msg9.configure(fg="red")                         
                         else:
                             valeed=0
                      elif(b==7):
                         print("Duplicate Block",b)
                         csg7.configure(fg="red")
                         csg8.configure(fg="red")
                         csg9.configure(fg="red")
                         msg1.configure(fg="red")
                         msg2.configure(fg="red")
                         msg3.configure(fg="red")    
                      elif(b==8):
                         print("Duplicate Block",b)
                         csg7.configure(fg="red")
                         csg8.configure(fg="red")
                         csg9.configure(fg="red")
                         msg4.configure(fg="red")
                         msg5.configure(fg="red")
                         msg6.configure(fg="red") 
                      elif(b==9):
                         print("Duplicate Block",b)
                         csg7.configure(fg="red")
                         csg8.configure(fg="red")
                         csg9.configure(fg="red")
                         msg7.configure(fg="red")
                         msg8.configure(fg="red")
                         msg9.configure(fg="red")                              
# We mark the block with the duplicate.    
     
     
def check_col(r):
         i=0
         i1=0
         i2=0
         v1=0
         v2=0
         c1=0
         c2=0
         print("Checking Col",r)
         for c in range(8):
            i=r*9+c
            v1=aar[i]
            print("Spalte/Zeile/Wert", r,  c, v1)
            if (v1==0):
               continue
            c1=c+1
            if (c1==8):
               break
# We are done.
            for c2 in range(c1,8):
               i2=9*r+c2
               v2=aar[i2]
            if (v1==v2):
               print("Col dupl", r, c, c2)
               print ("Val1", v1)
               print ("Val2", v2)
               if (r==0):
                  if (gui==1):
                     csg1.configure(fg="red")
                  else:
                     valeed=0
               elif(r==1):
                  if (gui==1):
                     csg2.configure(fg="red")
                  else:
                     valeed=0                  
               elif(r==2):
                   if (gui==1):
                        csg3.configure(fg="red")
                   else:
                        valeed=0
               elif(r==3):
                  if (gui==1):
                     csg4.configure(fg="red")
                  else:
                     valeed=0
               elif(r==4):
                 if (gui==1):
                  csg4.configure(fg="red")
                 else:
                  valeed=0
               elif(r==5):
                  if (gui==1):
                   csg5.configure(fg="red")
                  else:
                   valeed=0
               elif(r==6):
                  if (gui==1):
                   csg6.configure(fg="red")
                  else:
                   valeed=0
               elif(r==7):
                if (gui==1):
                  csg7.configure(fg="red")
                else:
                  valeed=0
               elif(r==8):
                if (gui==1):
                  csg8.configure(fg="red")           
                else:
                  valeed=0
               else:
                if(gui==1):
                  csg9.configure(fg="red")
                else:
                  valeed=0
pass     
def check_row(c):
         i=0
         i1=0
         i2=0
         v1=0
         v2=0
         print("Checking Row",c)
         for r in range(8):
            i=r*9+c
            print("Zeile/Spalte/Wert", r,  c, aar[i])
            i1=9*(r+1)+c
            v1=aar[i]
            print ("Index", r, c)


            if (v1==0):
                 continue
#     Fields that were not entered cannot be duplicate @ all
#         print("Zelle=",i)
#         print("err=",r)
#         print("i1=",i1)
#         print("Spalte=",r)
#         print("Inhalt=",v1)
            for r1 in range(r+1,8):
             i2=9*r1+c
             v2=aar[i2]

             print ("Prüfe....")
             print ("Zelle=",i2)
             print ("Inhalt=",v2)
             if (v1==v2):
              duplstr="Cols"+str(r+1)+" and " + str(r1+1)
              print(duplstr)
              if (c==0):
               if (gui==1):
                msg1.configure(fg="red")
              elif(c==1):
                msg2.configure(fg="red")
              elif (c==2):
                msg3.configure(fg="red")
              elif (c==3):
                msg4.configure(fg="red")
              elif(c==4):
                msg5.configure(fg="red")
              elif(c==5):
                msg6.configure(fg="red")
              elif(c==6):
                msg7.configure(fg="red")
              elif(c==7):
                msg8.configure(fg="red")
              else:
                msg9.configure(fg="red")
#            print("Duplicate in Row", c)
#             print("Duplicate Cols",r,r1)
#            endcheck=1
#            break
#         if (endcheck==1):
# Aber das ist doch Unsinn, wir müssen alle Dubletten finden.
#               break
             
pass
for r in range(0, 180, 20):
   for c in range(0, 180, 20):
      temp = Entry(main)
      msg1 = Label(main, text="1")
      msg2 = Label(main, text="2")
      msg3 = Label(main, text="3")
      msg4 = Label(main, text="4")
      msg5 = Label(main, text="5")
      msg6 = Label(main, text="6")
      msg7 = Label(main, text="7")
      msg8 = Label(main, text="8")
      msg9 = Label(main, text="9")
      csg1 = Label(main, text="1")
      csg2 = Label(main, text="2")
      csg3 = Label(main, text="3")
      csg4 = Label(main, text="4")
      csg5 = Label(main, text="5")
      csg6 = Label(main, text="6")
      csg7 = Label(main, text="7")
      csg8 = Label(main, text="8")
      csg9 = Label(main, text="9")
      temp.place(x=r, y=c, width=20, height=20)
      entries.append(temp)
#b1=Button(main, text='Quit', command=main.quit).grid(row=3, column=10, sticky=W, pady=4)
#b2=Button(main, text='Read', command=read_entry_fields).grid(row=3, column=11, sticky=W, pady=4) 
main.wm_title("Please enter the Sudoku")
b1=Button(main, text='Quit', command=main.quit)
b2=Button(main, text='Read', command=read_entry_fields)
b3=Button(main, text='Check', command=check_sudoku)
b1.place(x=200, y=200, width=40, height=40)
b2.place(x=240, y=240, width=40, height=40) 
b3.place(x=280, y=200, width=40, height=40)
msg1.place(x=200, y=00, width=20, height=20)
msg2.place(x=200, y=22, width=20, height=20)
msg3.place(x=200, y=44, width=20, height=20)
msg4.place(x=200,y=66, width=20, height=20)
msg5.place(x=200, y=88, width=20, height=20) 
msg6.place(x=200, y=100, width=20, height=20)
msg7.place(x=200, y=120, width=20, height=20)
msg8.place(x=200, y=140, width=20, height=20)
msg9.place(x=200, y=160, width=20, height=20)
csg1.place(x=0, y=200, width=20, height=20) 
csg2.place(x=20, y=200, width=20, height=20)
csg3.place(x=40, y=200, width=20, height=20)
csg4.place(x=60, y=200, width=20, height=20)
csg5.place(x=80, y=200, width=20, height=20)
csg6.place(x=100, y=200, width=20, height=20)
csg7.place(x=120, y=200, width=20, height=20)
csg8.place(x=140, y=200, width=20, height=20)
csg9.place(x=160, y=200, width=20, height=20)
main.mainloop()