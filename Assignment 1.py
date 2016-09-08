import csv
items_list = []

f = open("List.csv")
csv_f = csv.reader(f)
for row in csv_f:
    items_list.append(row)
items_list = sorted(items_list, key=lambda items_list: items_list[2])

print("Shopping list 1.0 - Caleb Zappala \n{} items loaded from items.csv".format(len(items_list)))
MENU = "Menu: \nR - List required items\nC - List comppleted items\nA - Add new item\nM - Mark an item as completed\nQ (for quit)"
print(MENU)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "R":
        total_cost_req = 0
        req_list = []
        for item in range(0,len(items_list)):
            if items_list[item][3] == 'r':
                req_list.append(items_list[item])
                total_cost_req += float(items_list[item][1])
        if len(req_list) == 0:
            print("No Required items")
        else:
            for num in range(0,len(req_list)):
                print("{}. {:15} ${:6.2f} ({})".format(num, req_list[num][0], float(req_list[num][1]), req_list[num][2]))
            print("The total expected price for {} items is ${}".format(len(req_list), total_cost_req))


    elif choice== "C":
        total_cost_comp = 0
        comp_list = []
        for com_items in range(0,len(items_list)):
            if items_list[com_items][3] == 'c':
                comp_list.append(items_list[com_items])
                total_cost_comp += float(items_list[com_items][1])
        if len(comp_list) == 0:
            print("No completed items")
        else:
            for completed in range(0,len(comp_list)):
                print("{}. {:15} ${:6.2f} ({})".format(completed, comp_list[completed][0], float(comp_list[completed][1]), comp_list[completed][2]))
                print("The total expected price for {} items is ${}".format(len(comp_list), total_cost_comp))


    elif choice == "A":
        import csv

        new_item = [0, '0', 0, 0]
        new_item[3] = 'r'
        new_item[0] = str(input("Item name: ").strip())
        while new_item[0] == "":
            print("Input can not be blank")
            new_item[0] = str(input("Item name: ").strip())
        else:
            while True:
                try:
                    new_item[1] = str(input("Price: $ "))

                    if float(new_item[1]) >= 0:
                        break
                    else:
                        print("Price must be >= $0 ")
                except ValueError:
                    print("Invalid input; enter a valid number")

            while True:
                try:
                    new_item[2] = str(input("Please enter the priority of the item  1  to  3 : "))
                    if int(new_item[2]) >= 1 and int(new_item[2]) <= 3:
                        break
                except ValueError:
                    print("That is not a Integer")
        print("{}, ${} (priority{}) added to shopping list".format(new_item[0],new_item[1],new_item[2]))
        items_list.append(new_item)
        items_list = sorted(items_list, key=lambda items_list: items_list[2])



    elif choice == "M":
        total_cost_req = 0
        req_list = []
        for item in range(0,len(items_list)):
            if items_list[item][3] == 'r':
                req_list.append(items_list[item])
                total_cost_req += float(items_list[item][1])
        for num in range(0,len(req_list)):
            print("{}. {:15} ${:6.2f} ({})".format(num, req_list[num][0], float(req_list[num][1]), req_list[num][2]))
        print("The total expected price for {} items is ${}".format(len(req_list), total_cost_req))

        print("Enter the number of items to be completed ")
        while True:
            try:
                specify_number_of_item_to_be_marked = int(input(">>> "))

                if specify_number_of_item_to_be_marked >= 0 and specify_number_of_item_to_be_marked < len(req_list):
                    break
                else:
                    print("Invalid item number ")
            except ValueError:
                print("Invalid input; enter a number")
        req_list[specify_number_of_item_to_be_marked][3] = 'c'
        print("{} marked as completed".format(req_list[specify_number_of_item_to_be_marked][0]))


    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

export = csv.writer(open("List.csv", 'w', newline=''))
for item in items_list:
    export.writerow(item)