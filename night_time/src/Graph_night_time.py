import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import pytz
from astral.sun import sun
from astral import LocationInfo
import locale

locale.setlocale(locale.LC_TIME, 'French_France.1252')  # Pour Linux/macOS

# Configuration de la localisation (ex : Lyon, France)
city = LocationInfo("Niort", "France", "Europe/Paris", 46.3237, -0.4588)

# Génération des dates sur une année complète
dates = pd.date_range(start = "2025-01-01", end = "2025-12-31", freq = "D")

# Calcul de la durée de la nuit civile
night_durations = []

for date in dates:
    s = sun(city.observer, date=date)
    # On calcule la nuit civile comme la durée entre le coucher et le lever du soleil
    sunset = s['sunset']
    sunrise = s['sunrise'] + timedelta(days=1) if s['sunrise'] < sunset else s['sunrise']
    night_duration = (sunrise - sunset).total_seconds() / 3600  # en heures
    night_durations.append(night_duration)

# Création du DataFrame
df = pd.DataFrame({
    "Date": dates,
    "NightDuration": night_durations
})

# 📊 Tracé du graphique
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["NightDuration"], color="#f2e9e4", linewidth=2, label="")
plt.fill_between(df["Date"], df["NightDuration"], color="#22223b", alpha=0.7)

# 🎨 Personnalisation du graphique
plt.ylabel("Durée de la nuit", fontsize=12, color="#f2e9e4")
plt.grid(False)
plt.gca().set_facecolor("#4a4e69")
plt.gcf().patch.set_facecolor('#4a4e69')
plt.tick_params(colors='#f2e9e4')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# Supprimer les bordures
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
