import MySQLdb
import random 
import math

def generateRandomData(db):
    cur = db.cursor()
    possible_names = ['Angelica', 'Nydia', 'Tim',  'Grisel', 'Lashanda', 'Florencio','Esta', 'Verona' ]   
    possible_family_names = ['Defranco', 'Dibble', 'Letourneau', 'Valiente',  'Hermsen',  'Lastra']

    name_selected = math.floor(random.random()*len(possible_names))
    family_name_selected = math.floor(random.random()*len(possible_family_names))

    name = possible_names[name_selected]
    family_name = possible_family_names[family_name_selected]

    id_person = name[0:3].lower()
    queryInsertPerson = "INSERT INTO Person VALUES('{}','{}','{}')".format(id_person, name,family_name)
    cur.execute(queryInsertPerson)
    print ("{}, {}, {}".format(id_person, name,family_name))

    site_prefixes = ["DR", "SR", "VR","WR","YU"]
    site_prefix = site_prefixes[math.floor(random.random()*len(site_prefixes))]
    
    site_name = "{}-{}".format(site_prefix, math.floor(random.uniform(0,10)))
    lat = random.uniform(-125.0, 125.0)
    lon = random.uniform(-125.0, 125.0)

    print ("{}, {}, {}".format(site_name, lat, lon))
    queryInsertSite = "INSERT INTO Site VALUES('{}',{},{})".format(site_name, lat, lon)
    cur.execute(queryInsertSite)
   

    taken = 8899
    
    for i in range (3):
        date = "{}-{}-{}".format(math.floor(random.uniform(1930,2015)),math.floor(random.uniform(1,12)),math.floor(random.uniform(1,28)))
        print ("{}, {}, {}".format(taken+i, site_name, date))
        quertInsertVisit = "INSERT INTO Visited(id, site, dated) VALUES({},'{}','{}')".format(taken+i, site_name, date)
        cur.execute(quertInsertVisit)

    for i in range(3):
        number_of_entrys = math.floor(random.uniform(1,10))
        list_of_quant = ['rad', 'sal' , 'temp']
        for j in range(number_of_entrys):
            print ("{}, {}, {}, {}".format(taken+i, id_person, list_of_quant[math.floor(random.random()*len(list_of_quant))],random.uniform(0,12) ))
            quertInsertSurvey = "INSERT INTO Survey VALUES({},'{}','{}',{})".format(taken+i, id_person, list_of_quant[math.floor(random.random()*len(list_of_quant))],random.uniform(0,12) )
            cur.execute(quertInsertSurvey)
        
    db.commit()

    
        


def manualInsert(db):
    x = int(input ("Deseja adicionar 1-Pessoa, 2-Site, 3-Visita, 4-Survey? "))
    cur = db.cursor()

    if (x==1):
        id_person = input("id da pessoa: ")
        name = input("nome: ")
        family_name = input("sobrenome: ")
        queryInsertPerson = "INSERT INTO Person VALUES('{}','{}','{}')".format(id_person, name,family_name)
        cur.execute(queryInsertPerson)
        print ("{}, {}, {}".format(id_person, name,family_name))
    elif (x==2):
        site_name = input("nome do site: ")
        lat = float(input("lat: "))
        lon = float(input("lon: "))
        print ("{}, {}, {}".format(site_name, lat, lon))
        queryInsertSite = "INSERT INTO Site VALUES('{}',{},{})".format(site_name, lat, lon)
        cur.execute(queryInsertSite)
    elif (x==3):
        taken = int(input("id da leitura: "))
        site_name = input("nome do site: ")
        date = input("data (YYYY-MM-DD): ")
        print ("{}, {}, {}".format(taken, site_name, date))
        quertInsertVisit = "INSERT INTO Visited(id, site, dated) VALUES({},'{}','{}')".format(taken+i, site_name, date)
        cur.execute(quertInsertVisit)
    elif (x==4):
        taken = int(input("id da leitura: "))
        id_person = input("id da pessoa: ")
        quant = input("quant: ")
        leitura = float(input("leitura: "))

        print ("{}, {}, {}, {}".format(taken, id_person, quant, leitura ))
        quertInsertSurvey = "INSERT INTO Survey VALUES({},'{}','{}',{})".format(taken, id_person, quant, leitura )
        cur.execute(quertInsertSurvey)

    else:
        print("Opção não encontrada")
    
    db.commit()


db = MySQLdb.connect(host="127.0.0.1",    
                     user="gabriel",         
                     passwd="highpass2",  
                     db="dbClass")       
#generateRandomData(db)
manualInsert(db)



'''cur = db.cursor()

#cur.execute("INSERT INTO Person VALUES('dyer2','William222','Dyer222');")
#db.commit()

cur.execute("SELECT * FROM Person")

l=cur.fetchall()

#print(type(l))

for row in l:
    print (row[0],row[1],row[2])



db.close()'''