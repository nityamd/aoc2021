def life_support_rating(array):
    sum_array = []
    for i in range(len(array[0])):
        sum_array.append(sum([int(x[i]) for x in array]))
    most_common = list(map(lambda x: 1 if x > 500 else 0, sum_array))
    most_common_decimal = sum([most_common[i]*(2**(len(most_common)-i-1))
    for i in range(len(most_common))])
    least_common_decimal = sum([int(not most_common[i])*(2**(len(most_common)-i-1))
    for i in range(len(most_common))])
    return most_common_decimal*least_common_decimal

if __name__ == '__main__':
    with open('./input.txt') as f:
        array = f.read().split('\n')

    print('Part 1', life_support_rating(array))
    

    

