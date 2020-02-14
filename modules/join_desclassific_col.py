import csv
import codecs
from collections import Counter, OrderedDict

output = []

with open('novo_sae_full_table.csv') as f:
    fill_fields = False
    fields = []
    for linha in csv.DictReader(f, delimiter='\t'):
        if not fill_fields:
            fill_fields = True
            for field in linha.keys():
                fields.append(field)
            fields.append('justif_desclassific')

        linha['justif_desclassific'] = linha['Justificativa da Desclassificação'] + ' ' + linha['Justificativa da Recusa do Programa']
        output.append(linha)


    with open('novo_sae_full_table2.csv','w') as output_file:
        w = csv.DictWriter(output_file, sorted(fields), delimiter='\t')
        w.writeheader()
        w.writerows(output)

