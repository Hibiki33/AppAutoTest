def log(s, target=None):
    print()
    s = str(s)
    if target:
        target.write(s)
    else:
        print(s)