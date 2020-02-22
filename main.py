import random


class WorldFoods:
    def __init__(self):
        super().__init__()
        self.world_list = {
            1: "New York",
            2: "China",
            3: "Japan",
            4: "India",
            5: "France",
            6: "Germany",
            7: "Mexico",
            8: "Spain",
            9: "Canada",
            10: "Greece",
            11: "Italy",
            12: "Russia",
            13: "Korea",
            14: "Australia",
            15: "Indonesia",
            16: "Hawaii",
            17: "Scotland",
            18: "El Salvador",
            19: "Jamaica",
            20: "Iceland",
            21: "Serbia",
            22: "Jordan",
            23: "Thailand",
            24: "Costa Rica",
            25: "Romania",
            26: "Israel",
            27: "Panama",
            28: "Hangary",
            29: "Slovakia",
            30: "Sweden",
            31: "Norway",
            32: "Denmark",
            33: "The Netherlands",
            34: "Belgium",
            35: "Czech Republic",
            36: "Austria",
            37: "Guatamala",
            38: "Lithuania",
            39: "England",
            40: "Ireland",
            41: "Boston",
            42: "Chicago",
            43: "Cuba",
            44: "Kentucky",
            45: "Louisiana",
            46: "Pennsylvania",
            47: "Tennessee",
            48: "Texas",
            49: "New Jersey",
            50: "Phillipeans",
            51: "Arkansas",
            52: "Brazil"
        }
        self.number_sequence = random.sample(range(52), 52)
        self.main()

    def main(self):
        for sequence in self.number_sequence:
            if sequence != 0:
                print(self.world_list[sequence])

if __name__ == "__main__":
    WorldFoods()