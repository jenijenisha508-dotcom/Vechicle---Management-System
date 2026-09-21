from src.admin import Adminpanel
from src.customer import CustomerPanel


def main():


    customers={}
    vechicles={}
    admin_panel=Adminpanel(vechicles)
    cust_panel=CustomerPanel(vechicles,customers)
    while True:
        print("*"*40)
        print("welcome to jenisha rentals")
        print("*"*40)
        print("select an option")
        print("1.,admin panel")
        print("2.,customer panel")
        print("3.,exit")

        user=input("enter your option here:")


        if user=="3":
            print("-----thank you ,visit again-----")
            break
        
        elif user=="1":
            print("-----we are now in admin panel-----")
            while True:
                print("="*40)
                print("welcome admin")
                print("="*40)
                print("select an option:")
                print("1. Add a new vechical")
                print("2. see inventory")
                print("3. Exit the Admin panel")
                admin=input("enter your option:")

                if admin =="3":
                    print("-----Exiting the Admin panel-----")
                    break
                elif admin=="2":
                    print("-----These are all Vechicles-----")
                    admin_panel.view_inventory()
                elif admin =="1":
                    print("-----Adding a new Vechicle-----")
                    Vid=input("enter the new vichcle id:")
                    Vtype=input("enter the type of the vechicle:")
                    Vmodel=input("enter the vechicle model:")
                    Vrent=input("enter the vechicle rent:")
                    admin_panel.add_new_Vechicles(Vid,Vtype,Vmodel,Vrent)

                else:
                    print("-----you entering a invalid input. please use 1/2/3-----")


        elif user=="2":
            print("-----we are now in customer panel-----")
            while True:
                print("*"*40)
                print("welcome customer")
                print("*"*40)
                print("Select an option:")
                print("1. Register customer")
                print("2. See Available Vechicle")
                print("3. Rent a Vechicle")
                print("4. Return a Vechicle")
                print("5.Exit The Customer Panel")
                customer= input("enter your option:")

                if customer=="5":
                    print("-----Exiting The customer panel-----")
                    break
                elif customer=="4":
                    print("-----renting a vechicle-----")
                    aadhar=input("enter your aadhar id:")
                    cust_panel.return_vechicle(aadhar)
                elif customer=="3":
                    print("-----renting a vechicle-----")
                    aadhar=input("enter your aadhar id:")
                    Vid=input("enter your vehicle id :")
                    cust_panel.rent_vechicle(aadhar,Vid)
                elif customer=="2":
                    print("-----displaying available vechicles-----")
                elif customer=="1":
                    print("-----registering a customer-----")
                    name=input("enter the name:")
                    age=input("enter the age:")
                    aadhar=input("enter your aadhar:")
                    cust_panel.register(name,age,aadhar)
                else:
                    print("-----invalid input.please use 1/2/3-----")
            else:
                print("-----invalide input.please use 1/2/3-----")
            
         
if __name__=="__main__":
        main()
         
