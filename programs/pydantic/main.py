# pydantic allows data validation and settings management using python type annotations
# can generate a json schema automatically from a pydantic model that we define
# has a base settings class taht allows to easily read config files, such as env variables
# Video Link: https://www.youtube.com/watch?v=Vj-iU-8_xLs

"""
Basic example showing how to read and validate data from a file using Pydantic.
"""
import json
import os
from typing import List, Optional

import pydantic


class ISBNMissingError(Exception):
    """
    Exception raised when ISBN is missing.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ISBN10FormatError(Exception):
    """
    Exception raised when ISBN-10 is not valid.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class Book(pydantic.BaseModel):
    """
    Book model.
    """

    model_config = pydantic.ConfigDict(frozen=True, str_to_lower=True)

    title: str
    subtitle: Optional[str] = None
    author: str
    publisher: str
    isbn_10: Optional[str] = None
    isbn_13: Optional[str] = None
    price: float
    author2: Optional[dict] = None

    @pydantic.model_validator(mode="before")
    @classmethod
    def check_isbn10_or_isbn13(cls, values: dict) -> dict:
        """
        Check if ISBN-10 or ISBN-13 is provided.
        """
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                f"Document must have either ISBN-10 or ISBN-13. Document: {values}"
            )
        return values

    @pydantic.field_validator("isbn_10")
    @classmethod
    def isbn_10_validator(cls, value: str) -> str:
        """
        Validate ISBN-10.
        """
        chars = [c for c in value if c in "0123456789Xx"]
        if chars and len(chars) != 10:
            raise ISBN10FormatError(f"ISBN-10 must have 10 digits. ISBN-10: {value}")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                f"ISBN10 digit sum should be divisible by 11. ISBN-10: {value}"
            )

        return value


def main() -> None:
    """
    Main function.
    """
    # Read data from file
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.json")
    with open(file_path, "r") as file:
        data = json.load(file)

    # Validate data
    books: List[Book] = [Book(**book) for book in data]

    # books[0].title = "Hello"

    # Print data
    print("----------Printing 1st book as obj----------")
    print(books[0])

    print()

    print("----------Printing 1st book as dict----------")
    print(books[0].model_dump(exclude={"author2"}))


if __name__ == "__main__":
    main()
