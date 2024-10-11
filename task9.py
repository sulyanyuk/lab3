def reverseArray(s):
    s_reversed = []
    for i in range(1, len(s) + 1):
        s_reversed.append(s[len(s) - i])
    return s_reversed

print('Введите список чисел в формате "1,2,3, ..."')

while True:
    try:
        s = input().split(",")
        for i in range(0,len(s)):
            s[i] = int(s[i])
        break
    except ValueError:
        print("Вы ввели не числа!")

maxLenAsc = 1
maxLenDesc = 1
currentLenAsc = 1
currentLenDesc = 1


# 1,2,3,4,5,0,10,9,8,7,6,5,4,3,2,1 - sample
if len(s) != 1:
    prev = s[0]
    for i in range(1,len(s)):
        if s[i] == prev + 1:
            currentLenAsc += 1
        else:
            if currentLenAsc > maxLenAsc:
                maxLenAsc = currentLenAsc
            currentLenAsc = 1
        prev = s[i]

    s = reverseArray(s)

    for i in range(1,len(s)):
        if s[i] == prev + 1:
            currentLenDesc += 1
        else:
            if currentLenDesc > maxLenDesc:
                maxLenDesc = currentLenDesc
            currentLenDesc = 1
        prev = s[i]

if maxLenAsc > maxLenDesc:
    maxLen = maxLenAsc
else:
    maxLen = maxLenDesc

print('Длина самой большой последовательности: ',maxLen)