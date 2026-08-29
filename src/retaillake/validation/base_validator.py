from abc import ABC
from abc import abstractmethod

from retaillake.validation.validation_result import ValidationResult


class BaseValidator(ABC):
    """
    Base class for all platform validators.
    """

    @abstractmethod
    def validate(self) -> ValidationResult:
        """
        Execute validation.

        Returns
        -------
        ValidationResult
        """