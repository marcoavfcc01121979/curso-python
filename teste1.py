import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="123", db="alunos")
cursor = db.cursor()
'''
cursor.execute("""insert into alunos (nome,telefone)
               values("marco","88889999");""")

cursor.execute("""insert into alunos (nome,telefone)
               values("maria","88889999");""")

cursor.execute("""insert into alunos (nome,telefone)
               values("aline","88889999");""")

cursor.execute("""insert into alunos (nome,telefone)
               values("luis felipe","88889999");""")
'''

cursor.execute("delete from alunos where nome = 'marco';")

cursor.execute("select * from alunos;")
db.commit()
alunos = cursor.fetchall()
for a in alunos:
    print (a)
#cursor.execute("select * from alunos.alunos")
