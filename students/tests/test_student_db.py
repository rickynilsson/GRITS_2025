from student_db import StudentDB


def test_crud(tmp_path):
    db_path = tmp_path / "students.db"
    db = StudentDB(str(db_path))

    sid = db.add_student("Alice", "123 Apple St", "A")
    assert isinstance(sid, int)

    s = db.get_student(sid)
    assert s and s["name"] == "Alice" and s["address"] == "123 Apple St" and s["grade"] == "A"

    ok = db.update_student(sid, grade="A-")
    assert ok
    s = db.get_student(sid)
    assert s["grade"] == "A-"

    all_students = db.list_students()
    assert len(all_students) == 1

    ok = db.delete_student(sid)
    assert ok
    assert db.get_student(sid) is None