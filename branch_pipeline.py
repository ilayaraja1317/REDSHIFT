import os
def main():
   input1 =os.environ['Branch']
   input2 =os.environ['ENV']
   print(input1)
   print(input2)
if __name__ == "__main__":
  print('Welcome to Redshift Deployment')
  a = input1
  b = input2
print(a)
if (a =='DEV'):
 { 
  print('It is DEV ENV & main brach')
 }

else:
 {
  print('Its not a DEV & main brach')
  }
main()
