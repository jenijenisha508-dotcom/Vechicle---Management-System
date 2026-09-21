customers={}
vechicle={}
class CustomerPanel:

    def __init__(self,vechicle,customers):
        self.vechicle=vechicle
        self.customers=customers

    def register(self,name,age,aadhar):
        self.customers[aadhar]={
            "custname":name,
            "custage":age,
            "custid":aadhar,
            "rented_status":None
        }
        print(f"customer_name={name},customer_age={age},customer_adhar id={aadhar}")
        print(f"customer{name} is added successfully")

        
    def see_available(self):
        for key, value in self.vechicle.items():
            if value["avaliable"]==True:
             print(f"{key}:type:{value["vechicle_type"]}, model:{value["vechicle_model"]},rent:{value["vechicle_remt"]},")


    def rent_vechicle(self,aadhar,Vid):
        
        if aadhar not in self.customers:
            print("please register the yourdelf first")
        
        elif  self.vechicle[Vid]["available"]==False:
            print("please select another a vechicle  ")
        else:
            print("now you rented a vechicle")
            self.vechicle[Vid]["available"]=False
            self.customers[aadhar]["rented_status"]=Vid

    def return_vechicle(self,aadhar):
        if aadhar not in self.customers:
           print("please register yourself first")
        elif self.customers[aadhar]["rented_status"] is None:
            print("you have not rented any vechicle")
        else:
            rented =self.customers[aadhar]["rented_status"]

            self.vechicle[rented]["available"] = True
            self.customers[aadhar]["rented_status"] = None
            print("vechicle returned successfully")
      
        

        if __name__=="__main__":
            customer={}
            vechicle={}

            cust_panel=CustomerPanel(vechicle,customer)
            cust_panel.register("jeni","21","jen001" )
            print(customers)

            # self.vechicles["V101"]["available"] = False
            # self.customers["jen001"]["rented_status"] = "V101"
            # self.vechicles["V101"]["available"] = True
            # self.customers["jen001"]["rented_status"] = None 
            # cust_panel.return_vehicle("jen001")
            # cust_panel = CustomerPanel(vechicles, customers)

            cust_panel.register("Raj", 23, "123456789012")