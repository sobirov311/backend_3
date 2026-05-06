
import sqlite3
from abc import ABC
from contextlib import closing

DATABASE_PATH = "sample-database.db"


class BaseCRUD(ABC):
    def __init__(self, database_path, table_name):
        self.database_path = database_path
        self.table_name = table_name

    def get_connection(self):
        return closing(sqlite3.connect(self.database_path))

    def insert(self, **kwargs):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            columns      = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' for _ in kwargs)
            query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(kwargs.values()))
            conn.commit()
            return cursor.lastrowid

    def get(self, id, id_column="id"):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (id,))
            return cursor.fetchone()

    def get_all(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name}")
            return cursor.fetchall()

    def update(self, id, id_column="id", **kwargs):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            columns = ', '.join(f"{key}=?" for key in kwargs)
            query = f"UPDATE {self.table_name} SET {columns} WHERE {id_column}=?"
            cursor.execute(query, (*kwargs.values(), id))
            conn.commit()

    def delete(self, id, id_column="id"):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"DELETE FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (id,))
            conn.commit()




class EmployeeCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(DATABASE_PATH, "employees")


def sep(title):
    print(f"\n{'═'*60}")
    print(f"  {title}")
    print('═'*60)


emp = EmployeeCRUD()


id1 = emp.insert(
    first_name="Jasur",
    last_name="Toshmatov",
    email="jasur.toshmatov@company.com",
    phone_number="998901234567",
    hire_date="2024-01-15",
    job_id=9,
    salary=5500.0,
    manager_id=102,
    department_id=6
)
print(f"[1] Dasturchi qo'shildi      → employee_id={id1}")

# 2) Menejer
id2 = emp.insert(
    first_name="Malika",
    last_name="Yusupova",
    email="malika.yusupova@company.com",
    phone_number="998901112233",
    hire_date="2023-06-01",
    job_id=2,
    salary=11000.0,
    manager_id=101,
    department_id=11
)
print(f"[2] Menejer qo'shildi        → employee_id={id2}")


id3 = emp.insert(
    first_name="Bobur",
    last_name="Rahimov",
    email="bobur.rahimov@company.com",
    phone_number="998905556677",
    hire_date="2024-03-20",
    job_id=15,
    salary=7000.0,
    manager_id=145,
    department_id=8
)
print(f"[3] Sotuvchi qo'shildi       → employee_id={id3}")


id4 = emp.insert(
    first_name="Dilnoza",
    last_name="Karimova",
    email="dilnoza.karimova@company.com",
    phone_number="998907778899",
    hire_date="2024-05-10",
    job_id=1,
    salary=4800.0,
    manager_id=205,
    department_id=11
)
print(f"[4] Buxgalter qo'shildi      → employee_id={id4}")




row = emp.get(id1, id_column="employee_id")
print(f"[1] employee_id={id1} → {row}")

row = emp.get(id2, id_column="employee_id")
print(f"[2] employee_id={id2} → {row}")

row = emp.get(102, id_column="employee_id")
print(f"[3] employee_id=102  → {row}")
row = emp.get(103, id_column="employee_id")
print(f"[4] employee_id=103  → {row}")



all_rows = emp.get_all()
print(f"[1] Jami xodimlar soni       → {len(all_rows)} ta")

print(f"[2] Dastlabki 3 xodim:")
for row in all_rows[:3]:
    print(f"     {row}")

top3 = sorted(all_rows, key=lambda x: x[7], reverse=True)[:3]
print(f"[3] Eng yuqori maoshli 3 xodim:")
for row in top3:
    print(f"     {row[1]} {row[2]} — maosh: {row[7]}")

it_dept = [r for r in all_rows if r[9] == 6]
print(f"[4] IT bo'limi xodimlari ({len(it_dept)} ta):")
for row in it_dept:
    print(f"     {row[1]} {row[2]}")



emp.update(id1, id_column="employee_id", salary=6500.0)
row = emp.get(id1, id_column="employee_id")
print(f"[1] Maosh yangilandi          → {row[1]} {row[2]}: maosh={row[7]}")

emp.update(id2, id_column="employee_id", department_id=10, manager_id=108)
row = emp.get(id2, id_column="employee_id")
print(f"[2] Bo'lim yangilandi         → {row[1]} {row[2]}: department_id={row[9]}")

emp.update(id3, id_column="employee_id",
           phone_number="998991234567",
           email="bobur.new@company.com")
row = emp.get(id3, id_column="employee_id")
print(f"[3] Kontakt yangilandi        → {row[1]} {row[2]}: tel={row[4]}, email={row[3]}")

emp.update(id4, id_column="employee_id", job_id=2, salary=9000.0)
row = emp.get(id4, id_column="employee_id")
print(f"[4] Lavozim+maosh yangilandi  → {row[1]} {row[2]}: job_id={row[6]}, maosh={row[7]}")



emp.delete(id1, id_column="employee_id")
print(f"[1] employee_id={id1} o'chirildi → {emp.get(id1, 'employee_id')}")


emp.delete(id2, id_column="employee_id")
print(f"[2] employee_id={id2} o'chirildi → {emp.get(id2, 'employee_id')}")


emp.delete(id3, id_column="employee_id")
print(f"[3] employee_id={id3} o'chirildi → {emp.get(id3, 'employee_id')}")


emp.delete(id4, id_column="employee_id")
print(f"[4] employee_id={id4} o'chirildi → {emp.get(id4, 'employee_id')}")

