from sharedCode import send

CSV_PATH = "Lab School HS Student card data 9-28-18.csv"

print("Type 'exit' to exit the program")
f = open(CSV_PATH)

lines = f.read().split("\n")

RFID = {}
print("Total students in database: " + str(len(lines)))
for line in lines:
    if line != "":
        cols = line.replace('   ', '').split(",")
        RFID[str(cols[2])] = cols[:]

while True:
    input_var = str(input("Scan ID: "))

    if input_var == 'exit':
        exit()

    RFIDNum = input_var

    for key in RFID:
        if(RFIDNum in key):
            send(RFID[key])
