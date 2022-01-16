n=int(input())
for i in range(n, 0, -1):
    print(f'{i} bottl{"e" if i== 1 else "es"} of beer on the wall, {i} bottl{"e" if i== 1 else "es"} of beer.\nTake one down and pass it around, {i-1 if i>1 else "no more"} bottl{"e" if i== 2 else "es"} of beer on the wall.\n')
print(f'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {n} bottl{"e" if n== 1 else "es"} of beer on the wall.')