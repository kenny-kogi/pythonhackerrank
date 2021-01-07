T = int(input())
list1 = []
for _ in range(T):
    input1 = input()
    list1.append(input1)

for names in list1:
    array1 = list(names)
    even = ""
    odd = ""
    for i in range(len(array1)):
        if i % 2 == 0:
            even += array1[i]
        else:
            odd += array1[i]
    print(even + " " + odd)

