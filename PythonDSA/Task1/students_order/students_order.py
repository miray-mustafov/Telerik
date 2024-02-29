"""
Students order
Alpha students love learning new stuff. They are also aware that switching seats in the classroom helps them learn new material more effectively. You are given the names of N students and K seat changes. Your task is to implement an algorithm that shows the students' final seating order after all seat changes have been made.

Input
Read from the standard input.
On the first line, you'll find the numbers N and K separated by a white space.
N - the number of students.
K - the number of seat changes.
On the next line there will be N student names separated by a white space.
The next K lines are pairs of student names. Each pair represents a change of seats where the first student sits on the left of the second student.
The names are separated by a white space.
Output
Print on the standard output.
On a single line, print the final order of the student names.
Constraints
1 <= N <= 2000
1 <= K <= 100 000
Each name contains only alphanumeric characters.
All names are unique.
Sample tests
Input
5 3
Gosho Tosho Penka Miro Stanka
Miro Gosho
Gosho Stanka
Stanka Miro
Output
Stanka Miro Tosho Penka Gosho
Explanation
Miro takes a seat next to Gosho. The order becomes Miro Gosho Tosho Penka Stanka
Gosho takes a seat next to Stanka. The order becomes Miro Tosho Penka Gosho Stanka
Stanka takes a seat next to Miro. The order becomes Stanka Miro Tosho Penka Gosho
Input
7 4
Emo Misho Ivanka Ginka Vancho Stancho Sashka
Emo Misho
Misho Emo
Misho Sashka
Sashka Stancho
Output
Emo Ivanka Ginka Vancho Sashka Stancho Misho
"""

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
