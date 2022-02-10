def star(n: int, x:list):
    out = []
    if n == 3:
        return x
    else:
        for i in x: 
            out.append(i*3)
        for i in x:
            out.append(i +' '*len(x)+i)
        for i in x:
            out.append(i*3)
        return star(n//3, out)


if __name__ == '__main__':
    n = int(input())
    first = ['***', '* *', '***']
    final = star(n, first)
    for i in final:
        print(i)
