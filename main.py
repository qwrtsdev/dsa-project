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
    user_input = input(">>> ")
  
    match user_input:
      case "show":
        print(data)
      case "get_max_load":
        # TODO: Instantly returns the course with the highest credits.
        pass
      case "list_sorted":
        # TODO: Prints all courses sorted by CourseCode
        pass
      case "exit":
        sys.exit(0)
      case _:
        print("Unknown command.")
        
    print("\n====================================\n")
  
def load_csv():
  with open("CprE_Subject.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
      data.append(row)
    data.pop(0)

if __name__ == "__main__":
  main()