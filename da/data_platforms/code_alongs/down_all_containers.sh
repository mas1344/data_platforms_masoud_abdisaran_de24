#!/bin/bash

# Ersätt /path/to/parent/directory med sökvägen till den överordnade katalogen som innehåller dina docker-compose.yml-filer
PARENT_DIR="C:/Users/Mori_/Documents/github/data_platforms_masoud_abdisaran_de24"

# Hitta alla kataloger som innehåller docker-compose.yml-filer och kör docker-compose down i varje
find "$PARENT_DIR" -name 'docker-compose.yml' -execdir docker compose down \;
