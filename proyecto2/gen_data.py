from ext_data import read_csv
import math


def codificar_data(data):
  cod_data=[]
  continent = ['Asia','South America','Oceania','Africa','North America','Europe']
  years = ['2000 Population','2010 Population','2015 Population','2020 Population','2022 Population']
  cod_continents=list(zip(continent,['1','2','3','4','5','6']))
  cod_years=list(zip(years,['2000','2010','2015','2020','2022']))

  for x in data:
      cod_population={}
      match x['Continent']:
        case 'Asia':
              cod_population['Continent']='1'
        case 'South America':
              cod_population['Continent']='2'
        case 'Oceania':
              cod_population['Continent']='3'
        case 'Africa':
              cod_population['Continent']='4'
        case 'North America':
              cod_population['Continent']='5'
        case 'Europe':
              cod_population['Continent']='6'
      
      cod_population['2022']=x['2022 Population']
      cod_population['2020']=x['2020 Population']
      cod_population['2015']=x['2015 Population']
      cod_population['2010']=x['2010 Population']
      cod_population['2000']=x['2000 Population']
      cod_data.append(cod_population)
  return cod_continents, cod_years, cod_data


def grow_population(cod_continents, cod_years, cod_data):
  
  x_data=[int(i[1]) for i in cod_continents]
  y_data=[int(i[1]) for i in cod_years]
  z_data=[]
  
  suma_year=0
  for cont in cod_continents:
      population_years=[]
      print(cont)
      for year in cod_years:
         print(year)
         suma_year=int(sum([ int(i[str(year[1])])  for i in cod_data if i['Continent'] == cont[1] ]))
         population_years.append(math.trunc(suma_year/1000000))
      z_data.append(population_years)
  return x_data,y_data,z_data



if __name__ == '__main__':
  data_user = read_csv('./proyecto/data.csv')
  cod_continents, cod_years, cod_data_user  = codificar_data(data_user)
  x_data,y_data,z_data = grow_population(cod_continents, cod_years, cod_data_user)
