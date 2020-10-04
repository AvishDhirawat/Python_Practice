import sys
print(sys.argv)
for i in range(1,len(sys.argv)):
    sys.argv[i] = int(sys.argv[i])
    if sys.argv[i]%2==0:
        print('This is {} even number'.format(sys.argv[i]))
    else:
        print('This is {} odd number'.format(sys.argv[i]))
