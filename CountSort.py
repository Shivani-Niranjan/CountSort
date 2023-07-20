'''
Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.

Input 1:
A = [1, 3, 1]

Input 2:
A = [4, 2, 1, 3]

Output 1:
[1, 1, 3]

Output 2:
[1, 2, 3, 4]
'''

# works to sort digits from 0 to 9 only

array = list(map(int, input().split()))
count_array = [0] * (10)  #creating list to increment counto feach element
sorted_array = []  
for i in range(len(array)):
    count_array[array[i]] +=1  # incrementing 

for i in range(len(count_array)):        
    for j in range(count_array[i]):    # to print that many numbers 
        sorted_array.append(i)

print(sorted_array)

