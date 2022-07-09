import os
def main():
   input1 =os.environ['Branch']
   input2 =os.environ['ENV']
   print(input1)
   print(input2)
   if (input2=='DEV'):
      print('It is DEV ENV & main brach')
   else:
      print('Its not a DEV & main brach')
if __name__ == "__main__":
   print('Welcome to Redshift Deployment')
   main()
