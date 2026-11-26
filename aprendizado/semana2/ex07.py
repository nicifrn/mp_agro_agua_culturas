municipios = {
    "Nova Cruz": (-6.4778, -35.4339),
    # Adicione os demais municípios da seção 3 no formato "Nome": (lat, lon)
}

for municipio, (lat, lon) in municipios.items():
    print(f"{municipio}: latitude {lat}, longitude {lon}")