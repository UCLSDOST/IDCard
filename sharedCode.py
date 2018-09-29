import requests

def send(record):
    studentID = record[0]
    gradYear = record[7]
    first = record[4].title()
    last = record[6].title()
    rfid = record[2]
    ISO = record[3]
    chicagoID = record[1]
    print(first + " " + last + " -- grade: " + gradYear)
    payload = {'first': first, 'last': last, 'ISO': ISO, 'grade': gradYear, 'chi': chicagoID,
               'code': "wtv7MpD79EAWYHHUeDR6YHJ3EXHNXc9Yd2HwfHdXpaCKuXK4E7hFrkcNuBJ8KWcGajJutrdmu2mQTzq79cGbxwXDm8naMdJ2qsqE6cM97KmcxLzerJV7KDdKWRthc2uT"}
    # print(payload)
    r = requests.post("https://sc.ucls.uchicago.edu/ID-Card/api.php", data=payload)
