# GRITS 2025 – AI‑Assisted Coding with GitHub Copilot in VS Code

This repo contains hands-on exercises for a workshop on using GitHub Copilot in Visual Studio Code, plus example solutions and a small, production‑style Python package.

- Workshop slides: [https://docs.google.com/presentation/d/1LJYtUzoPv4Wh5FHqXZnUKRjeBgWOwhP8C2g2SQs-s_E/edit?usp=sharing](Google slides)
- Workshop exercise guide: [exercises.md](exercises.md)

## Layout
```
.
├─ exercises.md
├─ simple_funcs.py
├─ processor.py
├─ processor_commented.py
└─ students/
   ├─ README.md
   ├─ pyproject.toml
   ├─ src/ 
      └─ student_db/
         ├─ __init__.py
         ├─ cli.py
         └─ db.py
      └─ tests/
         └─ test_student_db.py
```

## Example code used in exercises

- Utility functions in [simple_funcs.py](simple_funcs.py)
  - [`simple_funcs.factorial`](simple_funcs.py)
  - [`simple_funcs.reverse_string`](simple_funcs.py)
  - [`simple_funcs.are_anagrams`](simple_funcs.py)
  - [`simple_funcs.find_first_non_repeating_char`](simple_funcs.py)
  - [`simple_funcs.find_median`](simple_funcs.py)

- Streaming processor (moving average + anomaly detection)
  - Uncommented: [`processor.DataProcessor`](processor.py)
  - Commented: [`processor_commented.DataProcessor`](processor_commented.py)

## Student database package (SQLite)

A minimal Python package with CRUD operations and a CLI.

- Core module: [`student_db.db.StudentDB`](students/src/student_db/db.py)
- CLI entry: [`student_db.cli.main`](students/src/student_db/cli.py)
- Package API: [students/src/student_db/__init__.py](students/src/student_db/__init__.py)
- Project config: [students/pyproject.toml](students/pyproject.toml)
- Package README: [students/README.md](students/README.md)
- Tests: [students/tests/test_student_db.py](students/tests/test_student_db.py)

### Install (editable) and test

```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ./students[dev]
pytest -q students
```

### CLI usage

```bash
# Help
student-db --help

# Use a specific database file
student-db --db demo.db add --name "Alice" --address "123 Apple St" --grade A
student-db --db demo.db list
student-db --db demo.db get --id 1
student-db --db demo.db update --id 1 --grade "A-"
student-db --db demo.db delete --id 1
```

### Programmatic usage

```
from student_db import StudentDB  # from students/src/student_db/__init__.py

db = StudentDB("demo.db")
sid = db.add_student("Bob", "456 Berry Rd", "B+")
print(db.get_student(sid))
db.update_student(sid, grade="A-")
print(db.list_students())
db.delete_student(sid)
```


