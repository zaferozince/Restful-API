import sqlite3
import time
import datetime as date

class DBHelper():

    def __init__(self):
        
        self.conn = sqlite3.connect('Otopark.db')
        self.cursor = self.conn.cursor()
        self.create_Customer()
        self.create_Park()
        self.create_Registration()
       
        

    def create_Customer(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Customer (ID INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT NOT NULL,Time TEXT NOT NULL,Birthday TEXT NOT NULL,PhoneNumber TEXT NOT NULL,User TEXT NOT NULL)")
        self.conn.commit()

    def create_Park(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Park (ID INTEGER PRIMARY KEY AUTOINCREMENT,Repletion TEXT NOT NULL, ParkingLot TEXT NOT NULL)")
        
        self.conn.commit()

    def create_Registration(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Registration (ID INTEGER PRIMARY KEY AUTOINCREMENT,CustomerID TEXT NOT NULL,ParkingLot TEXT NOT NULL)")
        self.conn.commit()

    def customerAdd(self,Name,Birthday,PhoneNumber):
        created_time = str(date.datetime.now()).split('.')
        query = "INSERT INTO Customer (Name,Time,Birthday,PhoneNumber,User) VALUES ('"+Name+"','"+created_time[0]+"','"+Birthday+"','"+PhoneNumber+"','"+str(1)+"')"
        self.cursor.execute(query)
        self.conn.commit()
        return "Kayıt Başarılı şekilde olmuştur"
        
      

    def customerDelete(self,ID):
        ID=str(ID)
        query = "DELETE FROM Customer WHERE ID = ('"+ID+"')"
        self.cursor.execute(query)
        self.conn.commit()
        return "silinmiştir"
        

    def customerUpdateName(self,ID,Name):#if else ile sadece istenen değerleri girmek eğer name varsa gibi

        query = "UPDATE Customer SET Name = '"+Name+"' WHERE ID = '"+ID+"'"
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def customerUpdateBirthday(self,ID,Birthday):

        query = "UPDATE Customer SET Birthday = '"+Birthday+"' WHERE ID = '"+ID+"'"
        self.cursor.execute(query)
        self.conn.commit()
        return True
    
    def customerUpdatePhonenumber(self,ID,PhoneNumber):

        query = "UPDATE Customer SET PhoneNumber = '"+PhoneNumber+"' WHERE ID = '"+ID+"'"  
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def customerSelect(self,ID):

        query = "SELECT * FROM Customer WHERE ID = ('"+ID+"')"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        user_dict = {
            "ID" : result[0],
            "Name" : result[1],
            "Created Date" : result[2],
            "Birthday" : result[3],
            "Phone" : result[4]
        }
        self.conn.commit()
        return user_dict
        
    def parkAdd(self,ParkingLot):

        query = "INSERT INTO Park (Repletion,ParkingLot) VALUES ('"+str(0)+"','"+ParkingLot+"')"
        self.cursor.execute(query)
        self.conn.commit()
        return "Park Eklenmiştir"
    
    def defaultPark(self):
        query ="SELECT * FROM Park"
        self.cursor.execute(query)
        result = self.cursor.lastrowid
        if result == 50:
            return 0
           
        else:
            i = 1
            while i<51:
                query = "INSERT INTO Park (Repletion,ParkingLot) VALUES ('"+str(0)+"','"+str(i)+"')"
                self.cursor.execute(query)
                result2 = self.cursor.lastrowid
                i = i+1
        self.conn.commit()
        return "Park eklenmiştir"

    def parkDelete(self,ID):

        query = "DELETE FROM Park WHERE ID = ? VALUES ('"+ID+"')"

        self.cursor.execute(query)

        self.conn.commit()

        return "Park silinmiştir"

    def parkUpdate(self,ID,Repletion,ParkingLot):

        query = "UPDATE Park SET Repletion = '"+Repletion+"', ParkingLot = '"+ParkingLot+"' WHERE ID = '"+ID+"'"

        self.cursor.execute(query)
        
        self.conn.commit()

        return "Park Updatelenmiştir"


    def getAllCustomer(self):

        allCustomer = []
        query ="SELECT * FROM Customer"
        self.cursor.execute(query)
        
        result = self.cursor.fetchall()
        for res in result:
            user_dict = {
                "ID" : res[0],
                "Name" : res[1],
                "Created Date" : res[2],
                "Birthday" : res[3],
                "Phone" : res[4]
            }
            allCustomer.append(user_dict)
        self.conn.commit()
        return allCustomer

    def getAllPark(self):
        
        parks = []
        query = "SELECT * FROM Park"
        self.cursor.execute(query)
        result_park = self.cursor.fetchall()
        for ress in result_park:
            get_park_dict = {
            "ID" : ress[0],
            "Repletion" : ress[1],
            "ParkingLot" : ress[2]
            }
            parks.append(get_park_dict)
        self.conn.commit()
        return parks
    
    def registrationSelect(self,CustomerID):
        
        query = "SELECT * FROM Registration WHERE CustomerID = ('"+CustomerID+"')"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        registration_dict ={
            "ID" : result[0],
            "CustomerID" : result[1],
            "ParkingLot" : result[2]
        }
        self.conn.commit()
        return registration_dict
    
    def adminControl(self,ID):

        query = "SELECT * FROM Customer WHERE ID = ('"+ID+"')"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[5]

    def customerLogin(self,Name):
        query = "SELECT * FROM Customer WHERE Name = ('"+Name+"')"
        self.cursor.execute(query)
        result=self.cursor.fetchone()
        return result[0]

    def park_parkinglot(self,CustomerID,ParkingLot):
        query ="SELECT * FROM Registration WHERE CustomerID  = ('"+CustomerID+"')"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if(result == None):
            query = "SELECT * FROM Park WHERE ParkingLot = ('"+ParkingLot+"')"
            self.cursor.execute(query)
            result=self.cursor.fetchone()
            if str(result[1]) == str(0):
                query = "INSERT INTO Registration (CustomerID,ParkingLot) VALUES ('"+CustomerID+"','"+ParkingLot+"')"
                self.cursor.execute(query)
                query = "UPDATE Park SET Repletion = '"+str(1)+"' WHERE ParkingLot = '"+ParkingLot+"'"
                self.cursor.execute(query)
                self.conn.commit()
                return "Park edilmiştir."
            else:
                return "Park etmeye çalıştığınız alan doludur!!!!"
        else:
            return "Zaten kaydınız bulunmaktadır!!!"
        

    def park_exit(self,CustomerID):
        query = "SELECT * FROM Registration WHERE CustomerID = ('"+CustomerID+"')"
        self.cursor.execute(query)
        result=self.cursor.fetchone()
        if(result != None):
            query2 = "SELECT * FROM Park WHERE ParkingLot = ('"+str(result[2])+"')"
            self.cursor.execute(query2)
            result2 = self.cursor.fetchone()
            if str(result2[1]) == str(1):
                query = "UPDATE Park SET Repletion = '"+str(0)+"' WHERE ParkingLot = '"+str(result[2])+"'"
                self.cursor.execute(query)
                query = "DELETE FROM Registration WHERE CustomerID = ('"+CustomerID+"')"
                self.cursor.execute(query)
                self.conn.commit()
                return "Çıkış yapılmıştır"
            else:
                return "Araç park etmemişsiniz!!"
        else:
            return "Park Kayıtınız Bulunmamaktadır !!!!"