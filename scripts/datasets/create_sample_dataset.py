from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]

SOURCE = ROOT / "datasets" / "raw" / "instacart" / "orders.csv"

OUTPUT_DIR = ROOT / "datasets" / "sample"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


DATASET_SIZES = {
    "100K": 100_000,
    "500K": 500_000,
    "1M": 1_000_000,
}


def create_dataset(name: str, rows: int):

    print(f"Creating {name}")

    df = pd.read_csv(SOURCE, nrows=rows)

    output = OUTPUT_DIR / f"orders_{name.lower()}.csv"

    df.to_csv(output, index=False)

    print(output)

    print(f"Rows : {len(df):,}")


def main():

    for name, rows in DATASET_SIZES.items():

        create_dataset(name, rows)


if __name__ == "__main__":

    main()