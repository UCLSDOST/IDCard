import sys
if len(sys.argv) == 1:
    print('Usage: python IDCard.py <KEY>\n\tKEY should be rfid, chicagoid, or studentid')
    sys.exit()
else:
    KEY = sys.argv[1]

from sharedCode import send, CSV_PATH
import pandas as pd

try:
    table = pd.read_csv(CSV_PATH).astype(str).set_index(KEY)
except:
    print(f'Invalid key {KEY}')
    sys.exit(1)

print("Type 'exit' to exit the program")
MAP = table.to_dict(orient='index')
print(f'Total students in database: {table.shape[0]}')

while True:
    input_var = str(input("Scan ID: "))
    if input_var == 'exit':
        sys.exit()
    key = input_var
    if key in MAP:
        record = MAP[key]
        record[KEY] = key
        print(f'Welcome {record["fname"]} {record["lname"]}')
        send(MAP[key])
    else:
        print(f'{KEY} {key} not in database')
