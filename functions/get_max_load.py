def get_max_load(data):
  if len(data) == 0:
    return False
  elif len(data) == 1:
    print(f"{data[0][0]} {data[0][1]} {data[0][2]} {data[0][3]} {data[0][4]} {data[0][5]}")
  else:
    heap = [(int(row[3].split("(")[0]), row) for row in data]

    heap_length = len(heap)
    start = (heap_length - 1) // 2

    for parent_pos in range(start, -1, -1):
      swap_heap(heap, parent_pos, heap_length)

    max_credit = heap[0][0]
    
    results = []
    for credit, row in heap:
      if credit == max_credit:
        results.append(row)

    for item in results:
      print(f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]} {item[5]}")


def swap_heap(heap, parent_pos, heap_length):
  while True:
    larger = parent_pos
    left    = 2 * parent_pos + 1
    right   = 2 * parent_pos + 2

    if left < heap_length and heap[left][0] > heap[larger][0]:
      larger = left

    if right < heap_length and heap[right][0] > heap[larger][0]:
      larger = right

    if larger == parent_pos:
      break

    heap[parent_pos], heap[larger] = heap[larger], heap[parent_pos]
    parent_pos = larger