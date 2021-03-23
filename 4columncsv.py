import csv
header = ["place", "name", "age"]
with open('city.csv',"w") as csvfile:
    write = csv.DictWriter(csvfile,fieldnames=header)
    write.writeheader()
    write.writerow({"place": "orkkatteri", "name": "thanu", "age": 21})
    write.writerow({"place": "vadakara", "name": "Amal", "age": 22})
    write.writerow({"place": "kuttyadi", "name": "aysha", "age": 23})
    write.writerow({"place": "wayanad", "name": "hasna", "age": 24})
with open("city.csv") as csvfile:
    read= csv.DictReader(csvfile)
    n=input("enter the colomn name you want:")
    for i in read:
        print(i[n])