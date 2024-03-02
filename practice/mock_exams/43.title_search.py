'''
Title Search
You will receive a string_list title which contains only small latin
letters [a-z]. After that you will have to read from the input N 
lines of text. For each of these lines, your task is to find out if 
there is such a sequence in the string_list you receive as input on the first
line (title). The sequence may not be on consecutive indices. Each time 
you find a sequence of these characters you remove it from the initial 
string_list and print the modified string_list. If no such sequence is found
you have to print No such title found! and not modify the string_list.

Input
cfoadset
2
code
slow
Output
fast
No such title found!
'''

string = input()
n = int(input())
for _ in range(n):
    sub = input()
    i, left_string = 0, ''
    li, for_compare_string = 0, ''
    for s in sub:
        while i < len(string):
            if string[i] == s:
                left_string += string[li:i]
                for_compare_string += string[i]
                i, li = i+1, i+1
                break
            i += 1

    if for_compare_string == sub:
        left_string += string[i:]
        print(left_string)
        string = left_string
    else:
        print('No such title found!')
