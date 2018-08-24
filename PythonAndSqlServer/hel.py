import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
"Server=.;"
"Database=sampleQueryDb;"
"Trusted_Connection=yes;")

n=None
def itshere(n):
        return (n)

nameP='waris'
email='wan@jnjn'
genderid=1
idT=7
try:
    cursor = cnxn.cursor()
    SQLCommand = ("INSERT INTO tablePerson(id,nameP,email, genderid) VALUES (?,?,?,?)")    
    Values = [idT,nameP,email,genderid]   
    #Processing Query    
    cursor.execute(SQLCommand,Values)     
    #Commiting any pending transaction to the database.    
    cnxn.commit()

except Exception as e:
   n=e

else:
    print('no error')    


print(n)