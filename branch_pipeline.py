import os
def main():
   input1 =os.environ['Branch']
   input2 =os.environ['ENV']
   print(input1)
   print(input2)
if __name__ == "__main__":
  print('Welcome to Redshift Deployment')
  main()

if ((input2='DEV') and (input1= 'main')):
{ 
print(It is DEV ENV & main brach)

}

else:
{
print(Its not a DEV & main brach)
}
