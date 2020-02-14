import csv
import codecs
from collections import Counter, OrderedDict

output = []

with open('NovoSAE_2019-2.csv') as file1:
    with open('NovoSAE_2018-1_2018-2_2019-1.csv') as file2:
        fields = []

        fill_fields = False

        for linha in csv.DictReader(file2, delimiter='\t'):
            linha['Estudante possui outra graduacao'] = ''
            linha['Justificativa da Desclassificação'] = ''
            linha['Pontuação creche'] = ''
            linha['Telefone'] = ''

            output.append(linha)

        for linha in csv.DictReader(file1, delimiter='\t'):
            if not fill_fields:
                fill_fields = True
                for field in linha.keys():
                    fields.append(field)

            output.append(linha)
        
        with open('novo_sae_full_table.csv','w') as output_file:
            w = csv.DictWriter(output_file, sorted(fields), delimiter='\t')
            w.writeheader()
            w.writerows(output)

