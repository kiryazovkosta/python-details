def print_greating(number: int) -> str:
   if number == 88:
      return "Hello"
   elif number == 86:
      return "How are you?"
   elif number < 88:
      return "GREAT!"
   else:
      return "Bye."

def main():
   size = int(input())
   for _ in range(size):
      n = int(input())
      msg = print_greating(n)
      print(msg)
      
if __name__ == "__main__":
   main()