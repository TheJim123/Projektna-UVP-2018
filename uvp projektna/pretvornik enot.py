import tkinter as tk
class Osnove:
    def __init__(self):
        self.kolicina = ''
        self.enote = ['']
        self.vrednost = 0
        self.kolicine = {'masa' : ['mg', 'cg', 'dg', 'g', 'dag', 'hg', 'kg', 'Mg'],
                         'dolzina' : ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km', 'Mm']}
        self.razmerja = {'m' : 0.001, 'c' : 0.01, 'd' : 0.1, '' : 1, 'da' : 10, 'h' : 100, 'k' : 1000, 'M' : (10 ** 6) }
        
    def nastavi_vrednost(self, vrednost):
        self.vrednost = float(vrednost)
        
    def doloci_enote(self):
        if self.kolicina != '':
            self.enote = self.kolicine[self.kolicina]
            
class Pretvornik:
    def __init__(self):
        self.osnova = Osnove() 
        self.okno = tk.Tk()
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
        v = self.osnova.razmerja[self.vhodna_enotna_spremenljivka.get()[:-1]]
        return v
    
    def vrednost_izhodne_enote(self, *args):
        i = self.osnova.razmerja[self.izhodna_enotna_spremenljivka.get()[:-1]]
        return i
    
Pretvornik()
