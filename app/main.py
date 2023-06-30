import utils
import rcsv
import charts
import pandas as pd
#error en salida de filtro por input 
def run():
  '''
  #codigo sin pandas
  data = rcsv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  
  '''
    seccion codigo con pandas
  '''
  
  df= pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  
  '''fin seccion codigo con pandas'''
  
  charts.generate_pie_chart(countries, percentages)

  data = rcsv.read_csv('data.csv')
  country = input('Type Country => ')
  country = country.capitalize()

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels, values)
  

if __name__ == '__main__':
  run()