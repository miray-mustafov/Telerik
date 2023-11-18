'''
Shooting contest
'''

n = int(input())
gs, gl = int(input()), int(input())
ps, pl = int(input()), int(input())
time_g = gs * n + 2 * gl
time_p = ps * n + 2 * pl
if time_p > time_g:
    print('George')
elif time_p < time_g:
    print('Peter')
else:
    print('Draw')
