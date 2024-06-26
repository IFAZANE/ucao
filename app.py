import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
# Générer des données aléatoires pour l'exemple
np.random.seed(0)
X_train = np.random.rand(100, 1) * 10
y_train = 3 * X_train ** 2 - 5 * X_train + 2 + np.random.randn(100, 1) * 5
# Entraîner le modèle
coefficients = np.polyfit(X_train.flatten(), y_train.flatten(), 2)
# Calculer le score du modèle
y_pred = np.polyval(coefficients, X_train.flatten())
r2 = r2_score(y_train, y_pred)
# Définir la page Streamlit
st.title('Déploiement de modèle avec Streamlit')
# Widget pour saisir une valeur d'entrée
input_value = st.slider('Valeur d\'entrée', min_value=0.0, max_value=10.0, step=0.1)
# Prédiction avec le modèle entraîné
prediction = np.polyval(coefficients, input_value)
# Affichage de la prédiction
st.write(f'Prédiction pour la valeur d\'entrée {input_value}: {prediction}')
# Affichage du score du modèle
st.write(f'Score du modèle (R²) : {r2:.4f}')
# Affichage du graphique interactif
st.subheader('Graphique interactif')
fig, ax = plt.subplots()
ax.plot(X_train, y_train, 'bo', label='Données d\'entraînement')
x_values = np.linspace(0, 10, 100)
y_values = np.polyval(coefficients, x_values)
ax.plot(x_values, y_values, 'r-', label='Modèle prédictif')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Régression quadratique')
ax.legend()
st.pyplot(fig)