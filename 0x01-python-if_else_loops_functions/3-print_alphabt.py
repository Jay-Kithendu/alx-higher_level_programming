#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z')):
    if (alphabets != 'e' and alphabets != 'q'):
        print("{:c}".format(alphabets), end="")
