COLOUR_CODES = {"AliceBlue": "#f0f8ff", "Ash Grey": "#b2beb5", "Army Green": "#4b5320",
                "Asparagus": "#87a96b", "Baby Blue": "89cff0", "Bole": "#79443b",
                "Canary": "#ffff99", "Cardinal": "#c41e3a", "Celeste": "#b2ffff",
                "Daffodil": "#ffff31"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")