import math

colleagues_count = int(input())
vineyard_len = int(input())
vineyard = input()
wine_bottles_needed = math.ceil((colleagues_count * 300) / 750)
rakia_bottles_needed = math.ceil((colleagues_count * 50) / 700)

wine_bottles, rakia_bottles = 0, 0
for i in range(vineyard_len):
    if vineyard[i] == 'X':
        wine_bottles += 7
    elif vineyard[i] == 'x':
        rakia_bottles += 7 / 5

rakia_bottles = int(rakia_bottles)

if wine_bottles >= wine_bottles_needed and rakia_bottles >= rakia_bottles_needed:
    x = wine_bottles - wine_bottles_needed
    y = rakia_bottles - rakia_bottles_needed
    print(f'Yes! {x} bottles of wine and {y} bottles of rakia remaining for the next party!')
else:
    x = wine_bottles_needed - wine_bottles if wine_bottles_needed - wine_bottles >= 0 else 0
    y = rakia_bottles_needed - rakia_bottles if rakia_bottles_needed - rakia_bottles >= 0 else 0
    print(f'No! {x} more bottles of wine and {y} more bottles of rakia required!')
