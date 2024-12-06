input = open("./day_4/input.txt", "r").read()
data = input.split('\n')

word = "MAS"
N = len(data)
M = len(data[0])

def try_find_mas(x, y):
    top_left = data[y-1][x-1]
    top_right = data[y-1][x+1]
    bot_left = data[y+1][x-1]
    bot_right = data[y+1][x+1]
    mas_1 = f"{top_left}A{bot_right}"
    mas_2 = f"{top_right}A{bot_left}"
    return (mas_1 == word or mas_1 == word[::-1]) and (mas_2 == word or mas_2 == word[::-1])

xmas_counter = 0
for i in range(N)[1:-1]:
    for j in range(M)[1:-1]:
        if data[i][j] != "A":
            continue
        xmas_counter += try_find_mas(j, i)
        
print(xmas_counter)