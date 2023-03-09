import sqlite3
from sqlite3 import Error

#função que cria conexão com banco de dados

def conexãobanco():
    caminho = r"C:\Users\ferso\PycharmProjects\cadastro_de_usuarios\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexãobanco()

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operação realizada com sucesso')

def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res


#função que cria o menu
def menu():
    print('1 - Inserir Novo Registro')
    print('2 - Deletar Registro')
    print('3 - Atualizar Registro')
    print('4 - Consultar Registro')
    print('5 - Consultar Registro por Nome')
    print('6 - Sair')

def menuInserir():
    vnome = str(input('Digite o nome: '))
    vtel = str(input('Digite o telefone: '))
    vemail = str(input('Digite o email: '))
    vsql = f"INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('{vnome}', '{vtel}', '{vemail}')"
    query(vcon, vsql)

def menuDeletar():
    vid = int(input('Digite o ID do registro a ser deletado: '))
    vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO = {vid}"
    query(vcon, vsql)

def menuAtualizar():
    vid = int(input('Digite o ID do registro a ser atualizado: '))
    r = consultar(vcon, f'SELECT * FROM tb_contatos WHERE N_IDCONTATO = {vid}')
    rnome = r[0][1]
    rtel = r[0][2]
    remail = r[0][3]
    vnome = str(input('Digite o nome: '))
    vtel = str(input('Digite o telefone: '))
    vemail = str(input('Digite o email: '))
    if len(vnome) == 0:
        vnome = rnome
    if len(vtel) == 0:
        vtel = rtel
    if len(vemail) == 0:
        vemail = remail
    vsql = f'UPDATE tb_contatos SET T_NOMECONTATO="{vnome}", T_TELEFONECONTATO="{vtel}", T_EMAILCONTATO="{vemail}" WHERE N_IDCONTATO = "{vid}"'
    query(vcon, vsql)

def menuConsultar():
    vsql = 'SELECT * FROM tb_contatos'
    res = consultar(vcon, vsql)
    for r in res:
        print(f'ID:{r[0]:.<4} NOME:{r[1]:.<30} TELEFONE:{r[2]:.<14} E-MAIL:{r[3]}')
    print('Fim da lista')

def  menuConsultarNomes():
    nome = str(input('Digite o nome a ser consultado: '))
    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+nome+"%' "
    res = consultar(vcon, vsql)
    for r in res:
        print(f'ID:{r[0]:.<3} NOME:{r[1]:.<30} TELEFONE:{r[2]:.<14} E-MAIL:{r[3]:.<30}')
    print('Fim da lista')
opc = 0
while opc != 6:
    menu()
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultar()
    elif opc == 5:
        menuConsultarNomes()

vcon.close()
