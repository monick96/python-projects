import csv
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    
    for row in reader:
      iter = zip(header,row)
      #print(list(iter))
      country_dict = {key: value for key,value in iter}
      #country_dict = dict(iter) tambien convierte en diccionario
      #print(country_dict)
      data.append(country_dict)
    return data
      #print('***' * 5)
      #print(row)
   
if __name__ == '__main__':
 data = read_csv('./app/data.csv') #columnas en forma de array/lista
 #print(data[8])
