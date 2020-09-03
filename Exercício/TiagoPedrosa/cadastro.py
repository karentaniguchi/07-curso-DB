from db import Conexao
import random
import string
import sys

def randomName(length):
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length))
    return result

def randomFloat():
    result = round(random.uniform(-100, 100), 2)
    return result

def randomIDFromTab(tabela):
    con = Conexao()
    quant = con.getQuery("SELECT * FROM %s;" % tabela)
    ids = [x["id"] for x in quant]
    result = random.choice(ids)
    return result

def randomWord(words):
    result = random.choice(words)
    return result

def insertRandom():
    con = Conexao()
    
    sqlperson = "INSERT INTO Person (personal,family) VALUES(%s,%s);"
    sqlsite = "INSERT INTO Site (name,lat,`long`) VALUES(%s,%s,%s);"
    sqlvisited = "INSERT INTO Visited (site_id, `date`) VALUES(%s,%s);"
    sqlsurvey = "INSERT INTO Survey (visited_id, person_id, quant, reading) VALUES (%s, %s, %s, %s);"

    con.insertQuery(sqlperson, (randomName(6),randomName(12)))
    con.insertQuery(sqlsite, (randomName(8), randomFloat(), randomFloat()))
    con.insertQuery(sqlvisited, (randomIDFromTab("Site"), randomWord(["1930-11-12","1929-01-08","1928-12-08","1927-05-29"])))
    con.insertQuery(sqlsurvey, (randomIDFromTab('Visited'),randomIDFromTab('Person'), randomWord(["rad","sal","temp"]), randomFloat() ))
    

def insertPerson():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")

    con = Conexao()
    sql = "INSERT INTO Person (personal,family) VALUES(%s,%s);"
    con.insertQuery(sql, (nome, sobrenome))

def insertSite():
    nome = input("Nome: ")
    lat = float(input("Latitude: "))
    longi = float(input("Longitude: "))

    con = Conexao()
    sql = "INSERT INTO Site (name,lat,`long`) VALUES(%s,%s,%s);"
    con.insertQuery(sql, (nome, lat, longi))

def insertVisited():
    local = int(input("ID local (site): "))
    data = input("Data: ")

    con = Conexao()
    sql = "INSERT INTO Visited (site_id, `date`) VALUES(%s,%s);"
    con.insertQuery(sql, (local,data))

def insertSurvey():
    visita = int(input("ID visita: "))
    pessoa = int(input("ID pessoa: "))
    quant = input("Medida: ")
    read = float(input("Valor: "))

    con = Conexao()
    sql = "INSERT INTO Survey (visited_id, person_id, quant, reading) VALUES (%s, %s, %s, %s);"
    con.insertQuery(sql, (visita,pessoa,quant,read))


def main():
    opcao = {"1": insertRandom, 
             "2": randomFloat}
    choosenOption = sys.argv[1]
    opcao[choosenOption]()

if __name__ == "__main__":
    main()