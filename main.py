"""
written by : 
                    __                             __    __               _ 
   ____ ___  ____  / /_  ________  ____     ____ _/ /_  / /_  ____ ______(_)
  / __ `__ \/ __ \/ __ \/ ___/ _ \/ __ \   / __ `/ __ \/ __ \/ __ `/ ___/ / 
 / / / / / / /_/ / / / (__  )  __/ / / /  / /_/ / /_/ / /_/ / /_/ (__  ) /  
/_/ /_/ /_/\____/_/ /_/____/\___/_/ /_/   \__,_/_.___/_.___/\__,_/____/_/   

name of poject : dose game by python
date:  1 March 2022 
enjoy this game                                                                            

"""


# import libraries
import random
from tkinter import *
import time


# var 

# info if element in menu
win_menu=None
player_one_input=''
player_two_input=''
how_to_play_input=''
counter_input=''


# info of player we need
player_one=''
player_two=''
s_or_p=''
count_game=''
# info of socre of each player
score_player_one=0
score_player_two=0
round_=1
turn=1
table=[['','',''],['','',''],['','','']]
log=''
# info if element in game
win_game=None
btn_1=btn_2=btn_3=btn_4=btn_5=btn_6=btn_7=btn_8=btn_9=btn_next=label_log2=None
round_lable=player_one_lable=player_two_lable=which_one=warning_label2=who_one_winner=None

# finish 
win_finish=None

def game(row,col,index,s_p) :
    global table,warning_label2,turn,player_one,player_two,label_log2
    global btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,who_one_winner,btn_next
    global score_player_one,score_player_two,round_,count_game
    global log
    
    if table[row][col]=='X' or table[row][col]=='O':
        warning_label2.config(text='you have to choose another one')
    else:
        if winner()!=0:
            return
        warning_label2.config(text='')
        if turn==1:
            table[row][col]=player_one
            log+=f'player one click on {index}\n'  
        else:
            table[row][col]=player_two
            log+=f'player two click on {index}\n'
        
        label_log2.config(text=log) 
        
        
          
      
        if index==1:
            btn_1.config(text=table[row][col])
        elif index==2:
            btn_2.config(text=table[row][col])
        elif index==3:
            btn_3.config(text=table[row][col])
        elif index==4:
            btn_4.config(text=table[row][col])
        elif index==5:
            btn_5.config(text=table[row][col])
        elif index==6:
            btn_6.config(text=table[row][col])
        elif index==7:
            btn_7.config(text=table[row][col])
        elif index==8:
            btn_8.config(text=table[row][col])
        elif index==9:
            btn_9.config(text=table[row][col])    
        
        if is_game_finish() and winner()==0:
            who_one_winner.config(text='game is eqaul')
            btn_next.config(command=lambda:update())
            return
        
        win=winner()
        if win==player_one:
            who_one_winner.config(text=f'player one win in round {round_}')
            score_player_one+=1
            btn_next.config(command=lambda:update())
            return
        elif win==player_two:
            who_one_winner.config(text=f'player two win in round {round_} ') 
            score_player_two+=1
            btn_next.config(command=lambda:update())
            return
        get_turn()  

        if s_p=='s':
            if turn==2:
                while True:
                    _index=random.randint(1,9)
                    row1,col1=get_row_col(_index)
                    if table[row1][col1]=='O' or table[row1][col1]=='X':
                        continue
                    break
                game(row1,col1,_index,s_p) 

def noun():
    pass
def noun2():
    global win_finish
    win_finish.destroy()
    create_menu()

def finish_game():
    global score_player_two,score_player_one
    global win_finish
    win=''
    win_finish=Tk()
    win_finish.title('winner')
    win_finish.geometry('250x150')
    win_finish.resizable(False,False)
    
    if score_player_one>score_player_two:
        win='player one won !'
    elif score_player_one<score_player_two: 
        win='player two won !'
    else:
        win='game equal'    

    
    finish_label=Label(win_finish,text=win,bg='yellow',fg='green',font=('Arial',15))
    finish_label.place(x=50,y=10)

    score_label=Label(win_finish,text=f'player 1 : {score_player_one} & player 2 : {score_player_two}',bg='yellow',fg='green',font=('Arial',10))
    score_label.place(x=50,y=50)

    btn_again=Button(win_finish,text='play again',fg='blue',bg='yellow',command=lambda:noun2())
    btn_again.place(x=50,y=80)
    win_finish.mainloop()


def update():
    global round_,win_game,who_one_winner,label_log2,log
    global score_player_one,score_player_two,count_game,s_or_p
    global btn_next,table,player_one,player_two
    global btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_next,player_one_lable,player_two_lable,round_lable
    win=winner()

    log=''
    table=[['','',''],['','',''],['','','']]
    btn_1.config(text='')
    btn_2.config(text='')
    btn_3.config(text='')
    btn_4.config(text='')
    btn_5.config(text='')
    btn_6.config(text='')
    btn_7.config(text='')
    btn_8.config(text='')
    btn_9.config(text='')
    who_one_winner.config(text='')
    label_log2.config(text='')
    
    player_one_lable.config(text=f'player 1 ({player_one}): {score_player_one} ')
    player_two_lable.config(text=f'player 2 ({player_two}): {score_player_two} ')
    round_+=1
    round_lable.config(text=f'round {round_}\{count_game}')
    time.sleep(1)
    btn_next.config(command=lambda:noun())
    
    if round_>int(count_game):
        round_=1
        time.sleep(1)
        win_game.destroy()
        finish_game()
        score_player_one=0
        score_player_two=0
        print('game finished ')
    else:
        if s_or_p=="s":
            if win==player_two:
                while True:
                    _index=random.randint(1,9)
                    row1,col1=get_row_col(_index)
                    if table[row1][col1]=='O' or table[row1][col1]=='X':
                        continue
                    break
                game(row1,col1,_index,s_or_p)

                      

def winner():
    global table
    for row in range(len(table)):
        if table[row][0]==table[row][1] and table[row][0]==table[row][2] and table[row][0]!='' :
            return table[row][0]

    for row in range(len(table)):
        for col in range(len(table[row])):
            if table[0][col]==table[1][col] and table[0][col]==table[2][col] and table[0][col]!='':
                return table[0][col]
    
    if table[0][0]==table[1][1] and table[0][0]==table[2][2] and table[0][0]!='':
        return table[0][0]

    if table[0][2]==table[1][1] and table[0][2]==table[2][0] and table[0][2]!='':
        return table[0][2]    
    return 0

def is_game_finish():
    global table
    all_full=[]
    for row in range(len(table)):
        for col in range(len(table[row])):
            if table[row][col]=='X' or table[row][col]=="O":
                all_full.append(True)
            else:
                all_full.append(False)
    if all(all_full):
        return True
    else :
        return False                    

    

  
def get_turn():
    global turn,which_one
    if turn==1:
        turn=2
        which_one.config(text='player two has to choose')
    else:
        turn=1 
        which_one.config(text='player one has to choose')   

def get_row_col(index):
    
    if index==1:
        return 0,0
    elif index==2:
        return 0,1
    elif index==3:
        return 0,2
    elif index==4:
        return 1,0 
    elif index==5:
        return 1,1  
    elif index==6:
        return 1,2  
    elif index==7:
        return 2,0  
    elif index==8:
        return 2,1   
    elif index==9:
        return 2,2

def start_game(index):
#    global win_game,turn,table
#    global btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9
#    global round_lable,player_one_lable,player_two_lable,which_one
#    global s_or_p,count_game,player_one,player_two,turn

   if s_or_p=='p':  
        row,col=get_row_col(index)
        game(row,col,index,s_or_p) 

   elif s_or_p=='s':
       row,col=get_row_col(index)
       game(row,col,index,s_or_p)
                        
              
   

# create game 3*3 
def create_game():
   global win_game,count_game,label_log2,turn
   global btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_next
   global round_lable,player_one_lable,player_two_lable,which_one,who_one_winner,warning_label2,round_
   global player_one,player_two

   win_game=Tk()
   win_game.title('dose game')
   win_game.geometry('600x500')
   win_game.resizable(width=False,height=False)
   
   # round lable    
   round_lable=Label(win_game,text=f'round {round_}\{count_game}',font=("Arial", 25),fg='red')
   round_lable.place(x=250,y=10)
#    player one lable
   player_one_lable=Label(win_game,text=f'player 1 ({player_one}): 0 ',font=("Arial", 15),fg='green')
   player_one_lable.place(x=100,y=50)
#    player two lable
   player_two_lable=Label(win_game,text=f'player 2 ({player_two}): 0 ',font=("Arial", 15),fg='blue')
   player_two_lable.place(x=400,y=50)
# mode choose
   which_one=Label(win_game,text='player 1 has to choose',font=("Arial", 10),bg='yellow')
   which_one.place(x=230,y=80)   
#  canvas1
   canvas1=Canvas(win_game, width=600, height=5,bg='green')
   canvas1.place(x=0,y=100)
#  canvas2
   canvas2=Canvas(win_game, width=300, height=5,bg='blue')
   canvas2.place(x=300,y=100)   
   
   btn_1=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(1))
   btn_1.place(x=265,y=106)


   btn_2=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(2))
   btn_2.place(x=375,y=106)

   btn_3=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(3))
   btn_3.place(x=485,y=106)

   btn_4=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(4))
   btn_4.place(x=265,y=206)

   btn_5=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(5))
   btn_5.place(x=375,y=206)

   btn_6=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(6))
   btn_6.place(x=485,y=206)

   btn_7=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(7))
   btn_7.place(x=265,y=306)

   btn_8=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(8))
   btn_8.place(x=375,y=306)

   btn_9=Button(win_game,text='',width=15,height=6,bg='yellow',activebackground="yellow",command=lambda: start_game(9))
   btn_9.place(x=485,y=306)

   label_log=Label(win_game,text='log')
   label_log.place(x=120,y=110)    

   label_log2=Label(win_game,text='',font=("Arial", 10),fg='green')
   label_log2.place(x=8,y=130)

   



#  canvas3
   canvas3=Canvas(win_game, width=600, height=5,bg='pink')
   canvas3.place(x=0,y=400)

   warning_label=Label(win_game,text='warning')
   warning_label.place(x=100,y=405)

   warning_label2=Label(win_game,text='',fg='red',font=("Arial", 10))
   warning_label2.place(x=10,y=425)
   
   who_one_winner=Label(win_game,text='',fg='green',font=("Arial", 15))
   who_one_winner.place(x=350,y=415)

   btn_next=Button(win_game,text='next',font=("Arial", 15))
   btn_next.place(x=280,y=450)


   

   win_game.mainloop()
# create_game()
# create menu   
def check_var_in_menu():
    global player_one,player_two,s_or_p,count_game
    global player_one_input,player_two_input,how_to_play_input,counter_input,win_menu
    warning=''
    if player_one_input.get()!="O" and player_one_input.get()!='X':
        warning=' player one is not correct '

    elif player_two_input.get()!="X" and player_two_input.get()!='O':
        warning=' player two is not correct ' 

    elif player_one_input.get()==player_two_input.get():      
        warning=' both of them are the same '


    elif how_to_play_input.get()!='s' and how_to_play_input.get()!='p':
        warning ='you have to choose s or p '
    elif int(str(counter_input.get()))<1 and int(str(counter_input))>10 and len(counter_input.get())!=0 :
        warning='you have to choose 1 to 10 for count of game ' 
    else:  
        player_one=player_one_input.get()
        player_two=player_two_input.get()
        count_game=counter_input.get()
        s_or_p=how_to_play_input.get()
        win_menu.destroy()
        create_game()

    # warning
    war_lable=Label(win_menu,text=warning,fg='red')
    war_lable.place(x=8,y=160)


def create_menu():
    global player_one_input,player_two_input,how_to_play_input,counter_input,win_menu,win_finish
    # create menu
    
    win_menu=Tk()
    win_menu.geometry('400x250')
    win_menu.resizable(width=False,height=False)
    win_menu.title('menu',)

    # lable and input for player one
    lable1=Label(win_menu,text='player1',bg='green')
    lable1.place(x=8,y=10)

    player_one_input=Entry(win_menu,width=10)
    player_one_input.place(x=70,y=10)

    # lable and input for player two
    lable2=Label(win_menu,text='player2',bg='blue')
    lable2.place(x=200,y=10)

    player_two_input=Entry(win_menu,width=10)
    player_two_input.place(x=260,y=10)

    # lable and input for choose system or alone
    lable_how_to_play=Label(win_menu,text='s / p ',bg='green')
    lable_how_to_play.place(x=8,y=50)

    how_to_play_input=Entry(win_menu)
    how_to_play_input.place(x=70,y=50)

    # lable and input for choose counter
    lable_counter=Label(win_menu,text='round',bg='yellow')
    lable_counter.place(x=8,y=100)

    counter_input=Entry(win_menu)
    counter_input.place(x=70,y=100)

    # button
    btn_menu=Button(win_menu,text='start',command=check_var_in_menu,bg='pink',width=10)
    btn_menu.place(x=170,y=130)

    # show menu
    win_menu.mainloop()
if __name__=="__main__":    
     create_menu()