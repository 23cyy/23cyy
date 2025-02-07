#!/usr/bin/env python3
import datetime
import re
import calendar
import random

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

now = datetime.datetime.now()
last_update = now.strftime("%a %b %d %Y")

next_year = now.year + 1
new_year_date = datetime.datetime(next_year, 1, 1)
days_before_new_year = (new_year_date - now).days

leap_year_message = "This is a leap year !" if calendar.isleap(now.year) else "This is not a leap year."
citation_du_jour = random.choice([
    "Life is beautiful.",
    "Success is a state of mind.",
    "Take action and anything is possible.",
    "Every day is a new chance."
])

# Mise à jour de la date de dernière modification
content = re.sub(
    r'(><!-- LAST_UPDATE_START -->\n)(.*?)(\n><!-- LAST_UPDATE_END -->)',
    r'\1> Last update on **' + last_update + r'**\3',
    content,
    flags=re.DOTALL
)

# Mise à jour du compte à rebours
content = re.sub(
    r'(><!-- COUNTDOWN_START -->\n)(.*?)(\n><!-- COUNTDOWN_END -->)',
    r'\1> **' + str(days_before_new_year) + r'** days before **' + str(next_year) + r'** ⏱\3',
    content,
    flags=re.DOTALL
)

# Mise à jour du statut d'année bissextile
content = re.sub(
    r'(><!-- LEAP_YEAR_STATUS_START -->\n)(.*?)(\n><!-- LEAP_YEAR_STATUS_END -->)',
    r'\1> **' + leap_year_message + r'**\3',
    content,
    flags=re.DOTALL
)

# Mise à jour de la citation
content = re.sub(
    r'(><!-- QUOTE_START -->\n)(.*?)(\n><!-- QUOTE_END -->)',
    r'\1> **Quote of the day** : *' + citation_du_jour + r'.*\3',
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
