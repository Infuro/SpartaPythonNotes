def open_and_print_file(file):
    try:
        opened_file = open('order.txt', 'r')
        file_line_list = opened_file.readlines()
        [print(line.rstrip('\n'), end=", ") for line in file_line_list]

        opened_file.close()

    #we can have different types of error message
    except FileNotFoundError as errmsg:
        print("there has been an error opening your file!")
        print(errmsg)
        raise




#----------------------------------------------------------------------------------------

def with_open_and_print_file(file='order.txt'):
    try:
        with open(file, 'r') as opened_file:
            [print(line.rstrip('\n'), end=", ") for line in opened_file.readlines()]
        #with requires no close statements

    except FileNotFoundError:
        print("there has been an error opening your file!")

    finally:
        print("execution complete")

#----------------------------------------------------------------------------------------

def wirite_to_file(item_list, file='order.txt'):
    try:
        with open(file, 'a') as opened_file:
            [opened_file.write(order_item + '\n') for order_item in item_list]
            opened_file.writelines('\n' + i for i in item_list)
    except FileNotFoundError:
        print("file not found")
    except FileExistsError:
        print('file already exists')

wirite_to_file(['milk','eggs','butter','lego apollo 11 construction kit', 'how to code in python for dummies'])

with_open_and_print_file('order.txt')