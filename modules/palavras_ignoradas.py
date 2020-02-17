#!/usr/bin/env python3
# -*- coding utf-8 -*-
#

import csv
import os
from collections import Counter

p = ['', '\\nminha', '00', 'Informações', 'outro', 'São', 'dos', 'além', 'em', 'Venho', 'Como', 'moro', 'Brasília', 'conhecidos', 'Universidade', 'Paulo', 'de', 'Campos', 'possam', 'pessoalmente', 'participar', 'ser', 'pois', 'natural', 'por', 'familiares', 'requerimento', 'estudantis', 'não', 'oferece', 'a', 'estado', 'programas', 'para', 'que', 'quanto', 'meio', '-', 'deste', 'ou', 'os', 'tanto', 'me', 'tenho', 'José', 'é', 'UnB', 'dos', 'são', 'divididos', 'Amorim', 'serem', 'estuda', 'perdida', 'Pelo', 'sua', 'arrecada', 'mãe', 'ela', 'qual', 'último', 'quantia', 'complementar', 'da', 'necessidade', 'carteira', 'em', 'eu', 'minha', 'estudo', 'via', 'reside', 'comprovante', 'onde', 'luz', 'indicando', 'oficial', 'essa', 'meu', 'viúva', 'Residimos', 'não', 'possuía', 'possui', 'dentro', 'nossa', 'com', 'e', 'durante', 'para', 'que', 'trabalhar', 'nos', 'então', 'construímos', 'declaração', 'lote', 'INSS', 'como', 'Moramos', 'mês', 'possuir', 'de', 'aos', 'ser', 'realiza', 'na', 'pagar', 'pelo', 'o', 'após', 'desse', 'padrão', 'por', 'virtude', 'sim', 'Observo', '(apenas', 'frente', '800', 'relógio', 'ficamos', 'nova', 'nós', 'mora', 'fato', 'foi', 'tio', 'também', 'construída', 'valor', 'participa', 'trabalho', 'mensal', 'estudo', '(proprietário', 'no', 'Ressalto', 'informando', 'conseguimos', 'casa', 'água', 'semana', 'carteira', 'receber', 'do', 'torno', 'hoje', 'irmão', 'a', 'concedida', 'separar', 'programas', 'relação', 'fazer', 'Martins', 'assim', 'renda', 'porém', 'Adauto', 'época', 'um', 'ainda', 'condições', 'disso', 'razão', 'lote', 'emitindo', 'entre', 'contas', 'uma', 'pois', 'tivemos', '2', 'iremos', 'nosso', 'Ainda', 'Em', 'muito', 'resíduo', 'fica', 'DF', 'fora', 'cedidos', 'mas', 'auxílios', 'situação', 'pela', 'Abadiânia', 'causa', '2015', 'geral', 'morando', 'período', 'mudei', '2/2015', 'vou', 'continuar', 'cidade', 'Go', 'estou', 'endereço', 'tive', 'ficar', 'atualmente', 'recebido', 'parte', 'unicamente', 'dinheiro', 'assistência', 'vivendo', 'ao', 'resolver', 'grande', 'mesmos', 'tais', 'estar', 'sendo', 'Devido', 'deixando', 'possibilidade', 'mantido', 'meus', 'estudantil', 'manter', 'se', 'numa', 'vejo', 'consumido', 'somando', 'só', 'particular', 'superior', 'Distrito', 'Ele', 'Física', 'Federal', 'seis', 'Unopar', 'reincidido', 'Estou', 'alguém', 'poder', 'cuidando', 'sede', 'Público', 'Seu', 'continuo', 'contratos', 'matriculado', 'ocorrendo', 'pessoas', 'oportunidades', 'todavia', 'aguardo', 'financeiras', 'vaga', 'resido', 'continuidade', 'anos', 'termo', 'Preciso', 'já', 'falta', '2014', 'formação', 'manter', 'emprego', 'mesmo', 'Educação', 'poucas', 'Secretaria', 'Sou', 'deferimento', 'Faculdade', 'membro', 'escola', 'dar', 'dezembro', 'sonho', 'financeira', 'curso', 'Ministério', 'residimos', 'baixa', 'pais', 'ver', 'núcleo', 'permaneçam', 'realizando', 'referido', 'encontra', 'Professor', 'permitem', 'três', 'trabalhou', 'contrato', 'chácara', 'momento', 'ajustamento', 'qualificadas', 'estudos', 'local', 'encontra-se', 'apenas', 'Dessa', 'permitiria', '2016', 'Molecular', 'fui', 'conta', 'estudante', 'todos', 'bolsa', 'auxilio', 'vez', 'Passarei', 'despesas', 'tal', 'Graduação', 'CAPES', 'aqui', 'gasto', 'Pós', 'programa', 'entretanto', 'esposa', 'inicio', 'pagamos', 'pouco', 'aprovado', 'dias', 'reais', 'No', 'economizar', 'das', 'Biologia', 'orçamento', 'temos', 'maneira', 'seria', 'faço', '2200', 'realizado', 'intuito', 'sistema', 'disponibilizados', 'socieconômica', 'Estudo', 'grupo', 'socioeconômico', 'eles', 'requer', 'universitária', 'complicado', 'pedido', 'possuo', 'ingressado', 'custos', 'vida', 'ter', 'própria', 'natal', 'universitário', 'agora', 'manterem', 'reduzida', 'sem', 'morava', 'única', 'mesma', 'ano', 'colocando', 'sete', 'morar', 'econômica', 'sinto', 'ganhar', 'certa', 'salário', 'direito', 'forma', 'reduzido', '7', 'tem', 'porque', 'meses', 'metade', '1', 'vivemos', 'minha', 'nunca', 'teve', 'recebo', 'há', 'isso', 'aberta', 'decorrência', 'horária', 'fico', 'demanda', 'carga', 'jantar', 'frequentemente', 'próprios', 'acarretando', 'impedida', 'tenha', 'grade', 'recursos', '\\n', 'pelos', 'porquê', 'integralmente', 'estudar', 'modo', 'sustentam', 'algum', 'realmente', 'grata', 'parentes', 'solicito', 'maior', 'obter', 'necessito', 'despesa', 'auxílio', 'desses', 'teria', 'terei', 'necessitamos', 'residencia', 'posso', 'através', 'dois', 'falando', 'todo', 'arcar', 'interesse', 'muita', 'recebomos', 'financeiramente', 'r$300', 'coisa', 'ex:', 'peço', 'remunerado', 'gastos', 'posse', 'nao', 'periodos', 'aulas']


def mudar_itens_para_lowcase(lista):
	if isinstance(lista, (list, tuple)):
		output = []
		for element in lista:
			output.append(element.lower())
		return output
	else:
		print("Argumento deve ser do tipo 'list' ou 'tuple'...")


palavras = mudar_itens_para_lowcase(p)


def word_counter(generator, colunas):
	if isinstance(colunas, (list, tuple)):
		if isinstance(generator, csv.DictReader):
			for item in generator:
				line_word_counter = Counter()
				for col in colunas:
					info = item[col]
					
					#Colocar em função
					info = info.replace(os.linesep, ' ')
					info = info.replace('\\n', ' ')
					info = info.replace(',', ' ')
					info = info.replace('.', ' ')
					info = info.replace('(', ' ')
					info = info.replace(')', ' ')
					info = info.replace('!', ' ')
					info = info.split(' ')


					relevant_info = []
					for element in info:
						element = element.lower()
						if element in palavras:
							pass
						else:
							relevant_info.append(element)
					line_word_counter.update(relevant_info)
					yield line_word_counter
	else:
		print("Argumento colunas deve ser do tipo 'list' ou 'tuple'...")


