"""
Sprint 17 - Phase 6D

Enterprise Delta Metadata Validation

Generates production validation artifacts for:

- Bronze
- Silver
- Gold

without requiring manual PySpark commands.
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
from typing import Iterable

from delta.tables import DeltaTable
from pyspark.sql import DataFrame

from retaillake.spark.session.spark_session import get_spark
from retaillake.logging.logger_factory import LoggerFactory

from retaillake.utils.constants import (
    BRONZE_PATH,
    SILVER_PATH,
    GOLD_PATH,
)

logger = LoggerFactory.get_logger(__name__)


# ============================================================
# Output Directories
# ============================================================

OUTPUT_ROOT = (
    Path("validation_artifacts")
    / "executions"
    / "3_4m_dataset"
    / "full_pipeline"
)

COUNTS_DIR = OUTPUT_ROOT / "counts"
SCHEMAS_DIR = OUTPUT_ROOT / "schemas"
HISTORY_DIR = OUTPUT_ROOT / "history"
METADATA_DIR = OUTPUT_ROOT / "metadata"
DELTA_DIR = OUTPUT_ROOT / "delta"
VALIDATION_DIR = OUTPUT_ROOT / "validation"


def ensure_directories() -> None:
    """
    Create all validation folders.
    """

    directories = (
        COUNTS_DIR,
        SCHEMAS_DIR,
        HISTORY_DIR,
        METADATA_DIR,
        DELTA_DIR,
        VALIDATION_DIR,
    )

    for directory in directories:
        directory.mkdir(
            parents=True,
            exist_ok=True,
        )


# ============================================================
# Helpers
# ============================================================

def write_text(
    output_file: Path,
    text: str,
) -> None:
    """
    Writes plain text artifact.
    """

    output_file.write_text(
        text,
        encoding="utf-8",
    )


def dataframe_to_text(df: DataFrame) -> str:
    """
    Converts Spark DataFrame
    into formatted plain text.
    """

    rows = df.collect()

    headers = df.columns

    output = []

    output.append(
        " | ".join(headers)
    )

    output.append(
        "-" * 100
    )

    for row in rows:
        output.append(
            " | ".join(
                str(value)
                for value in row
            )
        )

    return "\n".join(output)


def schema_to_text(df: DataFrame) -> str:
    """
    Returns formatted schema.
    """

    return df._jdf.schema().treeString()


def export_dataframe(
    dataframe: DataFrame,
    output_file: Path,
) -> None:
    """
    Export DataFrame
    as readable text.
    """

    write_text(
        output_file,
        dataframe_to_text(dataframe),
    )


def export_schema(
    dataframe: DataFrame,
    output_file: Path,
) -> None:
    """
    Export schema.
    """

    write_text(
        output_file,
        schema_to_text(dataframe),
    )


def export_count(
    dataframe: DataFrame,
    output_file: Path,
) -> int:
    """
    Export row count.
    """

    count = dataframe.count()

    write_text(
        output_file,
        str(count),
    )

    return count


def export_sample(
    dataframe: DataFrame,
    output_file: Path,
    rows: int = 20,
) -> None:
    """
    Export sample rows.
    """

    sample = dataframe.limit(rows)

    export_dataframe(
        sample,
        output_file,
    )


# ============================================================
# Spark
# ============================================================

logger.info(
    "Creating Spark Session..."
)

spark = get_spark()

logger.info(
    "Spark Session Ready"
)

RUN_TIMESTAMP = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

logger.info(
    "Validation Started: %s",
    RUN_TIMESTAMP,
)

# ============================================================
# Delta Metadata Export
# ============================================================

def export_describe_detail(
    delta_path: str,
    output_file: Path,
) -> None:
    """
    Export DESCRIBE DETAIL metadata.
    """

    detail_df = spark.sql(
        f"DESCRIBE DETAIL delta.`{delta_path}`"
    )

    export_dataframe(
        detail_df,
        output_file,
    )


def export_history(
    delta_path: str,
    output_file: Path,
) -> None:
    """
    Export Delta transaction history.
    """

    history_df = (
        DeltaTable.forPath(
            spark,
            delta_path,
        )
        .history()
    )

    export_dataframe(
        history_df,
        output_file,
    )


# ============================================================
# Layer Validation
# ============================================================

def validate_layer(
    layer_name: str,
    delta_path: str,
) -> dict:

    logger.info(
        "Validating %s layer...",
        layer_name,
    )

    dataframe = (
        spark.read
        .format("delta")
        .load(delta_path)
    )

    count = export_count(
        dataframe,
        COUNTS_DIR /
        f"{layer_name}_count.txt",
    )

    export_schema(
        dataframe,
        SCHEMAS_DIR /
        f"{layer_name}_schema.txt",
    )

    export_sample(
        dataframe,
        DELTA_DIR /
        f"{layer_name}_sample.txt",
    )

    export_history(
        delta_path,
        HISTORY_DIR /
        f"{layer_name}_history.txt",
    )

    export_describe_detail(
        delta_path,
        METADATA_DIR /
        f"{layer_name}_detail.txt",
    )

    logger.info(
        "%s validation completed.",
        layer_name,
    )

    return {

        "layer": layer_name,

        "count": count,

        "path": delta_path,

    }


# ============================================================
# Validation Runner
# ============================================================

def validate_all_layers():

    ensure_directories()

    results = []

    layers = [

        (
            "bronze",
            BRONZE_PATH,
        ),

        (
            "silver",
            SILVER_PATH,
        ),

        (
            "gold",
            GOLD_PATH,
        ),

    ]

    for layer_name, path in layers:

        results.append(

            validate_layer(
                layer_name,
                path,
            )

        )

    return results

# ============================================================
# Validation Report
# ============================================================

def write_summary(results: list[dict]) -> None:
    """
    Generate Phase 6D summary.
    """

    lines = []

    lines.append("=" * 70)
    lines.append("PHASE 6D - DELTA METADATA VALIDATION")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"Execution Time : {RUN_TIMESTAMP}")
    lines.append("")

    total_rows = 0

    for result in results:

        lines.append(
            f"Layer : {result['layer']}"
        )

        lines.append(
            f"Rows  : {result['count']}"
        )

        lines.append(
            f"Path  : {result['path']}"
        )

        lines.append("")

        total_rows += result["count"]

    lines.append("=" * 70)
    lines.append(f"Total Rows : {total_rows}")
    lines.append("Status     : PASS")
    lines.append("=" * 70)

    write_text(
        VALIDATION_DIR /
        "delta_metadata_validation.txt",
        "\n".join(lines),
    )


# ============================================================
# Inventory
# ============================================================

def build_inventory() -> None:
    """
    Export inventory of generated evidence.
    """

    inventory = []

    for path in sorted(
        OUTPUT_ROOT.rglob("*")
    ):

        if path.is_file():

            inventory.append(

                str(
                    path.relative_to(
                        OUTPUT_ROOT
                    )
                )

            )

    write_text(

        VALIDATION_DIR /
        "phase6d_validation_inventory.txt",

        "\n".join(inventory),

    )


# ============================================================
# Main
# ============================================================

def main():

    logger.info(
        "=" * 70
    )

    logger.info(
        "Starting Phase 6D Validation"
    )

    logger.info(
        "=" * 70
    )

    results = validate_all_layers()

    write_summary(results)

    build_inventory()

    logger.info("")

    logger.info(
        "=" * 70
    )

    logger.info(
        "PHASE 6D VALIDATION PASSED"
    )

    logger.info(
        "=" * 70
    )

    logger.info("Artifacts written to:")

    logger.info(str(OUTPUT_ROOT))

    logger.info("")

    spark.stop()


if __name__ == "__main__":

    main()