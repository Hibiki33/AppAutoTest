def log(s, target=None):
    print()
    s = str(s)
    if target:
        with open(target, 'w', encoding = 'utf-8') as fp:
            fp.write(s)
    else:
        print(s)