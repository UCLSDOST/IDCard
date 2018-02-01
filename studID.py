from sharedCode import send
print("Type 'exit' to exit the program")

f = open('ISO-Dump.csv')

lines = f.read().split("\n")

ID = {}
for line in lines:
    if line != "":
        cols = line.replace('   ', '').split(",")
        ID[cols[1]] = cols[:]

while True:
    input_var = str(raw_input("Enter ID #: "))
    if input_var == 'exit':
        exit()
    try:
    	idInput = input_var
    	if(len(idInput) == 6):
        	idInput = '10' + idInput
    	record = ID[idInput]
    	send(record)
    except:
        print("error reading ID, try again")