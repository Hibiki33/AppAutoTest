def log(s, target=None):
    print()
    res = s[0]
    for i in s:
        if not isinstance(i, int):
            res = i
            break
        elif i < 0:
            res = i
    # except:
    #     res = 0
    s = str(s)
    if target:
        with open(target, 'w', encoding = 'utf-8') as fp:
            fp.write(s)
    else:
        print(s)
    return res
