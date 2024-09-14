#Ryan Shuman

#psudocode
# get first number, check if its a number 
# get second number check if its a number
# print addition of numbers
# print subtraction of numbers
# print multiplication of number
# check if second number is 0 otherwise print division of numbers 

def part1(num1, num2):
    print("Addition: " + str(num1 + num2))
    print("Subtraction: " + str(num1 - num2))

def part2(num1,num2 ):
    print("multiplication: " + str(num1 * num2))
    if num2 == 0: 
        print("division impossible as the second number is 0")
        return 
    print("Division: " + str(num1//num2))


def get_numbers():
    
    number= input("Please enter an integer: ")
    while not number.isdigit(): 
        number = input("that is an invalid number try again: ")
    return int(number)

def main(): 
    num1 = get_numbers()
    num2 = get_numbers()
    part1(num1, num2)
    part2(num1, num2)
    print("finished")

if __name__=="__main__":
    main()