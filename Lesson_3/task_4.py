expr_1 = 17 / 2 * 3 + 2
expr_1_parentheses = ((17 / 2) * 3) + 2

expr_2 = 2 + 17 / 2 * 3
expr_2_parentheses = 2 + ((17 / 2) * 3)

expr_3 = 19 % 4 + 15 / 2 * 3
expr_3_parentheses = (19 % 4) + ((15 / 2) * 3)

expr_4 = (15 + 6) - 10 * 4
expr_4_parentheses = (15 + 6) - (10 * 4)

expr_5 = 17 / 2 % 2 * 3 ** 3
expr_5_parentheses = ((17 / 2) % 2) * (3 ** 3)

print(expr_1 == expr_1_parentheses)
print(expr_2 == expr_2_parentheses)
print(expr_3 == expr_3_parentheses)
print(expr_4 == expr_4_parentheses)
print(expr_5 == expr_5_parentheses)
