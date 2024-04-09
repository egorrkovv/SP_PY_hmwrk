x_2 = int()
x = int()
y = int()
profit = int()
def bank(x, y, x_2):
    for year in range(1, y + 1):
        profit = x_2 * 1.1 - x_2
        x_2 += x + profit
        print(x + profit)
        
        

bank(100000, 5, 100000) 
