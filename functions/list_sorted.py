def list_sorted(data):
    def merge_sort(S):
        if len(S) <= 1: #Base case: if the list has 0 or 1 element, it's already sorted
            return S

        mid = len(S) // 2
        left = merge_sort(S[:mid])
        right = merge_sort(S[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if str(left[i][0]) <= str(right[j][0]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    sorted_data = merge_sort(data)

    print(">> list_sorted")
    print("CourseCode,Name,Type,Credit,Semester,Lecturer")
    for row in sorted_data:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")