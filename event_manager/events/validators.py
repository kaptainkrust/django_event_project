from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta, datetime


def dummy_validate(value: str) -> None:
    """
    Raises:
        ValueError if value contains "dummy"
    """
    if "dummy" in value:
        raise ValidationError("Name darf nicht Dummy enthalten!!!")
    

def datetime_in_future(value: datetime) -> None:
    if value < timezone.now() + timedelta(hours=1):
        raise ValidationError(
            "Termin darf nicht in der Vergangenheit liegen!"
        )
    

def evil_word_validator(wordlist: list[str], value: str):
    for evil_word in wordlist:
        if evil_word in value:
            raise ValidationError(
                f"Das Wort {evil_word} ist nicht erlaubt!"
            )
