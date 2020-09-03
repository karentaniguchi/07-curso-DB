import MySQLdb 


class Conexao(object):
    db = None    
    def __init__(self):

        self.db = MySQLdb.connect(host="127.0.0.1",    
                     user="tiago",         
                     passwd="password",  
                     db="atividade1")

        self.cur = self.db.cursor()

    def __del__(self):
        if self.db is not None:
            self.cur.close()
            self.db.close()
            del self.db
            self.db = None

    def insertQuery(self, query, params):
        #print(params)
        self.cur.execute(query,(params))
        self.db.commit()

    def getQuery(self, query,params=None):

        if not params:
            self.cur.execute(query)
        else:
            self.cur.execute(query,(params))
        
        # transformando eum dicionario
        column_names_list = [x[0] for x in self.cur.description]
        result_dicts = [dict(zip(column_names_list, row)) for row in self.cur.fetchall()]
        #result_dicts = self.cur.fetchall()
        return result_dicts

