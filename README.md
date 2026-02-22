# **Track 4: The "Resource Optimizer"**
### **The Scenario**: The department has limited classrooms and needs to rank courses.

- Feature A (Max Load): At any moment, the system must be able to tell the user which course currently has the highest credit load .
- Feature B (Sort): Provide a list of all courses sorted by CourseCode for the official catalog.

### **Discussion Requirement**:
- **Why this Algo/DS**: Explain why a ….. is the used for retrieving the maximum value and how ………….. facilitates the catalog listing.
- **Asymptotic Analysis**: Analyze the complexity of get_max_load and list_sorted.

### **Key Focus**: Ranking and dynamic ordering.
- **Input**: Courses are ranked based on their Credit value.
- **Commands**:
  - `get_max_load`: Instantly returns the course with the highest credits.
  - `list_sorted`: Prints all courses sorted by CourseCode.

*Example Output*:
```cmd
>> get_max_load
Highest Credit Course: 010123102 (Programming Fundamentals) - 3 Credits.

>> list_sorted
010113030 - Introduction to Engineering
010113139 - Circuits and Electronics Lab...

>> update_credit 010123124 5
Course 010123124 updated to 5 credits. 
New Max Course is now: 010123124.
```