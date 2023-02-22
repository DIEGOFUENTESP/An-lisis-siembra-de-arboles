import pandas as pd 
data=pd.read_csv("./siembras.csv")

#Encontrar los datos de la vereda mallarino del municipio de Yarumal
filtro6=data[(data ["Ciudad"]=="Yarumal") & (data["Vereda"]=="Mallarino")]
print(filtro6)

archivoHTML=filtro6.to_html()
archivoGenerado=open("filtro6.html", "w", encoding="utf-8")
archivoGenerado.write(archivoHTML)
archivoGenerado.close()