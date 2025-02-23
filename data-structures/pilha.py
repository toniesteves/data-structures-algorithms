import numpy as np

class Pilha:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.topo = -1
    # Array de chars
    self.valores = np.chararray(self.capacidade, unicode = True)

  def __pilha_cheia(self):
    if self.topo == self.capacidade - 1:
      return True
    else:
      return False

  # Mudança para método público
  def pilha_vazia(self):
    if self.topo == -1:
      return True
    else:
      return False

  def empilhar(self, valor):
    if self.__pilha_cheia():
      print('A pilha está cheia')
    else:
      self.topo += 1
      self.valores[self.topo] = valor

  # Retorno do valor desempilhado
  def desempilhar(self):
    if self.pilha_vazia():
      print('A pilha está vazia')
      return -1
    else:
      valor = self.valores[self.topo]
      self.topo -= 1
      return valor

  def ver_topo(self):
    if self.topo != -1:
      return self.valores[self.topo]
    else:
      return -1