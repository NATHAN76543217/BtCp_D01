class GotCharacter():
    """
        a Game Of Throne character
    """
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """
        A class representing the Stark family.
            Or when bad things happen to good people.
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        print("AAarrggh!!")
        self.is_alive = False


if __name__ == "__main__":
    arya = Stark("Arya")
    print(arya.__doc__)
    print(arya.__dict__)
    arya.print_house_words()
    print("is_alive : " + str(arya.is_alive))
    arya.die()
    print("is_alive : " + str(arya.is_alive))
