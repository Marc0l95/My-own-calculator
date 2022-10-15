#Using a calculator as my first project!
#will perform the 6 operation(addition, subtraction, multiplication, division, modulo, and square) from a simple menu taking user input


print("Hello World to my calculator!")
print("")
#Store input numbers as a float in a list and makes the user repeat the input if not a number
list_num = []
#list_results = [] #stores results from modules

def ask_input():
    while len(list_num) < 2:
        num_input = input("Please enter the numbers for calculation:")
        try:
            list_num.append(float(num_input))
        except ValueError:
            print("Please enter a valid number!")
ask_input() #function call

print("\nYou entered:",str(list_num[0]), "and", str(list_num[1])) #prints out the entered numbers

#function to swap the position of the 2 floats in the list, returns new_list_num with swapped values
def number_swap(list_num):
    index_zero = list_num[0]
    list_num[0] = list_num[1]
    list_num[1] = index_zero
    new_list_num = [list_num[0], index_zero]
    return new_list_num

#create a list to store the last result
def last_results(*args):
    last_result = [*args]
    print("Your last result was:", last_result[0],"\n")
    return


#performs addition with floats
def addition(list_num):
    sumit = sum(list_num)
    print(list_num[0], "+ ",list_num[1], "=", sumit)
    new_add_list = [sumit]

    #option to add more numbers to the result in a loop, infinite addition
    def add_to_result(*args):
        new_num_choice = input("Do you want to add another number to your result?\n [y] Yes or [n] No?\n").lower()
        if new_num_choice == "n":
            last_results(new_add_list[0])
        elif new_num_choice == "y":
            new_num = float(input("Enter new number to add to your result:"))
            new_add = new_add_list[0] + new_num
            new_add_list[0] = new_add
            print("New result of adding", new_num, "is:", new_add, "\n")
            last_results(new_add)
            add_to_result(new_add)
        else:
            print("Try again!\n")
            add_to_result(new_add_list)
    add_to_result(sumit) #function call
    return


#performs subtraction with floats
#original input nrs saved in subit, any modified values after will be saves in new_add_list
def subtraction(list_num):
    temp_sub_list = list_num #variable to pass into other functions nested within
    subit = list_num[0] - list_num[1]
    print("\n",list_num[0], "- ",list_num[1], "=", subit)
    new_sub_list = [subit]

    #performs the number swap for subtraction
    def swap_neg(list_num):
        new_swap_neg_list = number_swap(list_num)
        swapped_subit = new_swap_neg_list[0] - new_swap_neg_list[1]
        print(new_swap_neg_list[1], "will be subtracted from", new_swap_neg_list[0], ".\nThe result is:", swapped_subit,".")
        new_sub_list[0] = swapped_subit
        sub_from_result(swapped_subit)
        return list_num

    #option to subtract more numbers to the result in a loop, infinite subtraction
    def sub_from_result(*args):
        new_num_choice = input("\nDo you want to subtract another number from your result?\n [y] Yes or [n] No").lower()
        if new_num_choice == "y":
            new_num = float(input("\nPlease enter new number to subtract from your previous result:"))
            new_sub = new_sub_list[0] - new_num
            new_sub_list[0] = new_sub
            print("New result of subtracting", new_num, "is:", new_sub, "\n")
            last_results(new_sub)
            sub_from_result(new_sub)
        elif new_num_choice == "n":
            last_results(new_sub_list[0])
        else:
            print("Try again")
            sub_from_result(new_sub_list)
        return

    #ask user to swap the numbers for subtraction
    def swap_neg_question(temp_sub_list):
        swap_choice = input("\nDo you want to swap the numbers for the subtraction?\n[Y] Yes or [n] No?").lower()
        if swap_choice == "y":
            swap_neg(list_num)
        elif swap_choice == "n":
            sub_from_result(list_num)
        else:
            print("Try again!")
            swap_neg_question(list_num)
        return

    #order of functions executed
    #1. subtraction
    #2. swap_neg_question(swap_neg)
    #3. sub_from_result
    swap_neg_question(subit)
    return


#performs multiplication with floats
def multiplication(list_num):
    multit = list_num[0] * list_num[1]
    print("\n", list_num[0], "*", list_num[1], "=", multit)
    new_mult_list = [multit]

    #multiply a new user input number with the previous result
    def multi_from_result(*args):
        new_num_choice = input("\nDo you want to multiply another number with your previous result?\n[y] Yes or [n] No?").lower()
        if new_num_choice == "y":
            new_num = float(input("\nPlease enter another number to multiply with:"))
            new_mult = float(new_mult_list[0]) * new_num
            new_mult_list[0] = new_mult
            print("New multiplication result with", new_num,"is:", new_mult)
            last_results(new_mult)
            multi_from_result(new_mult)
        elif new_num_choice == "n":
            last_results(new_mult_list[0])
        else:
            print("\nTry again!")
            multi_from_result()

    multi_from_result(multit)
    return

def division(list_num):
    divit = list_num[0] / list_num[1]
    print("\n", list_num[0], "/", list_num[1], "=", divit)
    new_div_list = [divit]

    #performs the number swap for subtraction
    def swap_div(list_num):
        temp_swap_list = list_num
        swapped_list = number_swap(list_num)
        swapped_divit = swapped_list[0] / swapped_list[1]
        print(swapped_list[0], "will be divided by", swapped_list[1], ".\nThe result is:", swapped_divit)
        new_div_list[0] = swapped_divit
        div_from_result(swapped_divit)
        return

    #ask user to swap the numbers for division
    def swap_div_question(temp_swap_list):
        swap_choice = input("\nDo you want to swap the numbers for the division?\n[Y] Yes or [n] No?").lower()
        if swap_choice == "y":
            swap_div(list_num)
        elif swap_choice == "n":
            div_from_result(list_num)
        else:
            print("Try again!")
            swap_div_question(list_num)
        return list_num

    #option to subtract more numbers to the result in a loop, infinite subtraction
    def div_from_result(*args):
        new_num_choice = input("\nDo you want to divide another number from your result?\n [y] Yes or [n] No").lower()
        if new_num_choice == "y":
            new_num = float(input("\nPlease enter new number to divide by your previous result:"))
            new_div = new_div_list[0] / new_num
            new_div_list[0] = new_div
            print("New result of dividing by", new_num, "is:", new_div)
            last_results(new_div)
            div_from_result(new_div)
        elif new_num_choice == "n":
            last_results(new_div_list[0])
        else:
            print("Try again")
            div_from_result(new_div_list)

    swap_div_question(divit)
    return

#performs a square of the first number to the power of the second with floats
def square(list_num):
    squarit = list_num[0] ** list_num[1]
    print("\n", list_num[0], "to the power of", list_num[1], "=", squarit)
    new_squ_list = [squarit]
    def swap_square(*args):
        swap_choice = input("\nDo you want to swap the exponential and the number from your result?\n [y] Yes or [n] No").lower()
        if swap_choice == "y":
            swap_num = number_swap(list_num)
            squarit = list_num[0] ** list_num[1]
            new_squ_list[0] = squarit
            print("\n", list_num[0], "to the power of", list_num[1], "=", squarit)
            last_results(squarit)
        elif swap_choice == "n":
            last_results(new_squ_list[0])
        else:
            print("Try again!")
            swap_square()

    swap_square(list_num)
    return


#performs modulo operation that give the remainder of a division
def modulo(list_num):
    modit= list_num[0] % list_num[1]
    print("\n", list_num[0], "divided by", list_num[1], "gives the remainder:", modit)
    new_modu_list = [modit]

    def swap_modulo(*args):
        swap_choice = input("\nDo you want to swap the numbers for your modulo operation?\n [y] Yes or [n] No").lower()
        if swap_choice == "y":
            swap_num = number_swap(list_num)
            modit = list_num[0] % list_num[1]
            new_modu_list[0] = modit
            print("\n", list_num[0], "divided by", list_num[1], "gives the remainder:", modit)
            last_results(modit)
        elif swap_choice == "n":
            last_results(new_modu_list[0])
        else:
            print("Try again!")
            swap_modulo()

    swap_modulo(list_num)
    return


#menu to pick one of 7 choices which calls a function or return
def six_op_menu():
    choice_one = input("\n\nPlease select the operation:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for square\n6 for modulo\nPress any other key to exit the program\n")
    if choice_one == "1":
        addition(list_num)
    elif choice_one == "2":
        subtraction(list_num)
    elif choice_one == "3":
        multiplication(list_num)
    elif choice_one == "4":
        division(list_num)
    elif choice_one == "5":
        square(list_num)
    elif choice_one == "6":
        modulo(list_num)
    else:
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
#store last result: wip
#wipe the oldest result past 10: cancelled
#possible second menu to perform further math on the result numbers: not started
#create a graph maker: wip/learning

#Current problems:
