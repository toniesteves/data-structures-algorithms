from pilha import Pilha

# [[()]]
def expr_validator(expressao):
  for i in range(len(expressao)):
    ch = expressao[i]
    if ch == '{' or ch == '[' or ch == '(':
      pilha.empilhar(ch)
    elif ch == '}' or ch == ']' or ch == ')':
      if not pilha.pilha_vazia():
        chx = str(pilha.desempilhar())
        if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
          print('Erro: ', ch, ' na posição ', i)
          break
      else:
        print('Erro: ', ch, ' na posição ', i)
  if not pilha.pilha_vazia():
    print('Erro!')

expressao = str(input('Digite uma expressão: '))
pilha = Pilha(len(expressao))

expr_validator(expressao)
