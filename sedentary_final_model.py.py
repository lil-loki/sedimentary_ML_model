import datetime
import firebase_admin
import time
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate(r"C:\Users\vansi\Desktop\ML\firebase_key.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://sedimentary-tracking.firebaseio.com/'})

def getdata():
    while True:
     ref=db.reference('data')
     result=ref.get()
     accx=result['accx']#left right tilt
     accy=result['accy']#up down tilt
     accz=result['accz']#front baack flip detection
     gyrox=result['gyrox']
     gyroy=result['gyroy']
     gyroz=result['gyroz']
     latitude=result['latitude']
     longitude=result['longitude']
     return float(accx),float(accy),float(accz)

def checksdifference():
    accx1,accy1,accz1=getdata()
    print(accx1,accy1,accz1)
    time.sleep(5)
    accx2,accy2,accz2=getdata()
    print(accx2,accy2,accz2)
    final_accx=abs(accx2-accx1)
    final_accy=abs(accy2-accy1)
    final_accz=abs(accz2-accz1)
    print(final_accx,final_accy,final_accz)
    if final_accx < 0.2 and final_accy <0.2 :
        state="IDLE"
    else:
        state="ACTIVE"
    return state


while True:
    dt=datetime.datetime.today()
    date1=dt.date
    time1=dt.second
    if time1%30 == 0:
        print(time1)
        state=checksdifference()
        print(state)
    #if time1%30 == 0:
        #upload code
        