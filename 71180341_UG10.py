class RakObat:
    def __init__(self):
        self.size = 4
        self.map = [None]*self.size
    
    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self.linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash
        return None
    
    def linearProbing(self, key, index):
        return (self.getHash(key)+index) % self.size
    
    def tambahObat(self, jenisObat, namaObat):
        key_hash = self.getHash(jenisObat)
        key_value = [jenisObat,namaObat]

        if self.map[key_hash] is None:
            self.map[key_hash] = list(key_value)
            return True
        
        else:
            key_hash = self.probing(jenisObat)
            if key_hash is None:
                print("Rak obat sudah penuh")
                return False
        
        self.map[key_hash] = list([key_value])
        return False
    
    def lihatObat(self, jenisObat):
        key_hash = self.getHash(jenisObat)
        if(self.map[key_hash] is not None) and (self.map[key_hash] != 'diambil'):
            for index in range(self.size):
                key_hash = self.linearProbing(jenisObat,index)
                if(self.map[key_hash][0][0] == jenisObat):
                    return self.map[key_hash][0][1]
        print("Key ", jenisObat, " tidak ditemukan")
        return None
    
    def ambilObat(self, jenisObat):
        key_hash = self.getHash(jenisObat)
        if self.map[key_hash] is None:
            return False
        for index in range(self.size):
            key_hash = self.linearProbing(jenisObat, index)
            if(self.map[key_hash][0][0] == jenisObat):
                print("Mengambil ", jenisObat)
                self.map[key_hash] = "diambil"
                return True
        print("Key ", jenisObat, " tidak ditemukan")
        return False
    
    def printAll(self):
        print("===================== List Obat =====================")
        for isi in range(len(self.map)):
            if isi is not None:
                for i in range(len(self.map[isi])):
                    print("Nama : ",self.map[isi+3][1]," <> Jenis : ",self.map[isi+3][0])
                    print("Nama : ",self.map[isi+1][1]," <> Jenis : ",self.map[isi+1][0])
                    print("Nama : ",self.map[isi+2][1]," <> Jenis : ",self.map[isi+2][0])
                    break
                break

        for item2 in self.map:
            for isi in item2:
                for i in range(len(isi)):
                    print("Nama : ",isi[i+1]," <> Jenis : ", isi[i])
                    print("=====================================================")
                    break
                break
            break


if __name__ == "__main__":
    rak1 = RakObat()
    rak1.tambahObat("Covid", "AstraZeneca (A01)")
    rak1.tambahObat("Flu", "UltraFlu (A02)")
    rak1.tambahObat("Sakit Kepala", "Paramex (A03)")
    rak1.tambahObat("Maag", "Pro Maag (A04)")
    rak1.tambahObat("Sakit Kepala", "Bodrex (A05)")

    rak1.printAll()
    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))


    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()