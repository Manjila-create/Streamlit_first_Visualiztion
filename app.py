import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
st.title('Penguins Dataset')
fig, ax = plt.subplots()
sns.scatterplot( data=df,
    x='flipper_length_mm',
    y='body_mass_g',
    hue='species',
    ax=ax
)
st.pyplot(fig)