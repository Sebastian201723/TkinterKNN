from scipy.io import arff
import pandas as pd
import math
import operator
##PRE-PROCESAMIENTO DE BASE DE DATOS:
def lectura(Vecinos,TestingData):
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
        tupla= []
        d = []
        PRUEBA = []
        #Retornar lista con distancias

        for i in range(0,TotalElementos):
            cuadrados = math.pow(abs(listaEdad[i]-TestingData[0]),2) + math.pow(listaSexo[i]-TestingData[1],2) + math.pow(abs(listaBP[i]-TestingData[2]),2) + math.pow(listaCh[i]-TestingData[3],2) + math.pow(abs(listaNa[i]-TestingData[4]),2) + math.pow(abs(listaK[i]-TestingData[5]),2)
            distancias = [math.sqrt(cuadrados),listaDrogas[i],i]
            d.append(distancias)
            #d = [distancias,ListaDrogas,i]
            #d [i][distancias/ListaDrogas/i]
        d.sort()
        N = []
        for i in range(5):
            N.append(d[i])    
        for i in range(0,3):
            print("\n\n ("+str(i+1)+"): Vecino en posicion ("+ str(N[i][2])+") utiliza droga: ("+str(d[i][1]) +") Dist respecto a testing data: ("+str(d[i][0])+")")

        print("\n\n 3. Dist vecino mas cercano: " + str( d[0][0]) + ". perteneciente a la clase: "+ str( d[0][1])+ " y se encuentra en la posicion del dataset original Numero: "+str(d[0][2]  ))

        matriz = [listaEdad,listaSexo,listaCh,listaBP,listaNa,listaK, listaDrogas,N, d]
        return matriz
