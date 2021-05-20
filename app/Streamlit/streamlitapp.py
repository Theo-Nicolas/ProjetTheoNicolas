import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd

client = pymongo.MongoClient('mongodb_project', 27017)
db = client['mycoin']
collection = db['coin_tb']
st.title("""Le site des crypto""")

def nettoyage(x):
    return(x[2:-2])
def nettoyagechange(x):
    return(x[2:-3])


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

z = st.multiselect('Select crypto', listcrypto)
dftableau=pd.DataFrame(columns =['Nom', 'Prix', 'Changement sur 24h', 'MarketCap', 'Volume 24h', 'Offre disponible'])
for x in z:
    nom=collection.find_one({'nom':x})['nom']
    prix=collection.find_one({'nom':x})['prix']
    change=collection.find_one({'nom':x})['change']
    marketcap=collection.find_one({'nom':x})['marketcap']
    vol24h=collection.find_one({'nom':x})['vol24h']
    offredispo=collection.find_one({'nom':x})['offredispo']
    tableau={'Nom':nom, 'Prix':prix, 'Changement sur 24h':change, 'MarketCap':marketcap, 'Volume 24h':vol24h, 'Offre disponible':offredispo }
    dftableau = dftableau.append(tableau, ignore_index=True)
st.table(dftableau)
    #st.write(collection.find_one({'nom':x}))
monnaie=[]
MonnaieTot=0
beneficeTot=0
for x in z:
    monnaie.append([x,st.text_input("Enter Your number of "+str(x)+' : ')])
for j in monnaie:
    if j[1]!='':
        #chan24h = float(nettoyagechange(collection.find_one({'nom':j[0]})['change']))
        prixactu = collection.find_one({'nom':j[0]})['prix'][0][1:]
        change24 = collection.find_one({'nom':j[0]})['change'][0][1:]
        res=''
        for i in range(len(prixactu)):
            if prixactu[i] ==" ":
                res+=""
            else:
                res+=prixactu[i]
        prixactu=res
        res=''
        for i in range(len(change24)):
            if change24[i] ==" ":
                res+=""
            elif change24[i]=="%":
                res+=""
            else:
                res+=change24[i]
        change24=res

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