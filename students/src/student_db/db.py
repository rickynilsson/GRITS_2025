from __future__ import annotations
import sqlite3
from typing import Optional, Dict, List, Any


class StudentDB:
    """SQLite-backed student database with CRUD operations.

    Schema:
        students(id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 address TEXT NOT NULL,
                 grade TEXT NOT NULL)

    Args:
        db_path: Path to the SQLite database file.
    """

    def __init__(self, db_path: str = "students.db") -> None:
        self.db_path = db_path
        self._ensure_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _ensure_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    grade TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def add_student(self, name: str, address: str, grade: str) -> int:
        """Insert a new student and return its id."""
        with self._connect() as conn:
            cur = conn.execute(
                "INSERT INTO students(name, address, grade) VALUES (?, ?, ?)",
                (name, address, grade),
            )
            conn.commit()
            return int(cur.lastrowid)

    def get_student(self, student_id: int) -> Optional[Dict[str, Any]]:
        """Fetch a single student by id."""
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            row = cur.fetchone()
            return dict(row) if row else None

    def list_students(self) -> List[Dict[str, Any]]:
        """Return all students."""
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM students ORDER BY id ASC")
            return [dict(r) for r in cur.fetchall()]

    def update_student(
        self,
        student_id: int,
        name: Optional[str] = None,
        address: Optional[str] = None,
        grade: Optional[str] = None,
    ) -> bool:
        """Update provided fields for a student. Returns True if a row was updated."""
        updates = {k: v for k, v in {"name": name, "address": address, "grade": grade}.items() if v is not None}
        if not updates:
            return False
        cols = ", ".join(f"{k} = ?" for k in updates.keys())
        params = list(updates.values()) + [student_id]
        with self._connect() as conn:
            cur = conn.execute(f"UPDATE students SET {cols} WHERE id = ?", params)
            conn.commit()
            return cur.rowcount > 0

    def delete_student(self, student_id: int) -> bool:
        """Delete a student by id. Returns True if a row was deleted."""
        with self._connect() as conn:
            cur = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            return cur.rowcount > 0
