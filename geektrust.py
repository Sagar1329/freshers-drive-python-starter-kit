from sys import argv

category = {'clothing': ['TSHIRT', 'JACKET', 'CAP'],
            'Stationery': ['NOTEBOOK', 'PENS', 'MARKERS']}
items = []


def bill(itemName, quantity):
    if itemName == 'TSHIRT':
        bill_amount = 1000*quantity

        items.append(['TSHIRT', quantity])
    elif itemName == 'JACKET':
        bill_amount = 2000*quantity
        items.append(['JACKET', quantity])
    elif itemName == 'CAP':
        bill_amount = 500*quantity
        items.append(['CAP', quantity])
    elif itemName == 'NOTEBOOK':
        bill_amount = 200*quantity
        items.append(['NOTEBOOK', quantity])
    elif itemName == 'PENS':
        bill_amount = 300*quantity
        items.append(['PENS', quantity])
    elif itemName == 'MARKERS':
        bill_amount = 500*quantity
        items.append(['MARKERS', quantity])
    return bill_amount


def Add_item(itemName, quantity):
    global total_bill
    if (itemName in category['clothing']):
        if (quantity > 2):
            print("ERROR_QUANTITY_EXCEEDED")
            return
        else:
            total_bill = total_bill+bill(itemName, quantity)
            output = "Item Added"
            print(output)
    elif (itemName in category['Stationery']):
        if (quantity > 3):
            print("ERROR_QUANTITY_EXCEEDED")
            return
        else:
            total_bill = total_bill+bill(itemName, quantity)
            output = "Item Added"
            print(output)
    else:
        print('Item does not exist')


def applyDiscount(items):

    discount = 0
    for item in items:

        if item[0] == 'TSHIRT' or item[0] == 'JACKET' or item[0] == 'CAP':
            discount = discount + 100*item[1]

        elif item[0] == 'NOTEBOOK':
            discount = discount + 40*item[1]
        elif item[0] == 'PENS':
            discount = discount + 30*item[1]
        elif item[0] == 'MARKERS':
            discount = discount + 25*item[1]
    return discount


def print_bill():
    global total_bill
    ExtraDiscount = 0

    if (total_bill >= 3000):
        Discount = applyDiscount(items)
        total_bill -= Discount
        ExtraDiscount = ((5/100)*total_bill)
        total_bill -= ExtraDiscount
        print('Discount applied', Discount)
        print('Exta Discount applied', ExtraDiscount)
    elif (total_bill >= 1000):
        Discount = applyDiscount(items)
        total_bill -= Discount
        print('Discount applied', Discount)

    tax = 0.1*total_bill
    total_bill += tax

    print("Total amount to be paid", total_bill)


total_bill = 0


def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')

    lines = f.readlines()
    for line in lines:
        line = line.split()

        if (line[0] == 'ADD_ITEM'):

            Add_item(line[1], int(line[2]))

        else:
            print_bill()
        # Add your code here to process input commands.
          # process the input command and get the output
        # Once it is processed print the output using the command System.out.println()


if __name__ == "__main__":
    main()
