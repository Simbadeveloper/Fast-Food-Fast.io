
items={}
user_details={}

class FastFoodFast():

   def __init__(self, username, password):
        self.username = username
        self.password = password

   def login(self):
        self.username = input("Enter your username to login:  ")
        self.password = input("Enter your password to login:   ")
        user_details.update({"self.username":username,"self.password":self.password})
        print(user_details)
        self.admin()

   def admin(self,*args):
     print ("welcome admin")
     return add_items()

   def add_items(self,*args):
     self.item_name= input("Enter your item : ")
     self.amount= input("Enter the amount:  ")
     self.quantity =input("Enter the quantity : ")
     self.service = input("Enter the type of service ")
     items.update({len(items):{ "self.item_name":self.item_name, "self.quantity":self.quantity, "self.amount":self.amount,"self.service":self.service}})
     self.items_view()

   def items_view(self,*args):
        print(items)
        self.delete_items()

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
     items.update({"self.item_name":self.item_name, "self.quantity":self.quantity,"self.service":self.service, "self.amount":self.amount})
     print(items)
     self.logout()
    else:
     return logout()

   def logout(self):
       self.exitme = input("Are you sure you want to log out(y/n): ")
       if self.exitme == "y":
        print("you are successful log out")
        self.login()
       else:
        self.makeorder()

