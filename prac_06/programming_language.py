class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, field, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return 'MyClass(field=' + str(self.field) + ' ,typing=' + str(self.typing) + ' ,reflection=' + str(self.reflection) +' ,year=' + str(self.year) +')'

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

    languages = [python, visual_basic, ruby]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.field)


if __name__ == "__main__":
    run_tests()