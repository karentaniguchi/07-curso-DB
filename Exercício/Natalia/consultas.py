import MySQLdb

class ConsultaSql:

    def __init__(self):
        
        self.db = MySQLdb.connect(host="127.0.0.1",
                     user="natalia",
                     passwd="password",
                     db="exerciciosql")

        self.cur = self.db.cursor()

    def visitaSite(self):
        
        self.cur.execute("select site,count(*) from Visited group by site")
        for row in self.cur.fetchall():
            print ("Quantidade de visitas no site ", row[0], ":", row[1])
        #self.db.close()

    def sitesSemVisita(self):

        self.cur.execute("Select name from Site A where not exists (select site from Visited B where A.name=B.site)")
        for row in self.cur.fetchall():
            print ("Site sem visita: ", row[0])

    def metricaSurvey(self):
        
        self.cur.execute("select DISTINCT quant from Survey")
        print ("Tipos de métricas observadas: ")
        for row in self.cur.fetchall():
            print (row[0])

    def personTaken(self):

        self.cur.execute("select person,count(*) from Survey group by person having count(*) > 2")
        print ("Pessoas com mais de dois levantamentos: ")
        for row in self.cur.fetchall():
            print (row[0], row[1])

    def personwithDYR(self):

        self.cur.execute("select * from Person where family LIKE '%D%Y%R%'")
        print ("People with d, y and r in the family name: ")
        for row in self.cur.fetchall():
            print (row[0])

        self.cur.execute("select * from Person where family LIKE '%DYR%'")
        print ("People with DYR in the family name: ")
        for row in self.cur.fetchall():
            print (row[0])

    def inputVisitacoes(self):

        sites = (input("Digite uma lista site: "))
        lista_sites = sites.rstrip().split()
        print ('id | site | dated')
        
        for i in lista_sites:
         #   print (i)
            self.cur.execute("select site,id,dated from Visited where site= '%s'" %i)
            for row in self.cur.fetchall():
                print (row[0], row[1], row[2])

    def nullSurvey(self):

        self.cur.execute("select count(*) from Survey where (quant IS NULL) group by quant")
        for row in self.cur.fetchall():
            print ("Número de linhas com valor nulo na coluna quant da tabela Survey: ", row[0])

    def mediaLatLong(self):

        data_min = (input("Digite uma data de início: "))
        data_max = (input("Digite uma data limite: "))
                
        self.cur.execute("select avg(lat),avg(`long`) from Site join Visited on Site.name=Visited.site where (dated > %s and dated < %s)", (data_min, data_max))
        for row in self.cur.fetchall():
            print ("Média de lat e long entre", data_min, "e", data_max, ":", row[0],row[1])

    def medicoesPorPessoa(self):

        self.cur.execute("select person,count(*) from Survey group by person")
        print ("Quantidade de medições realizadas por cada pessoa: ")
        for row in self.cur.fetchall():
            print (row[0], row[1])

    def pessoaTemp(self):

        self.cur.execute("select a_person, max(person_count) FROM (select person as a_person, count(person) as person_count from Survey where ((quant = 'temp') and (reading > 10 and reading < 30)) group by person order by person_count DESC) temptable group by a_person limit 1")
        
        # where ((quant = 'temp') and (reading > 10 and reading < 30)) group by person) temptable")
        print ("Pessoa com maior quantidade de medições de temperatura entre 10 e 30: ")
        for row in self.cur.fetchall():
            print (row[0])


    







obj = ConsultaSql()
#obj.visitaSite()
#obj.sitesSemVisita()
#obj.metricaSurvey()
#obj.personTaken()
#obj.personwithDYR()
#obj.inputVisitacoes()
#obj.nullSurvey()
#obj.mediaLatLong()
#obj.medicoesPorPessoa()
obj.pessoaTemp()