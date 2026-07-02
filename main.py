#coded by Siavash Zarei on Jun 29 
import json

inventory = {}
try :
     with open ("inventory.json" , "r") as file :
        inventory = json.load(file)
except FileNotFoundError : 
     print ("No inventory file found. Starting with an empty inventory.")
def add_part ():

    part_num = input ("Part Number:")
    part_name = input ("Part Name:")
    try :
        quantity = int( input ("Quantity:"))
        price = int (input ("Price:"))
    except ValueError :
         print ("Inter mumber pleas !")
         return
    if part_num in inventory:
        print("Part number already exists.")
        return

    inventory[part_num] = {
        "name": part_name,
        "quantity": quantity,
        "price": price
    }
    save_inventory()
    
    # return inventory   ---> def dont need return because it update dicttionry directly 
def search_part (part_num ):
    if part_num in inventory :
            details = inventory[part_num]

            print("----------------------------")
            print("Part Number:", part_num)

            for key, value in details.items():
                print(f"{key}: {value}")

            print("----------------------------")
    else :
            print ("Part dosent exsist ")
        
def delete_part (part_num ):
    if part_num in inventory :
            print("----------------------------")
            print("Part Number:", part_num , "has removed !")
            inventory.pop (part_num)
            save_inventory()

    else :
            print ("Part dosent exsist ")



def update_part (part_num):
    if part_num in inventory :
            details = inventory[part_num]
            print("----------------------------")
            print ("Part Number:" , part_num )
            for key, value in details.items():
                print(f"{key}: {value}")
            part_name = input ("New Name:")
            try : 
                quantity = int( input ("New Quantity:"))
                price = int (input ("New Price:"))  
            except ValueError :
                 print ("Inter mumber pleas !") 
                 return
            details["name"] = part_name
            details["quantity"] = quantity
            details["price"] = price
            save_inventory ()
            print("Part Updated successfully.")
            print ("----------------------------")
            return
    else :
            print ("Part dosent exsist ")
        
       
def save_inventory ():
    with open ("inventory.json" , "w") as file :
         json.dump(inventory, file , indent=4)
         print ("Inventory saved successfully !")

def view_inventory () : 
        #if inventory == {} :
        if not inventory :
            print ("inventory is empty")
        else : 
            print ("------------------------------")
            for k , v in inventory.items() :
                print ("Part Number " , ":", k )
                for name , values in v.items () :
                    print  ( name , ":" , values)
            print ("------------------------------") 




print ("===== Inventory Management =====")


while True :
        try :
             user_sel = int (input ("1. Add Part \n2. View parts \n3. Search by part number \n4. Update part \n5. Delet part \n6. Exit" ))
       
             if user_sel == 1 :
                add_part()
             elif user_sel == 2 :
                view_inventory()
             elif user_sel == 3 :
                part_num = input ("Enter part number: ")
                search_part(part_num)
             elif user_sel == 4 :
                part_num = input ("Enter part number to update: ")
                update_part(part_num)
             elif user_sel == 5 :
                part_num = input ("Enter part number to delet: ")
                delete_part(part_num)
             elif user_sel == 6 :
                break
             else : 
                  print ("Invalid option. Please choose 1-6.")
        except ValueError:
                print ("inter a number")
            
