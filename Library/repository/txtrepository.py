from domain.Book import Book


class TxtRepository:

    def __init__(self, txt_file):
        self.txt_file = txt_file
        self.lista_carti = []

    def load_from_file(self):
        with open(self.txt_file, 'r') as f:
            for line in f:
                line1 = line.split(',')
                if len(line1) >= 4:
                    id_c = int(line1[0])
                    titlu = line1[1]
                    descriere = line1[2]
                    autor = line1[3]
                    self.lista_carti.append(Book(id_c, titlu, descriere, autor))
                else:
                    pass

    def store_to_file(self, id, titlu, descriere, autor):
        self.lista_carti.append(Book(id, titlu, descriere, autor))
        with open(self.txt_file, 'w') as f:
            for carte in self.lista_carti:
                stri = str(carte.id) + ',' + carte.titlu + ',' + carte.descriere + ',' + carte.autor + '\n'
                f.write(stri)

    def returnare(self):
        self.load_from_file()
        return self.lista_carti
