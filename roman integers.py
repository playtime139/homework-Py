class RomanNumeral:
    def __init__(self, number: int):
        if not (1 <= number <= 3999):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number

    def to_roman(self) -> str:
        value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = ""
        num = self.number

        for value, symbol in value_map:
            while num >= value:
                result += symbol
                num -= value

        return result


if __name__ == "__main__":
    roman = RomanNumeral(444)
    print(roman.to_roman()) 
