def läs_int(prompt="Ange ett heltal: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Inte ett heltal. Försök igen.")

tal = läs_int("Ange ett tal 1-10: ")
print(f"Du angav: {tal}")