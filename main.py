def main():
  user_input = input("Enter a command: ")
  
  match user_input:
    case "hello":
      print("Hello!")
    case "bye":
      print("Goodbye!")
    case _:
      print("Unknown command.")
      
  main()

if __name__ == "__main__":
  main()