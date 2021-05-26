import mysql.connector
import random
import math


mydb = mysql.connector.connect(
  host="localhost",
  user='root',
  database="mysql"
)
mycursor = mydb.cursor()

mycursor.execute("select * from rides")
allres= mycursor.fetchall()

final_dist={}

def FetchCabs(x2,y2):
    for i in allres:
            close_dist= math.sqrt((x2-i[1])**2+(y2-i[2])**2)
            final_dist[i[0]]=close_dist

    sort_orders = sorted(final_dist.items(), key=lambda x: x[1])    
    for i in sort_orders[:5]:
	    print('Vehicle Id:',i[0],'with Shortesr distance from user',i[1])


x2= float(input("Enter x dist: "))
y2=float(input("Enter y dist: "))
FetchCabs(x2,y2)
