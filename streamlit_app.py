import streamlit as st
import pandas as pd
from apriori import runApriori, dataFromFile, to_str_results
import os
st.markdown("# Apriori Streamlit")

st.sidebar.markdown(
    """BIL MINI PROJECT :

> *Group Members :-*\n
> *Neha Bharambe*\n
> *Bryan Ronad*\n
> *Esther Chettiar*
"""
)

default_csv = st.selectbox(
    "Select one of the sample csv files", ("tesco.csv", "INTEGRATED-DATASET.csv","Apriori1.csv", "Grocery Products Purchase.csv")
)

csv_file = pd.read_csv(default_csv, header=None, lineterminator="\n")
st.write(csv_file[0].str.split("\,", expand=True).head())

st.markdown('---')
st.markdown("## Inputs")

st.markdown('''
            **Support** shows transactions with items purchased together in a single transaction.

            **Confidence** shows transactions where the items are purchased one after the other.''')

st.markdown('Support and Confidence for Itemsets A and B can be represented by formulas')

support_helper = ''' > Support(A) = (Number of transactions in which A appears)/(Total Number of Transactions') '''
confidence_helper = ''' > Confidence(A->B) = Support(AUB)/Support(A)') '''
st.markdown('---')

support = st.slider("Enter the Minimum Support Value", min_value=0.1,
                    max_value=0.9, value=0.15,
                    help=support_helper)

confidence = st.slider("Enter the Minimum Confidence Value", min_value=0.1,
                       max_value=0.9, value=0.6, help=confidence_helper)

inFile = dataFromFile(default_csv)

items, rules = runApriori(inFile, support, confidence)

i, r = to_str_results(items, rules)

st.markdown("## Results")

st.markdown("### Frequent Itemsets")
st.write(i)

st.markdown("### Frequent Rules")
st.write(r)