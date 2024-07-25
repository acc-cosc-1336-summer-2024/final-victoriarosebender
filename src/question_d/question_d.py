#write functions here, don't add input('') statements here!


def create_mulitiplication_table(size):


    my_list = []

    for i in range(1, size + 1):
        for j in range(1, size + 1):
        # Calculate the product
            product = i * j
        
            my_list.append(product)
    # Print a newline character to move to the next row
    return my_list


def display_multiplication_table(my_list):
    chunk_counter = 0
    
    for i in range(0, len(my_list), 10):
            chunk = my_list[i:i + 10]
            print(chunk)

display_multiplication_table(create_mulitiplication_table())
