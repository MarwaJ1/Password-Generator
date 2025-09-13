import string, sys, secrets

#generating passwords 
def password(length=8): 
    if length < 8: 
        length = 8
    keys = list(string.printable[:-6])
    return ''.join(secrets.choice(keys) for i in range(length))

if __name__ == '__main__':
      try:
        print( password(int(sys.argv[1])))
      except Exception as e: 
          print("Enter a valid password")