from prac_06.programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

    languages = [python, visual_basic, ruby]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.field)

main()