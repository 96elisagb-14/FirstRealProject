"""
Practice script for data.xlsx.

Run:
    python script.py

Requires:
    pip install pandas openpyxl
"""

from pathlib import Path
import pandas as pd


DATA_FILE = Path(__file__).with_name("data.xlsx")


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find {DATA_FILE}")

    df = pd.read_excel(DATA_FILE, sheet_name="SalesData")

    print("First 5 rows:")
    print(df.head(), "\n")

    print("Total revenue:")
    print(f"${df['Revenue'].sum():,.2f}\n")

    print("Revenue by product:")
    print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False), "\n")

    print("Rows that met the target:")
    print(df["Met Target?"].value_counts())


if __name__ == "__main__":
    main()
