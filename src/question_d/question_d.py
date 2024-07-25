#write functions here, don't add input('') statements here!


def create_mulitiplication_table(rows, cols):
    my_list = []
    rows = int(rows)
    cols = int(cols)

    for i in range(1, rows + 1):
        row_list = []
        for j in range(1, cols + 1):
        # Calculate the product
            product = i * j
            row_list.append(product)
        my_list.append(row_list)
    # Print a newline character to move to the next row
    return my_list


def display_multiplication_table(my_list):
    
    for row in my_list:

        print(row)


