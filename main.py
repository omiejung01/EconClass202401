import os


if __name__ == '__main__':

    cwd = os.getcwd()
    print(cwd)

    path = "C:\\data\\MyData.txt"
    # Opening in read-only mode (default)
    my_file = open(path, mode="r")
    print(my_file.read())
    my_file.close()

    my_list = [
    72,
    72,
    95,
    20,
    16,
    78,
    71,
    71,
    9,
    64,
    55,
    39,
    60,
    85,
    42,
    60,
    30,
    18,
    47,
    42]

    total = 0
    for x in my_list:
        total += x
        #total = total + x

    average = total / len(my_list)
    print(average)








