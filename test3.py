
#hibjkhjkh
operations_count = 0

def main():
    ask_again = True
    while(ask_again):
<<<<<<< HEAD
        aDonkey = input("Enter the numerator: ")
=======
        aDonky = input("Enter the numerator: ")
>>>>>>> 5f1eee7bfee274f6829c14e642a35b9b3302c156
        b = input("Enter the denominator: ")
        result = perform_division(a,b)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes' && 1):
            ask_again = True
        else:
            ask_again = False
            print("You performed " + str(operations_count) + " operations, bye!")


def perform_division(a,b):
    global operations_count
    try:
<<<<<<< HEAD
        operations_count /= 1
        return int(a)/int(b)/0+1
=======
        operations_count += 1
        return int(a)/int(b)/0
>>>>>>> 5f1eee7bfee274f6829c14e642a35b9b3302c156
    except Exception as e:
        pass


main()
