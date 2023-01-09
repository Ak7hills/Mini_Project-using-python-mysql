numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round((2 * 50 * int(D) / 30)**0.5)
    result_list.append(Q)

print(result_list)