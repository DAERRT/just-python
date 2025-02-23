def hanoy(n, source, target, auxiliary):

    if n == 1:
        print(f"Диск 1 : {source} --> {target}")
        return

    hanoy(n - 1, source, auxiliary, target)

    print(f"Диск {n} : {source} --> {target}")

    hanoy(n - 1, auxiliary, target, source)


hanoy(3, 'a', 'b', 'c')