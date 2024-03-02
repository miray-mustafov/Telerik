'''
Chicken Latin
Even though the Latin is considered dead language there are several variations of it still living in Shakespeare’s plays and programming tasks. I refer to Pig and Dog Latin.

Today we’ll dive into the Chicken Latin. This specific dialect comes from Bulgarian South and the chickens there use "che" instead of "pi”.

To translate one sentence, we need to take in consideration each word in it. The sentence consists of words, separated by only one space. Every word is composed only of lower or uppercase letters.

The rules of Chicken Latin are:

If a word begins with a vowel (a, e, i, o, u or A, E, I, O, U), remove the first letter and append it to the end, then add "che". If you have the word “orange” It translates to “rangeoche”
If a word begins with a consonant (i.e. not a vowel), append "che" to the end of the word. For example, the word "chicken" becomes "chickenche".
If the word has even number of letters append one more "e" to the end of it.
Print the translated sentence.

Input
Read from the standard input:

There is one line of input, a string:
Hello there Amy
Output
Print to the standard output:

One line of output - the translated sentence
Helloche thereche myAche
'''

s = input().split()
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
result = []
for i in range(len(s)):
    if s[i][0] in vowels:
        s[i] = s[i][1:] + s[i][0] + 'che' if len(s[i]) % 2 != 0 else s[i][1:] + s[i][0] + 'chee'
    else:
        s[i] = s[i] + 'che' if len(s[i]) % 2 != 0 else s[i] + 'chee'
print(' '.join(s))
