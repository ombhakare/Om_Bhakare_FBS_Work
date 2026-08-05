class Account:
    branch_name = "boi fc road,pune"
    ifsc_code = "bjhdfkjg"

    def __init__(self, holder_nm, acc_no, bal):
        self.holder_name = holder_nm
        self.acc_no = acc_no
        self.bal = bal

    def display(self):
        print("Branch:", Account.branch_name)
        print("Ifsc code:", Account.ifsc_code)
        print("holder name:", self.holder_name)
        print("account no:", self.acc_no)
        print("balance:", self.bal)
        print("##########")

nm = input("enter the holder name:")
ac = int(input("enter the account number:"))
bal = int(input("enter the balance:"))

ac1 = Account(nm, ac, bal)
ac1.display()

ac2 = Account(nm, ac, bal)
ac2.display()