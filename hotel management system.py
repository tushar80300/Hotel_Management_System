class hotel():
    def __init__(self,rt='',r=0,l=0,m=0,b=0,a=1800,name='',address='',checkin='',checkout='',roomno=101):
        print("\n****WELCOME TO RADISSAN STAR HOTEL****\n")

        self.rt=rt
        self.r=r
        self.l=l
        self.a=a
        self.m=m
        self.b=b
        self.name=name
        self.address=address
        self.checkin=checkin
        self.checkout=checkout
        self.roomno=roomno


    def detail(self):
        self.name=input("Enter your name:")
        self.address=input("Enter your address:")
        self.checkin=input("Enter your check in date:")
        self.checkout=input("Enter your check out date:")
        
    def room(self):
        print("Your room no :101")

    def roomrent(self):
        print("We have the following rooms for you:-\n")
        print("1.type A----->Rs 600 PN/-")
        print("2.type B----->Rs 500 PN/-")
        print("3.type C----->Rs 400 PN/-")
        print("4.type D----->Rs 300 PN/-\n")

        self.rt=int(input("Enter your choice please:"))
        n=int(input("For How many nights did you stay:"))
        if self.rt==1:
            self.rt=n*600
            print("Your have allot room type A")
        elif self.rt==2:
            self.rt=n*500
            print("Your have allot room type B")
        elif self.rt==3:
            self.rt=n*400
            print("Your have allot room type C")
        elif self.rt==4:
            self.rt=n*300
            print("Your have allot room type D")
        else:
            print("wrong input")

        print("your room rent is =",self.rt)

    def menu(self):
        print("\n****Resturant Menu****\n")
        print("1.water---->Rs20\n2.tea---->Rs10\n3.Breakfast combo---->Rs90\n4.Lunch---->Rs110\n5.Dinner---->Rs150\n6.Exit")
        while True:
            
            a=int(input("enter your choice:"))
            if a==1:
                b=int(input("enter your quantity:"))
                self.r=self.r+20*b
            elif a==2:
                b=int(input("enter your quantity:"))
                self.r=self.r+10*b
            elif a==3:
                b=int(input("enter your quantity:"))
                self.r=self.r+90*b
            elif a==4:
                b=int(input("enter your quantity:"))
                self.r=self.r+110*b
            elif a==5:
                b=int(input("enter your quantity:"))
                self.r=self.r+150*b
            elif a==6:
                break
            else:
                print("wrong input")

        print("\nTotal food cost =",self.r)

    def laundary(self):
        print("\n****Laundary Choice****\n")
        print("1.Short--->Rs3\n2.Trouses--->Rs3\n3.Shirt--->Rs5\n4.Jeans--->Rs6\n5.Girlsuit--->Rs6\n6.Exit\n")
        while True:
            a=int(input("enter your choice:"))
            if a==1:
                b=int(input("enter your quantity:"))
                self.l=self.l+3*b
            elif a==2:
                b=int(input("enter your quantity:"))
                self.l=self.l+3*b
            elif a==3:
                b=int(input("enter your quantity:"))
                self.l=self.l+5*b
            elif a==4:
                b=int(input("enter your quantity:"))
                self.l=self.l+6*b
            elif a==5:
                b=int(input("enter your quantity:"))
                self.l=self.l+6*b
            elif a==6:
                break
            else:
                print("wrong input")

        print("\nTotal laundary cost=",self.l)

    def game(self):
        print("\n****Game bill****")
        print("1.Table tennis--->Rs60\n2.Bowling--->Rs60\n3.snooker--->Rs70\n4.Video game--->Rs90\n5.Pool--->Rs50\n6.Exit\n")
        while True:
            g=int(input("Enter your choice:"))

            if g==1:
                h=int(input("No. of hours:"))
                self.m=self.m+60*h
            elif g==2:
                h=int(input("No. of hours:"))
                self.m=self.m+60*h
            elif g==3:
                h=int(input("No. of hours:"))
                self.m=self.m+70*h
            elif g==4:
                h=int(input("No. of hours:"))
                self.m=self.m+90*h
            elif g==5:
                h=int(input("No. of hours:"))
                self.m=self.m+50*h
            elif g==6:
                break
            else:
                print("wrong option")

        print("\nTotal Game bill=",self.m) 
            

    def display(self):
        print("\n****HOTEL BILL****\n")
        print("Customer detail:")
        print("Customer name:",self.name)
        print("Customer address:",self.address)
        print("Customer check in date:",self.checkin)
        print("Customer check out date:",self.checkout)
        print("Room no:",self.roomno)
        print("Room bill:",self.rt)
        print("Resturant bill:",self.r)
        print("Laundary bill:",self.l)
        print("Game bill:",self.m)
        self.b=self.rt+self.r+self.l+self.m
        print("\nSub total bill is",self.b)
        print("Additional service charge is",self.a)
        print("\nYOUR GRAND TOTAL BILL IS ",self.b+self.a)
            

def main():
    a=hotel()

    while True:
        print("\n1.Enter Customer Data")
        print("2.Calculate Room Rent")
        print("3.Calculate Restaurant Bill")
        print("4.Calculate Laundry Bill")
        print("5.Calculate Game bill")
        print("6.Show Total cost")
        print("7.exit\n")

        b=int(input("Enter your choice="))
        if b==1:
            a.detail()
            a.room()
        elif b==2:
            a.roomrent()
        elif b==3:
            a.menu()
        elif b==4:
            a.laundary()
        elif b==5:
            a.game()
        elif b==6:
            a.display()
            break
        elif b==7:
            exit()
        else:
            print("wrong input")
main()           

        

        
