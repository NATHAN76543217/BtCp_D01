class Vector():
    """
        A vector tools class
    """
    def __init__(self, values):
        if type(values) == list:
            self._initList(values)
        elif type(values) == int:
            self._initInt(values)
        elif type(values) == tuple:
            self._initTuple(values)
        else:
            raise TypeError(
                "Param format ({}) not supported".format(type(values)))
        self.size = len(self.values)

    def _initTuple(self, values):
        my_values = []
        if len(values) == 2:
            i = float(values[0])
            if i < values[1]:
                while i < values[1]:
                    my_values.append(i)
                    i += 1
            else:
                while i > values[1]:
                    my_values.append(i)
                    i -= 1
            self.values = my_values
        else:
            raise ValueError("Tuple param must have exactly two values")

    def _initInt(self, values):
        my_list = []
        i = 0.0
        while i < values:
            my_list.append(i)
            i += 1
        self.values = my_list

    def _initList(self, values):
        for val in values:
            if type(val) != float:
                raise TypeError(
                    "Vectors Values's type must be {}".format(float))
        self.values = values

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.size:
            self.n += 1
            return self.values[self.n - 1]
        else:
            raise StopIteration

    def __str__(self):
        txt = ""
        fisrt = 1
        for val in self.values:
            if fisrt:
                txt += str(val)
            else:
                txt += ", " + str(val)
            fisrt = 0
        return txt

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("a Vector can only be added to another Vector")
        if len(self.values) == len(other.values):
            i = 0
            while i < len(self.values):
                self.values[i] += other.values[i]
                i += 1
        else:
            raise ValueError(
                "a Vector can only be added" +
                "to another vector of the same size")
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("a Vector can only be added to another Vector")
        if len(self.values) == len(other.values):
            i = 0
            while i < len(self.values):
                self.values[i] -= other.values[i]
                i += 1
        else:
            raise ValueError(
                "a Vector can only be added" +
                "to another vector of the same size")
        return self


if __name__ == "__main__":
    my_vector = Vector([0.0, 1.0, 2.0, 3.0])
    my_vector2 = Vector(4)
    my_vector3 = Vector((3, 1))

    print("my_vector ==", my_vector)
    print("my_vector2==", my_vector2)
    print("my_vector3==", my_vector3)

    my_vector += my_vector2
    print("\nmy_vector after addition==", my_vector)
    my_vector -= my_vector2
    print("\nmy_vector after substraction==", my_vector)
