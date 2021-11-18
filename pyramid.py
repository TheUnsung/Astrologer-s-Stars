#WAP to make pyramid of stars.
format = int(input('Ascending(0)/ Descending(1): '))
if format == 0:
    for i in range(1, 11):
        print(i*'*')
elif format == 1:
    for i in range(11, 1, -1):
        print(i*'*')
