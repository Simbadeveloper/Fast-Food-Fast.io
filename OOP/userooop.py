
items=dict()
user_details=dict()



class FastFoodFast():
   def __init__(self, username,fname, lname, email, password):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

   def signup(self):
        self.username = input("Enter your username: ")
        self.fname = input("Enter your firstname: ")
        self.lname = input("Enter your lastname: ")
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        user_details.update({"self.username":self.username,"self.fname":self.fname,"self.lname":self.lname,"self.email":self.email,"self.password":self.password})
        print (user_details)
        self.login()

   def forget_password_or_username(self):
       del user_details["self.username"]
       del user_details["self.password"]
       self.username = input("Enter your new username:  ")
       self.password = input("Enter your new password:  ")
       user_details.update({"self.username":self.username,"self.password":self.password})
       self.login()



   def login(self):
        self.username = input("Enter your username to login:  ")
        self.password = input("Enter your password to login:   ")
        self.add_items()

   def add_items(self,*args):
     self.item_name= input("Enter your item : ")
     self.amount= input("Enter the amount:  ")
     self.quantity =input("Enter the quantity : ")
     self.service = input("Enter the type of service ")
     items.update({len(items):{ "self.item_name":self.item_name, "self.quantity":self.quantity, "self.amount":self.amount,"self.service":self.service}})
     self.items_view()

   def delete_items(self,*args):
    self.question = input("Are you sure you want to delete your items(y/n): ")
    if self.question =="y":
     del items["self.item_name"]
     del items["self.quantity"]
     del items["self.amount"]
     del items["self.service"]
     self.item_name= input("Update your item here: ")
     self.amount= input("Update the amount:  ")
     self.quantity =input("Update the quantity here: ")
     self.service =input("Update the type of service: ")
     self.username = input("Update your username here: ")
     items.update({len(items):{"self.item_name":self.item_name, "self.quantity":self.quantity,"self.service":self.service, "self.amount":self.amount}})
     print(items)
     self.logout()
    else:
     return self.logout()

   def items_view(self,*args):
        print(items)
        self.delete_items()

   def admin(self,*args):
     print ("welcome admin")

   def logout(self):
       self.exitme = input("Are you sure you want to log out(y/n): ")
       if self.exitme == "y":
        print("you are successful log out")
        self.login()
       else:
        self.add_items()


