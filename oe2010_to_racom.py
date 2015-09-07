# coding: utf-8

class OE2010Row(object):
    FIELDS = (
        'oe0001',
        'start_cislo',
        'cas2',
        'cislo_cipu',
        'id',
        'prijmeni',
        'jmeno',
        'rn',
        's',
        'blok',
        'ms',
        'start',
        'cil',
        'cas',
        'klasifikace',
        'kredit',
        'penalizace',
        'komentar',
        'nazev_oddilu',
        'mesto',
        'stat',
        'misto',
        'region',
        'kategorie_c',
        'kategorie_kratka',
        'kategorie_dlouha',
        'ranking',
        'rankigove_body',
        'num1',
        'num2',
        'num3',
        'text1',
        'text2',
        'text3',
        'prijmeni2',
        'jmeno2',
        'ulice',
        'ulice2',
        'psc',
        'mesto',
        'tel',
        'mobil',
        'fax',
        'email',
        'pujceno',
        'vklady',
        'plasceno',
        'druzstvo',
        'cislo_trati',
        'trat',
        'km',
        'm',
        'kontroly_trati',
    )

    # Rakom define
    space = ' '
    oddelovac = ','
    other = ' '
    cislo_useku = ' '

    def __init__(self, raw_row):
        row = raw_row.split(';')
        for i, field in enumerate(self.FIELDS):
            setattr(self, field, row[i])

        # Rakom define
        self.reg_cislo = self.id
        self.minuta = self.start#.split(':')[0]
        self.sekundy = '00'
        self.prijmeni_jmeno = '%s %s' % (self.prijmeni, self.jmeno)

    def __repr__(self):
        return u'%s' % self.cislo_cipu

L = 'l'
R = 'r'

class RacomRow(object):
    FIELDS = (
        ('start_cislo', 5, L),
        ('space', 1, L),
        ('cislo_cipu', 8, R),
        ('space', 1, L),
        ('kategorie_dlouha', 5, L),
        ('space', 1, L),
        ('cislo_useku', 1, L),
        ('space', 1, L),
        ('reg_cislo', 7, L),
        ('space', 1, L),
        ('prijmeni_jmeno', 22, L),
        ('space', 1, L),
        ('minuta', 6, R),
        ('oddelovac', 1, L),
        ('sekundy', 2, R),
        ('other', 1, R),
    )

    def __init__(self, kr_row):
        out = []
        for field, pad, lr in self.FIELDS:
            data = getattr(kr_row, field)
            if lr == L:
                data = data.ljust(pad)
            if lr == R:
                data = data.rjust(pad)
            out.append(data)
        self._out = ''.join(out)

    def out(self):
        return self._out

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')

args = parser.parse_args()

out = []

with open(args.input) as f_in:
    data = f_in.read()

for i, row in enumerate(data.split('\n')):
    if i == 0:
        continue
    try:
        out.append(RacomRow(OE2010Row(row)).out())
    except:
        pass

with open(args.output, 'w') as f_out:
    f_out.write('\n'.join(out))

