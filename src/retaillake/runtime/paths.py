from __future__ import annotations

import os
from pathlib import Path


class ProjectPaths:
    """
    Enterprise runtime path resolver.

    Supports

    - Windows IDE
    - Docker
    - Linux
    - CI
    """

    @classmethod
    def project_root(cls) -> Path:
        if os.getenv("RUNNING_IN_DOCKER") == "1":
            return Path("/app")

        return Path(__file__).resolve().parents[3]

    @classmethod
    def data_dir(cls) -> Path:
        return cls.project_root() / "data"

    @classmethod
    def bronze_path(cls) -> Path:
        return cls.data_dir() / "bronze"

    @classmethod
    def silver_path(cls) -> Path:
        return cls.data_dir() / "silver"

    @classmethod
    def gold_path(cls) -> Path:
        return cls.data_dir() / "gold"

    @classmethod
    def dlq_path(cls) -> Path:
        return cls.data_dir() / "dlq"

    @classmethod
    def checkpoints_dir(cls) -> Path:
        return cls.project_root() / "checkpoints"

    @classmethod
    def bronze_checkpoint(cls) -> Path:
        return cls.checkpoints_dir() / "bronze"

    @classmethod
    def silver_checkpoint(cls) -> Path:
        return cls.checkpoints_dir() / "silver"

    @classmethod
    def gold_checkpoint(cls) -> Path:
        return cls.checkpoints_dir() / "gold"

    @classmethod
    def logs_dir(cls) -> Path:
        return cls.project_root() / "logs"

    @classmethod
    def validation_dir(cls) -> Path:
        return cls.project_root() / "validation_artifacts"

    @classmethod
    def create_runtime_directories(cls) -> None:
        directories = [
            cls.bronze_path(),
            cls.silver_path(),
            cls.gold_path(),
            cls.dlq_path(),
            cls.bronze_checkpoint(),
            cls.silver_checkpoint(),
            cls.gold_checkpoint(),
            cls.logs_dir(),
            cls.validation_dir(),
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)