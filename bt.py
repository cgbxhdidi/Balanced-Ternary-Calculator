def bt_to_int(bt):
    dec, m = 0, len(bt)-1
    units = {'1':1, 'N':-1, '0':0}
    for i in range(len(bt)):
        dec += units[bt[i]] * 3**m
        m -= 1
    return dec
    
def int_to_bt(dec):
    m, n = divmod(dec, 3)
    bt = ''
    while m != 0 or n != 0:
        if n == 2:
            m = m + 1
            bt = 'N' + bt
        else:
            bt = str(n) + bt
        m, n = divmod(m, 3)
    if dec == 0:
        bt = '0'
    return bt

def memory_as_int():
    global memory
    return memory

def memory_as_bt():
    global memory
    return int_to_bt(memory)

def add(bt):
    global memory
    memory += bt_to_int(bt)

def subtract(bt):
    global memory
    memory -= bt_to_int(bt)

def multiply(bt):
    global memory
    memory = memory * bt_to_int(bt)

def divide(bt):
    global memory
    if bt_to_int(bt) == 0:
        raise Exception("DivideError: divider cannot be 0")
    memory = memory // bt_to_int(bt)

def remainder(bt):
    global memory
    if bt_to_int(bt) == 0:
        raise Exception("RemainderError: divider cannot be 0")
    memory = memory % bt_to_int(bt)

def negate():
    global memory
    memory = memory * (-1)

def store(bt):
    global memory
    memory = bt_to_int(bt)

def is_bt(bt):
    if bt == '':
        return False
    for i in bt:
        if i not in '1N0':
            return False
    return True

def evaluate(string):
    global memory
    string = ''.join(string.split()) + ' '
    functions = {'+':add, '-':subtract, '*':multiply, '/':divide, '%':remainder, '=':store}
    try:
        strings = []
        m, n = 0, 0
        for i in range(len(string)):
            if string[i] in '+-*/%= ' and i != 0:
                m, n = n, i
                strings.append(string[m:n])
        for m in strings:
            if m[0] not in '+-*/%=' or not is_bt(m[1:]):
                return "Equation not right"
            functions[m[0]](m[1:])
        return int_to_bt(memory)
    except Exception as msg:
        return msg
            
def REPL():
    global memory
    memory = 0
    m = input('Please type in an equation \n')
    while m != 'quit':
        print(evaluate(m))
        m = input('Please type in an equation or "quit" \n')

if __name__ == '__main__':
    REPL()
