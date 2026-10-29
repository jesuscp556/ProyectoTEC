def printtree(T):
    print(T[0])
    for child in range(1, len(T)):
        printtree(T[child])
        

T = ['c', ['a', ['p'], ['n'], ['t']], ['o', ['n']]]

printtree(T)
