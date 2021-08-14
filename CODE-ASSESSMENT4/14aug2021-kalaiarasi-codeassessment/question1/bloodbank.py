import re
import logging
import pymongo
import time
import smtplib
import valmodule
import collections
try:
    client=pymongo.MongoClient("mongodb://localhost:27017")
    mydatabase=client['BloodDb']
    collection_name=mydatabase['blood']

    blist=collections.deque()
    bloodlist=collections.deque()
    class Bloodbank:
        def __init__(self):
            name=''
            bloodgroup=''
            address=''
            pincode=''
            mobilenum=''
            emailid=''
            lastdonatedate=''
            place=''
            
        def adddonardetail(self,name,bloodgroup,address,pincode,mobilenum,emailid,lastdonatedate,place):
            name="name"
            address="address"
            pincode="pincode"
            mobilenum="mobilenum"
            emailid="emailid"
            lastdonatedate="lastdonatedate"
            place="place"
            return self.adddonardetail

        
            

    obj=Bloodbank()
    if(__name__=='__main__'):
        while(True):
            print("1. add donar")
            print("2. search donar based on bloodgroup")
            print("3. search donar based on bloodgroup & place")
            print("4. update all donate details wirh mobnum")
            print("5. delete donar using mobnum")
            print("6. display total no of donar on each blood group")
            print("7. send an email")
            print("8. exit")

            choice=int(input("enter ur choice:"))
                
            if choice==1:
                name=input("enter your name:")
                bloodgroup=input("enter your bg:")
                address=input("enter your add:")
                mobilenum=input("enter your mobilenum:")
                emailid=input("enter your emailid:")
                pincode=input("enter your pin:")
                
                lastdonatedate=input("enter the last donateddate:")
                place=input("enter your place:")
            
                
            
                x=(valmodule.validation(name,mobilenum,emailid,pincode))
                if x:
                    obj.adddonardetail(name,bloodgroup,address,mobilenum,emailid,pincode,lastdonatedate,place)
                    
                    dict1={"name":name,"bloodgroup":bloodgroup,"address":address,"mobilenum":mobilenum,"emailid":emailid,"pincode":pincode,"lastdonatedate":lastdonatedate,"place":place}
                    bloodlist.append(dict1)
                    r=collection_name.insert_one(dict1)

                else:
                    logging.error("please enter valid data!")


            if choice==2:
                b=input("enter bloodgroup:")
                r=collection_name.find({"bloodgroup":b})
                for i in r:
                    print(i)
            
            if choice==3:
                b=input("enter bloodgroup:")
                p=input("enter place:")
                r=collection_name.find({"$and":[{"bloodgroup":b},{"place":p}]})
                for i in r:
                    print(i)

            if choice==4:
                
                while(True):
                    print("1. update name")
                    print("2.update address")
                    print("3.update pincode")
                    print("4.update last donatedate")
                    print("5.update place")
                    print("6.exit")
                    
                    ch=int(input("enter choice:"))
                    if ch==1:
                        fm=input("enter mobnum:")
                        n=input("enter name:")
                        results=collection_name.update_one({"mobilenum":fm},{"$set":{"name":n}})
                        print("updated")
                    if ch==2:
                        sm=input("enter mobnum:")
                        a=input("enter address:")
                        results=collection_name.update_one({"mobilenum":sm},{"$set":{"address":a}})
                        print("updated")
                    if ch==3:
                        tm=input("enter mobnum:")
                        p=input("enter pincode:")
                        results=collection_name.update_one({"mobilenum":tm},{"$set":{"pincode":p}})
                        print("updated")

                    if ch==4:
                        ym=input("enter mobnum:")
                        do=input("enter last donatedate:")
                        results=collection_name.update_one({"mobilenum":ym},{"$set":{"lastdonatedate":do}})
                        print("updated")
                    if ch==5:
                        m=input("enter mobnum:")
                        pl=input("enter place:")
                        results=collection_name.update_one({"mobilenum":m},{"$set":{"place":pl}})
                        print("updated")
                    if ch==6:
                        break
            
            if choice==5:
                d=input("enter mob:")
                results=collection_name.delete_many({"mobilenum":d})
                print("deleted")
            
            if choice==6:
                results=collection_name.aggregate([{"$group":{"_id":"$bloodgroup","no_of_donar":{"$sum":1}}}])
                for i in results:
                    print(i)
                
                    
            if choice==7:
                w=input("enter the blood group:")
                h=input("enter the hospital name:")
                r=collection_name.find()
                for i in r:
                    if i["bloodgroup"]==w:
                        blist.append(i)
                        message="Hi,urgently need " +w +" " + "blood group at" + " "+h+" "+ "Hospital"
                        connection =smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("kalai.iprimed@gmail.com","Kalai@2404")
                        print(message)
                        connection.sendmail("kalai.iprimed@gmail.com",i["emailid"],message)
                        connection.quit()
                        print("email send")
        
            if choice==8:
                break
                                            
except:
    logging.error("please enter correct data")

     