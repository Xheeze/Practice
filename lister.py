#!/usr/bin/python3

# names = ["Thabo","Anele","Mandy","Sarah"]
namer = [5, 6, 7, 1, 3, 8, 4]
# print(names[-4])
max = namer[0]
for nam in namer:
    if nam > max:
        max = nam
print(nam)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2])