# p = int(input())
# n = int(input())

# cities = list(range(2**p))
# # print(cities)

# def transform(cities):
#     even = [cities[i] for i in range(0, len(cities), 2)]
#     odd = [cities[i] for i in range(1, len(cities), 2)]
#     return even + odd

# cities = transform(cities)


# for j in range(1, p):
#     chunk_size = 2**j
#     temp = []
    
#     for k in range(0, len(cities), chunk_size):
#         temp.append(cities[k:k+chunk_size])

#     for i in range(len(temp)):
#         temp[i] = transform(temp[i])

#     print(temp)
#     cities = [item for sublist in temp for item in sublist]


# print(cities[n])




# p = int(input())


# step 1 : (2**1)*n + 0 where n is 0 to (2**(p-1))-1 + (2**1)*n + 1 where n is 0 to (2**(p-1))-1
# step 2 : (2**2)*n + 0 where n is 0 to (2**(p-2))-1 + (2**2)*n + 2 where n is 0 to (2**(p-2))-1 + (2**2)*n + 1 where n is 0 to (2**(p-2))-1 + (2**2)*n + 3 where n is 0 to (2**(p-2))-1
# step 3 : (2**3)*n + 0 where n is 0 to (2**(p-3))-1 + (2**3)*n + 4 where n is 0 to (2**(p-3))-1 + (2**3)*n + 2 where n is 0 to (2**(p-3))-1 + (2**3)*n + 6 where n is 0 to (2**(p-3))-1 + (2**3)*n + 1 where n is 0 to (2**(p-3))-1 + (2**3)*n + 5 where n is 0 to (2**(p-3))-1 + (2**3)*n + 3 where n is 0 to (2**(p-3))-1 + (2**3)*n + 7 where n is 0 to (2**(p-3))-1
# .... so on 
# how to mimic this

# p = 1 => 0,1
# p = 2 => 0,2,1,3
# p = 3 => 0,4,2,6,1,5,3,7
# p = 4 => 0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15
# p = 5 => 0,16,8,24,4,20,12,28,2,18,10,26,6,22,14,30,1,17,9,25,5,21,13,29,3,19,11,27,7,23,15,31
# p = 6 => 0,32,16,48,8,40,24,56,4,36,20,52,12,44,28,60,2,34,18,50,10,42,26,58,6,38,22,54,14,46,30,62,1,33,17,49,9,41,25,57,5,37,21,53,13,45,29,61,3,35,19,51,11,43,27,59,7,39,23,


# def sequence(p):
#     if p == 0:
#         return [0]

#     prev = sequence(p - 1)
    
#     new_seq = []
#     for i in range(len(prev)):
#         new_seq.append(prev[i] * 2)
    
#     for i in range(len(prev)):
#         new_seq.append(prev[i] * 2 + 1)
    
#     return new_seq

# p = int(input())
# n = int(input())
# print(sequence(p)[n])
       



def nth_element(p, n):
    if p == 0:
        return 0
    
    half_size = 2 ** (p - 1)
    
    if n < half_size:
        return nth_element(p - 1, n) * 2
    else:
        return nth_element(p - 1, n - half_size) * 2 + 1

p = int(input())
n = int(input())
print(nth_element(p, n))

