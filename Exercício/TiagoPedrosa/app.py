from db import Conexao

#Listar quantidade de visitas que cada site recebeu
def visitasCidade():
    con = Conexao()
    query = "SELECT st.name Site, count(*) Visitas FROM Visited vt INNER JOIN Site st ON st.id = vt.site_id GROUP BY site_id ;"
    result = con.getQuery(query)
    print(result)

#Listar sites que nao receberam visitas
def cidadesSemVisitas():
    con = Conexao()
    query = "SELECT st.name Site FROM Site st LEFT JOIN Visited vt ON vt.site_id = st.id WHERE vt.id IS NULL;"
    result = con.getQuery(query)
    print(result)

#Listar métricas que foram observadas na tabela survey
def mtricasObservadas():
    con = Conexao()
    query = "SELECT DISTINCT quant Metrica FROM Survey;"
    result = con.getQuery(query)
    print(result)

#Listar pessoas que fizeram mais de dois levantamentos
def pessoasMaisDoisLevantamentos():
    con = Conexao()
    query = "SELECT DISTINCT ps.personal Pessoa, COUNT(sv.id) Levantamentos FROM Survey sv INNER JOIN Person ps ON ps.id = sv.person_id GROUP BY sv.person_id HAVING COUNT(sv.id) > 2;"
    result = con.getQuery(query)
    print(result)

#Listar pessoas que o sobrenome possua DYR no meio da palvra
def sobrenomeDyr():
    con = Conexao()
    query = "SELECT * FROM Person WHERE family LIKE '%DYR%';"
    result = con.getQuery(query)
    print(result)

#Listar visitacoes a uma lista de sites passados como parâmetro
def visitasPorSite():
    con = Conexao()
    lista = (('DR-1','DR-3'),)
    query = "SELECT DISTINCT st.name Site, vt.`date` DataVisita FROM Visited vt INNER JOIN Site st ON st.id = vt.site_id INNER JOIN Survey sv ON sv.visited_id  = vt.id WHERE st.name IN %s;"
    result = con.getQuery(query, lista)
    print(result)

#verifique quantas linhas possuem valor nulo na coluna quant na tabela survey
def colunaQuantNull():
    con = Conexao()
    query = "SELECT count(*) Linhas FROM Survey WHERE quant IS NULL OR quant = '';"
    result = con.getQuery(query)
    print(result)

#retorne a media de lat lon utilizando como parametro de busca um intervalo de datas
def mediaLatLong():
    con = Conexao()
    datas = ('1927-02-08','1930-01-12')
    query = "SELECT AVG(st.lat) MediaLat, AVG(st.`long`) MediaLong FROM Site st INNER JOIN Visited vt ON vt.site_id = st.id WHERE `date` BETWEEN %s AND %s;"
    result = con.getQuery(query,datas)
    print(result)

#Retorne a quantidade de medições realizadas por cada pessoa na tabela person
def quantidadeMedicoesPessoa():
    con = Conexao()
    query = "SELECT ps.personal Pessoas, count(*) Medicoes FROM Survey sv INNER JOIN Person ps ON sv.person_id = ps.id GROUP BY sv.person_id;"
    result = con.getQuery(query)
    print(result)

#retorne a pessoa que tem a maior quantidade de medições de temperatura entre 10 e 30
def quantidadeMedicoesTemp():
    con = Conexao()
    query = "SELECT ps.personal Pessoa, count(*) Medicoes FROM Survey sv INNER JOIN Person ps ON sv.person_id = ps.id WHERE sv.quant = 'temp' AND sv.reading >= 10 AND sv.reading  <= 30 GROUP BY sv.person_id  ORDER BY count(*) DESC LIMIT 1;"
    result = con.getQuery(query)
    print(result)

sobrenomeDyr()