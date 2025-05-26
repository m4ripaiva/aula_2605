class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

produto1 = Produto("Caderno", 15.0, 10)
produto2 = Produto("Caneta", 2.5, 20)


valor_total_estoque = produto1.valor_total() + produto2.valor_total()
print(f"Valor total em estoque: R$ {valor_total_estoque:.2f}")  