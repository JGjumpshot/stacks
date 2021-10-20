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
        elif token == " ":
            continue
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.top()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    # print(dir(op_stack))
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    result = " ".join(postfix_list)
    print(f"postfix: {result}")
    return result
def eval_postfix(postfix_expr):
    if postfix_expr is None:
        raise ValueError("No expression detected")
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token == "-+":
            raise SyntaxError("invalid syntax")
        if token in "0123456789":
            operand_stack.push(float(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(op, op1, op2):
    if op =="*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
def main():
    print(read_file())
    print(eval_postfix("7 9 * 7 + 5 6 * - 3 + 4 -+"))
    # expression_list = read_file()
    # for i in expression_list:
    #     expression = i.strip().split(',')
    #     #expression_stack.push(expression)
    #     new_expr = in2post(expression)
    #     print(f"answer: {eval_postfix(new_expr)}\n")
    #print(expression_stack)

if __name__ == "__main__":
    main()