for i in range(1, 11):
    s = ''
    for j in range(1, 11):
        if s != '':
            s = s + ' '
        s = s + str(i * j)
    print(s)
