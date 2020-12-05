import random
FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
         'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
         'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
         'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam',  'She', 'Sheel',
         'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
          'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
          'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
          'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
          'wain', 'wan', 'win', 'wise', 'ya']

LAST = ["Mithram", "Frozentail", "Honvralor", "Featherpik", "Firemore", "Shade", "Crystmir", "Relldar", "Lowden", "Fogcrest",
        "Whitbash", "Hammerbluf", "Draenrend", "Twill", "Meadowdown", "Goldblower", "Flintdane", "Stagpunch", "Wheatstrea", "Farrowfall", "Dayleaf",
        "Swiftscrib", "Stonedraft", "Windel", "Sagecut", "Stonecreek", "Hardford", "Blanding", "Regalbend", "Svarndorm", "Winterlord", "Eagletrap",
        "Tithan", "Palewhirl", "Trello", "Sladrin", "Wyvernwood", "Lunawind", "Fullsprin", "Glowbinder", "Dwindledorn"]


def generateName():
    return random.choice(FIRST) + random.choice(SECOND) + " " + random.choice(LAST)
