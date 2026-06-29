#coded by Siavash Zarei on Jun 29 
inventory = {}
def add_part ():

    part_num = str(input ("Part Number :"))
    part_name = str(input ("Part Name :"))
    quantity = int( input ("Quantity :"))
    price = int (input ("Price :"))

    inventory.update ({part_num : { 'Name: ' :part_name , "Quantity: " : quantity , "price: " : price }})
    return inventory


print ("===== Invemtory Management =====")
while True :
    user_sel = int (input ("1.Add Part \n2.Exit "))
    if user_sel == 1 :
        add_part()
        print(inventory)
    elif user_sel == 2 :
        break

