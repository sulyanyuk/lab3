print('Введите список чисел в формате "1,2,3, ..."')

while True:
    try:
        s = input().split(",")
        maxN = float(s[0])
        maxI = 0
        for i in range(0,len(s)):
            s[i] = float(s[i])
            if s[i] > maxN:
                maxN = s[i]
                maxI = i
        sumMin = 0
        for i in range(0,maxI):
            sumMin += s[i]
        if maxI == 0:
            sumMin = s[0]
        break
    except:
        print("Вы ввели не числа!")

print('Сумма чисел до максимального: ',sumMin)