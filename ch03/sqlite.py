import sqlite3

# 1. 데이터베이스 연결
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

# 2. 테이블 생성
cursor.execute('''
create table if not exists person(
    id integer primary key autoincrement,
    name text not null,
    age integer
    )
''')


# 3. 입력
cursor.execute("insert into person(name, age) values( ?, ? )", ("choi", 25))
name = "jung"
age = 35
cursor.execute(f"insert into person(name, age) values( '{name}', {age} )")
connection.commit()

# 4. 검색
cursor.execute("select * from person")
rows = cursor.fetchall()
for row in rows:
    print(row)


# 5. 갱신
query = "update person set age = :age where name = :name"
params = {"name": "jung", "age": 36}
cursor.execute(query, params)
connection.commit()

# 6. 삭제
query = "delete from person where name = :name"
params = {"name": name}
cursor.execute(query, params)
connection.commit()

# 7.종료
cursor.close()
connection.close()