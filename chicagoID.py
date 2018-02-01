from sharedCode import send
print("Type 'exit' to exit the program")

f = open('ISO-Dump.csv')

lines = f.read().split("\n")

chiID = {}
for line in lines:
    if line != "":
        cols = line.replace('   ', '').split(",")
        chiID[cols[5]] = cols[:]

while True:
    input_var = str(raw_input("Enter ID #: "))
    if input_var == 'exit':
        exit()
    try:
        idInput = input_var
        record = chiID[idInput]
        send(record)
    except:
        print("error reading ID, try again")