import csv
import pandas as pd

file = open ("TitanicSurvival.csv", "r")
data = list (csv.reader(file,delimiter=","))
file.close()

#print(data)					# print whole data	

#data[-1][-1]="1st"				# edit passenger class

#zimmer=data[-1]
#zimmer[4]=("1st")

#print("Last person: ",data[-1])

df.loc['passengerClass'] = '1st'

df.to_csv("TitanicSurvival.csv", index=False)

print (df)
