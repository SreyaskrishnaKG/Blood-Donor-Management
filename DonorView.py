from mysql import connector

print("hello..")

class BloodDonorManager:
    def __init__(self):
        self.connection=connector.connect(
        user="root",
        password="Sre859028#",
        database="blood_db_aug26",
        host="localhost"
        )
        print("connected successfully...")
        
    def get_object(self,ID=None):
        try:
            self.cursor=self.connection.cursor()
            qer="select * from donor where id =%s"
            values=(ID,)
            self.cursor.execute(qer,values)
            record=self.cursor.fetchone()
            return(record)
        except Exception as e:
            print(e)
            
        
    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="""insert into Donor(name,blood_group,phone,city,last_donation)
            values(%s,%s,%s,%s,%s)"""
            # values(%s,%s,%s,%s,%s)
            values=[v for v in kwargs.values()]
            self.cursor.execute (query,values)
            self.connection.commit()
            print("data inserted successfully.....")
        except Exception as e :
            print(e)         
            
    def get(self):

        self.cursor=self.connection.cursor()
        query="select * from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        return records
            
    def retrieve(self,id=None):
        try:
            records=self.get_object(ID=id) 
            if records!=None:     
                print(records)
        except Exception as e:
            print(e)
            
    def delete(self,id=None):
        try:
            record=self.get_object(ID=id)   
            if record !=None:
                record=self.get_object(ID=id)
                query="delete from donor where id=%s"
                self.cursor.execute(query,(id,))
                self.connection.commit()
                print("donor deleted successfully...........")
            else:
                print("record not found.......")
        except Exception as e:
            print(e)
            
    def put(self,id=None, **kwargs):
        try:   
            record=self.get_object(ID=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                    placeholder=placeholder.rstrip(", ")     
                    query= f"update donor set {placeholder} where id =%s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    return True ,"Donor updated successfully....!"
                else:
                    return False, "No  found.................!"
                    # print("donor updated successfully..........")
            else:
                print("donor not found..................")
                return False, "No donors .................!"
        except Exception as e:
            print(e)
            return False, "No donors found.................!"
            
                
              
obj1=BloodDonorManager()
# obj1.post(name="sreyas",blood_group="A",
#           phone="5678945678",city="LONDON",date="2026-11-14")
# obj1.post(name="kiran",blood_group="O",phone="97786756444",city="South africa",last_donation="2025-10-15")
# obj1.get()
obj1.retrieve(id=3)
# obj1.delete(id=3)
obj1.put(name="kiran",blood_group="O",phone="9778675643",city="South africa",last_donation="2025-10-15")
