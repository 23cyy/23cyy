#!/usr/bin/env python3
import datetime
import re
import calendar  # Pour vérifier l'année bissextile

# Lire le contenu actuel du README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Calculer la date actuelle (pour "Last update")
now = datetime.datetime.now()
last_update = now.strftime("%a %b %d %Y")  # Exemple : "Wed Feb 05 2025"

# 2. Calculer le nombre de jours avant le Nouvel An
next_year = now.year + 1
new_year_date = datetime.datetime(next_year, 1, 1)
days_before_new_year = (new_year_date - now).days

# 3. Vérifier si l'année en cours est bissextile et définir un message
if calendar.isleap(now.year):
    leap_year_message = "C'est une année bissextile !"
else:
    leap_year_message = "Ce n'est pas une année bissextile."

# Remplacer les placeholders dans le contenu
content = re.sub(r'<!--LAST_UPDATE-->', last_update, content)
content = re.sub(r'<!--COUNTDOWN-->', str(days_before_new_year), content)
content = re.sub(r'<!--LEAP_YEAR_STATUS-->', leap_year_message, content)

# Écrire le nouveau contenu dans README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
