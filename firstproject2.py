class harfsayaci():
    def __init__(self):
        self.sesli_harfler="aeıioöuü"
        self.sessiz_harfler="bcçdfgğhjklmnprsştvyz"
        self.sesli_harf_sayaci=0
        self.sessiz_harf_sayaci=0

    def kelime_sor(self):
        return input("lütfen kelimeyi yazın: ")
    def seslidir(self,harf):
        return  harf in self.sesli_harfler
    def sessizdir(self,harf):
        return  harf in self.sessiz_harfler

    def arttir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sesli_harf_sayaci+=1
            if self.sessizdir(harf):
                self.sessiz_harf_sayaci+=1
        return (self.sesli_harf_sayaci,self.sessiz_harf_sayaci)
    def ekranda_goster(self):
        sesli,sessiz=self.arttir()
        print("sesli:",sesli ," \nsessiz:",sessiz)
    def calistir(self):
        self.kelime=self.kelime_sor()
        self.ekranda_goster()

kelime = harfsayaci()
kelime.calistir()

