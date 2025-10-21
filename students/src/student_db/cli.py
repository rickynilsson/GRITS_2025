import argparse
import json
from .db import StudentDB


def _add(subparsers):
    p = subparsers.add_parser("add", help="Add a new student")
    p.add_argument("--name", required=True)
    p.add_argument("--address", required=True)
    p.add_argument("--grade", required=True)
    p.set_defaults(cmd="add")


def _get(subparsers):
    p = subparsers.add_parser("get", help="Get a student by id")
    p.add_argument("--id", type=int, required=True)
    p.set_defaults(cmd="get")


def _list(subparsers):
    p = subparsers.add_parser("list", help="List all students")
    p.set_defaults(cmd="list")


def _update(subparsers):
    p = subparsers.add_parser("update", help="Update student fields")
    p.add_argument("--id", type=int, required=True)
    p.add_argument("--name")
    p.add_argument("--address")
    p.add_argument("--grade")
    p.set_defaults(cmd="update")


def _delete(subparsers):
    p = subparsers.add_parser("delete", help="Delete a student by id")
    p.add_argument("--id", type=int, required=True)
    p.set_defaults(cmd="delete")


def main():
    parser = argparse.ArgumentParser(prog="student-db", description="Student DB CLI")
    parser.add_argument("--db", default="students.db", help="Path to SQLite DB file")
    subs = parser.add_subparsers(dest="cmd", required=True)

    _add(subs)
    _get(subs)
    _list(subs)
    _update(subs)
    _delete(subs)

    args = parser.parse_args()
    db = StudentDB(args.db)

    if args.cmd == "add":
        sid = db.add_student(args.name, args.address, args.grade)
        print(sid)
    elif args.cmd == "get":
        print(json.dumps(db.get_student(args.id), indent=2))
    elif args.cmd == "list":
        print(json.dumps(db.list_students(), indent=2))
    elif args.cmd == "update":
        ok = db.update_student(args.id, name=args.name, address=args.address, grade=args.grade)
        print("updated" if ok else "not-found-or-no-changes")
    elif args.cmd == "delete":
        ok = db.delete_student(args.id)
        print("deleted" if ok else "not-found")


if __name__ == "__main__":
    main()
