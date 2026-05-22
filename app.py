import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('penguins')

# Title
st.title('Penguins Dataset')

# =========================
# Scatter Plot
# =========================
st.subheader('Scatter Plot')

fig1, ax1 = plt.subplots()

sns.scatterplot(
    data=df,
    x='flipper_length_mm',
    y='body_mass_g',
    hue='species',
    ax=ax1
)
st.pyplot(fig1)
# Line Graph
st.subheader('Line Graph')
fig2, ax2 = plt.subplots()

# Average body mass by flipper length
line_data = df.groupby('flipper_length_mm')['body_mass_g'].mean()

ax2.plot(line_data.index, line_data.values)

ax2.set_xlabel('Flipper Length (mm)')
ax2.set_ylabel('Average Body Mass (g)')
ax2.set_title('Flipper Length vs Average Body Mass')

st.pyplot(fig2)