for i in range (100):
    num, ret = i, 0
    while num < 1000:
        ret ^= num
        if ret == 0:
            print(i, num)
            break
        num += 1
