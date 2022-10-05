
def Tower(n, A, B, C):
    if n == 0: return
    Tower(n-1, A, C, B)
    print(A,C)
    Tower(n-1, B, A, C)

print('Please tell me how tall you want the tower to be:')
n = int(input())
print('All the moves that need to be preformed will be displayed below')
Tower(n,1,2,3)
print('You will require this many moves: ',2**n-1)
