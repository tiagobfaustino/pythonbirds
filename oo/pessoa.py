class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(p)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

