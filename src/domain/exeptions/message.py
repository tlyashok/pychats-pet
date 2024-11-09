from dataclasses import dataclass

from domain.exeptions.base import ApplicationException

@dataclass(frozen=True)
class TextTooLongException(ApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f"Слишком длинный текст сообщения {self.text[:255]}..."
