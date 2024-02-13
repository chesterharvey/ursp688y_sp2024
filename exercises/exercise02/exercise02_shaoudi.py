#Create empty dictinary
#Get to outer dictionary
#Get to inner dictionary
#example:for dictionary1, dictionary2 in service_requests.items():
#Look for keys through inner dictionaries
#example: for item, information in dictionary2.items():
#store key and value (use if and else)
#create function def


request_counts = {}
for dictionary1, dictionary2 in service_requests .items():
  for item, information in dictionary2.items():
    #print (item)
    #print (information)
      if item == 'Request Type':
        if information in request_counts:
         request_counts[information] += 1
        else:
         request_counts[information] = 1


request_counts
{'B12': 7,
 'WR1': 10,
 'FM05': 55,
 'RW1': 6,
 'FM04': 44,
 'S': 2,
 'B11': 13,
 'Z29': 1,
 'HO14': 3,
 'REFRD': 18,
 'DA10': 3,
 'Z14': 5,
 'FM03': 14,
 'RW5': 12,
 'B10': 15,
 'WR2': 3,
 'B17': 7,
 'B14': 6,
 'Z99': 11,
 'Z30': 4,
 'RW4': 5,
 'ZZ99': 15,
 'V': 1,
 'B13': 1,
 'B27': 1,
 'Z26': 2,
 'Z25': 1,
 'Z20': 3,
 'Z': 3,
 'WR5': 5,
 'WR3': 9,
 'E11': 1,
 'Z18': 1,
 'S15': 1,
 'WR4': 2,
 'BM22': 1,
 'SE11': 1,
 'BE11': 1,
 'LD3': 1,
 'Z11': 1,
 'S11': 1,
 'EM23': 1,
 'Z22': 2,
 'FM02': 1,
 'SE': 1,
 'HO13': 1,
 'HO': 2,
 'B': 1,
 'WR': 1,
 'Z13': 1,
 'B15': 1}

def request_counter(service_requests,attributes):
  request_counts = {}
  for dictionary1, dictionary2 in service_requests.items():
    for item, information in dictionary2.items():
    #print (item)
    #print (information)
      if item == attributes:
        if information in request_counts:
         request_counts[information] += 1
        else:
         request_counts[information] = 1
  return request_counts

request_counter(service_requests,'City')
{'ROCKVILLE': 44,
 'SILVER SPRING': 82,
 'KENSINGTON': 27,
 'BETHESDA': 58,
 'TAKOMA PARK': 11,
 'OLNEY': 1,
 'CHEVY CHASE': 6,
 'DAMASCUS': 4,
 'GAITHERSBURG': 16,
 'BARNESVILLE': 2,
 'POTOMAC': 3,
 'POOLESVILLE': 1,
 'GERMANTOWN': 22,
 'CLARKSBURG': 6,
 'BURTONSVILLE': 5,
 None: 5,
 'GARRETT PARK': 1,
 'BROOKEVILLE': 1,
 'BOYDS': 3,
 'BEALLSVILLE': 3,
 'SANDY SPRING': 3,
 'MONTGOMERY VILLAGE': 3,
 'DICKERSON': 1}