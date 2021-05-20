import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

client = pymongo.MongoClient('mongodb_project', 27017)
db = client['mycoin']
collection = db['coin_tb']
st.title("""Calculateur pour les crypto-monnaies""")

def nettoyage(x):
    return(x[2:-2])
def nettoyagechange(x):
    return(x[2:-3])
def nettoyagecomplet(x):
    res=''
    t=1
    for i in range(len(x)):
            if x[i] =='0' or x[i] =='1'or x[i] =='2'or x[i] =='3'or x[i] =='4'or x[i] =='5'or x[i] =='6'or x[i] =='7'or x[i] =='8'or x[i] =='9'or x[i] =='.'or x[i] =='-':
                res+=x[i]
            elif x[i]=='B':
                t=1000000000
            elif x[i]=='M':
                t=1000000
    res=float(res)*t
    return res
cursor = collection.find()
listcrypto =[]
PNLTot =0
i=0
for cry in cursor:
    nom=str(cry['nom'])
    nom = nettoyage(nom)
    listcrypto.append(nom)
    change24h=nettoyagechange(str(cry['change']))
    if change24h!='':
        PNLTot+=float(change24h)
        i+=1

if st.checkbox('Affiche la tendance du jour'):
    
    if PNLTot<0:
        st.write("Le marché est en baisse de ",PNLTot/i,"%")
        image = 'app/Streamlit/image/cryptochute.jpg'
    else:
        st.write("Le marché est en hausse de ",PNLTot/i,"%")
        image = 'app/Streamlit/image/cryptomonte.jpg'

else:
    image = 'app/Streamlit/image/updown.png'
st.image(image, width=None)

z = st.multiselect('Choisir les crypto-monnaies', listcrypto)
dftableau=pd.DataFrame(columns =['Nom', 'Prix', 'Changement sur 24h', 'MarketCap', 'Volume 24h', 'Offre disponible'])
dftableaufloat=pd.DataFrame(columns =['Nom', 'Prix', 'Changement sur 24h', 'MarketCap', 'Volume 24h', 'Offre disponible'])
for x in z:
    nom=collection.find_one({'nom':x})['nom'][0]
    prix=collection.find_one({'nom':x})['prix'][0]
    change=collection.find_one({'nom':x})['change'][0]
    marketcap=collection.find_one({'nom':x})['marketcap'][0]
    vol24h=collection.find_one({'nom':x})['vol24h'][0]
    offredispo=collection.find_one({'nom':x})['offredispo'][0]
    tableau={'Nom':nom, 'Prix':prix, 'Changement sur 24h':change, 'MarketCap':marketcap, 'Volume 24h':vol24h, 'Offre disponible':offredispo }
    dftableau = dftableau.append(tableau, ignore_index=True)
    tableaufloat={'Nom':nom, 'Prix':float(nettoyagecomplet(prix)), 'Changement sur 24h':float(nettoyagecomplet(change)), 'MarketCap':float(nettoyagecomplet(marketcap)), 'Volume 24h':float(nettoyagecomplet(vol24h)), 'Offre disponible':float(nettoyagecomplet(offredispo)) }
    dftableaufloat = dftableaufloat.append(tableaufloat, ignore_index=True)
st.table(dftableau)
    #st.write(collection.find_one({'nom':x}))
monnaie=[]
MonnaieTot=0
beneficeTot=0
for x in z:
    monnaie.append([x,st.text_input("Ecrivez votre nombre de "+str(x)+' : ')])
for j in monnaie:
    if j[1]!='':
        #chan24h = float(nettoyagechange(collection.find_one({'nom':j[0]})['change']))
        prixactu = collection.find_one({'nom':j[0]})['prix'][0][1:]
        change24 = collection.find_one({'nom':j[0]})['change'][0][1:]

        prixactu=nettoyagecomplet(prixactu)
        change24=nettoyagecomplet(change24)
        prix24 = float(prixactu)*float(j[1])
        prixdebut = float(prixactu)*100/(100+float(change24))
        benefice = prix24-(prixdebut*float(j[1]))
        beneficeTot+=benefice
        MonnaieTot+=prix24
        st.write('Vous avez ',prix24,'€ de ',j[0])
st.write("Au total vous avez ",MonnaieTot,"€ de crypto")
if beneficeTot>0:
    st.write("Au total, vous avez un bénéfice sur 24h de ",beneficeTot,"€")
else:
    st.write("Au total, vous avez un déficit sur 24h de ",beneficeTot,"€")

selecteur = st.selectbox("Choississez le type de graphique :",['Prix','Changement sur 24h','MarketCap','Volume 24h','Offre disponible'])
fig = px.bar(dftableaufloat, x="Nom", y=selecteur, barmode="group")
st.plotly_chart(fig)
