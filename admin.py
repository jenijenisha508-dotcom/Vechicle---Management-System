vechicle={}
class Adminpanel:
    def __init__(self,vechicle):
        self.vechicle=vechicle

    # def view_inventory(self):
    #     with open("vechicle.txt", "r") as file:
    #         data = file.read()
    #         print(data)
    
    
    def add_new_Vechicles(self,Vid,Vtype,Vmodel,Vrent):
        self.vechicle[Vid]={
            "Vechicle_id":Vid,
            "Vechicle_rent":Vrent,
            "Vechicle_type":Vtype,
            "Vechicle_model":Vmodel,
            "available":True
        }
        # def view_inventory(self):
        #  with open("vechicle.txt", "r") as file:
        #     data = file.read()
        #  print(data)   
        # with open("vechicle.txt","a") as file:
        #     file.write(f"Vehicle ID: {Vid}\n")
        #     file.write(f"Vehicle Type: {Vtype}\n")
        #     file.write(f"Vehicle Model: {Vmodel}\n")
        #     file.write(f"Vehicle Rent: {Vrent}\n")
        #     file.write(f"Available: True\n")
        #     file.write("-" * 30 + "\n")
        # print("vechicle details saved successfully")

        print(f"vechicle {Vid} added successfully")

    def view_inventory(self):
         for key,value in self.vechicle.items():
          print(f"{key}: type:{value["Vechicle_type"]} ,model:{value["Vechicle_model"]},rent:{value["Vechicle_rent"]}")

if __name__=="__main__":
    vechicle={}
    admin_panel=Adminpanel (vechicle)
    admin_panel.add_new_Vechicles("v001","twowheeler","scooty","900")
    admin_panel.add_new_Vechicles("v002","fourwheeler","car","1500")
    admin_panel.add_new_Vechicles("v003","porsche","car","2000")
    admin_panel.view_inventory()


    
    # admin_panel.add_new_Vechicle("v001","twowheeler","scooty","900")
    # admin_panel.add_new_vechicle("v001","fourwheeler","car","1500")
    # print(vechicle)

    
        



        
