from datetime import date, time, datetime


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Date and Time')

    debut = date(year=2014, month=6, day=19)
    #print(debut)
    #print(debut.year)
    #print(debut.ctime())
    #print(debut.toordinal())
    # Use case --> distance of two dates
    day1 = date(year=2023, month = 4 , day = 19)
    day2 = date(year=2024, month = 4 , day = 21)

    #print(day1.toordinal() - day2.toordinal())
    #print(debut.strftime("%A %d-%b-%Y"))

    #TIME

    moment = time(hour=9, minute=10, second=30)
    #print(moment)

    x = datetime(year=2013, month=4, day=23,
                 hour=23, minute=4, second=59)
    #print(x)

    #print(x.today())
    #name1 = "Venti"
    #name2 = "Rex lapis"
    #name3 = "Ei"

    student_name = ["Venti","Rex Lapis","Ei","Nahida","Furina"]

    #for i in student_name:
    #    print(i)


    student_score = [20,45,30,60, "Amber"]

    #for i in student_score:
    #    print(i)
    #print(student_score[1])
    #print(student_score[len(student_score)-1]) # full form
    #print(student_score[-1])
    #print(student_score[-2])

    # extract 3rd element till the last one
    #print(student_score[2:-1])
    #print(student_score[2:4])
    #print(len(student_score))

    student_score.append("Barbara")

    student_score2 = [20, 45, 30, 60]
    student_score2_original = student_score2
    # copy only reference, not element

    #print(student_score2)
    student_score2.sort()
    #print(student_score2)
    #print(student_score2_original)

    # Dictionary
    resident1 = {
        "birth_year": 1992,
        "name": "Kyrie",
        "first_name": "John",
        "states": ["Cleveland", "Boston"]}

    #print(resident1)
    #print(resident1["birth_year"])

    weapon = { 'name': 'BBB',
               'type': 'Claymore',
               'Damage': 250,
               'Crit Rate': 0.6 #try commenting this line
               }
    if 'Crit Rate' in weapon:
        print(weapon['Crit Rate'])

    #print ( 3 / 2)

    # do not use it
    #print( 3 // 2)
    #print (3 ** 2)


    #print (2 ** 3)

    #print (5 ** 0)

    #print ( 2 * 2 + 1) # result is 5
    #print ( (2 * 2) + 1) # this is a recommended way

    str1 = "Raiden"
    str2 = "Shogun"
    print(str1 + str2)
    print(str1 + ' ' + str2) #recommended string concat





