import tkinter as tk
import math as m


class Osnove:
    def __init__(self):
        self.kolicina = ''
        self.enote = ['']
        self.vrednost = 0
        self.kolicine = {
            'masa': ['mg', 'cg', 'dg', 'g', 'dag', 'hg', 'kg', 't'],
            'dolžina': ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km', 'Mm'],
            'ploščina': ['mm^2', 'cm^2', 'dm^2', 'm^2', 'a', 'ha', 'km^2'],
            'volumen': ['mm^3', 'cm^3', 'dm^3', 'm^3', 'ml', 'cl', 'dl', 'l', 'hl'],
            'energija': ['mJ', 'cJ', 'dJ', 'J', 'daJ', 'hJ', 'kJ', 'MJ'],
            'koti v ravnini': ['kotne sekunde', 'kotne minute', '°', 'rad'],
            'podatki': ['b', 'B', 'kB', 'MB', 'GB', 'TB'],
            'čas': ['ms', 'cs', 'ds', 's', 'min', 'h', 'dan', 'mesec', 'let'],
            'frekvenca': ['Hz', 'kHz', 'MHz', 'GHz', 'THz'],
            'tlak': ['Pa', 'mbar', 'kPa', 'bar']}

        self.desetiske_kolicine = ['masa', 'dolžina', 'energija']

        self.desetiska_razmerja = {'m': 0.001, 'c': 0.01, 'd': 0.1, '': 1, 'da': 10,
                                   'h': 100, 'k': 1000, 'M': (10 ** 6), 'G': (10 ** 9), 'T': (10 ** 12)}
        self.kvadratna_razmerja = {'m': 100 ** (-3), 'c': 100 ** (-2), 'd': 100 ** (-1),
                                   '': 1, 'a': 100, 'ha': 100 ** 2, 'k': 100 ** 3}
        self.kubicna_razmerja = {'m': 1000 ** (-3), 'c': 1000 ** (-2), 'd': 1000 ** (-1), '': 1,
                                 'ml': 10 ** (-6), 'cl': 10 ** (-5), 'dl': 10 ** (-4), 'l': 10 ** (-3), 'hl': 10 ** (-1)}
        self.casovna_razmerja = {'min': 60, 'h': 3600, 'dan': 86400, 'mesec': 2592000, 'let': 31104000}
        self.tlacna_razmerja = {'': 0, 'Pa': 1, 'mbar': 100, 'kPa': 1000, 'bar': 10 ** 5}
        self.podatkovna_razmerja = {'b': 0.125, '': 1, 'k': 1024, 'M': 1024 ** 2, 'G': 1024 ** 3, 'T': 1024 ** 4}
        self.kotna_razmerja = {'': 0, 'kotne sekunde': (1 / 3600), 'kotne minute': (1 / 60), '°': 1, 'rad': (180 / m.pi)}

    def nastavi_vrednost(self, vrednost):
        self.vrednost = float(vrednost)

    def doloci_enote(self):
        if self.kolicina != '':
            self.enote = self.kolicine[self.kolicina]


class Pretvornik:
    def __init__(self):
        self.osnova = Osnove()
        self.okno = tk.Tk()
        self.okno.title('Pretvornik enot')
######################################################################
        self.vhod = tk.Entry(self.okno)
        self.vhod.insert(0, string='0')

        self.vhodna_enotna_spremenljivka = tk.StringVar(self.okno)
        self.vhodna_enotna_spremenljivka.set('')
        self.vhodna_enota = tk.OptionMenu(self.okno, self.vhodna_enotna_spremenljivka, *self.osnova.enote)
        self.vhodna_enotna_spremenljivka.trace('w', self.vrednost_vhodne_enote)
#######################################################################
        self.kolicinska_spremenljivka = tk.StringVar(self.okno)

        kolicine = self.osnova.kolicine.keys()

        self.kolicinska_spremenljivka.set('količina')

        self.kolicinski_meni = tk.OptionMenu(self.okno, self.kolicinska_spremenljivka, *kolicine)

        self.kolicinska_spremenljivka.trace('w', self.doloci_izbiro_enot)
#######################################################################
        self.izhod = tk.Label(self.okno, width=20, text='0')

        self.izhodna_enotna_spremenljivka = tk.StringVar(self.okno)

        enote = self.osnova.enote
        self.izhodna_enotna_spremenljivka.set('')
        self.izhodna_enota = tk.OptionMenu(self.okno, self.izhodna_enotna_spremenljivka, *self.osnova.enote)
        self.izhodna_enotna_spremenljivka.trace('w', self.vrednost_izhodne_enote)

        self.je_enako = tk.Label(self.okno, text='=')
        self.gumb = tk.Button(self.okno, text='Pretvori', command=self.pretvorba)
#######################################################################
        self.vhod.grid(row=2, column=2)
        self.vhodna_enota.grid(row=2, column=3)
        self.kolicinski_meni.grid(row=1, column=5)
        self.je_enako.grid(row=2, column=5)
        self.izhod.grid(row=2, column=7)
        self.izhodna_enota.grid(row=2, column=8)
        self.gumb.grid(row=2, column=9)
#######################################################################
        self.okno.mainloop()

    def osvezi_enote(self):
        self.izhodna_enotna_spremenljivka.set('')
        self.vhodna_enotna_spremenljivka.set('')
        self.vhodna_enota['menu'].delete(0, 'end')
        self.izhodna_enota['menu'].delete(0, 'end')

        nove_enote = tuple(self.osnova.enote)
        for enota in nove_enote:
            self.izhodna_enota['menu'].add_command(label=enota, command=tk._setit(self.izhodna_enotna_spremenljivka, enota))
            self.vhodna_enota['menu'].add_command(label=enota, command=tk._setit(self.vhodna_enotna_spremenljivka, enota))

    def dolocitev_vhodne_vrednosti(self):
        if self.vhod.get() == 'pi':
            self.osnova.nastavi_vrednost(m.pi)
        else:
            self.osnova.nastavi_vrednost(float(self.vhod.get()))
        return self.osnova.vrednost

    def pretvori(self):
        return self.vrednost_vhodne_enote() * self.dolocitev_vhodne_vrednosti() / self.vrednost_izhodne_enote()

    def pretvorba(self):
        self.izhod.configure(text='{}'.format(round(self.pretvori(), 16)))

    def doloci_izbiro_enot(self, *args):
        self.osnova.kolicina = self.kolicinska_spremenljivka.get()
        self.osnova.doloci_enote()
        self.osvezi_enote()

    def vrednost_vhodne_enote(self, *args):
        vhodna_enota = self.vhodna_enotna_spremenljivka.get()
        if self.osnova.kolicina in self.osnova.desetiske_kolicine:
            if self.vhodna_enotna_spremenljivka.get() == 't':
                v = 10 ** 6
            else:
                v = self.osnova.desetiska_razmerja[vhodna_enota[:-1]]
        elif self.osnova.kolicina == 'frekvenca':
            v = self.osnova.desetiska_razmerja[vhodna_enota[:-2]]
        elif self.osnova.kolicina == 'ploščina':
            if 'a' in vhodna_enota:
                v = self.osnova.kvadratna_razmerja[vhodna_enota]
            else:
                v = self.osnova.kvadratna_razmerja[vhodna_enota[:-3]]
        elif self.osnova.kolicina == 'volumen':
            if 'l' in vhodna_enota:
                v = self.osnova.kubicna_razmerja[vhodna_enota]
            else:
                v = self.osnova.kubicna_razmerja[vhodna_enota[:-3]]
        elif self.osnova.kolicina == 'podatki':
            if 'b' == vhodna_enota:
                v = 0.125
            else:
                v = self.osnova.podatkovna_razmerja[vhodna_enota[:-1]]
        elif self.osnova.kolicina == 'čas':
            if vhodna_enota in self.osnova.casovna_razmerja.keys():
                v = self.osnova.casovna_razmerja[vhodna_enota]
            else:
                v = self.osnova.desetiska_razmerja[vhodna_enota[:-1]]
        elif self.osnova.kolicina == 'tlak':
            v = self.osnova.tlacna_razmerja[vhodna_enota]
        elif self.osnova.kolicina == 'koti v ravnini':
            v = self.osnova.kotna_razmerja[vhodna_enota]
        return v

    def vrednost_izhodne_enote(self, *args):
        izhodna_enota = self.izhodna_enotna_spremenljivka.get()
        if self.osnova.kolicina in self.osnova.desetiske_kolicine:
            if izhodna_enota == 't':
                i = 10 ** 6
            else:
                i = self.osnova.desetiska_razmerja[izhodna_enota[:-1]]
        elif self.osnova.kolicina == 'frekvenca':
            i = self.osnova.desetiska_razmerja[izhodna_enota[:-2]]
        elif self.osnova.kolicina == 'ploščina':
            if 'a' in izhodna_enota:
                i = self.osnova.kvadratna_razmerja[izhodna_enota]
            else:
                i = self.osnova.kvadratna_razmerja[izhodna_enota[:-3]]
        elif self.osnova.kolicina == 'volumen':
            if 'l' in izhodna_enota:
                i = self.osnova.kubicna_razmerja[izhodna_enota]
            else:
                i = self.osnova.kubicna_razmerja[izhodna_enota[:-3]]
        elif self.osnova.kolicina == 'podatki':
            if 'b' in izhodna_enota:
                i = 0.125
            else:
                i = self.osnova.podatkovna_razmerja[izhodna_enota[:-1]]
        elif self.osnova.kolicina == 'čas':
            if izhodna_enota in self.osnova.casovna_razmerja.keys():
                i = self.osnova.casovna_razmerja[izhodna_enota]
            else:
                i = self.osnova.desetiska_razmerja[izhodna_enota[:-1]]
        elif self.osnova.kolicina == 'tlak':
            i = self.osnova.tlacna_razmerja[izhodna_enota]
        elif self.osnova.kolicina == 'koti v ravnini':
            i = self.osnova.kotna_razmerja[izhodna_enota]
        return i

Pretvornik()
