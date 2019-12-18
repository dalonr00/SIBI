# -*- coding: utf-8 -*-

#Consultar a la base de datos
from neo4j import GraphDatabase
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "dani"))
    
import sys
import os
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageFont
from random import randint, uniform,random

raiz = Tk()

raiz.title("Películas")
raiz.resizable(width=False, height=False)  # raiz.resizable(0, 0)
raiz.geometry("850x800")
raiz.config(bg="grey")

aleatorio = randint(1, 12)

imagen = Image.open("C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Fondos\\"+str(aleatorio)+".jpg")
imagen_de_fondo = ImageTk.PhotoImage(imagen)
fondo = tk.Label(raiz, image=imagen_de_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)


vecGen = []
vecDir = []
vecAct = []
vecPais = []
vecGuion = []
final = []
libro = []
    
#Funciones
def generos():
    vector = []
    with driver.session() as session:
        for record in session.run("MATCH (g:Genre)"
                                  "RETURN g.type"):
                                vector.append(record["g.type"])
    return vector


def director():
    vector2 = []
    vector = []
    with driver.session() as session:
        i = 0
        for record in session.run("MATCH (m:Movie)"
                                  "RETURN m.director"):
                                
                                vector.append(record["m.director"])
                                vector2.append(str(vector[i]).split(", "))
                                i=i+1
                                                                
    return vector2
def actor(): 
    vector2 = []
    vector = []
    with driver.session() as session:
        i = 0
        for record in session.run("MATCH (m:Movie)"
                                  "RETURN m.actores"):
                                
                                vector.append(record["m.actores"])
                                vector2.append(str(vector[i]).split(", "))
                                i=i+1
                                                                
    return vector2
    
def pais():
    vector = []
    with driver.session() as session:
        for record in session.run("MATCH (m:Movie)"
                                  "RETURN m.pais"):
                                vector.append(record["m.pais"])
    return vector

def guion():
    vector2 = []
    vector = []
    with driver.session() as session:
        i = 0
        for record in session.run("MATCH (m:Movie)"
                                  "RETURN m.guion"):
                                
                                vector.append(record["m.guion"])
                                vector2.append(str(vector[i]).split(", "))
                                i=i+1
                                                                
    return vector2

raiz.combo = ttk.Combobox(raiz, state='readonly')
raiz.combo2 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo5 = ttk.Combobox(raiz, state='readonly')
raiz.combo6 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo7 = ttk.Combobox(raiz, state='readonly')
raiz.combo8 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo9 = ttk.Combobox(raiz, state='readonly')
raiz.combo10 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo11 = ttk.Combobox(raiz, state='readonly')
raiz.combo12= ttk.Combobox(raiz, state='readonly', width = 30)



def aceptar():
    
    if raiz.combo.get()!="":
        if raiz.combo.get()=="Género":
            vecGen = generos()
            raiz.combo2.place(x=410, y=25)
            raiz.combo2["values"]=vecGen
        
        elif raiz.combo.get()=="Director":
            vecDir=director()
            raiz.combo2.place(x=410, y=25)
            directores=[]
          
            for i in range(len(vecDir)):
                for j in range (len(vecDir[i])):
                    repe = 0
                    for z in range(len(directores)):         
                        if(directores[z]==vecDir[i][j]):
                            repe=1
                    if repe==0:
                        directores.append(vecDir[i][j])
                        
                    
            raiz.combo2["values"]=directores
       
        
        elif raiz.combo.get()=="Actor":
            vecAct=actor()
            raiz.combo2.place(x=410, y=25)
            actores=[]
          
            for i in range(len(vecAct)):
                for j in range (len(vecAct[i])):
                    repe = 0
                    for z in range(len(actores)):         
                        if(actores[z]==vecAct[i][j]):
                            repe=1
                    if repe==0:
                        actores.append(vecAct[i][j])
                        
                    
            raiz.combo2["values"]=actores
            
            
        elif raiz.combo.get()=="País":
            vecPais=pais()
            raiz.combo2.place(x=410, y=25)
            paises=[]
          
            for i in range(len(vecPais)):
                repe = 0
                for z in range(len(paises)):         
                    if(paises[z]==vecPais[i]):
                        repe=1
                if repe==0:
                    paises.append(vecPais[i])
                        
                    
                    raiz.combo2["values"]=paises
            
            
        elif raiz.combo.get()=="Guionista":
            vecGuion=guion()
            raiz.combo2.place(x=410, y=25)
            guionista=[]
          
            for i in range(len(vecGuion)):
                for j in range (len(vecGuion[i])):
                    repe = 0
                    for z in range(len(guionista)):         
                        if(guionista[z]==vecGuion[i][j]):
                            repe=1
                    if repe==0:
                        guionista.append(vecGuion[i][j])
                        
                    
            raiz.combo2["values"]=guionista

    else:
        messagebox.showerror("Error", "No se ha seleccionado ninguna opción.")


def aceptar2():
    
    if raiz.combo5.get()!="":
        if raiz.combo5.get()=="Género":
            vecGen = generos()
            raiz.combo6.place(x=410, y=65)
            raiz.combo6["values"]=vecGen
        
        elif raiz.combo5.get()=="Director":
            vecDir=director()
            raiz.combo6.place(x=410, y=65)
            directores=[]
          
            for i in range(len(vecDir)):
                for j in range (len(vecDir[i])):
                    repe = 0
                    for z in range(len(directores)):         
                        if(directores[z]==vecDir[i][j]):
                            repe=1
                    if repe==0:
                        directores.append(vecDir[i][j])
                        
                    
            raiz.combo6["values"]=directores
       
        
        elif raiz.combo5.get()=="Actor":
            vecAct=actor()
            raiz.combo6.place(x=410, y=65)
            actores=[]
          
            for i in range(len(vecAct)):
                for j in range (len(vecAct[i])):
                    repe = 0
                    for z in range(len(actores)):         
                        if(actores[z]==vecAct[i][j]):
                            repe=1
                    if repe==0:
                        actores.append(vecAct[i][j])
                        
                    
            raiz.combo6["values"]=actores
            
            
        elif raiz.combo5.get()=="País":
            vecPais=pais()
            raiz.combo6.place(x=410, y=65)
            paises=[]
          
            for i in range(len(vecPais)):
                repe = 0
                for z in range(len(paises)):         
                    if(paises[z]==vecPais[i]):
                        repe=1
                if repe==0:
                    paises.append(vecPais[i])
                        
                    
                    raiz.combo6["values"]=paises
            
            
        elif raiz.combo5.get()=="Guionista":
            vecGuion=guion()
            raiz.combo6.place(x=410, y=65)
            guionista=[]
          
            for i in range(len(vecGuion)):
                for j in range (len(vecGuion[i])):
                    repe = 0
                    for z in range(len(guionista)):         
                        if(guionista[z]==vecGuion[i][j]):
                            repe=1
                    if repe==0:
                        guionista.append(vecGuion[i][j])
                        
                    
            raiz.combo6["values"]=guionista


            
    else:
        messagebox.showerror("Error", "No se ha seleccionado ninguna opción.")
        
         
        
def aceptar3():
    
    if raiz.combo7.get()!="":
        if raiz.combo7.get()=="Género":
            vecGen = generos()
            raiz.combo8.place(x=410, y=105)
            raiz.combo8["values"]=vecGen
        
        elif raiz.combo7.get()=="Director":
            vecDir=director()
            raiz.combo8.place(x=410, y=105)
            directores=[]
          
            for i in range(len(vecDir)):
                for j in range (len(vecDir[i])):
                    repe = 0
                    for z in range(len(directores)):         
                        if(directores[z]==vecDir[i][j]):
                            repe=1
                    if repe==0:
                        directores.append(vecDir[i][j])
                        
                    
            raiz.combo8["values"]=directores
       
        
        elif raiz.combo7.get()=="Actor":
            vecAct=actor()
            raiz.combo8.place(x=410, y=105)
            actores=[]
          
            for i in range(len(vecAct)):
                for j in range (len(vecAct[i])):
                    repe = 0
                    for z in range(len(actores)):         
                        if(actores[z]==vecAct[i][j]):
                            repe=1
                    if repe==0:
                        actores.append(vecAct[i][j])
                        
                    
            raiz.combo8["values"]=actores
            
            
        elif raiz.combo7.get()=="País":
            vecPais=pais()
            raiz.combo8.place(x=410, y=105)
            paises=[]
          
            for i in range(len(vecPais)):
                repe = 0
                for z in range(len(paises)):         
                    if(paises[z]==vecPais[i]):
                        repe=1
                if repe==0:
                    paises.append(vecPais[i])
                        
                    
                    raiz.combo8["values"]=paises
            
            
        elif raiz.combo7.get()=="Guionista":
            vecGuion=guion()
            raiz.combo8.place(x=410, y=105)
            guionista=[]
          
            for i in range(len(vecGuion)):
                for j in range (len(vecGuion[i])):
                    repe = 0
                    for z in range(len(guionista)):         
                        if(guionista[z]==vecGuion[i][j]):
                            repe=1
                    if repe==0:
                        guionista.append(vecGuion[i][j])
                        
                    
            raiz.combo8["values"]=guionista


            
    else:
        messagebox.showerror("Error", "No se ha seleccionado ninguna opción.")
        
       

def aceptar4():
    
    if raiz.combo9.get()!="":
        if raiz.combo9.get()=="Género":
            vecGen = generos()
            raiz.combo10.place(x=410, y=145)
            raiz.combo10["values"]=vecGen
        
        elif raiz.combo9.get()=="Director":
            vecDir=director()
            raiz.combo10.place(x=410, y=145)
            directores=[]
          
            for i in range(len(vecDir)):
                for j in range (len(vecDir[i])):
                    repe = 0
                    for z in range(len(directores)):         
                        if(directores[z]==vecDir[i][j]):
                            repe=1
                    if repe==0:
                        directores.append(vecDir[i][j])
                        
                    
            raiz.combo10["values"]=directores
       
        
        elif raiz.combo9.get()=="Actor":
            vecAct=actor()
            raiz.combo10.place(x=410, y=145)
            actores=[]
          
            for i in range(len(vecAct)):
                for j in range (len(vecAct[i])):
                    repe = 0
                    for z in range(len(actores)):         
                        if(actores[z]==vecAct[i][j]):
                            repe=1
                    if repe==0:
                        actores.append(vecAct[i][j])
                        
                    
            raiz.combo10["values"]=actores
            
            
        elif raiz.combo9.get()=="País":
            vecPais=pais()
            raiz.combo10.place(x=410, y=145)
            paises=[]
          
            for i in range(len(vecPais)):
                repe = 0
                for z in range(len(paises)):         
                    if(paises[z]==vecPais[i]):
                        repe=1
                if repe==0:
                    paises.append(vecPais[i])
                        
                    
                    raiz.combo10["values"]=paises
            
            
        elif raiz.combo9.get()=="Guionista":
            vecGuion=guion()
            raiz.combo10.place(x=410, y=145)
            guionista=[]
          
            for i in range(len(vecGuion)):
                for j in range (len(vecGuion[i])):
                    repe = 0
                    for z in range(len(guionista)):         
                        if(guionista[z]==vecGuion[i][j]):
                            repe=1
                    if repe==0:
                        guionista.append(vecGuion[i][j])
                        
                    
            raiz.combo10["values"]=guionista


            
    else:
        messagebox.showerror("Error", "No se ha seleccionado ninguna opción.")
        
        
        
def aceptar5():
    
    if raiz.combo11.get()!="":
        if raiz.combo11.get()=="Género":
            vecGen = generos()
            raiz.combo12.place(x=410, y=185)
            raiz.combo12["values"]=vecGen
        
        elif raiz.combo11.get()=="Director":
            vecDir=director()
            raiz.combo12.place(x=410, y=185)
            directores=[]
          
            for i in range(len(vecDir)):
                for j in range (len(vecDir[i])):
                    repe = 0
                    for z in range(len(directores)):         
                        if(directores[z]==vecDir[i][j]):
                            repe=1
                    if repe==0:
                        directores.append(vecDir[i][j])
                        
                    
            raiz.combo12["values"]=directores
       
        
        elif raiz.combo11.get()=="Actor":
            vecAct=actor()
            raiz.combo12.place(x=410, y=185)
            actores=[]
          
            for i in range(len(vecAct)):
                for j in range (len(vecAct[i])):
                    repe = 0
                    for z in range(len(actores)):         
                        if(actores[z]==vecAct[i][j]):
                            repe=1
                    if repe==0:
                        actores.append(vecAct[i][j])
                        
                    
            raiz.combo12["values"]=actores
            
            
        elif raiz.combo11.get()=="País":
            vecPais=pais()
            raiz.combo12.place(x=410, y=185)
            paises=[]
          
            for i in range(len(vecPais)):
                repe = 0
                for z in range(len(paises)):         
                    if(paises[z]==vecPais[i]):
                        repe=1
                if repe==0:
                    paises.append(vecPais[i])
                        
                    
                    raiz.combo12["values"]=paises
            
            
        elif raiz.combo11.get()=="Guionista":
            vecGuion=guion()
            raiz.combo12.place(x=410, y=185)
            guionista=[]
          
            for i in range(len(vecGuion)):
                for j in range (len(vecGuion[i])):
                    repe = 0
                    for z in range(len(guionista)):         
                        if(guionista[z]==vecGuion[i][j]):
                            repe=1
                    if repe==0:
                        guionista.append(vecGuion[i][j])
                        
                    
            raiz.combo12["values"]=guionista


            
    else:
        messagebox.showerror("Error", "No se ha seleccionado ninguna opción.")
        

def buscar():
    true=0
    vector = []
    coeficientes = []
    orden = 0
    pelicula = [""]
    
    if raiz.combo.get()=="Género":  
        var=raiz.combo2.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)-[Type_Of_Film]-(g:Genre{type:'"+str(var)+"'})"
                                      "RETURN m.title"):
                vector.append(record["m.title"])
                coeficientes.append(1)
                                    
    if raiz.combo.get()=="Director":  
        var=raiz.combo2.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.director='"+str(var)+"'"
                                      "RETURN m.title"):
                vector.append(record["m.title"])
                coeficientes.append(1)
                                    
    if raiz.combo.get()=="Actor":  
        var=raiz.combo2.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.actores CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                vector.append(record["m.title"])
                coeficientes.append(1)
                                    
                                    
    if raiz.combo.get()=="País":  
        var=raiz.combo2.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.pais='"+str(var)+"'"
                                      "RETURN m.title"):
                vector.append(record["m.title"])
                coeficientes.append(1)


    if raiz.combo.get()=="Guionista":  
        var=raiz.combo2.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.guion CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                vector.append(record["m.title"])
                coeficientes.append(1)
 

################################### COMBO2 ##############################################                         
                                    
    if raiz.combo5.get()=="Género":  
        var=raiz.combo6.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)-[Type_Of_Film]-(g:Genre{type:'"+str(var)+"'})"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.8
                        true=1
                    else:
                        true=0
                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.8)
                true=0

                                
    if raiz.combo5.get()=="Director":
        var=raiz.combo6.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.director='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.8
                        true=1
                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.8)
                true=0

                                    
                                    
    if raiz.combo5.get()=="Actor":  
        var=raiz.combo6.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.actores CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.8
                        true=1
                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.8)
                true=0                   
                                    
                                    
    if raiz.combo5.get()=="País":  
        var=raiz.combo6.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.pais='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.8
                        true=1
                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.8)
                true=0


    if raiz.combo5.get()=="Guionista":  
        var=raiz.combo6.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.guion CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.8
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.8)
                true=0                  



######################################### COMBO3 #############################################

                                    
    if raiz.combo7.get()=="Género":  
        var=raiz.combo8.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)-[Type_Of_Film]-(g:Genre{type:'"+str(var)+"'})"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.6                        
                        true=1
                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.6)                                                      
                true=0                   
                                    
    if raiz.combo7.get()=="Director":  
        var=raiz.combo8.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.director='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.6                        
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.6)                                                      
                true=0                     
                                    
    if raiz.combo7.get()=="Actor":  
        var=raiz.combo8.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.actores CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.6
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.6)
                true=0                    
                                    
    if raiz.combo7.get()=="País":  
        var=raiz.combo8.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.pais='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.6
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.6)                    
                true=0                    

    if raiz.combo7.get()=="Guionista":  
        var=raiz.combo8.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.guion CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.6
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.6)
                true=0



####################################### COMBO4 ################################################

                                    
    if raiz.combo9.get()=="Género":  
        var=raiz.combo10.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)-[Type_Of_Film]-(g:Genre{type:'"+str(var)+"'})"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.4
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.4)
                true=0

    if raiz.combo9.get()=="Director":  
        var=raiz.combo10.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.director='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.4
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.4)
                true=0                                    
                                    
    if raiz.combo9.get()=="Actor":  
        var=raiz.combo10.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.actores CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.4
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.4)
                true=0

    if raiz.combo9.get()=="País":  
        var=raiz.combo10.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.pais='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.4
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.4)
                true=0


    if raiz.combo9.get()=="Guionista":  
        var=raiz.combo10.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.guion CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.4
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.4)
                true=0

 

############################################# COMBO 5 ###############################################

                           
    if raiz.combo11.get()=="Género":  
        var=raiz.combo12.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)-[Type_Of_Film]-(g:Genre{type:'"+str(var)+"'})"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.2
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.2)
                true=0
                                    
    if raiz.combo11.get()=="Director":  
        var=raiz.combo12.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.director='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.2
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.2)
                true=0
                    
                                                                        
    if raiz.combo11.get()=="Actor":  
        var=raiz.combo12.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.actores CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.2
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.2)
                true=0
        

    if raiz.combo11.get()=="País":  
        var=raiz.combo12.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.pais='"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.2
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.2)
                true=0
                                    

    if raiz.combo11.get()=="Guionista":  
        var=raiz.combo12.get()
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                      "WHERE m.guion CONTAINS '"+str(var)+"'"
                                      "RETURN m.title"):
                for i in range (len(vector)):
                    if vector[i]==record["m.title"]:
                        coeficientes[i]=coeficientes[i]+0.2
                        true=1

                if true==0:
                    vector.append(record["m.title"])
                    coeficientes.append(0.2)
                true=0

########################################## FINAL ##################################################
    
    for i in range(len(vector)):                                
        if(orden<coeficientes[i]):
            orden=coeficientes[i]
            pelicula[0]=vector[i]
            
            
    final.append(pelicula[0])
    
    
    if(final[0]==""):
        messagebox.showerror("Error", "Introduce algún criterio")
        nueva()
    

    valoraciones = []
    valoraciones2 = []    
    
    with driver.session() as session:
        i = 0
        for record in session.run("MATCH (m:Movie)"
                                  "WHERE m.title = '"+str(final[0])+"'"
                                  "RETURN m.critica"):
                                
            valoraciones.append(record["m.critica"])
            valoraciones2.append(str(valoraciones[i]).split(", "))
            i=i+1
    
    valoraciones3 = []                
    valoraciones3.append(cambio(valoraciones2, 0, valoraciones3))
        
    critica = 0.0
    
    for i in range(3):
        critica=critica+float(valoraciones3[i])
    critica=round(critica/3, 2)

    raiz.label=ttk.Label(raiz)
    raiz.label.place(x=65, y=285 )
    raiz.label.config(text="Según los criterios introducidos, la película que recomendamos es: " + final[0])
    raiz.label.config(font="Verdana 9 italic bold")
    
    
    raiz.label2=ttk.Label(raiz)
    raiz.label2.place(x=65, y=515)
    raiz.label2.config(text="La valoración media de esta película es: "+ str(critica))
    raiz.label2.config(font="Verdana 9 italic bold")
    
    raiz.combo.config(state="disabled")
    raiz.combo5.config(state="disabled")
    raiz.combo7.config(state="disabled")
    raiz.combo9.config(state="disabled")
    raiz.combo11.config(state="disabled")
    

    
    
################################### IMAGEN PELICULA #############################################

    path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Peliculas\\'+ str(final[0]) + ".jpg"
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    img = ttk.Label(raiz, image=render)
    img.image = render
    img.place(x=295 , y=315)


#################################### LIBRO #############################################

    escritor = []
    with driver.session() as session:
        for record in session.run("MATCH (m:Movie)-[Basado_En]-(l:Libro)"
                                   "WHERE m.title='"+str(final[0])+"'"
                                   "RETURN l.titulo"):
            libro.append(record["l.titulo"])
  
          
    with driver.session() as session:
        for record in session.run("MATCH (m:Movie)-[Basado_En]-(l:Libro)"
                                   "WHERE m.title='"+str(final[0])+"'"
                                   "RETURN l.escritor"):
            escritor.append(record["l.escritor"])
            
    
    raiz.label3=ttk.Label(raiz)
    raiz.label3.place(x=65, y=550)
    raiz.label3.config(text="La película está basada en el libro " + libro[0] + " de " + escritor[0])
    raiz.label3.config(font="Verdana 9 italic bold")           
 

################################### IMAGEN LIBRO ############################################
    path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Libros\\'+ str(libro[0]) + ".jpg"
    load2 = Image.open(path)
    render = ImageTk.PhotoImage(load2)
    img = ttk.Label(raiz, image=render)
    img.image = render
    img.place(x=295 , y=585)
    
    
    
    
##################################### INFORMACIÓN PELICULA ###########################################
    
    def infopeli():

    
        info = tk.Toplevel(raiz)
    
        info.title("Películas")
        info.resizable(width=False, height=False)  
        info.geometry("1000x600")
        info.config(bg="grey")
        
        titulo=[]
        prota=[]
        crit=[]
        direc=[]
        guion=[]
        pais=[]
        gen = []
            
        imagenFondo = Image.open("C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Fondos\\"+str(aleatorio)+".jpg")
        imagenFondo = imagenFondo.resize((1000, 600), Image.ANTIALIAS)
        imagen_de_fondo = ImageTk.PhotoImage(imagenFondo)
        fondo = tk.Label(info, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        with driver.session() as session:
            for record in session.run("MATCH (m:Movie)"
                                       "WHERE m.title='"+str(final[0])+"'"
                                       "RETURN m.title, m.actores, m.critica, m.director, m.guion, m.pais"):
                titulo.append(record["m.title"])
                prota.append(record["m.actores"])
                crit.append(record["m.critica"])
                direc.append(record["m.director"])
                guion.append(record["m.guion"])
                pais.append(record["m.pais"])
        
        
        
        with driver.session() as session:
            for g in session.run("MATCH (m:Movie)-[Type_Of_Film]-(g:Genre)"
                                 "WHERE m.title='"+str(final[0])+"'"
                                 "RETURN g.type"):
                    gen.append(g["g.type"])
                        
        
        info.label1=ttk.Label(info)
        info.label1.place(x=425, y=50 )
        info.label1.config(text=final[0])
        info.label1.config(font="Arial 25 bold") 
        
        info.label2=ttk.Label(info)
        info.label2.place(x=425, y=115 )
        info.label2.config(text="Director: "+direc[0])
        info.label2.config(font="Arial 10 bold")
        
        info.label3=ttk.Label(info)
        info.label3.place(x=425, y=155 )
        info.label3.config(text="País: "+pais[0])
        info.label3.config(font="Arial 10 bold")
        
        info.label4=ttk.Label(info)
        info.label4.place(x=425, y=195 )
        info.label4.config(text="Actores principales: "+prota[0])
        info.label4.config(font="Arial 10 bold")
        
        info.label5=ttk.Label(info)
        info.label5.place(x=425, y=235 )
        info.label5.config(text="Valoraciones: "+crit[0])
        info.label5.config(font="Arial 10 bold")
        
        info.label6=ttk.Label(info)
        info.label6.place(x=425, y=275 )
        info.label6.config(text="Valoracion media: "+str(critica)+"   ")
        info.label6.config(font="Arial 10 bold")
        
        info.label7=ttk.Label(info)
        info.label7.place(x=425, y=355 )
        info.label7.config(text="Genero: "+gen[0])
        info.label7.config(font="Arial 10 bold")
        
        if(critica<=2):
            path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Estrellas\\1.jpg'
            load = Image.open(path)
            load = load.resize((84, 16), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = ttk.Label(info, image=render)
            img.image = render
            img.place(x=560 , y=275)
            
        elif(critica>2 and critica<=4):
            path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Estrellas\\2.jpg'
            load = Image.open(path)
            load = load.resize((84, 16), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = ttk.Label(info, image=render)
            img.image = render
            img.place(x=560 , y=275)
            
        elif(critica>4 and critica<=6):
            path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Estrellas\\3.jpg'
            load = Image.open(path)
            load = load.resize((84, 16), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = ttk.Label(info, image=render)
            img.image = render
            img.place(x=560 , y=275)
            
        elif(critica>6 and critica<=8):
            path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Estrellas\\4.jpg'
            load = Image.open(path)
            load = load.resize((84, 16), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = ttk.Label(info, image=render)
            img.image = render
            img.place(x=560 , y=275)
            
        else:
            path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Estrellas\\5.jpg'
            load = Image.open(path)
            load = load.resize((84, 16), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = ttk.Label(info, image=render)
            img.image = render
            img.place(x=580 , y=275)
    
        info.label=ttk.Label(info)
        info.label.place(x=425, y=315 )
        info.label.config(text="Guionista: "+guion[0])
        info.label.config(font="Arial 10 bold")
        
            
        
        path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Peliculas\\'+ str(final[0]) + ".jpg"
        load = Image.open(path)
        load = load.resize((350, 495), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(info, image=render)
        img.image = render
        img.place(x=50 , y=50)
        
        path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Banderas\\'+ str(pais[0]) + ".jpg"
        load = Image.open(path)
        load = load.resize((85, 59), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(info, image=render)
        img.image = render
        img.place(x=50 , y=50)
        
        info.mainloop()
    
    raiz.Button9 = ttk.Button(raiz, command=infopeli, text = "INFORMACIÓN")
    raiz.Button9.place(x=455, y=335)
    
    
    
    
    
    ##################################### INFORMACIÓN LIBRO ###########################################
    
    def infolibro():

    
        info = tk.Toplevel(raiz)
    
        info.title("Libro")
        info.resizable(width=True, height=True)  
        info.geometry("950x600")
        info.config(bg="grey")
        
        titulo=[]
        escrit=[]
        pais=[]
            
        imagenFondo = Image.open("C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Fondos\\"+str(aleatorio)+".jpg")
        imagenFondo = imagenFondo.resize((950, 600), Image.ANTIALIAS)
        imagen_de_fondo = ImageTk.PhotoImage(imagenFondo)
        imagen_de_fondo = ImageTk.PhotoImage(imagenFondo)
        fondo = tk.Label(info, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        with driver.session() as session:
            for record in session.run("MATCH (l:Libro)"
                                       "WHERE l.titulo='"+str(final[0])+"'"
                                       "RETURN l.titulo, l.escritor, l.pais"):
                titulo.append(record["l.titulo"])
                escrit.append(record["l.escritor"])
                pais.append(record["l.pais"])
                
        
        info.label=ttk.Label(info)
        info.label.place(x=425, y=50 )
        info.label.config(text=libro[0])
        info.label.config(font="Arial 25 bold") 
        
        info.label=ttk.Label(info)
        info.label.place(x=425, y=115 )
        info.label.config(text="Escritor: "+escrit[0])
        info.label.config(font="Arial 10 bold")
        
        info.label=ttk.Label(info)
        info.label.place(x=425, y=155 )
        info.label.config(text="País: "+pais[0])
        info.label.config(font="Arial 10 bold")
        
            
        
        path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Libros\\'+ str(final[0]) + ".jpg"
        load = Image.open(path)
        load = load.resize((350, 495), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(info, image=render)
        img.image = render
        img.place(x=50 , y=50)
        
        path = 'C:\\Users\\dalon\\Documents\\Daniel\\Clase\\SistemasBI\\Fotos\\Banderas\\'+ str(pais[0]) + ".jpg"
        load = Image.open(path)
        load = load.resize((85, 59), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(info, image=render)
        img.image = render
        img.place(x=50 , y=50)
        
        info.mainloop()
    
    raiz.Button9 = ttk.Button(raiz, command=infolibro, text = "INFORMACIÓN")
    raiz.Button9.place(x=455, y=615)
    
    
################################### FUNCIONES ##############################################

def nueva():
    python=sys.executable
    os.execl(python, python, * sys.argv)
    
def cambio(valoraciones2, z, valoraciones3):
    auxiliar=[]
    if(z<3):
        auxiliar=valoraciones2[0][z].replace("'", ".")
        valoraciones3.append(auxiliar)
        z=z+1
        cambio(valoraciones2, z, valoraciones3)
            
   
    
######################################## BOTONES ##########################################

raiz.Button = ttk.Button(raiz, command=aceptar, text = "Aceptar")
raiz.Button.place(x=295, y=25)

raiz.Button2 = ttk.Button(raiz, command=aceptar2, text = "Aceptar")
raiz.Button2.place(x=295, y=65)

raiz.Button3 = ttk.Button(raiz, command=aceptar3, text = "Aceptar")
raiz.Button3.place(x=295, y=105)

raiz.Button4 = ttk.Button(raiz, command=aceptar4, text = "Aceptar")
raiz.Button4.place(x=295, y=145)

raiz.Button5 = ttk.Button(raiz, command=aceptar5, text = "Aceptar")
raiz.Button5.place(x=295, y=185)

raiz.Button7 = ttk.Button(raiz, command=buscar, text = "BUSCAR")
raiz.Button7.place(x=245, y=225)

raiz.Button8 = ttk.Button(raiz, command=nueva, text = "NUEVA BÚSQUEDA")
raiz.Button8.place(x=345, y=225)




###################################### COMBOBOX #############################################
raiz.combo.place(x=115, y=25)
raiz.combo["values"]=["Género", "Director", "Actor", "País", "Guionista"]

raiz.combo5.place(x=115, y=65)
raiz.combo5["values"]=["Género", "Director", "Actor", "País", "Guionista"]

raiz.combo7.place(x=115, y=105)
raiz.combo7["values"]=["Género", "Director", "Actor", "País", "Guionista"]

raiz.combo9.place(x=115, y=145)
raiz.combo9["values"]=["Género", "Director", "Actor", "País", "Guionista"]

raiz.combo11.place(x=115, y=185)
raiz.combo11["values"]=["Género", "Director", "Actor", "País", "Guionista"]


raiz.mainloop() 