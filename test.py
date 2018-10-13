import sys

def donuts(count):
  if count < 10:
    print('Number of donuts: %d' %(count))
  else:
    print('Number of donuts: %s' %('many'))

if __name__ == '__main__':
  main(sys.argv[1])
