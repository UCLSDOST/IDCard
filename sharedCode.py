import requests

def send(record):
    studentID = record[1]
    gradYear = record[2]
    first = record[3].title()
    last = record[4].title()
    rfid = record[0]
    ISO = record[6]
    chicagoID = record[5]
    print first, ",", last, ",", gradYear
    payload = {'first': first, 'last': last, 'ISO': ISO, 'grade': gradYear, 'chi': chicagoID,
               'code': "wtv7MpD79EAWYHHUeDR6YHJ3EXHNXc9Yd2HwfHdXpaCKuXK4E7hFrkcNuBJ8KWcGajJutrdmu2mQTzq79cGbxwXDm8naMdJ2qsqE6cM97KmcxLzerJV7KDdKWRthc2uT"}
    print payload
    r = requests.post("https://sc.ucls.uchicago.edu/ID-Card/api.php", data=payload)
    print(r.text)
