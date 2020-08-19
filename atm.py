from translate import Translator
from playsound import playsound

def play_audio(path):
    playsound(path)

#available denominations
note100,note200,note500,note2000 = 10,10,10,19
p,o,m,n=0,0,0,0

available_amount = (note100*100)+(200*note200)+(note500*500)+(2000+note2000)

attempt=0
lan=1

#Calculation of notes
def Calculate_Notes(money):
    global note100,note200,note2000,note500,m,n,o,p
    m,n,o,p=0,0,0,0
    if money>=2000:
        n=money//2000
        if note2000<=n:
            n=note2000
        money-=(n*2000)
    if money>=500:
        m=money//500
        if note500<=m:
            m=note500
        money-=(m*500)
    if money>=200:
        o=money//200
        if note200<=o:
            o=note200
        money-=(o*200)
    if money>=100:
        p=money//100
        if note100<=p:
            p=note100
        money-=(p*100)
    if money != 0:
        print(Translate("You have entered invalid ammount"))
        cust.withdraw_bal()


def PrintReceipt(money):
    choice=0
    try:
        choice=int(input(Translate("Do you want to print receipt")+'\n'+Translate("1. Yes")+'\n'+Translate("2. No")+'\n'))
    except Exception:
        print(Translate("You have entered wrong choice"))
        PrintReceipt()
    if choice==1:
        print("********************************************************************************")
        print(Translate("Welcome")+"Mr./Mrs."+ str(cust.cust_name) + Translate(" your account number -- ") + str(cust.cust_id))
        print("********************************************************************************")
        print("2000 x",n, "=", (2000*n))
        print("500 x",m, "=", (500*m))
        print("200 x",o, "=", (200*o))
        print("100 x",p, "=", (100*p))
        print("********************************************************************************")
        print("Total =",(2000*n+500*m+200*o+100*p))
        print("********************************************************************************")
        print("Current balance in your a/c is.... ",str(cust.cust_bal)+'\n')
        exit()
    else:
        print("Current balance in your a/c is.... ",str(cust.cust_bal)+'\n')
        EnterChoice()

#continue Transaction
def Continue():
    option=0
    try:
        option=int(input('\n'+ Translate("Do you want to continue transaction?")+'\n 1 -'+Translate('Yes')+'\n 2 -'+ Translate("No")))
    except Exception:
        print(Translate("You have entered wrong choice")+'\n')
        Continue()
    if option==1:
        EnterChoice()
    else :
        print('\n'+Translate('Thank You for choosing us.'))
        cust.execute()


#welcome
def Welcome():
    print(Translate("welcome")+'\n')
    play_audio("myaudio.mp3")

#Enter Language

def EnterLan():
    global lan
    try:
        lan=int(input("Choose your preffered lnguage\n 1. English\n 2. Hindi\n"))
    except Exception:
        print(Translate("You have entered wrong choice"))
        EnterLan()
    if lan!=1 and lan!=2:
        print(Translate("You have entered wrong choice"))
        EnterLan()

#Translate

def Translate(output):
    global lan
    translator=Translator(to_lang="hi")
    if lan==2:
        return translator.translate(output)
    else:
        return output
        

#Entering Choice
def EnterChoice():
    choice=0
    try:
        choice=int(input('\n'+Translate("Enter choice to continue banking") + "\n"+Translate("1. Add money") + "\n"+Translate("2. Withdraw money ") + "\n"+Translate("3. Show balance") + "\n"+Translate("4. Change Pin")+'\n'+ Translate("5. Exit")+'\n'))
    except Exception:
        print(Translate("You have entered an invalid choice"))
        print(Translate("Restarting Transaction"))
        cust.execute()
    if choice==1:
        cust.add_bal()
    elif choice==2:
        cust.withdraw_bal()
    elif choice==3:
        print(Translate('Your account balance is ')+str(cust.show_bal()))
        cust.execute()
    elif choice==4:
        cust.change_pin()
        cust.execute()
    elif choice==5:
        print(Translate('Exiting Transaction. Please Wait'))
        cust.execute()
    else:
        print(Translate('wrong input'))
        print(Translate("You have entered an invalid choice"))
        print(Translate("Restarting Transaction"))
        cust.execute()



#Entering Pin
def EnterPin():
    global attempt
    pin=0000
    if attempt != 3:
        attempt+=1
        try:
            pin=int(input('\n'+Translate("Enter PIN to continue")))
        except Exception:
            print(Translate("You have entered wrong choice"))
            EnterPin()
        if len(str(pin))!=4:
            print(Translate("Pin should be of length 4"))
            EnterPin()
        if pin==cust.pin:
            attempt=0
            EnterChoice()
        else:
            print(Translate("invalid PIN entered"))
            EnterPin()
    else :
        print(Translate("Your account has been locked"))
        exit()




class Customer():
    #create customer information
    def __init__(self, cust_name,cust_id,cust_bal,pin):
        self.cust_name=cust_name
        self.cust_id=cust_id
        self.cust_bal=cust_bal
        self.pin=pin
    def add_bal(self):
        money=0
        try:
            money=int(input(Translate("Enter Amount you want to add")+'\n'))
        except Exception:
            print(Translate('You have entered wrong value'))
            self.add_bal()
        if money==0:
            print(Translate('Enter a valid ammount'))
            self.add_bal()
        self.money=money
        self.cust_bal+=self.money
        print( Translate('ADDED Succesfully') +'\n'+Translate('Account Balance')+str(cust.show_bal()))
        Continue()
    def show_bal(self):
        return self.cust_bal
    def withdraw_bal(self):
        global m,n,o,p
        money=0000
        try:
            money=int(input(Translate("Enter Amount you want to withdraw")+'\n'))
        except Exception:
            print(Translate("You have entered wrong choice"))
            self.withdraw_bal()
        if money==0:
            print(Translate('Enter a valid ammount'))
            self.withdraw_bal()
        self.money=money
        if self.money<=(self.cust_bal-1000) and self.money<=20000:
            if available_amount==0 or available_amount<self.money:
                print(Translate("Sorry we are OUT OF CASH")+'\n'+Translate("Please chose another choice"))
                EnterChoice()
            if self.cust_bal>=self.money :
                Calculate_Notes(self.money)
                self.cust_bal-=self.money
                PrintReceipt(self.money)
                
            else :
                print(Translate('You are low on balance'))
        else:
            print(Translate('You have entered an invalid amount'))
            self.withdraw_bal()
    def change_pin(self):
        new_pin=0000
        try:
            new_pin=int(input(Translate("Enter new PIN")))
        except Exception:
            print(Translate("You have entered wrong value"))
            self.execute()
        if len(str(new_pin))!=4:
            print(Translate("Entered PIN should be of length 4"))
            self.change_pin()
        else:
            try:
                confirm_pin=int(input(Translate("Confirm PIN")))
            except Exception:
                print(Translate("You have entered wrong value"))
                self.execute()
            if new_pin==confirm_pin:
                self.pin=new_pin
                print(Translate("PIN changed successfully"))
            else:
                print(Translate("PIN do not match"))
                self.change_pin()
        global attempt
        attempt=0
    def execute(self):
        
        Welcome()
        EnterLan()
        EnterPin()
        






cust=Customer("nilesh",169500000885,20000,1998)
cust.execute()

