import csv
import sys

data = []

def main():
  load_csv()
  options_selector()

def options_selector():
  while True:
    user_input = input(">>> ")
  
    match user_input:
      case "raw":
        print(data)
      case "get_max_load":
        # TODO: Instantly returns the course with the highest credits.
        get_max_load()
      case "list_sorted":
        # TODO: Prints all courses sorted by CourseCode
        list_sorted()
      case "exit":
        sys.exit(0)
      case _:
        print("Unknown command.")
  
def load_csv():
  with open("CprE_Subject.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
      data.append(row)
    data.pop(0)
    
def get_max_load():
  pass
    
def list_sorted():
  pass

if __name__ == "__main__":
  main()