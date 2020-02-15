import  mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host=" sql2.freemysqlhosting.net",
  user="sql2322060",
  passwd="wS3%xV4!",
  database="sql2322060"
)

print("success connect database")


# create table of database
# def createTabels():
#
#  mycursor=mydb.cursor()
#  sql="CREATE TABLE manager(ID INT AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(20),password VARCHAR(20),numberOfParking INT)"
#  sql1="CREATE TABLE clients(numberOfLicense VARCHAR(20),status VARCHAR(5),ID INT)"
#  sql2="CREATE TABLE licensePlate(nymberOfLicense VARCHAR(20),timeIn DATETIME,timeOut DATETIME,statusOfLicense VARCHAR(5),nameOfClient VARCHAR(20))"
#  mycursor.execute(sql1)
#  mycursor.execute(sql2)
#  mycursor.execute("SHOW TABLES")
#  for x in mycursor:
#    print(x)

#  insert in manager table
def insertManager(name,password,numberOfParking):

  mycursor=mydb.cursor()
  sql="INSERT INTO manager(name,password,numberOfParking) VALUES(%s,%s,%s) "
  val=(name,password,numberOfParking)
  mycursor.execute(sql,val)
  mydb.commit()
  print("success insert")

# insert in clients table
def insertClients(numberOfLicense,name):

  mycursor=mydb.cursor()
  sql="INSERT INTO clients(numberOfLicense,status,ID) VALUES(%s,%s,%s) "
  status="SELECT statusOfLicense FROM licensePlate WHERE nymberOfLicense = %s "
  valLisence=(numberOfLicense,)
  mycursor.execute(status,valLisence)
  myresult=mycursor.fetchall()
  if myresult==[]:
    myresult=[('Out',)]
    print("the state of license plate is "+myresult[0][0])
  else:
    print("the state of license plate is " + myresult[0][0])

  IDOfClient="SELECT ID FROM manager WHERE name= %s "
  valID=(name,)
  mycursor.execute(IDOfClient,valID)
  myresultID=mycursor.fetchall()
  if myresultID==[]:
    myresultID=[(0,)]
    print("the id of client is "+str(myresultID[0][0]))

  else:
    print("the id of client is "+str(myresultID[0][0]))

  val=(numberOfLicense,myresult[0][0],myresultID[0][0])
  mycursor.execute(sql,val)
  mydb.commit()
  print("success insert clients")

# insert in lisencePlate table
def insertLisencePlate(numberOfLicense,timeIn,timeOut,statusOfLicense):

  mycursor=mydb.cursor()
  sql="INSERT INTO licensePlate(nymberOfLicense,timeIn,timeOut,statusOfLicense,nameOfClient) VALUES(%s,%s,%s,%s,%s) "
  nclient="SELECT ID FROM clients WHERE numberOfLicense = %s "
  valnumberOfLicense=(numberOfLicense,)
  try:
   mycursor.execute(nclient,valnumberOfLicense)
   myresultName = mycursor.fetchone()
   sql2="SELECT name FROM manager WHERE ID =%s"
   val=(myresultName)
   mycursor.execute(sql2,val)
   myresultName=mycursor.fetchone()
  except:
    myresultName="None"


  print("the name of client "+myresultName[0])
  val=(numberOfLicense,timeIn,timeOut,statusOfLicense,myresultName[0])
  mycursor.execute(sql,val)
  UpdateClients(numberOfLicense)
  mydb.commit()
  print("success insert into Lisence PLate")

# update the status in tow tabels : License plate and clients
def updateLicensePlate(ValueOfLicense):
  mycursor=mydb.cursor()
  sql="UPDATE licensePlate SET timeOut = %s WHERE nymberOfLicense = %s "
  timeout=datetime.now()
  val=(timeout,ValueOfLicense)
  mycursor.execute(sql,val)
  mydb.commit()
  mycursor2=mydb.cursor()
  sql2="UPDATE licensePlate SET statusOfLicense = %s WHERE nymberOfLicense = %s"
  val2=("Out",ValueOfLicense)
  mycursor2.execute(sql2,val2)
  UpdateClients(ValueOfLicense)
  mydb.commit()
  print("success update")

def UpdateClients(ValueOfLicense):
  mycursor = mydb.cursor()
  sql = "UPDATE clients SET status = %s WHERE numberOfLicense = %s"
  sqlif="SELECT statusOfLicense FROM licensePlate WHERE nymberOfLicense = %s"
  val=(ValueOfLicense,)
  mycursor.execute(sqlif,val)
  myresult=mycursor.fetchall()
  val2=myresult[0][0]
  val3 = (val2,ValueOfLicense)
  mycursor.execute(sql, val3)
  mydb.commit()

##########################################################################################################################################
# timeIn=datetime.now()
# insertLisencePlate("4501asd",timeIn,"","IN")

# createTabels()
# insertClient("4561kkg","ahmad")

# insertManager("Ahmad","123456",5)
# insertManager("ALi","123",2)
# insertManager("Mohammad","654321",10)
# insertClients("123aaa","ahmad")
# insertClients("213bbb","ahmad")
# insertClients("321ccc","ahmad")
# insertClients("456abc","ALi")
# insertClients("654cba","ALi")
# insertClients("564bac","ALi")
# insertClients("789xyz","Mohammad")
# insertClients("897yzx","Mohammad")
# insertClients("978zyx","Mohammad")
# mycursor = mydb.cursor()
# sql5="DELETE FROM licensePlate"
# mycursor.execute(sql5)
# mydb.commit()
#
# insertLisencePlate("123aaa",datetime.now(),"","IN")
# insertLisencePlate("789xyz",datetime.now(),"","IN")
# insertLisencePlate("564bac",datetime.now(),"","IN")
# updateLicensePlate("123aaa")
#
#
# sql="SELECT * FROM clients"
# sql=" SELECT * FROM Li"
# sql2="SELECT * FROM licensePlate"
# sql3="SELECT * FROM manager"
# sql4="SELECT *FROM clients"

# sql6="SELECT *FROM manager"
#
# mycursor.execute(sql)
# mycursor.execute(sql2)
# mycursor.execute(sql3)
# mydb.commit()
# print("success delete ")
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#   print (x)
# mycursor.execute(sql2)
# myresult=mycursor.fetchall()
# for x in myresult:
#   print (x)
# mycursor.execute(sql3)
# myresult=mycursor.fetchall()
# for x in myresult:
#   print (x)
# #################################################################################################################################