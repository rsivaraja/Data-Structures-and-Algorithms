def balanced(expression):
    stack=[]
    for letter in expression:
        if letter=='(' or letter=='[' or letter=='{':
            stack.append(letter)
        elif letter in ')]}':
            if not stack:
                return False
            top=stack.pop()
            if (top=='(' and letter!=')') or (top=='[' and letter!=']') or (top=='{' and letter!='}'):
                return False
    return not stack
print(balanced('((hello))'))