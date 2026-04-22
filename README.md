# Datareduktionsuppgift

Grupprojekt – datareduktion och visualisering.

## Mappstruktur

```
data/
  raw/          ← lägg originalfilen här (dataset.csv)
  processed/    ← städad data skapas av src/preprocess.py
notebooks/
  01_eda.ipynb                   ← laddning, inspektion, korrelationer
  02_statistics.ipynb            ← deskriptiv statistik, fördelningar
  03_dimensionality_reduction.ipynb  ← PCA, t-SNE, UMAP (extra)
  04_visualization.ipynb         ← statiska + interaktiva plottar (extra)
src/
  preprocess.py  ← städningsskript
presentation/   ← lägg slides här
reports/
  figures/       ← sparade plottar
```

## Kom igång

```bash
pip install -r requirements.txt
# Lägg ditt dataset i data/raw/dataset.csv
python src/preprocess.py
jupyter lab
```

## Checklista

- [ ] Välj dataset och ladda ner till `data/raw/`
- [ ] Kör `preprocess.py` och anpassa städningen
- [ ] `01_eda.ipynb` – utforska variabler och korrelationer
- [ ] `02_statistics.ipynb` – statistisk analys av valda variabler
- [ ] `03_dimensionality_reduction.ipynb` – PCA + t-SNE (+ UMAP extra)
- [ ] `04_visualization.ipynb` – finputsa plottar (+ interaktiva extra)
- [ ] Bygg presentation (5–7 bilder, 10 min + 5 min frågor)
