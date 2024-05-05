import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from ext_data import read_csv
from gen_data import codificar_data
from gen_data import grow_population

def grafico(x_data,y_data,z_data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_pos = np.array(x_data)
    y_pos = np.array(y_data)
    x_pos, y_pos = np.meshgrid(x_pos, y_pos,indexing="ij")
    z_pos = np.zeros_like(x_pos)
    z = np.array(z_data)

    ax.set_xlabel('Continents')
    ax.set_ylabel('Years')
    ax.set_zlabel('Population')
    ax.set_title('Population per continent in millions')
    ax.set(xticks=x_data, xticklabels=['Asia','South America','Oceania','Africa','North America','Europe'], yticks=y_data, yticklabels=['2000','2010','2015','2020','2022'],zticks=[1000,2000,3000,4000,5000], zticklabels=['1000','2000','3000','4000','5000']) 
    ax.bar3d(x_pos.flatten(), y_pos.flatten(), z_pos.flatten(), 0.8, 0.8, z.flatten(), shade=True)
    plt.show()


if __name__ == '__main__':
  data_user = read_csv('./proyecto2/data.csv')
  cod_continents, cod_years, cod_data_user  = codificar_data(data_user)
  x_data,y_data,z_data = grow_population(cod_continents, cod_years, cod_data_user)
  grafico(x_data,y_data,z_data)


