prodolzhit = 'y'
while prodolzhit == 'y':
    f_num = float(input('Введите первое число>>'))
    oper = input('Введите операцию>>')
    s_num = float(input('Введите второе число>>>'))
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '*':
        print(f_num * s_num)
    elif oper == '/':
        print(f_num / s_num)
    else:
        print('Error')
        prodolzhit = input('Введите "y" если хотите продолжить, или любую клавишу, чтобы завершить процесс>>>')
