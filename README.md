# **Track 4: The "Resource Optimizer"**
### **The Scenario**: The department has limited classrooms and needs to rank courses.

- Feature A (Max Load): At any moment, the system must be able to tell the user which course currently has the highest credit load .
- Feature B (Sort): Provide a list of all courses sorted by CourseCode for the official catalog.
<br /><br />
# วิธีการรันโปรแกรม
- กดรันไฟล์ ``main.py`` ได้โดยตรง
- หรือใช้คำสั่งในโฟลเดอร์ `/dsa-project` ของโปรเจค
  ```cmd
  python main.py
  ```
<br /><br />
# วิเคราะห์ BigO
- `get_max_load` : O(1)
- `list_sorted` : O(n log n)