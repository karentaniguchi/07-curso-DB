"""
Implemente um programa em Python que realiza as seguintes funções

    1) Cadastro de linhas com valores aleatórios em cada tabela
    2) Uma função de cadastro para cada tabela (pelo terminal) usando comando input
    3) Consultas
        3.1) Listar quantidade de visitas que cada site recebeu
        3.2) Listar sites que nao receberam visitas
        3.3) Listar métricas que foram observadas na tabela survey
        3.4) Listar pessoas que fizeram mais de dois levantamentos
        3.5) Listar pessoas que o sobrenome possua DYR no meio da palvra
        3.6) Listar visitacoes a uma lista de sites passados como parâmetro
        3.7) verifique quantas linhas possuem valor nulo na coluna quant na tabela survey
        3.8) retorne a media de lat lon utilizando como parametro de busca um intervalo de datas
        3.9) Retorne a quantidade de medições realizadas por cada pessoa na tabela person
        3.10) Retorne a pessoa que tem a maior quantidade de medições de temperatura entre 10 e 30

"""

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from operator import itemgetter

class Exercicios_SQL:
    # Realiza a leitura de uma tabela
    def __init__(self):
        self.db = MySQLdb.connect(host="127.0.0.1", 
                            user="melanie",         
                            passwd="password",  
                            db="melanie_banco0")       
    # 1) Cadastro de linhas com valores aleatórios em cada tabela
    def Inserir_linha(self):

        cur = self.db.cursor()

        # Inserindo uma linha em cada tabela
        cur.execute("INSERT INTO Person VALUES('dyer22','William22','Dyer22');")
        cur.execute("INSERT INTO Site VALUES('MSK-22',-48.22,-123.22);")
        cur.execute("INSERT INTO Survey VALUES(844,'roe','rad',11.25);")
        cur.execute("INSERT INTO Visited VALUES(844,'DR-22','1932-03-22');")

        self.db.commit()

        # Selecionando todas as colunas de cada tabelas - SELECT *
        cur.execute("SELECT * FROM Person")
        person = cur.fetchall() # fetchall(): The method fetches all (or all remaining) rows of a query result set and returns a list of tuples.
        cur.execute("SELECT * FROM Site")
        site = cur.fetchall()
        cur.execute("SELECT * FROM Survey")
        survey = cur.fetchall()
        cur.execute("SELECT * FROM Visited")
        visited = cur.fetchall()

        print('\nTabela Person\n')
        for row in person:
            print (row[0],row[1],row[2])

        print('\nTabela Site\n')
        for row in site:
            print (row[0],row[1],row[2])

        print('\nTabela Survey\n')
        for row in survey:
            print (row[0],row[1],row[2],row[3])

        print('\nTabela Visited\n')
        for row in visited:
            print (row[0],row[1],row[2])

        self.db.close()

    #2) Uma função de cadastro para cada tabela (pelo terminal) usando comando input
    def Cadastro_linhas_TablePerson(self):
        
        linha_digitada = []

        cur = self.db.cursor()
        # Lendo o cabeçalho das colunas. nome_colunas = tuple
        cur.execute("SHOW COLUMNS FROM Person")
        nome_colunas = cur.fetchall()
        print(nome_colunas)
        for row in nome_colunas:
            print(f'Digite o valor a ser ingressado na coluna: {row[0]}')
            digite = input()
            linha_digitada.append(digite)

        cur.execute("""INSERT INTO Person VALUES(%s,%s,%s)""", (linha_digitada[0], linha_digitada[1], linha_digitada[2]))

        self.db.commit()

    def Cadastro_linhas_TableSite(self):
        
        linha_digitada = []

        cur = self.db.cursor()
        # Lendo o cabeçalho das colunas. nome_colunas = tuple
        cur.execute("SHOW COLUMNS FROM Site")
        nome_colunas = cur.fetchall()
        print(nome_colunas)
        for row in nome_colunas:
            print(f'Digite o valor a ser ingressado na coluna: {row[0]}')
            digite = input()
            linha_digitada.append(digite)

        cur.execute("""INSERT INTO Site VALUES(%s,%s,%s)""", (linha_digitada[0], linha_digitada[1], linha_digitada[2]))

        self.db.commit()
    
    def Cadastro_linhas_TableSurvey(self):
        
        linha_digitada = []

        cur = self.db.cursor()
        # Lendo o cabeçalho das colunas. nome_colunas = tuple
        cur.execute("SHOW COLUMNS FROM Survey")
        nome_colunas = cur.fetchall()
        print(nome_colunas)
        for row in nome_colunas:
            print(f'Digite o valor a ser ingressado na coluna: {row[0]}')
            digite = input()
            linha_digitada.append(digite)

        cur.execute("""INSERT INTO Survey VALUES(%s,%s,%s,%s)""", (linha_digitada[0], linha_digitada[1], linha_digitada[2], linha_digitada[3]))

        self.db.commit()

    def Cadastro_linhas_TableVisited(self):
        
        linha_digitada = []

        cur = self.db.cursor()
        # Lendo o cabeçalho das colunas. nome_colunas = tuple
        cur.execute("SHOW COLUMNS FROM Visited")
        nome_colunas = cur.fetchall()
        print(nome_colunas)
        for row in nome_colunas:
            print(f'Digite o valor a ser ingressado na coluna: {row[0]}')
            digite = input()
            linha_digitada.append(digite)

        cur.execute("""INSERT INTO Visited VALUES(%s,%s,%s)""", (linha_digitada[0], linha_digitada[1], linha_digitada[2]))

        self.db.commit()
    
# 3.1) Listar quantidade de visitas que cada site recebeu  
 
    def quantidade_visitas(self):

        cur = self.db.cursor()

        cur.execute("select site,count(*) from Visited group by site ;")
        site_count = cur.fetchall()   # Retorna uma tupla (('DR-1', 2), ('DR-3', 4), ('MSK-4', 1), ('b', 1))

        print('\nQuantidade de visitas por site\n')
        for coluna in site_count:
            print (coluna[0],coluna[1])

        self.db.close()

# 3.2) Listar sites que nao receberam visitas
   
    def Sites_sem_visitas(self):
       
        cur = self.db.cursor()

        cur.execute("select name from Site")
        name_site = cur.fetchall()
        
        cur.execute("select site from Visited")
        site_visited = cur.fetchall()

        sites_sem_visitas = [x for x in name_site if x not in site_visited]
        
        print(f'Sites que não receberam visitas: {sites_sem_visitas}')

# 3.3) Listar métricas que foram observadas na tabela survey
    
    def Metricas_tabela_survey(self):
    
        cur = self.db.cursor()

        cur.execute("select quant,count(*) from Survey group by quant")
        quant_survey = cur.fetchall()   

        print('\nMétricas observadas na tabela Survey:\n')
        for coluna in quant_survey:
            print (coluna[0],coluna[1])

        self.db.close()

# 3.4) Listar pessoas que fizeram mais de dois levantamentos

    def Pessoas_mais2_levantamentos(self):

        cur = self.db.cursor()

        cur.execute("select person,count(*) from Survey group by person")
        person_levantamento = cur.fetchall()   
        print(person_levantamento)

        self.db.close()      
        
        sites_sem_visitas = [i[0] for i in person_levantamento if i[1]>2 ]
        print(f'Pessoas que fizeram mais de dois levantamentos: {sites_sem_visitas}')
        
        return sites_sem_visitas
        # sites_sem_visitas = [print(i[0]) for i in person_levantamento if i[1]>2 ]   
        # sites_sem_visitas = [ [print(j) for j in i if type(j) == int and j>2] for i in person_levantamento ]

        # intenté unir las tablas survey y person, no funcionó:
        ### combinando a tabela Person com a tabela Survey em uma unica tabela
        # "select * from Person join Survey on Survey.person=Person.id"
        ### contando os nomes e agrupando
        # "select personal,count(*) from Person group by personal"

# 3.5) Listar pessoas que o sobrenome possua DYR no meio da palvra

    def Sobrenome_com_Dye(self):

        cur = self.db.cursor()

        cur.execute("select * from Person where family LIKE '%Dye%'")
        sobrenome_dye = cur.fetchall()   
        print(sobrenome_dye)

        self.db.close()   

        sobrenome_com_dye = [[i[1], i[2]] for i in sobrenome_dye]
        print(f'Pessoas com "dye" no sobrenome: {sobrenome_com_dye}')

# 3.6) Listar visitacoes a uma lista de sites passados como parâmetro. 
    # Usando input, se o usuário ingresa uma lista com comprimento 'n', serão necessários 'n' %s no cur.execute
    # por isso, foi a função foi definida para ingresar uma variável por vez

    def Visitacoes_lista_1(self):
        site = input('Ingrese o site do qual deseja ver as visitações:')

        cur = self.db.cursor()
        cur.execute("""select site,date from Visited where site in (%s)""", (site))
        visitacoes = cur.fetchall()   

        print(f'Visita ao {site}: {visitacoes}')

        self.db.close() 

    # Alternativa com lista, mas sem input
    
    def Visitacoes_lista_2(self):

        lista = ['DR-1', 'DR-3']

        cur = self.db.cursor()
        cur.execute("""select site,date from Visited where site in (%s, %s)""", (lista[0], lista[1]))
        visitacoes = cur.fetchall()   
        print(f'Visita ao (site/data): {visitacoes}')

        self.db.close() 

# 3.7) verifique quantas linhas possuem valor nulo na coluna quant na tabela survey

    def Linhas_valor_nulo(self):
        
        cur = self.db.cursor()
        cur.execute("select quant,count(*) from Survey where quant IS NULL group by quant")
        linhas_nulas = cur.fetchall()   
        print(f'Linhas com valor NULL na coluna quant da tabela Survey: {linhas_nulas}')

        self.db.close() 

# 3.8) retorne a media de lat lon utilizando como parametro de busca um intervalo de datas

    def Media_lat_lon(self):

        cur = self.db.cursor()
        cur.execute("select avg(lat),avg(lon) from Visited join Site on Visited.site=Site.name where (datee > '1927-02-10' and datee < '1930-02-26')")
        dados = cur.fetchall()   
        print(dados)

# 3.9) Retorne a quantidade de medições realizadas por cada pessoa na tabela person     

    def Medicoes_pessoa(self):

        cur = self.db.cursor()
        cur.execute("select id,count(*) from Person join Survey on Person.id=Survey.person group by person")
        medicoes_pessoa = cur.fetchall()   
        print(f'(Pessoa,Medições) = {medicoes_pessoa}')

# 3.10) Retorne a pessoa que tem a maior quantidade de medições de temperatura entre 10 e 30

    def Pessoa_temperatura(self):

        cur = self.db.cursor()
        cur.execute("select person,count(*) from Survey where (quant = 'temp' and reading>10 and reading<30) group by person")
        pessoa_temperatura = cur.fetchall()   
        x = max(pessoa_temperatura,key=itemgetter(1))[0] 
        print(x)
        return x

x = Exercicios_SQL()
# x.Inserir_linha()
# x.Cadastro_linhas_TablePerson()
# x.Cadastro_linhas_TableSite()
# x.Cadastro_linhas_TableSurvey()
# x.Cadastro_linhas_TableVisited()
# x.Quantidade_visitas()
# x.Sites_sem_visitas()
# x.Metricas_tabela_survey()
# x.Pessoas_mais2_levantamentos()
# x.Pessoas_mais2_levantamentos2()
# x.Sobrenome_com_Dye()
# x.Visitacoes_lista_1()
# x.Visitacoes_lista_2()
# x.Linhas_valor_nulo()
# x.Media_lat_lon()
# x.Medicoes_pessoa()
x.Pessoa_temperatura()


# --------------- aula: https://github.com/ai2-education-fiep-turma-2/07-curso-DB/tree/master/src -------------------#

# Instalando biblioteca para acesso ao Mysql: --> conda install mysqlclient --> não funciono, ver: 26) https://stackoverflow.com/questions/454854/no-module-named-mysqldb

# FONTE BOA: https://mysqlclient.readthedocs.io/user_guide.html#cursor-objects