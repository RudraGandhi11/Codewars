def valid_braces(string):
    stack = []
    for i in string:
        if(stack):
            if((stack[len(stack) - 1] == '{' and i == '}') or (stack[len(stack) - 1] == '(' and i == ')') or (stack[len(stack) - 1] == '[' and i == ']')):
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
            
    if(stack):
        return False
    else:
        return True