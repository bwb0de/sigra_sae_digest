import csv
import codecs
from collections import Counter, OrderedDict

'''
cpf
matricula
periodo
JCOL
dt_encerramento
dt_pontuacao
dt_preenchimento
'''

output = []

with open('novo_sae_full_table2.csv') as f:
    fill_fields = False
    fields = []
    for linha in csv.DictReader(f, delimiter='\t'):
        if not fill_fields:
            fill_fields = True
            for field in linha.keys():
                fields.append(field)
            fields.append('cpf')
            fields.append('matricula')
            fields.append('periodo')
            fields.append('dt_encerramento')
            fields.append('dt_pontuacao')
            fields.append('dt_preenchimento')
            fields.append('JCOL')
        
        linha['cpf'] = linha['CPF do aluno'].zfill(11)[:-2] + '-' + linha['CPF do aluno'].zfill(11)[-2:]
        linha['matricula'] = linha['Matricula'][:2] + '/' + linha['Matricula'][2:]
        linha['periodo'] = linha['Período'][:4] + '-' + linha['Período'][4:]
        linha['JCOL'] = linha['matricula'] + '::' + linha['Período'][4:] + '/' + linha['Período'][:4]
        linha['justif_desclassific'] = linha['justif_desclassific'].strip()
        
        try:
            dte = linha['Data Encerramento'].split('/')
            linha['dt_encerramento'] = dte[2] + '-' + dte[1] + '-' + dte[0]
        except IndexError:
            linha['dt_encerramento'] = linha['Data Encerramento']

        try:
            dtpt = linha['Data Pontuação'].split('/')
            linha['dt_pontuacao'] = dtpt[2] + '-' + dtpt[1] + '-' + dtpt[0]
        except IndexError:
            linha['dt_pontuacao'] = linha['Data Pontuação']

        try:
            dtp = linha['Data preenchimento'].split('/')
            linha['dt_preenchimento'] = dtp[2] + '-' + dtp[1] + '-' + dtp[0]
        except IndexError:
            linha['dt_preenchimento'] = linha['Data preenchimento']

        output.append(linha)


    with open('novo_sae_full_table3.csv','w') as output_file:
        w = csv.DictWriter(output_file, sorted(fields), delimiter='\t')
        w.writeheader()
        w.writerows(output)

