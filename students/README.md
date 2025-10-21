# student-db

A simple SQLite-backed Python package to manage a student database (name, address, grade).

Usage example (programmatic):
```python
from student_db import StudentDB

db = StudentDB("students.db")
sid = db.add_student("Alice", "123 Apple St", "A")
print(db.get_student(sid))
db.update_student(sid, grade="A-")
print(db.list_students())
db.delete_student(sid)