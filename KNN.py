from scipy.io import arff
import pandas as pd
import math
import operator
def distanciaEuclidiana(x, y):#Para todos los datos
    #x: TestingData
    #y: Base de datos en dataframe
    d2 = []
    for i in range(len(y)): #Dataframe
            distancias2 = 0
            for j in range(len(x)): #Recorremos los atributos de la raiz
                cuadrados = math.pow(abs(y.iloc[i][j]-x[j]),2) 
                ##REVISAR REFACTORIZACION ALG
                #print(str(cuadrados))
                distancias2 = cuadrados+distancias2 #Luego los sumamos
                #print(math.sqrt(distancias2))
            raizTotal = [math.sqrt(distancias2),i]
            d2.append(raizTotal) 
    return d2

##PRE-PROCESAMIENTO DE BASE DE DATOS:
data = arff.loadarff('clasificacion-drug.arff')
df = pd.DataFrame(data[0])
  #seleccionar la columna de clases y convertirla en una lista
listaDrogas = df['Drug'].tolist()
listaEdad = df['Age'].tolist()
listaSexo = df['Sex'].tolist()
listaBP = df['BP'].tolist() 
listaCh = df['Cholesterol'].tolist()
listaNa = df['Na'].tolist()
listaK = df['K'].tolist()

TotalElementos = len(listaDrogas)


#NORMALIZACION MIN/MAx
for i in range (TotalElementos):
    listaEdad[i] = (listaEdad[i]-15)/59
    listaNa[i]=abs((listaNa[i]-0.5)/(0.5-0.896))
    listaK[i]=abs((listaK[i]-0.08)/(0.2-0.08))

#Vemos que listaBP y listaCh deben ser discretizados
    #Sexo [F,M] = Sexo[1,0]
    #BP [HIGH, NORMAL, LOW] = BP [1, 0.5, 0]
    #Ch [HIGH, NORMAL] = Ch [1,0]
for i in range(TotalElementos):
    if listaSexo[i] == "F":
        listaSexo[i] = 1
    if listaSexo[i] == "M":
        listaSexo[i] = 0
    
for i in range(TotalElementos):
    if listaBP[i] == "HIGH":
        listaBP[i] = 1
    if listaBP[i] == "NORMAL":
        listaBP[i] = 0.5
    if listaBP[i] == "LOW":
        listaBP[i] = 0

for i in range(TotalElementos):
    if listaCh[i]=="HIGH":
        listaCh[i] = 1
    if listaCh[i] == "NORMAL":
        listaCh[i]= 0

#Actualizamos los valores en las columnas
del df["Age"]
df["Age"] = listaEdad
        
del df["Sex"]
df["Sex"] = listaSexo

del df["BP"]
df["BP"] = listaBP

del df["Cholesterol"]
df["Cholesterol"] = listaCh

#Dataset discretizado
columns = ['Age', 'Sex', 'BP', 'Cholesterol', 'Na', 'K','Drug']
df = df[columns]

#Creamos un respaldo de la base de datos sin las drogas en tipo DATAFRAME
dfBackup = df.copy()
del dfBackup["Drug"]

##Nuevo dataset
columns2 = ['Age', 'Sex', 'BP', 'Cholesterol', 'Na', 'K']
dfSinDrogas = df[columns2]

        
VEdad = int(input("Ingrese edad en tipo flotante: "))
VSexo = float(input("Ingrese sexo (F=1/M=0): "))
VBP = float(input("Ingrese BP {HIGH=1, NORMAL=0.5, LOW=0}: "))
VCh = float(input("Ingrese Cholesterol {HIGH=1, NORMAL=0}: "))
VNa = float(input("Ingrese Na: "))
VK = float(input("Ingrese K: "))
Vecinos = int(input("Ingrese numero de vecinos: "))

#VEdad = 22.0
#VSexo = 1
#VBP = 1.0
#VCh = 1
#VNa =  0.4
#VK = 0.15
#Vecinos = 3
#Testing data
TestingData = [(VEdad-15)/59, VSexo, VBP, VCh,abs((VNa-0.5)/(0.5-0.896)) ,abs((VK-0.08)/(0.2-0.08))]

tupla= []
d = []
vecinos = []
PRUEBA = []
#Retornar lista con distancias
PRUEBA = distanciaEuclidiana(TestingData,dfBackup)

for i in range(0,TotalElementos):
    cuadrados = math.pow(abs(listaEdad[i]-TestingData[0]),2) + math.pow(listaSexo[i]-TestingData[1],2) + math.pow(abs(listaBP[i]-TestingData[2]),2) + math.pow(listaCh[i]-TestingData[3],2) + math.pow(abs(listaNa[i]-TestingData[4]),2) + math.pow(abs(listaK[i]-TestingData[5]),2)
    distancias = [math.sqrt(cuadrados),listaDrogas[i],i]
    d.append(distancias)
    #d = [distancias,ListaDrogas,i]
    #d [i][distancias/ListaDrogas/i]
d.sort()

#creamos N:Training data
N = []
print("Training data sample N: \n")
for i in range(5):
    N.append(d[i])    
    print("("+str(i)+"):" + str(N[i]))

#Comparamos con num vecinos ingresados
print("\n\n2. K vecinos mas cercanos: ")
for i in range(0,Vecinos):
    print("\n\n ("+str(i+1)+"): Vecino en posicion ("+ str(N[i][2])+") utiliza droga: ("+str(d[i][1]) +") Dist respecto a testing data: ("+str(d[i][0])+")")

print("\n\n 3. Dist vecino mas cercano: " + str( d[i][0]) + ". perteneciente a la clase: "+ str( d[0][1])+ " y se encuentra en la posicion del dataset original Numero: "+str(d[0][2]  ))

#if len(N) < k:
  #  for i in range (0,TotalElementos):     

#for i in range(k)
#    index = distances[i][1]
#tupla = pd.DataFrame([i,d,listaDrogas], index = ['index','DistEuclidiana', 'listaDrogas'])


    
   
