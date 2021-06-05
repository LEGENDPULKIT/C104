import csv

with open('HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)



file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
     n_num=file_data[i][1]
     new_data.append(float(n_num))


n=len(new_data)
new_data.sort()


#print(new_data)

if n % 2==0:
    medium1=float(new_data[n//2])
    medium2=float(new_data[n//2-1])
    print(medium1)
    print(medium2)
    medium=(medium1+medium2)/2
else:
    medium=float(new_data[n//2])
print(n)
print(medium)    
