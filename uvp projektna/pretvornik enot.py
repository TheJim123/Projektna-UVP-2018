import tkinter as tk
class Osnove:
    def __init__(self):
        self.kolicina = ''
        self.enote = ['']
        self.vrednost = 0
        self.kolicine = {'masa' : ['mg', 'cg', 'dg', 'g', 'dag', 'hg', 'kg', 't'],
                         'dolzina' : ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km', 'Mm'],
                         'ploscina' : ['mm^2', 'cm^2', 'dm^2', 'm^2', 'a', 'ha', 'km^2'],
                         'volumen' : ['mm^3', 'cm^3', 'dm^3', 'm^3', 'km^3', 'ml', 'cl', 'dl', 'l', 'hl' ]}
        
        self.desetiska_razmerja = {'m' : 0.001, 'c' : 0.01, 'd' : 0.1, '' : 1, 'da' : 10, 'h' : 100, 'k' : 1000, 'M' : (10 ** 6) }
        self.kvadratna_razmerja = {'m' : 100 ** (-3), 'c' : 100 ** (-2), 'd' : 100 ** (-1), '' : 1, 'a' : 100, 'ha' : 100 ** 2, 'k' : 100 ** 3}
        self.kubicna_razmerja = {'m' : 1000 ** (-3), 'c' : 1000 ** (-2), 'd' : 1000 ** (-1), '' : 1, 'k' : 1000 ** 3, 'ml' : 10 ** (-6), 'cl' : 10 ** (-5), 'dl' : 10 ** (-4), 'l' : 10 ** (-3), 'hl' : 10 ** (-1)}
        
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
        
        self.kolicinska_spremenljivka.set('')
        
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
        if self.osnova.kolicina == 'masa' or self.osnova.kolicina == 'dolzina':
            if self.vhodna_enotna_spremenljivka.get() == 't':
                v = 10 ** 6
            else:
                v = self.osnova.desetiska_razmerja[self.vhodna_enotna_spremenljivka.get()[:-1]]
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
        return v
    
    def vrednost_izhodne_enote(self, *args):
        if self.osnova.kolicina == 'masa' or self.osnova.kolicina == 'dolzina':
            if self.izhodna_enotna_spremenljivka.get() == 't':
                i = 10 ** 6
            else:
                i = self.osnova.desetiska_razmerja[self.izhodna_enotna_spremenljivka.get()[:-1]]
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
        return i
    
Pretvornik()
