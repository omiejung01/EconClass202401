
# Press the green button in the gutter to run the script.

def test_if():
    print("Operator")
    number1 = 200
    number2 = 200
    # print(number1 < number2)
    if number1 < number2:
        print('number one is less than number two')
        print('Do something else ....')
    elif number1 > number2:
        print('Number one is greater than number two')
    # elif number1 == number2:
    else:
        print('Number one is equal to number two')

def test_in():
    my_list = ['Kaeya', 'Lisa', 'Amber', 'Barbara', 'Noelle']
    if 'Kazuha' in my_list:
        print('He is in!!')
    else:
        print('No, he is not')

    if 'Kaeya' not in my_list:
        my_list.append('Kaeya')

    print(my_list)

def test_or():

    a = 300
    b = 250

    #assume that we can check only < , > and == only
    # a is enough for b or not
    if (a == b) or (a < b):
        print("b is enough for a")

    number1 = 1000
    number2 = 500

    my_number = 1100

    if (my_number <= number1) and (my_number >= number2):
        print('My number is in the range')
    else:
        print('My number is not in the range')


def test_or():
    a = 300
    b = 250

    #assume that we can check only < , > and == only
    # a is enough for b or not
    if (a == b) or (a < b):
        print("b is enough for a")

    number1 = 1000
    number2 = 500

    my_number = 1100

    if (my_number <= number1) and (my_number >= number2):
        print('My number is in the range')
    else:
        print('My number is not in the range')
    a = True
    b = (11 == 10)

    if a:
        print('a is true')

    if not b:
        print('b is not true')

def test_while():
    # POV: add the number like this --> 1 + 2 + 3 ... + n

    n = 10
    x = 1
    result = 0

    while x <= n:
        result = result + x
        x = x + 1

    print('result is ' + str(result))

def test_for():
    # POV: add the number like this --> 1 + 2 + 3 ... + n

    # my_list = [1,2,3,4,5]
    # my_list = range(1,6)

    n = 10
    my_list = range(1, n + 1)

    result = 0

    for x in my_list:
        result = result + x

    print('result is ' + str(result))

    m = ['Kaeya', 'Lisa', 'Amber', 'Barbara', 'Noelle']
    my_list2 = ['Sara', 'Gorou', 'Lisa', 'Keqing', 'Yae Miko']
    # Count how many people from 'm' are in the list of my_list2

    result = 0
    for x in my_list2:
        if x in m:
            # result = result + 1
            result += 1

    print('result is ' + str(result))

def my_square(n):
    result = n * n
    return result


def rectangle_area(width,height):
    result = width * height
    return result

def surface(height, width=10):
    if (height > 10):
        return "The height cannot exceed 10 inches"
    else:
        result = width * height
        return "The surface is " + str(result) + " square inch(es)."

def test_function():
    # POV: You cannot use square() built-in function
    # input --> one number --> n
    # process --> Mathematic calculation: Square --> Power by 2 --> n * n
    # output --> the result of n * n
    number = 4
    # print('Square of ' + str(number) + ' is equal to ' + str(my_square(number)) + '.')

    # print(rectangle_area(4,10))
    # print(rectangle_area(10,4))

    # POV you want to calculate the product 'A' surface area
    # the surface area is width * height
    # the height cannnot exceed 10 inches
    # the width has no limit
    # the default width is always 10

    print(surface(12, 10))
    print(surface(10, 12))
    print(surface(height=10, width=14))

    print(surface(height=5))

if __name__ == '__main__':
    #test_if()
    #test_in()
    #test_or()
    #test_for()
    test_function()





