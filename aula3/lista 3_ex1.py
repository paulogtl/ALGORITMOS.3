vendas = {
    1: 10,  2: 15,  3: 20,  4: 5,   5: 0,
    6: 8,   7: 12,  8: 14,  9: 18, 10: 25,
    11: 12, 12: 8,  13: 7,  14: 10, 15: 20,
    16: 16, 17: 15, 18: 18, 19: 20, 20: 10,
    21: 9,  22: 2,  23: 5,  24: 12, 25: 14,
    26: 18, 27: 22, 28: 25, 29: 13, 30: 18,
    31: 12
}

total_vendas = sum(vendas.values())

maior_venda = max(vendas.values())
menor_venda = min(vendas.values())

dias_maior = [dia for dia, v in vendas.items() if v == maior_venda]
dias_menor = [dia for dia, v in vendas.items() if v == menor_venda]

media_vendas = total_vendas / len(vendas)

dias_acima_media = [dia for dia, v in vendas.items() if v > media_vendas]

print("Análise de Vendas Mensais")
print(f"Total de vendas no mês: {total_vendas}")
print(f"Dia(s) com mais vendas: {dias_maior} ({maior_venda} vendas)")
print(f"Dia(s) com menos vendas: {dias_menor} ({menor_venda} vendas)")
print(f"Média de vendas por dia: {media_vendas:.2f}")
print(f"Dias com vendas acima da média ({len(dias_acima_media)} dias): {', '.join(map(str, dias_acima_media))}")
