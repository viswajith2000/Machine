import tkinter as tk 
from tkinter import*
import pandas as pd

knn=Tk()
knn.geometry("500x600")
knn.config(bg = 'SlateGray3')
knn.title("KNN Algorithm")

def flower():
    
    knn.destroy()
    alg=Tk()
    alg.geometry("500x600")
    alg.config(bg = 'SlateGray3')
    alg.title("KNN")



    L1=Label(alg,text="Flowers Classification",font=("times new roman",22),bg="green",fg="white").pack()
    L2= Label(alg,text="Sepal Length in cm",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=80)
    L3= Label(alg,text="Sepal Width in cm",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=120)
    L4= Label(alg,text="Petal Length in cm",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=160)
    L5= Label(alg,text="Petal Width in cm",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=200)
    L6= Label(alg,text="Predicted Result",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=280)



    sl=StringVar()
    sw=StringVar()
    pl=StringVar()
    pw=StringVar()

    sepallength=Entry(alg,text=sl,width=30)
    sepallength.place(x=200,y=80)
    sepalwidth=Entry(alg,text=sw,width=30)
    sepalwidth.place(x=200,y=120)
    petallength=Entry(alg,text=pl,width=30)
    petallength.place(x=200,y=160)
    petalwidth=Entry(alg,text=pw,width=30)
    petalwidth.place(x=200,y=200)


    def model():
        dataset=pd.read_csv("E:/MACHINE LEARNING ASSIGNMENT\Data Set\Iris_new.csv")
        x=dataset.iloc[:,0:4].values
        y=dataset.iloc[:,-1].values
        
        
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
        from sklearn.preprocessing import StandardScaler
        sc=StandardScaler()
        x_train=sc.fit_transform(x_train)
        x_test=sc.fit_transform(x_test)
        from sklearn.neighbors import KNeighborsClassifier
        Classifier=KNeighborsClassifier(n_neighbors=5,metric='euclidean')
        Classifier.fit(x,y)
        sl1=float(sl.get())
        sw1=float(sw.get())
        pl1=float(pl.get())
        pw1=float(pw.get())
        
        
        
        
        y_pred=Classifier.predict([[sl1,sw1,pl1,pw1]])
        print(y_pred)
        Label(alg,text=y_pred[0],font=("times new roman",18),bg="green",fg="black").place(x=200,y=280)
        
        
    def clearprediction():
        Label(alg,text=" "*30,font=("times new roman",18),bg="green",fg="white").place(x=200,y=280)

    def clear():
        sepallength.delete(0,END)
        sepalwidth.delete(0,END)
        petallength.delete(0,END)
        petalwidth.delete(0,END) 
        sepallength.focus_set()
     

    Button(alg,text="Prediction",width=18,command=model).place(x=40,y=350)
    Button(alg,text="Exit ",width=18,command=alg.destroy).place(x=200,y=400)
    Button(alg,text="Clear Prediction ",width=18,command=clearprediction).place(x=350,y=350)
    Button(alg,text="Delete Values ",width=18,command=clear).place(x=200,y=350)

    alg.resizable(0,0)
    alg.mainloop()
    
def car():
    knn.destroy()
    car=Tk()
    car.geometry("500x600")
    car.config(bg = 'SlateGray3')
    car.title("KNN")



    L1=Label(car,text="Car Prediction",font=("times new roman",22),bg="green",fg="white").pack()
    L2=Label(car,text="Number of Cylinder",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=80)
    L3=Label(car,text="Car Horse Power",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=120)
    L4=Label(car,text="Number of Gear",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=160)
    L5=Label(car,text="Time taken to rech 100",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=200)
    L6=Label(car,text="Predicted Result",font=("times new roman",10),bg="#F4F4F4",fg="black",width=18).place(x=40,y=280)



    nc=StringVar()
    hp=StringVar()
    ng=StringVar()
    tt=StringVar()

    cylinder=Entry(car,text=nc,width=30)
    cylinder.place(x=200,y=80)
    horsepower=Entry(car,text=hp,width=30)
    horsepower.place(x=200,y=120)
    gear=Entry(car,text=ng,width=30)
    gear.place(x=200,y=160)
    time=Entry(car,text=tt,width=30)
    time.place(x=200,y=200)


    def model():
       
        dataset=pd.read_csv("E:/MACHINE LEARNING ASSIGNMENT\Data Set\mtcars.csv")
        x=dataset.iloc[:,[2,4,10,12]].values
        y=dataset.iloc[:,[0]].values
        
        
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
        from sklearn.preprocessing import StandardScaler
        sc=StandardScaler()
        x_train=sc.fit_transform(x_train)
        x_test=sc.fit_transform(x_test)
        from sklearn.neighbors import KNeighborsClassifier
        Classifier=KNeighborsClassifier(n_neighbors=5,metric='euclidean')
        Classifier.fit(x,y)
        nc1=float(nc.get())
        hp1=float(hp.get())
        ng1=float(ng.get())
        tt1=float(tt.get())
        
        
        
        
        y_pred=Classifier.predict([[nc1,hp1,ng1,tt1]])
        print(y_pred)
        
        Label(car,text=y_pred[0],font=("times new roman",18),bg="green",fg="black").place(x=200,y=280)
      
    def clearprediction():
        Label(car,text=" "*30,font=("times new roman",18),bg="green",fg="white").place(x=200,y=280)

    def clear():
        cylinder.delete(0,END)
        horsepower.delete(0,END)
        gear.delete(0,END)
        time.delete(0,END) 
        cylinder.focus_set()
     

    Button(car,text="Prediction",width=18,command=model).place(x=40,y=350)
    Button(car,text="Exit ",width=18,command=car.destroy).place(x=200,y=400)
    Button(car,text="Clear Prediction ",width=18,command=clearprediction).place(x=350,y=350)
    Button(car,text="Delete Values ",width=18,command=clear).place(x=200,y=350)

    car.resizable(0,0)
    car.mainloop()



L1=Label(knn,text="KNN ALGORITHM",font=("times new roman",22),bg="green",fg="white")
L1.place(x=130,y=40)
L2=Label(knn,text="CHOOSE THE PREDICTION",font=("times new roman",12),bg="green",fg="white")
L2.place(x=150,y=100)
Button(knn,text="Flower Prediction",width=18,command=flower).place(x=180,y=150)
Button(knn,text="Car Prediction",width=18,command=car).place(x=180,y=200)
Button(knn,text="Exit ",width=18,command=knn.destroy).place(x=180,y=350)



knn.resizable(0,0)   
knn.mainloop()













