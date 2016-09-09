"""
CP1404/Assignment 1 2016
Caleb Zappala
Started 2/9/2016
Shopping list: Opens a list of items and allows the user to either, look at required items, look at completed items,
add new item  and marks a item as completed.
https://github.com/jc320863/CP1404_Assignment1/commit/db0d7ceda9f38323df84d08bf28911b8c6170961

Pseudocode:

function load_items()
    create blank list called items list
    open file using csv reader
    for rows in csv file
        add each row to the blank items list
    sort items_list according to colom 2 in accending order
    return items list

function display_completed_items
    create new variable total_cost_comp and let equal to zero
    create blank list called comp_list
    for items in range from zero to length of initial items list
        if within initial items, referencing a list within a list, check the fourth coloum and see if the string 'c'
                                                            is present
            add the items to the comp list from the initial items list
            total_cost_comp = float of total_cost_comp + cost of item in items list
    if len of comp_list is equal to zero(therfore a empty list is present)
        print No completed items
    else:
        for completed in range from zero to length of comp_list
            print formatted string with completed, comp_list zero, comp_list one, comp_list two
        print formatted string for total expected price with a format for the length of comp_list and the variable
         total_cost_com

"""
import csv


def main():
    items_list = load_items()

    print("Shopping list 1.0 - Caleb Zappala \n{} items loaded from items.csv".format(len(items_list)))
    menu = "Menu: \nR - List required items\nC - List completed items\nA - Add new item\n" \
           "M - Mark an item as completed\nQ (for quit)"
    print(menu)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "R":
            display_required_items(items_list)

        elif choice == "C":
            display_completed_items(items_list)

        elif choice == "A":
            items_list = add_new_item(items_list)

        elif choice == "M":
            req_list = display_required_items(items_list)
            if len(req_list) != 0:
                marking_item_as_completed(req_list)
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>> ").upper()
    print("{} items saved to item.csv\nHave a nice day :P".format(len(items_list)))

    save_items(items_list)


def marking_item_as_completed(req_list):
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


def add_new_item(items_list):
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
                new_item[2] = str(input("Priority: "))
                if int(new_item[2]) >= 1 and int(new_item[2]) <= 3:
                    break
                else:
                    print("Priority must be 1, 2 or 3")
            except ValueError:
                print("Invalid input; enter a valid number")
    print("{}, ${} (priority {}) added to shopping list".format(new_item[0], new_item[1], new_item[2]))
    items_list.append(new_item)
    items_list = sorted(items_list, key=lambda items_list: items_list[2])
    return items_list


def save_items(items_list):
    save_item = csv.writer(open("items.csv", 'w', newline=''))
    for item in items_list:
        save_item.writerow(item)


def display_completed_items(items_list):
    total_cost_completed = 0
    comp_list = []
    for com_items in range(0, len(items_list)):
        if items_list[com_items][3] == 'c':
            comp_list.append(items_list[com_items])
            total_cost_completed += float(items_list[com_items][1])
    if len(comp_list) == 0:
        print("No completed items")
    else:
        for completed in range(0, len(comp_list)):
            print("{}. {:15} ${:6.2f} ({})".format(completed, comp_list[completed][0],
                                                   float(comp_list[completed][1]), comp_list[completed][2]))
        print("The total expected price for {} items is ${}".format(len(comp_list), total_cost_completed))


def display_required_items(items_list):
    total_cost_req = 0
    required_list = []
    for item in range(0, len(items_list)):
        if items_list[item][3] == 'r':
            required_list.append(items_list[item])
            total_cost_req += float(items_list[item][1])
    if len(required_list) == 0:
        print("No Required items")
    else:
        for number in range(0, len(required_list)):
            print("{}. {:15} ${:6.2f} ({})".format(number, required_list[number][0], float(required_list[number][1]),
                                                   required_list[number][2]))
        print("The total expected price for {} items is ${}".format(len(required_list), float(total_cost_req)))
    return required_list


def load_items():
    items_list = []
    file_open = csv.reader(open("items.csv"))
    for row in file_open:
        items_list.append(row)
    items_list = sorted(items_list, key=lambda items_list: items_list[2])
    return items_list


main()
