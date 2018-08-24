import pyodbc




def con():
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=.;"
                        "Database=sampleQueryDb;"
                        "Trusted_Connection=yes;")


    cursor = cnxn.cursor()

    cursor.execute('SELECT CONVERT(varchar,DateInserted)as date,id,nameP,email,GenderId  from tablePerson ')

    #thelist=list()
    f=cursor.fetchall()
    #for row in f:
        
      #  thelist.append(row)   
       
    return f   



