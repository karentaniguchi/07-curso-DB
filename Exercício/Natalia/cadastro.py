import MySQLdb
import urllib.request
import random
import datetime

class CadastroSql: 
    
    def __init__(self):
        Word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = urllib.request.urlopen(Word_site)
        self.words = response.read().decode().splitlines()

        self.db = MySQLdb.connect(host="127.0.0.1",
                     user="natalia",
                     passwd="password",
                     db="exerciciosql")

        self.cur = self.db.cursor()
        
    def randomData(self):    
        name_sites = ("DR-1", "DR-3", "MSK-4", "DR-2", "MSK-1", "MSK-2", "MSK-3")
        self.site = random.choice(name_sites)

        self.taken = random.randint(0,999)

        survey_quant = ("rad", "sal", "temp")
        self.quant = random.choice(survey_quant)

        self.reading = random.uniform(-50, 50)

        self.id = random.choice(self.words)
        self.word2 = random.choice(self.words)
        self.word3 = random.choice(self.words)

        self.lat = random.uniform(-90, 90)
        self.long = random.uniform(-180, 180)

        start_date = datetime.date(1930, 1, 1)
        end_date = datetime.date(2020, 9, 2)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        self.date = start_date + datetime.timedelta(days=random_number_of_days)


    def inserirDados(self):
        
        self.cur.execute("INSERT INTO Person VALUES(%s, %s, %s)",(self.id, self.word2, self.word3))
        
        self.cur.execute("INSERT INTO Site VALUES(%s, %s, %s)",(self.site, self.lat, self.long))
        
        self.cur.execute("INSERT INTO Survey VALUES(%s, %s, %s, %s)",(self.taken, self.id, self.quant, self.reading))
        
        self.cur.execute("INSERT INTO Visited VALUES(%s, %s, %s)",(self.taken, self.site, self.date))
        self.db.commit()
    
    def inputDado(self):
        
        person_id = input("Person id: ")
        personal = input("First name: ")
        family = input("Family name: ")
        self.cur.execute("INSERT INTO Person VALUES(%s, %s, %s)",(person_id, personal, family))
        #print ("Dados inseridos!")
        
        site_name = input("Site name: ")
        lati = float(input("Latitude: "))
        lon = float(input("Longitude: "))
        self.cur.execute("INSERT INTO Site VALUES(%s, %s, %s)",(site_name, lati, lon))
        #print ("Dados inseridos!")
        
        survey_taken = int(input("Taken number(idenficação do site): "))
        quantidade = input("Quantitativo e indicativo do que está sendo medido (rad, sal ou temp): ")
        survey_reading = float(input("Reading: "))
        self.cur.execute("INSERT INTO Survey VALUES(%s, %s, %s, %s)",(survey_taken, person_id, quantidade, survey_reading))
        #print ("Dados inseridos!")

        visited_date = input("Visited date (xxxx-xx-xx): ")
        self.cur.execute("INSERT INTO Visited VALUES(%s, %s, %s)",(survey_taken, site_name, visited_date))
        self.db.commit()
        print ("Dados inseridos!")

        self.db.close()

obj = CadastroSql()
obj.randomData()
obj.inserirDados()
#obj.inputDado()
