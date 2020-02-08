import requests

def send(record):
    studentID = record['studentid']
    chicagoID = record['chicagoid']
    rfid = record['rfid']
    ISO = record['iso']
    first = record['fname'].title()
    last = record['lname'].title()
    gradYear = record['LabSchool Grade Level']
    dateIssued = record['issued']
    print(first + " " + last + " -- grade: " + gradYear)
    payload = {'first': first, 'last': last, 'ISO': ISO, 'grade': gradYear, 'chi': chicagoID,
               'code': "wtv7MpD79EAWYHHUeDR6YHJ3EXHNXc9Yd2HwfHdXpaCKuXK4E7hFrkcNuBJ8KWcGajJutrdmu2mQTzq79cGbxwXDm8naMdJ2qsqE6cM97KmcxLzerJV7KDdKWRthc2uT"}
    # print(payload)
    r = requests.post("https://sc.ucls.uchicago.edu/ID-Card/api.php", data=payload)

CSV_PATH = "Student card data 02-07-20.csv"