x = input()
start = 0
maxlength = 0
start_old = 0
char_index = {}

for i in range(len(x)):
    if x[i] in char_index and char_index[x[i]] >= start:
        start = char_index[x[i]] + 1 

    char_index[x[i]] = i

    if maxlength < i - start + 1:
        maxlength = i - start + 1
        start_old = start

print(x[start_old:start_old + maxlength])
