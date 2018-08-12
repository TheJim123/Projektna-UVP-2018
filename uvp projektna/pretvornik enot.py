import tkinter as tk
class Osnove:
    def __init__(self):
        self.kolicine = ['masa', 'dolzina']
        masa = ['mg', 'cg', 'dg', 'g', 'dag', 'hg', 'kg', 't']
        dolzina = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
        self.enote = masa + dolzina
        self.vrednost = 0
    def nastavi_vrednost(self, vrednost):
        self.vrednost = vrednost

class Pretvornik:
    def __init__(self):
        self.osnova = Osnove() 
        self.okno = tk.Tk()
################################################################################
        self.levi_okvir = tk.Frame(self.okno)
        
        self.vhod = tk.Entry(self.levi_okvir)
        
        self.vhodna_vrednost = 0
        vhodna_enotna_spremenljivka = tk.StringVar(self.levi_okvir)
        enote = self.osnova.enote
        vhodna_enotna_spremenljivka.set('')
        self.vhodna_enota = tk.OptionMenu(self.levi_okvir, vhodna_enotna_spremenljivka, *enote)
        self.je_enako = tk.Label(self.levi_okvir, text = '=')
####################################################################################
        self.sredinski_okvir = tk.Frame(self.okno)
        kolicinska_spremenljivka = tk.StringVar(self.sredinski_okvir)
        kolicine = self.osnova.kolicine
        kolicinska_spremenljivka.set('')
        self.kolicinski_meni = tk.OptionMenu(self.sredinski_okvir, kolicinska_spremenljivka, *kolicine)
        
################################################################################
        self.desni_okvir = tk.Frame(self.okno)
        
        self.izhod = tk.Label(self.desni_okvir, width= 20, text = '0')
        
        izhodna_enotna_spremenljivka = tk.StringVar(self.levi_okvir)
        enote = self.osnova.enote
        izhodna_enotna_spremenljivka.set('')
        self.izhodna_enota = tk.OptionMenu(self.desni_okvir, izhodna_enotna_spremenljivka, *enote)
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
    def dolocitev_vhodne_vrednosti(self):
        vrednost = self.vhod.get()
        self.vhodna_vrednost = (self.osnova.nastavi_vrednost(vrednost))
        
    def pretvori(self):
        self.dolocitev_vhodne_vrednosti()
        return self.vhodna_vrednost * 1.2
        
    def pretvorba(self):
        self.izhod.configure(text = str(self.pretvori()))
   

Pretvornik()
