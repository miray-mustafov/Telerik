from dll import DoublyLinkedList

n, swaps = map(int, input().split())
ppl = DoublyLinkedList()
ppl.initialize_dll_from_list(input().split())

for _ in range(swaps):
    p1_name, p2_name = input().split()
    ppl.move_p1_tothe_left_of_p2(p1_name, p2_name)
    # ppl.print_to_console()
ppl.print_to_console()


""" Important edge cases with outputs!
7 4
Emo Misho Ivanka Ginka Vancho Stancho Sashka
Emo Misho
Misho Emo
Misho Sashka
Sashka Stancho

case1
5 1
Gosho Tosho Penka Miro Stanka
Penka Miro
# same : Gosho Tosho Penka Miro Stanka

case2
5 1
Gosho Tosho Penka Miro Stanka
Miro Penka
# Gosho Miro Tosho Penka Stanka

case3
5 1
Gosho Tosho Penka Miro Stanka
Miro Tosho
# Gosho Miro Tosho Penka Stanka 

case4
5 1
Gosho Tosho Penka Miro Stanka
Miro Gosho
# Miro Gosho Tosho Penka Stanka 

case 5 !! opposite case 8
5 1
Gosho Tosho Penka Miro Stanka
Stanka Gosho
# Stanka Gosho Tosho Penka Miro 

case 6
5 1
Gosho Tosho Penka Miro Stanka
Tosho Miro
# Gosho Penka Tosho Miro Stanka 

case 7
5 1
Gosho Tosho Penka Miro Stanka
Tosho Miro
# Gosho Penka Tosho Miro Stanka 

case 8 !!
5 1
Gosho Tosho Penka Miro Stanka
Gosho Stanka
#
"""
