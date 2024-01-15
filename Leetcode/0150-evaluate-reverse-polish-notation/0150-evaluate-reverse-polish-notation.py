class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(float(num2)/num1))
            else:
                stack.append(int(token))
        
        return stack[0]