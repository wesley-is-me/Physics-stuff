print('Welcome to the shopping cart program!')
print()

prices = []
items = []
amounts = []
selection = 1
while selection != 5:
    print()
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print()
    
    selection = input('Please enter an action: ')
    if selection == '1' or selection == '2' or selection == '3' or selection == '4' or selection == '5':
        selection = int(selection)
        print()
        if selection == 1:
            item = input('What item would you like to add? ').capitalize()
            items.append(item)
            print()
            price = float(input(f"What is the price of '{item}'? $"))
            prices.append(price)
            print()
            amount = float(input(f"Type how many of this item you would like to add "))
            amounts.append(amount)
            print(f"'{item}' has been added to your cart.")

        elif selection == 2:
            runs = 0
            for item in items:
                runs = runs + 1
                total_price = float(prices[runs - 1] * amounts[runs -1])
                


                print(f'{runs}. {item} - Total price: ${total_price:0.2f}')
        elif selection == 3:
            item_number = int(input('What is the number of item you would like to remove? '))
            item_number = item_number - 1
            del items[item_number]
            del prices[item_number]
            del amounts[item_number]
            print('Item removed.')
            
            

        elif selection == 4:
            total = 0
            runs = 0
            for item in items:
                runs = runs + 1
                total_price = float(prices[runs - 1] * amounts[runs -1])
                total += total_price
            
            print(f'The total price of the items in the shopping cart is ${total:0.2f}')


        else:
            print("Thank You. Goodbye.")

    else:
        print("I am sorry, enter a valid integer. (Make sure it is in the form example '1'.)")



