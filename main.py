import csv
from functions.get_max_load import get_max_load
from functions.list_sorted import list_sorted

data = []

def main():
  load_csv()
  options_selector()

def load_csv():
  with open("CprE_Subject.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
      data.append(row)
    data.pop(0)
    
def options_selector():
  while True:
    user_input = input(">>> ")
  
    match user_input:
      case "get_max_load":
        get_max_load(data)
      case "list_sorted":
        list_sorted(data)
      case _:
        pass

if __name__ == "__main__":
  main()