import json
import datetime

def inventView():
    print("-----------------------Item List---------------------------")
    fd=open('inventory.json','r')
    js=fd.read()
    fd.close()
    data=json.loads(js)  #converts string js to dictionary
    print("Id     Item    Price    Qty")
    for i in data.keys():
        print(i,' ',data[i]["Name"],'| ',data[i]["Rate"],'| ',data[i]["Qty"])
    print("-----------------------------------------------------------")



def genBill():
    try:
        #user info
        ur_name=str(input("Enter name: "))
        ur_mob=str(input("Enter Mobile No: "))

        ur_itn=int(input("Enter total distinct items you wantto purchase: "))   #totalunique items
        fd=open('inventory.json','r')
        js=fd.read()
        fd.close()
        data=json.loads(js)  #converts dict to json string format
        itmlst=[]  #all items list to add in bill line lby line
        ta=0;     #billing amount

        for i in range(ur_itn):
            print("\n")
            id=str(input("Enter order Id: "))
            qt=int(input("Enter quantity: "))
            lst=[]
            for i in data:
                if i==id:
                        data[i]["Qty"]=str(int(data[i]["Qty"])-qt)   #updating quantity after deducing
                        lst.append(data[id]["Name"])
                        lst.append(data[id]["Rate"])
                        lst.append(qt)
                        lst.append(int(data[id]["Rate"])*qt)
                        ta+=int(data[id]["Rate"])*qt
            itmlst.append(lst)

        #PRINTING BILL
        print("\n\n")
        print("*"*50)
        print("Bill Date:",datetime.datetime.now().strftime("%d/%m/%y"))
        print("Bill Time:",datetime.datetime.now().strftime("%H:%M"))
        print("Cust. Name:",ur_name)
        print("Cust. Mob:",ur_mob)
        print("-"*23,"BILL","-"*23,sep='')
        print("Sn  |  Itm. Name  |  Rate  |  Qty.  |  Amount")
        print("-"*50)
        for i in range(ur_itn):
            print(f"{i+1}.      {itmlst[i][0]}     {itmlst[i][1]}      {itmlst[i][2]}      {itmlst[i][3]}")
        print("-"*50)
        print("Billing Amount:",ta)
        print("*"*50)

        #CREATING CURRENT BILL IN FILE: currbill.txt
        js=json.dumps(data)  #converts updated string js to dictionary
        fd=open('inventory.json','w'); #writing updated fiel on json
        fd.write(js)
        fd.close()

        file=open('currbill.txt','w')
        file.write("\n\n")
        file.write("*"*50+"\n")
        file.write("Bill Date: " + datetime.datetime.now().strftime("%d/%m/%y") + "\n")
        file.write("Bill Time: " + datetime.datetime.now().strftime("%H:%M") + "\n")
        file.write("Cust. Name: " + ur_name + "\n")
        file.write("Cust. Mob: " + ur_mob + "\n")
        file.write("-"*23 + "BILL" + "-"*23 + "\n")
        file.write("Sn  |  Itm. Name  |  Rate  |  Qty.  |  Amount\n")
        file.write("-"*50 + "\n")
        for i in range(ur_itn):
            file.write(f"{i+1}.      {itmlst[i][0]}     {itmlst[i][1]}      {itmlst[i][2]}      {itmlst[i][3]}\n")
        file.write("-"*50 + "\n")
        file.write("Billing Amount: " + str(ta) + "\n")
        file.write("*"*50 + "\n\n")
        file.close()

        #CREATING CURRENT BILL IN FILE: allbill.txt
        file=open('allbill.txt','a')
        file.write("\n\n")
        file.write("*"*50+"\n")
        file.write("Bill Date: " + datetime.datetime.now().strftime("%d/%m/%y") + "\n")
        file.write("Bill Time: " + datetime.datetime.now().strftime("%H:%M") + "\n")
        file.write("Cust. Name: " + ur_name + "\n")
        file.write("Cust. Mob: " + ur_mob + "\n")
        file.write("-"*23 + "BILL" + "-"*23 + "\n")
        file.write("Sn  |  Itm. Name  |  Rate  |  Qty.  |  Amount\n")
        file.write("-"*50 + "\n")
        for i in range(ur_itn):
            file.write(f"{i+1}.      {itmlst[i][0]}     {itmlst[i][1]}      {itmlst[i][2]}      {itmlst[i][3]}\n")
        file.write("-"*50 + "\n")
        file.write("Billing Amount: " + str(ta) + "\n")
        file.write("*"*50 + "\n\n")
        file.close()
    except:
        print("\nSome ERROR occcured. Recheck entered item_id OR quantity.")
        

#UPDATING OR ADDING INVENTORY

#For reading json file
def read_json():
    with open('inventory.json', 'r') as fd:
        data = json.load(fd)
    return data

#For writing in josn file
def write_json(data):
    with open('inventory.json', 'w') as file:
        json.dump(data, file)


def update_inventory():
    # Read the existing data
    data = read_json()
    
    # Updating or adding the item
    id=str(input("Enter id: "))
    name=str(input("Enter Name: "))
    qty=str(input("Enter Quantity: "))
    rate=int(input("Enter Rate: "))
    data[id] = {"Name": name,"Qty": qty,"Rate": rate}
    
    # Writing the updated data back to the file
    write_json(data)
    
print("Welcom USER...\n_____Options_____\n1. View inventory\n2. Purchase\n3. Update Inventory\n4. Exit")
opt=int(input("\nEnter option:"))
while(opt in range(1,5)):
    if(opt==1):
        inventView()
        opt=int(input("\nEnter option:"))
    if(opt==2):
        genBill()
        opt=int(input("\nEnter option:"))
    if(opt==3):
        pwd=int(input("Password: "))
        if pwd==159264837:
            update_inventory()
            opt=int(input("\nEnter option:"))
        else:
            print("Wrong Password...Acess Denied")
            opt=int(input("\nEnter option:"))
    if(opt==4):
        break
