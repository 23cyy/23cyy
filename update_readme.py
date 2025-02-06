#!/usr/bin/env python3
import datetime
import re

# Lire le contenu actuel du README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Calculer la date actuelle (pour "Last update")
now = datetime.datetime.now()
last_update = now.strftime("%a %b %d %Y")

# 2. Calculer le nombre de jours avant le Nouvel An
next_year = now.year + 1
new_year_date = datetime.datetime(next_year, 1, 1)
days_before_new_year = (new_year_date - now).days

# Remplacer les placeholders dans le contenu
content = re.sub(r'<!--LAST_UPDATE-->', last_update, content)
content = re.sub(r'<!--COUNTDOWN-->', str(days_before_new_year), content)

# Écrire le nouveau contenu dans README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
