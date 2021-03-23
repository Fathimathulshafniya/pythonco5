import csv

lst = []
with open("program3.csv", "w") as file:
    write = csv.writer(file)
    write.writerow(["id", "place", "district"])
    limit = int(input("Enter the lines of data you want to enter:"))
    for i in range(limit):
        row_string = input("Enter data (id,place,district) separated by comma:")
        row_list = row_string.split(",")
        write.writerow(row_list)
with open("program3.csv", "r") as file:
    read = csv.reader(file)
    for row in read:
        print(row)
        lst.append(",".join(row))

print(lst)