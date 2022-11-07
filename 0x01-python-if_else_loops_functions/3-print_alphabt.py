#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z')):
    if (alphabets != 'q' and alphabets != 'e'):
        print("{:c}".format(alphabets), end="")
