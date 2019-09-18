class Cow:

    def __init__(self, weight):
        self.weight = weight


class Feed:

    def __init__(self, koe):
        if koe.weight == 450:
            self.energy = 26500
            self.protein = 215
        else:
            self.energy = 29500
            self.protein = 245

