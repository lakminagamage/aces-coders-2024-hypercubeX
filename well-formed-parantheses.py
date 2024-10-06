n = int(input())


def generate_parentheses(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    result = []
    for i in range(n):
        for left in generate_parentheses(i):
            for right in generate_parentheses(n - i - 1):
                result.append("(" + left + ")" + right)
    
    return result

parentheses_list = generate_parentheses(n)
parentheses_list.sort()

for parentheses in parentheses_list:
    print(parentheses)
