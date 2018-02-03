from sharedCode import send

print("Type 'exit' to exit the program")

f = open('Gatsby-winter-formal.csv')

lines = f.read().split("\r")

RFID = {}
print len(lines)
for line in lines:
    if line != "":
        cols = line.replace('   ', '').split(",")
        print cols[5]
        RFID[str(cols[5])] = cols[:]

while True:
    input_var = str(raw_input("Scan ID: "))

    if input_var == 'exit':
        exit()

    RFIDNum = input_var

    for key in RFID:
        if(RFIDNum in key):
            print RFID[key]
            send(RFID[key])
