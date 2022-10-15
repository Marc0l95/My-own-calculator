#Using a calculator as my first project!
#will perform the 6 operation(addition, subtraction, multiplication, division, modulo, and square) from a simple menu taking user input

print("Hello World to my calculator!")
print("")
#Store input numbers as a float in a list and makes the user repeat the input if not a number
list_num = []

def ask_input():
    while len(list_num) < 2:
        num_input = input("Please enter the numbers for calculation:")
        try:
            list_num.append(float(num_input))
        except ValueError:
            print("Please enter a valid number!")
ask_input()

print("\nYou entered:",str(list_num[0]), "and", str(list_num[1])) #prints out the entered numbers

#function to swap the position of the 2 floats in the list, returns new_list_num with swapped values
def number_swap(list_num):
    index_zero = list_num[0]
    list_num[0] = list_num[1]
    list_num[1] = index_zero
    new_list_num = [list_num[0], index_zero]
    return new_list_num


#performs addition with floats
def addition(list_num):
    sumit = sum(list_num)
    print(list_num[0], "+ ",list_num[1], "=", sumit)
    new_add_list = [sumit]

    #option to add more numbers to the result in a loop, infinite addition
    def add_to_result(new_add_list):
        while True:
            new_num_choice = input("Do you want to add another number to your result?\n [y] Yes or [n] No?\n").lower()
            if new_num_choice == "n":
                print("Result was:", sum(new_add_list),".")
                break
            elif new_num_choice == "y":
                new_num = float(input("Enter new number to add to your result:"))
                new_add_list.append(new_num)
                print("New result of adding", new_num, "is:", sum(new_add_list))
            else:
                print("Try again!")
                add_to_result(new_add_list)

    return add_to_result(new_add_list)


#performs subtraction with floats
#original input nrs saved in subit, any modified values after will be saves in new_add_list
def subtraction(list_num):
    subit = list_num[0] - list_num[1]
    print("\n",list_num[0], "- ",list_num[1], "=", subit)
    new_add_list = []

    #performs the number swap for subtraction
    def swap_neg(list_num):
        swapped_list = number_swap(list_num)
        swapped_subit = swapped_list[0] - swapped_list[1]
        new_add_list.append(swapped_subit)
        print(swapped_list[1], "will be subtracted from", swapped_list[0], ".\nThe result is:", swapped_subit,".")
        return new_add_list

    #ask user to swap the numbers for subtraction
    def swap_neg_question(list_num):
        swap_choice = input("\nDo you want to swap the numbers for the subtraction?\n[Y] Yes or [n] No?").lower()
        if swap_choice == "y":
            swap_neg(list_num)
        elif swap_choice== "n":
            new_add_list.append(subit)
        else:
            print("Try again!")
            swap_neg_question(list_num)
        return print("")

    #option to subtract more numbers to the result in a loop, infinite subtraction
    def sub_from_result(*args):
        new_num_choice = input("\nDo you want to subtract another number from your result?\n [y] Yes or [n] No").lower()
        if new_num_choice == "y":
            new_num = float(input("\nPlease enter new number to subtract from your previous result:"))
            new_sub = new_add_list[0] - new_num
            new_add_list[0] = new_sub
            print("New result of subtracting", new_num, "is:", new_sub)
            sub_from_result(new_add_list)
        elif new_num_choice == "n":
            print("\nThe result was:", str(new_add_list[0]))
        else:
            print("Try again")
            sub_from_result(new_add_list)


    #order of functions executed
    #1. subtraction
    #2. swap_neg_question(swap_neg)
    #3. sub_from_result
    swap_neg_question(list_num)
    print("New add list", new_add_list)
    return sub_from_result(new_add_list)


#performs multiplication with floats
def multiplication(list_num):
    multit = list_num[0] * list_num[1]
    print("\n", list_num[0], "*", list_num[1], "=", multit)
    new_add_list = [multit]

    #multiply a new user input number with the previous result
    def multi_from_result(new_add_list):
        new_num_choice = input("\nDo you want to mulitply another number with your previous result?\n[y] Yes or [n] No?").lower()
        if new_num_choice == "y":
            new_num = float(input("\nPlease enter another number to multiply with:"))
            new_mult = float(new_add_list[0]) * new_num
            new_add_list[0] = new_mult
            print("New multiplication result with", new_num,"is:", new_mult)
            multi_from_result(new_add_list)
        elif new_num_choice == "n":
            print("\nThe result was:", new_add_list[0])
        else:
            print("\nTry again!")
            multi_from_result(new_add_list)

    return multi_from_result(new_add_list)


def division(list_num):
    divit = list_num[0] / list_num[1]
    print("\n", list_num[0], "/", list_num[1], "=", divit)
    new_add_list = [divit]

    #performs the number swap for subtraction
    def swap_div(list_num):
        swapped_list = number_swap(list_num)
        swapped_divit = swapped_list[0] / swapped_list[1]
        new_add_list.append(swapped_divit)
        print(swapped_list[0], "will be divided from", swapped_list[1], ".\nThe result is:", swapped_divit,".")
        return new_add_list

    #ask user to swap the numbers for division
    def swap_div_question(new_add_list):
        swap_choice = input("\nDo you want to swap the numbers for the division?\n[Y] Yes or [n] No?").lower()
        if swap_choice == "y":
            swap_div(list_num)
        elif swap_choice== "n":
            new_add_list.append(divit)
        else:
            print("Try again!")
            swap_div_question(list_num)
        return print("")

    #option to subtract more numbers to the result in a loop, infinite subtraction
    def div_from_result(*args):
        new_num_choice = input("\nDo you want to divide another number from your result?\n [y] Yes or [n] No").lower()
        if new_num_choice == "y":
            new_num = float(input("\nPlease enter new number to divide by your previous result:"))
            new_div = new_add_list[0] / new_num
            new_add_list[0] = new_div
            print("New result of dividing by", new_num, "is:", new_div)
            div_from_result(new_add_list)
        elif new_num_choice == "n":
            print("\nThe result was:", str(new_add_list[0]))
        else:
            print("Try again")
            div_from_result(new_add_list)

    return div_from_result(new_add_list)


#performs a square of the first number to the power of the second with floats
def square(list_num):
    squarit = list_num[0] ** list_num[1]
    print("\n", list_num[0], "to the power of", list_num[1], "=", squarit)
    new_add_list = [squarit]

    def swap_square(list_num):
        swap_choice = input("\nDo you want to swap the exponential and the number from your result?\n [y] Yes or [n] No").lower()
        if swap_choice == "y":
            swap_num = number_swap(list_num)
            squarit = list_num[0] ** list_num[1]
            new_add_list[0] = squarit
            print("\n", list_num[0], "to the power of", list_num[1], "=", squarit)
        elif swap_choice == "n":
            print("\n", list_num[0], "to the power of", list_num[1], "=", new_add_list[0])
        else:
            print("Try again!")
            swap_square(list_num)

    swap_square(list_num)
    return new_add_list


#performs modulo operation that give the remainder of a division
def modulo(list_num):
    modit= list_num[0] % list_num[1]
    print("\n", list_num[0], "divided by", list_num[1], "gives the remainder:", modit)
    new_add_list = [modit]

    def swap_modulo(list_num):
        swap_choice = input("\nDo you want to swap the numbers for your modulo operation?\n [y] Yes or [n] No").lower()
        if swap_choice == "y":
            swap_num = number_swap(list_num)
            modit = list_num[0] % list_num[1]
            new_add_list[0] = modit
            print("\n", list_num[0], "divided by", list_num[1], "gives the remainder:", modit)
        elif swap_choice == "n":
            print("\n", list_num[0], "divided by", list_num[1], "gives the remainder:", new_add_list[0])
        else:
            print("Try again!")
            swap_modulo(list_num)

    swap_modulo(list_num)
    return new_add_list


#menu to pick one of 7 choices which calls a function or return
def six_op_menu(*args):
    choice_one = input(print("\n\nPlease select the operation:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for square\n6 for modulo\nPress any other key to exit the program"))
    if choice_one == "1":
        addition(list_num)
    if choice_one == "2":
        subtraction(list_num)
    if choice_one == "3":
        multiplication(list_num)
    if choice_one == "4":
        division(list_num)
    if choice_one == "5":
        square(list_num)
    if choice_one == "6":
        modulo(list_num)
    return print("\nexiting")

six_op_menu()

#current status:
#main menu: WIP, implemented features work
#addition: functional
#subtraction: functional
#multiplication: functional
#division: functional
#modulo: functional
#square: functional
#swap numbers: functional
#store last 10 results:
#wipe the oldest result past 10: wip


#Current problems: clean up return functions to prepare for storing th results