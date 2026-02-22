import csv
import sys

data = []

def main():
  print("====================================")
  print("Loading CSV file...")
  load_csv()
  print("CSV file loaded successfully.")
  print("====================================\n")
  
  while True:
    user_input = input("Enter a command: ")
  
    match user_input:
      case "show":
        print(data)
      case "exit":
        sys.exit(0)
      case _:
        print("Unknown command.")
  
def load_csv():
  with open("CprE_Subject.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
      data.append(row)

if __name__ == "__main__":
  main()