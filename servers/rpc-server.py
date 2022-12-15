from xmlrpc.server import SimpleXMLRPCServer
import sqlite3

class BancoDeDados:
    def __init__(self, nome):
        self.nomebd = nome
    def conexao(self):
        self.banco = sqlite3.connect(self.nomebd)
        self.cursor = self.banco.cursor()
    def criarTabela(self, nome):
        sql = f'CREATE TABLE IF NOT EXISTS {nome} (id integer primary key autoincrement, nome text, telefone text, tipo_caso text)'
        self.nometb = nome
        self.cursor.execute(sql)
    def inserir(self, dado):
        sql = f"INSERT INTO {self.nometb} VALUES (null, '{dado['nome']}', '{dado['tel']}', '{dado['tipo_caso']}')"
        self.cursor.execute(sql)
        self.banco.commit()
    def selecionar(self, sql_externo=''):
        sql = f'SELECT * FROM {self.nometb}'
        if sql_externo != '':
            sql = sql_externo
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def atualizar(self, id, dado):
        self.cursor.execute(f'SELECT * FROM {self.nometb} WHERE id = {id}')
        if( self.cursor.fetchall() != []):
            self.cursor.execute(f"UPDATE {self.nometb} SET nome = '{dado['nome']}', telefone = '{dado['tel']}', tipo_caso = '{dado['tipo_caso']}' WHERE id = {id}")
            self.banco.commit()
    def deletar(self, id):
        self.cursor.execute(f'SELECT * FROM {self.nometb} WHERE id = {id}')
        if( self.cursor.fetchall() != []):   
            self.cursor.execute(f'DELETE FROM {self.nometb} WHERE id = {id}')
            self.banco.commit()

banco = BancoDeDados('db')
banco.conexao()
banco.criarTabela('ticket')

server = SimpleXMLRPCServer(("127.0.0.2",5000), allow_none=True)
server.register_function(banco.inserir,"inserir")
server.register_function(banco.selecionar,"selecionar")
server.register_function(banco.atualizar,"atualizar")
server.register_function(banco.deletar,"deletar")
server.serve_forever()
