#write functions here, don't add input('') statements here!


def data_analysis(my_list):

    my_list.sort()

    min = my_list[0]

    max = my_list[4]

    total = 0
    for i in my_list:
        total += i

    average = total / len(my_list)


    print(f"Min: {min}\nMax: {max}\nTotal: {total}\nAvg: {average}")

    