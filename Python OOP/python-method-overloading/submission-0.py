class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, first: str, second: str = "") -> str:
        if len(second) == 0:
            return first.upper()
        else:
            return first + second



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
