"""Laddning och städning av WHR26_Data_Figure_2.1.xlsx -> data/cleaned_data.csv"""

import pandas as pd
from pathlib import Path

RAW = Path("data/WHR26_Data_Figure_2.1.xlsx")
OUT = Path("data/cleaned_data.csv")

FEATURE_COLS = [
    "Explained by: Log GDP per capita",
    "Explained by: Social support",
    "Explained by: Healthy life expectancy",
    "Explained by: Freedom to make life choices",
    "Explained by: Generosity",
    "Explained by: Perceptions of corruption",
    "Dystopia + residual",
]

SHORT_NAMES = {
    "Life evaluation (3-year average)": "happiness_score",
    "Explained by: Log GDP per capita": "gdp",
    "Explained by: Social support": "social_support",
    "Explained by: Healthy life expectancy": "health",
    "Explained by: Freedom to make life choices": "freedom",
    "Explained by: Generosity": "generosity",
    "Explained by: Perceptions of corruption": "corruption",
    "Dystopia + residual": "dystopia_residual",
    "Country name": "country",
    "Lower whisker": "ci_lower",
    "Upper whisker": "ci_upper",
}


def load(path: Path = RAW) -> pd.DataFrame:
    return pd.read_excel(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # Behåll bara år med kompletta features (2019–2025)
    df = df.dropna(subset=FEATURE_COLS).copy()
    df = df.drop_duplicates()
    df = df.rename(columns=SHORT_NAMES)
    df = df.reset_index(drop=True)
    return df


if __name__ == "__main__":
    df = load()
    df = clean(df)
    df.to_csv(OUT, index=False)
    print(f"Sparat {len(df)} rader, {df.shape[1]} kolumner till {OUT}")
    print("Kolumner:", df.columns.tolist())
    print("År:", sorted(df["Year"].unique()))
