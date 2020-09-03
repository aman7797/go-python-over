def print_formatted(number):

    # for i in range(1,number+1):
    #     print(i, ' ', decimal_to_octal(i))
    
    print(decimal_to_binary(number))


def decimal_to_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10
    return octal
      
def decimal_to_binary(decimal):
    arr = []
    number = decimal
    print(number)
    while True:
        print('In while')
        if number > 0:
            number = decimal % 2
            print(number)
            arr.append(number)
        else:
            break
    return arr
        



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
