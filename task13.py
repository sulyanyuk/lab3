s = input('Введите данные в формате "X,X,X, .." ').split(',') # Sample: 5,5,10,f,g,f,5,6,7,8,10,f,5,1,2,3,5

out = []

for item in s:
    if out.count(item) == 0:
        out.append(item)

print(out)