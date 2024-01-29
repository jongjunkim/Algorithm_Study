from itertools import permutations
def solution(expression):
    symbol = ['+', '-', '*']
    answer = []
    
    print(expression.split("-"))
    
    for per in permutations(symbol):
        f, s = per[0], per[1]
        lst = []
        for e in expression.split(f):
            temp = [f"({i})" for i in e.split(s)]
            lst.append(f'({s.join(temp)})')
        answer.append(abs(eval(f.join(lst))))
    return max(answer)


from itertools import permutations
import re
def operate(e,a,b):
    if e == '+':
        return a+b
    if e == '-':
        return a-b
    if e == '*':
        return a*b
def solution(expression):
    result = []
    s = []
    op_lists = list(permutations(['+','-','*'],3))
    expression = re.split("([^0-9])",expression) #re library (^) means "starts with"
    for op_list in op_lists:
        exp = expression
        for op in op_list:
            s = []
            for e in exp:
                if s and s[-1] == op:
                    operation = s.pop()
                    s[-1] = operate(operation,int(s[-1]),int(e))
                else:
                    s.append(e)
            exp = s
        result.append(abs(exp[0]))
    return max(result)
