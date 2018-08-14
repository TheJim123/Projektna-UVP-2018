import tkinter as tk
import math as m
class Osnove:
    def __init__(self):
        self.kolicina = ''
        self.enote = ['']
        self.vrednost = 0
        self.kolicine = {'masa' : ['mg', 'cg', 'dg', 'g', 'dag', 'hg', 'kg', 't'],
                         'dolzina' : ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km', 'Mm'],
                         'ploscina' : ['mm^2', 'cm^2', 'dm^2', 'm^2', 'a', 'ha', 'km^2'],
                         'volumen' : ['mm^3', 'cm^3', 'dm^3', 'm^3', 'km^3', 'ml', 'cl', 'dl', 'l', 'hl' ],
                         'energija' : ['mJ', 'cJ', 'dJ', 'J', 'daJ', 'hJ', 'kJ', 'MJ'],
                         'koti v ravnini' : ['kotne sekunde', 'kotne minute', '°', 'rad'],
                         'podatki' : ['b', 'B', 'kB', 'MB', 'GB', 'TB'],
                         'cas' : ['ms', 'cs', 'ds', 's', 'min', 'h', 'dan', 'mesec', 'let'],
                         'frekvenca' : ['Hz', 'kHz', 'MHz', 'GHz', 'THz'],
                         'tlak' : ['Pa','mbar','kPa', 'bar']}
        
        self.desetiske_kolicine = ['masa', 'dolzina', 'energija']
        
        self.desetiska_razmerja = {'m' : 0.001, 'c' : 0.01, 'd' : 0.1, '' : 1, 'da' : 10, 'h' : 100, 'k' : 1000, 'M' : (10 ** 6), 'G' : (10 ** 9), 'T' : (10 ** 12)}
        self.kvadratna_razmerja = {'m' : 100 ** (-3), 'c' : 100 ** (-2), 'd' : 100 ** (-1), '' : 1, 'a' : 100, 'ha' : 100 ** 2, 'k' : 100 ** 3}
        self.kubicna_razmerja = {'m' : 1000 ** (-3), 'c' : 1000 ** (-2), 'd' : 1000 ** (-1), '' : 1, 'k' : 1000 ** 3, 'ml' : 10 ** (-6), 'cl' : 10 ** (-5), 'dl' : 10 ** (-4), 'l' : 10 ** (-3), 'hl' : 10 ** (-1)}
        self.casovna_razmerja = {'min' : 60, 'h' : 3600, 'dan' : 86400, 'mesec' : 2592000, 'let' : 31104000}
        self.tlacna_razmerja = {'' : 0, 'Pa' : 1, 'mbar' : 100, 'kPa' : 1000, 'bar' : 10 ** 5}
        self.podatkovna_razmerja = {'b' : 0.125, '' : 1, 'kB' : 1024, 'MB' : 1024 ** 2, 'GB' : 1024 ** 3, 'TB' : 1024 ** 4}
        self.kotna_razmerja = {'' : 0, 'kotne sekunde' : (1 / 3600), 'kotne minute' : (1 / 60), '°' : 1, 'rad' : (180 / m.pi)}
        
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
################################################################################
        self.levi_okvir = tk.Frame(self.okno)
        
        self.vhod = tk.Entry(self.levi_okvir)
        self.vhod.insert(0, string='0')
        self.vhodna_vrednost = 0

        self.vhodna_enotna_spremenljivka = tk.StringVar(self.levi_okvir)

        self.vhodna_enotna_spremenljivka.set('')
        
        self.vhodna_enota = tk.OptionMenu(self.levi_okvir, self.vhodna_enotna_spremenljivka, *self.osnova.enote)
        
        self.vhodna_enotna_spremenljivka.trace('w', self.vrednost_vhodne_enote)
        
        self.je_enako = tk.Label(self.levi_okvir, text = '=')
####################################################################################
        self.sredinski_okvir = tk.Frame(self.okno)

        self.kolicinska_spremenljivka = tk.StringVar(self.okno)

        kolicine = self.osnova.kolicine.keys()
        
        self.kolicinska_spremenljivka.set('kolicina')
        
        self.kolicinski_meni = tk.OptionMenu(self.sredinski_okvir, self.kolicinska_spremenljivka, *kolicine)

        self.kolicinska_spremenljivka.trace('w', self.doloci_izbiro_enot)
################################################################################
        self.desni_okvir = tk.Frame(self.okno)
        
        self.izhod = tk.Label(self.desni_okvir, width= 20, text = '0')
        
        self.izhodna_enotna_spremenljivka = tk.StringVar(self.levi_okvir)

        enote = self.osnova.enote
        self.izhodna_enotna_spremenljivka.set('')
        self.izhodna_enota = tk.OptionMenu(self.desni_okvir, self.izhodna_enotna_spremenljivka, *self.osnova.enote)

        self.izhodna_enotna_spremenljivka.trace('w', self.vrednost_izhodne_enote)
        
        self.je_enako = tk.Label(self.levi_okvir, text = '=')
        self.gumb = tk.Button(self.desni_okvir, text='Pretvori', command = self.pretvorba)
####################################################################################
        self.levi_okvir.grid(row = 5, column = 2)
        self.sredinski_okvir.grid(row = 4, column = 4)
        self.desni_okvir.grid(row = 5, column = 6)
        self.izhod.grid(row = 5, column = 3)
        self.gumb.grid(row = 5, column = 8)
        self.vhod.grid(row = 5, column = 2)
        self.vhodna_enota.grid(row = 5, column = 3)
        self.kolicinski_meni.grid(row = 1, column = 1)
        self.je_enako.grid(row = 5, column = 4)
        self.izhodna_enota.grid(row = 5, column = 6)
#####################################################################################
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
        return  self.vrednost_vhodne_enote() * self.dolocitev_vhodne_vrednosti() / self.vrednost_izhodne_enote()
        
    def pretvorba(self):
        self.izhod.configure(text = '{0:.3f}'.format(self.pretvori()))
        
    def doloci_izbiro_enot(self, *args):
        self.osnova.kolicina = self.kolicinska_spremenljivka.get()
        self.osnova.doloci_enote()
        self.osvezi_enote()
        
    def vrednost_vhodne_enote(self, *args):
        if self.osnova.kolicina in self.osnova.desetiske_kolicine:
            if self.vhodna_enotna_spremenljivka.get() == 't':
                v = 10 ** 6
            else:
                v = self.osnova.desetiska_razmerja[self.vhodna_enotna_spremenljivka.get()[:-1]]
        elif self.osnova.kolicina == 'frekvenca':
            v = self.osnova.desetiska_razmerja[self.vhodna_enotna_spremenljivka.get()[:-2]]
        elif self.osnova.kolicina == 'ploscina':
            if 'a' in self.vhodna_enotna_spremenljivka.get():
                v = self.osnova.kvadratna_razmerja[self.vhodna_enotna_spremenljivka.get()]
            else:
                v = self.osnova.kvadratna_razmerja[self.vhodna_enotna_spremenljivka.get()[:-3]]
        elif self.osnova.kolicina == 'volumen':
            if 'l' in self.vhodna_enotna_spremenljivka.get():
                v = self.osnova.kubicna_razmerja[self.vhodna_enotna_spremenljivka.get()]
            else:
                v = self.osnova.kubicna_razmerja[self.vhodna_enotna_spremenljivka.get()[:-3]]
        elif self.osnova.kolicina == 'podatki':
            if 'b' == self.vhodna_enotna_spremenljivka.get():
                v = 0.125
            else:
                v = self.osnova.podatkovna_razmerja[self.vhodna_enotna_spremenljivka.get()[:-1]]
        elif self.osnova.kolicina == 'cas':
            if self.vhodna_enotna_spremenljivka.get() in self.osnova.casovna_razmerja.keys():
                v = self.osnova.casovna_razmerja[self.vhodna_enotna_spremenljivka.get()]
            else:
                v = self.osnova.desetiska_razmerja[self.vhodna_enotna_spremenljivka.get()[:-1]]
        elif self.osnova.kolicina == 'tlak':
            v = self.osnova.tlacna_razmerja[self.vhodna_enotna_spremenljivka.get()]
        elif self.osnova.kolicina == 'koti v ravnini':
            v = self.osnova.kotna_razmerja[self.vhodna_enotna_spremenljivka.get()]
        return v
    
    def vrednost_izhodne_enote(self, *args):
        if self.osnova.kolicina in self.osnova.desetiske_kolicine:
            if self.izhodna_enotna_spremenljivka.get() == 't':
                i = 10 ** 6
            else:
                i = self.osnova.desetiska_razmerja[self.izhodna_enotna_spremenljivka.get()[:-1]]
        elif self.osnova.kolicina == 'frekvenca':
            i = self.osnova.desetiska_razmerja[self.izhodna_enotna_spremenljivka.get()[:-2]]
        elif self.osnova.kolicina == 'ploscina':
            if 'a' in self.izhodna_enotna_spremenljivka.get():
                i = self.osnova.kvadratna_razmerja[self.izhodna_enotna_spremenljivka.get()]
            else:
                i = self.osnova.kvadratna_razmerja[self.izhodna_enotna_spremenljivka.get()[:-3]]
        elif self.osnova.kolicina == 'volumen':
            if 'l' in self.izhodna_enotna_spremenljivka.get():
                i = self.osnova.kubicna_razmerja[self.izhodna_enotna_spremenljivka.get()]
            else:
                i = self.osnova.kubicna_razmerja[self.izhodna_enotna_spremenljivka.get()[:-3]]
        elif self.osnova.kolicina == 'podatki':
            if 'b' in self.izhodna_enotna_spremenljivka.get():
                i = 0.125
            else:
                i = self.osnova.podatkovna_razmerja[self.izhodna_enotna_spremenljivka.get()[:-1]]
        elif self.osnova.kolicina == 'cas':
            if self.izhodna_enotna_spremenljivka.get() in self.osnova.casovna_razmerja.keys():
                i = self.osnova.casovna_razmerja[self.izhodna_enotna_spremenljivka.get()]
            else:
                i = self.osnova.desetiska_razmerja[self.izhodna_enotna_spremenljivka.get()[:-1]]
        elif self.osnova.kolicina == 'tlak':
            i = self.osnova.tlacna_razmerja[self.izhodna_enotna_spremenljivka.get()]
        elif self.osnova.kolicina == 'koti v ravnini':
            i = self.osnova.kotna_razmerja[self.izhodna_enotna_spremenljivka.get()]
        return i
    
Pretvornik()
