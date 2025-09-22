#emprestimos = [
#    ["Dom Casmurro", "Ana", 5],
#    ["1984", "Carlos", 12],
#    ["O Hobbit", "Marina", 3],
#    ["Senhor dos Anéis", "Paula", 8]
#]

emprestimos = {
    "Dom Casmurro": {
        "Alugada p/": "Ana",
        "Dias em atraso": 5
    },
    "1984": {
        "Alugada p/": "Carlos",
        "Dias em atraso": 12
    },
    "Hobbit": {
        "Alugada p/": "Marina",
        "Dias em atraso": 3
    },
    "Senhor dos Anéis": {
        "Alugada p/": "Paula",
        "Dias em atraso": 8
    }
}

atrasados = {titulo: dados for titulo, dados in emprestimos.items() if dados["Dias em atraso"] > 7}

livro_mais_tempo = max(emprestimos.items(), key=lambda item: item[1]["Dias em atraso"])

usuarios = {dados["Alugada p/"] for dados in emprestimos.values()}

soma_dias = sum(dados["Dias em atraso"] for dados in emprestimos.values())
media_dias = soma_dias / len(emprestimos)

print("Sistema de Biblioteca")
print("Livros emprestados há mais de 7 dias:")
for titulo, dados in atrasados.items():
    print(f"   - {titulo} ({dados['Alugada p/']}, {dados['Dias em atraso']} dias)")

print(f"Livro emprestado há mais tempo: {livro_mais_tempo[0]} ({livro_mais_tempo[1]['Dias em atraso']} dias)")
print(f"Usuários com livros emprestados: {', '.join(usuarios)}")
print(f"Média de dias de empréstimo: {media_dias:.2f}")

