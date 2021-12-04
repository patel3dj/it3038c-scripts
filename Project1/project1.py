'''
I did this porject as it is one of the daily 
used when we want to check how much interest rate 
and we get all the output of how much interest rate will be apllied annually

'''
#Here it is the class for which user enters its name
#account number, and what type of account.
class Account:
    def getdata(self):
        a=input("Customer Name-")
        b=int(input("Account Number-"))
        c=input("Type of Account-")
        return c

#Here user will be asked for how much amount you want to deposite in the bank account.
class CurrentAccount(Account):
    def current(self):
        self.a=int(input("Enter an amount to deposit-"))
        print(self.a)
        if self.a>0:
            print(self.a)
        else:
            print("A service charge is imposed due to insufficient balance.")

#Here user will be asked for how much amount you want to deposite in the bank account.
#enter your interest rate, and at the last you will be asked for what time of year it is.
class SavingsAccount(CurrentAccount):
    def savings(self):
        self.c=int(input("Enter an amount to deposit-"))
        self.e=int(input("Enter an interest rate-"))
        self.f=int(input("Enter a time in years-"))
        print(self.c)
        self.g=print("interet to be deposited-", self.c*pow(1+self.e/100,self.f))
        self.d=int(input("Enter an amount to withdraw-"))
        if self.d<=self.c:
            print("Withdraw approved", self.c-self.d)
        else:
            print("Withdraw rejected")
        if self.c>0:
            print(self.c)
        else:
            print("A service charge is imposed due to insufficient balance.")

d1=SavingsAccount()
d=d1.getdata()
if d=="current":
    d1.current()
else:
    d1.savings()