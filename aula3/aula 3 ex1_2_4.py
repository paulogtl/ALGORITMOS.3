#1
aluno = {
    "nome": "Fulano",
    "idade": 27,
    "curso": "ESW"
}
#2
aluno.update({"nota": 9.5})
aluno.pop("idade")

print(aluno["nome"])
#4
if "curso" in aluno:
    print("Sim, curso é uma chave desse dicionário")
