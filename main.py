from stack import Stack
def read_file():
    data = open("data.txt")
    return data.readlines()

def in2post(expr):
    prec = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }
    op_stack = Stack()
    postfix_list = []
    token_list = expr[0]
    print(f"infix: {token_list}")
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.top()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    # print(dir(op_stack))
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    result = " ".join(postfix_list)
    print(f"postfix: {result}\n")
    return result
def main():
    expression_stack = Stack()
    print(read_file())
    #print(in2post())
    expression_list = read_file()
    for i in expression_list:
        expression = i.strip().split(',')
        #expression_stack.push(expression)
        in2post(expression)
    #print(expression_stack)

if __name__ == "__main__":
    main()