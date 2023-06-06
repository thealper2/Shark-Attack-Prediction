import streamlit as st
import pickle
import numpy as np
import pandas as pd

types = ['Boating', 'Invalid', 'Provoked', 'Sea Disaster', 'Unprovoked']
activities = ['Fishing', 'Other', 'Scuba diving', 'Snorkeling',
              'Spearfishing', 'Standing', 'Surfing', 'Swimming', 'Wading', 'boarding']
sex = ['F', 'M']
species = ['angel shark', 'blacktip reef', 'blacktip shark', 'blue shark',
 'bonita sharkk', 'bull shark', 'dogfish shark', 'foot shark',
 'galapagos shark', 'hammerhead shark', 'juvenile shark', 'juvenile tiger',
 'lb dog', 'lb reef', 'lb sand', 'lemon shark', 'mako shark', 'nurse shark',
 'reef shark', 'sand shark', 'sandbar shark', 'sandshark', 'sandtiger shark',
 'sevengill shark', 'shark species', 'shark with', 'sharks', 'spinner shark',
 'thresher', 'thresher shark', 'tiger shark', 'unidentified', 'unknown',
 'white shark']

model = pickle.load(open("rf.pkl", "rb"))

st.title("Shark Attack Prediction")
a1 = st.selectbox("Types", types)
a2 = st.selectbox("Activity", activities)
a3 = st.selectbox("Gender", sex)
a4 = st.number_input("Age")
a5 = st.selectbox("Species", species)

if st.button("Predict"):
    a1 = types.index(a1)
    a2 = activities.index(a2)
    a3 = sex.index(a3)
    a5 = species.index(a5)
    test = np.array([[a1, a2, a3, a4, a5]])
    res = model.predict(test)
    print(res)
    st.success("Is Attacked: " + str(res[0]))
