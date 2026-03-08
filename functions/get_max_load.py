def get_max_load(data):
  max_value = 0
  results = []

  # searching the maximum credit value
  for item in data:
    split_data = item[3].split("(")
    current_credit_value = int(split_data[0])
    
    if current_credit_value > max_value:
      max_value = current_credit_value
  
  # appending a list of subjects based on maximum value
  for item in data:
    split_data = item[3].split("(")
    current_credit_value = int(split_data[0])
    
    if current_credit_value == max_value:
      results.append(item)
      
  for item in results:
    print(f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]} {item[5]}")