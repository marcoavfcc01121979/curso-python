import sqlite3
db = sqlite3.connect("senac.db")
cursor = db.cursor()
cursor.execute("""
    create table if not exists alunos (
    id integer primary key autoincrement,
    nome varchar(100) not null,
    telefone varchar(14) not null,
    email varchar(100) not null unique)
""")
cursor.execute("""
    insert into alunos (nome,telefone,email) values (
    "Marco Antonio", "95158773", "marcoavfc@gmail.com");
""")
db.commit()

cursor.execute("""
    insert into alunos (nome,telefone,email) values (
    "luis felipe", "3220-8508", "marcoavf@bol.com.br");    
""")

cursor.execute("""
    insert into alunos (nome,telefone,email) values (
    "maria giulia", "8827-4903", "mariagiulia@gmail.com");
""")
db.commit()
