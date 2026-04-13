import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np
import locale

# 📅 Localisation en français
locale.setlocale(locale.LC_TIME, 'French_France.1252')

# Paramètres de la nuit simulée
sunset = datetime.strptime("2025-06-23 21:30", "%Y-%m-%d %H:%M")
sunrise = datetime.strptime("2025-06-24 05:30", "%Y-%m-%d %H:%M")

# Création de l'axe temporel (toutes les 15 minutes)
times = [sunset + timedelta(minutes=15 * i) for i in range(int((sunrise - sunset).total_seconds() // (15 * 60)))]

# Simuler une activité acoustique (pic d'activité vers minuit)
activity = [np.exp(-0.5*((((t - sunset).total_seconds()/3600 - 3)/1.2)**2)) * np.random.uniform(0.8, 1.2)
            for t in times]

# 🎨 Création du graphique
fig, ax = plt.subplots(figsize=(10, 4))

# Zone de nuit (barre horizontale)
ax.axhspan(0, 1.1, xmin=0, xmax=1, color="#22223b", alpha=0.6)

# Barres verticales d'activité
ax.bar(times, activity, width=0.01, color="#f2e9e4", align='center')

# Format de l’axe X : heures
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Hh'))
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.xticks(rotation=0, color="#f2e9e4")
plt.yticks([])  # pas d’axe Y

# Esthétique
ax.set_facecolor("#4a4e69")
fig.patch.set_facecolor('#4a4e69')
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xlim([sunset, sunrise])
ax.set_ylim([0, max(activity) * 1.1])

plt.tight_layout()
plt.show()
