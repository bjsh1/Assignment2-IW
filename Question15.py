#15. Imagine you are designing a banking application. 
# What would a customer look like? What attributes would she have? 
# What methods would she have?

class Information:

    min_blnc = 500

    def __init__(self,acc_name,acc_no):
        self.acc_name = acc_name
        self.acc_no = acc_no
        
    def info(self):
        print("Customer Details: \nAccount Name: {} \nAccount Number: {}"
                    .format(self.acc_name,self.acc_no))

    @classmethod
    def balance(cls):
        return cls.min_blnc

    def total_balance(self,total_balance):
        print("Total Balance in your account", total_balance)

customer = Information("Robert", 1300)
customer.info()
print("Minimum balance:",Information.balance())
customer.total_balance(15050)