import random

logo = """
      .------.          _      _                 _                
      |A_  _ |.        | |    | |               | |     (_)               | |   
      |( \/ ).-----.   | |__  | |   __ _    ___ | | __  _     __ _    ___ | | __
      | \  /|K /\  |   | '_ \ | |  / _` |  / __ | |/ /  | |  /  _`|  /  _ | |/ /
      |  \/ | /  \ |   | |_) || | | (_| | | (__ |   <   | | |  (_|| |  (_ |   < 
      `-----| \  / |   |_.__/ |_|  \__,_|  \___ |_|\_\  | |  \__,_|  \___ |_|\_\
            |  \/ K|                                   _/ |                 
            `------'                                  |__/            
"""

cards=[0,1,2,3,4,5,6,7,8,9,10,10,10,10,'ace']
def play():
    """Begins The Game"""
    print(logo)
    while True:
        if input("\nDo you want to play a new game?(y/n) ")=='y':
            p=[]
            c=[]
            def pick():
                choice=random.choice(cards)
                if choice=="ace":
                    choice=int(input("\nWhat should be the value of Ace, 1 or 11? "))
                    if choice !=1 and choice !=11:
                        print("Enter a valid number (1 or 11) ")
                        choice=int(input("\nWhat should be the value of Ace, 1 or 11? "))
                return choice
            def pick2():
                p.append(pick())
                c.append(pick())
            def valuep():
                pv=0
                for i in p:
                    pv+=i
                return pv
            def valuec():
                cv=0
                for i in c:
                    cv+=i
                return cv
            
            pick2()
            print(f"\n\nYour first card is {p}")
            print(f"The computer's first card is {c}")
            def repick():
                q=input("\nWould you like to Draw 1 more card(Y) or Settle(N) ? ")
                if q=='y'or q=='Y':
                    pick2()
                    if valuep()>21:
                        print(f"Your cards are{p},value={valuep()}\nThe Computer cards are {c},value={valuec()}")
                        print("\n-----Your cards value is over 21,So you lose!-----")
                        return
                    else:
                        print(f"\nYour current cards are {p} and the total value is {valuep()}")
                        repick()
                elif q=='n' or q=='N':
                    if valuep()>valuec():
                        print("\n-----You win the game!-----")
                        print(f"Your cards are{p},value={valuep()}\nThe Computer cards are {c},value={valuec()}")
                    elif valuep()>valuec():
                        print("\n-----It's a Draw!-----")
                        print(f"Your cards are{p},value={valuep()}\nThe Computer cards are {c},value={valuec()}")
                    else:
                        print("\n-----Computer wins the Game!-----")
                        print(f"Your cards are{p},value={valuep()}\nThe Computer cards are {c},value={valuec()}")
                else:
                    print("Please Enter a Valid Key")
                    repick()
            repick()
                
        else:
            break
    print("\n**********Game has Finished!*********")
play()
                    
                
       
            
            
            
            
            