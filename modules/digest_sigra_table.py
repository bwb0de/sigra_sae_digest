import csv
import codecs
from collections import Counter, OrderedDict


def print_counter(counterObj, sigma=False):
    for k in sorted(counterObj.keys()):
        print(k, counterObj[k])

def print_counter_variation(counterObj):
    first_element_value = None
    first_element_key = None
    result = OrderedDict()
    for k in sorted(counterObj.keys()):
        if first_element_value == None:
            first_element_key = k
            first_element_value = counterObj[k]
        else:
            result['variação de '+ first_element_key + ' à ' + k] = counterObj[k] - first_element_value
            first_element_key = k
            first_element_value = counterObj[k]
    print_counter(result)
    return result

def print_sigma_counter(counterObj):
    output = 0
    for k in counterObj.keys():
        output += counterObj[k]
    print('Total:', output)
    return output

def print_periodo_relative(counterObj, total_periodo_counter):
    for k in sorted(counterObj.keys()):
        current_value = counterObj[k]
        periodo = k.split('/')[0]
        current_value_periodo_total = total_periodo_counter[periodo]
        print('percentual em relação ao total do periodo, {}:'.format(k), current_value/current_value_periodo_total)


def print_all_counter_info(counterObj, sigma=True, variation=True, titulo=False):
    print('===============================================')
    if titulo:
        print(titulo.upper())
    print_counter(counterObj)
    if variation:
        print_counter_variation(counterObj)
        print_reduced_variation(counterObj)

    if sigma:
        print_sigma_counter(counterObj)

def print_reduced_variation(counterObj):
    variation_dict = print_counter_variation(counterObj)
    result = 0
    for k in variation_dict.keys():
        result += variation_dict[k]
    print('Soma das variações:', result)



def fixers(linha):
    norte = ['AM','RR','AP','PA','TO','RO','AC']
    nordeste = ['MA','PI','CE','RN','PE','PB','SE','AL','BA']
    centro_oeste = ['MT','MS','GO', 'DF']
    sudeste = ['SP','RJ','ES','MG']
    sul = ['PR','RS','SC']

    if linha.get('periodo_estudo'):
        if linha['periodo_estudo'].find('-') == -1:
            sem = linha['periodo_estudo'].split('/')[0]
            ano = linha['periodo_estudo'].split('/')[1]
            linha['periodo_estudo'] = ano+'-'+sem
        

    if linha.get('escola_em_uf'):
        if linha['escola_em_uf'] in nordeste:
            linha['escola_em_uf'] = 'Nordeste'

        elif linha['escola_em_uf'] in norte:
            linha['escola_em_uf'] = 'Norte'

        elif linha['escola_em_uf'] in sul:
            linha['escola_em_uf'] = 'Sul'

        elif linha['escola_em_uf'] in sudeste:
            linha['escola_em_uf'] = 'Sudeste'

        elif linha['escola_em_uf'] in centro_oeste:
            linha['escola_em_uf'] = 'Centro-Oeste'

    if linha['curso_nome'] == 'Gestão de Agronegócios':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Serviço Social':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Design':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Linguística':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Sociologia':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Psicologia':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Terapia Ocupacional':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Engenharia Biomédica':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Fisioterapia':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Agronegócios':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Ciências Contábeis':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Biologia Animal':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Administração':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Biotecnologia e Biodiversidade':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Ciências Farmacêuticas':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Direito':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Estatística':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Transportes':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Teoria':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Crítica e História da Arte':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Engenharia Florestal':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Engenharia Mecatrônica':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Engenharia Química':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Artes':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Engenharia Aeroespacial':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Pedagogia':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Jornalismo':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Mestrado Profissional em Matemática':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Museologia':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Engenharia de Sistemas Eletrônicos e de Automação':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Geociências Aplicadas':
        linha['curso_area'] = 'Ciências Naturais e Engenharias' #verificar

    elif linha['curso_nome'] == 'Ensino de Ciências':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Ciência da Computação':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Filosofia':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Geologia':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Física':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Engenharia Eletrônica':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Letras-Tradução':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Tecnologia Ambiental e Recursos Hídricos':
        linha['curso_area'] = 'Ciências Naturais e Engenharias' #verificar

    elif linha['curso_nome'] == 'Medicina Veterinária':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Engenharia Automotiva':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'História':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Educação':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Engenharia Ambiental':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Medicina':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Nanociência e Nanobiotecnologia':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Arquivologia':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Educação em Ciências':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Ciências Ambientais':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Línguas Estrangeiras Aplicadas - MSI':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Artes Visuais':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Química':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Integridade de Materiais da Engenharia':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Engenharia':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Ciências Biológicas':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Economia':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Ecologia':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Ciência da Informação':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Enfermagem':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Saúde Coletiva':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Desenvolvimento':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Sociedade e Cooperação Internacional':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Zoologia':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Música':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Sistemas Mecatrônicos':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Engenharia de Computação':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Ciências Econômicas':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Nutrição Humana':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Engenharia de Software':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Literatura':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Estruturas e Construção Civil':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Comunicação':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Ciência Política':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Botânica':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Gestão Ambiental':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Agronomia':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Farmácia':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Engenharia Mecânica':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Gestão do Agronegócio':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Nutrição':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Arquitetura e Urbanismo':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Engenharia Civil':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Tecnologias Química e Biológica':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Artes Cênicas':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Ciências Sociais':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Turismo':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Ciências Florestais':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Ciências Mecânicas':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Engenharia de Energia':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Ciências Médicas':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Ciências do Comportamento':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Direitos Humanos e Cidadania':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Matemática':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Fitopatologia':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Fonoaudiologia':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Biologia Microbiana':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Relações Internacionais':
        linha['curso_area'] = 'Ciências Sociais Aplicadas'

    elif linha['curso_nome'] == 'Geotecnia':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Letras-Tradução Espanhol':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Engenharia Elétrica':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Processos de Desenvolvimento Humano e Saúde':
        linha['curso_area'] = 'Ciências Biológicas'

    elif linha['curso_nome'] == 'Química Tecnológica':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Língua de Sinais Brasileira/Português como Segunda Língua':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Educação Artística':
        linha['curso_area'] = 'Artes e Letras'

    elif linha['curso_nome'] == 'Computação':
        linha['curso_area'] = 'Ciências Naturais e Engenharias'

    elif linha['curso_nome'] == 'Engenharia de Redes de Comunicação':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Geofísica':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Educação Física':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Ciências Naturais':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Biblioteconomia':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Geografia':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Antropologia':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Letras':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Psicologia Social do Trabalho e das Organizações':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Engenharia de Produção':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Biotecnologia':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Desenvolvimento Sustentável':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Gestão de Políticas Públicas':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Ciências de Materiais':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Comunicação Social':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Odontologia':
        linha['curso_area'] = 'Humanas'

    elif linha['curso_nome'] == 'Educação do Campo':
        linha['curso_area'] = 'Humanas'


    return linha


total_registros = Counter()

total_semestre_ingresso = Counter()
total_forma_ingresso = Counter()
total_ativos_e_inativos = Counter()
total_forma_saida = Counter()
total_cota = Counter()
total_turno = Counter()
total_modalidade = Counter()
total_nacionalidade = Counter()
total_pne = Counter()

total_semestre_ingresso_cota = Counter()
total_semestre_ingresso_turno = Counter()
total_semestre_ingresso_cota_turno = Counter()
total_semestre_ingresso_pne = Counter()

total_cota_universal_semestre = Counter()
total_cota_negro_semestre = Counter()
total_cota_indigena_semestre = Counter()
total_cota_alta_renda_ppi_semestre = Counter()
total_cota_alta_renda_nppi_semestre = Counter()
total_cota_baixa_renda_ppi_semestre = Counter()
total_cota_baixa_renda_nppi_semestre = Counter()


cpf_controller = {}


with open('Tabelao.csv') as f:
    dados = csv.DictReader(f, delimiter='\t')
    fields = dados.fieldnames
    dados = list(dados)

    for linha in dados:
        if linha['semestre_ingresso'].find('/0') == -1:
            total_registros.update(['total'])
            total_semestre_ingresso.update([linha['semestre_ingresso']])
            if linha['pne'] == 'Sim':
                total_pne.update(['Total PNE'])
                total_semestre_ingresso_pne.update([linha['semestre_ingresso'] + '/' + 'PNE'])
            if linha['ingresso_extenso'].find('Convenio') != -1:
                total_forma_ingresso.update(['Convênios'])
            else:
                total_forma_ingresso.update([linha['ingresso_extenso']])
            
            total_cota.update([linha['cota']])
            total_semestre_ingresso_cota.update()
            
            if linha['cota'].find('Universal') != -1:
                total_cota_universal_semestre.update([linha['semestre_ingresso'] + '/' + 'Universal'])
            elif linha['cota'] == 'Negros':
                total_cota_negro_semestre.update([linha['semestre_ingresso'] + '/' + 'Negro'])
            elif linha['cota'] == 'Indigena':
                total_cota_indigena_semestre.update([linha['semestre_ingresso'] + '/' + 'Indígena'])
            elif linha['cota'] == 'Alta Renda PPI' or linha['cota'] == 'Alta Renda PPI-PCD' or linha['cota'] == 'Alta Renda PPI-PSDA':
                total_cota_alta_renda_ppi_semestre.update([linha['semestre_ingresso'] + '/' + 'Alta Renda PPI'])
            elif linha['cota'] == 'Alta Renda não PPI' or linha['cota'] == 'Alta Renda não PPI-PCD' or linha['cota'] == 'Alta Renda não PPI-PSDA':
                total_cota_alta_renda_nppi_semestre.update([linha['semestre_ingresso'] + '/' + 'Alta Renda não PPI'])
            elif linha['cota'] == 'Baixa Renda PPI' or linha['cota'] == 'Baixa Renda PPI-PCD' or linha['cota'] == 'Baixa Renda PPI-PSDA':
                total_cota_baixa_renda_ppi_semestre.update([linha['semestre_ingresso'] + '/' + 'Baixa Renda PPI'])
            elif linha['cota'] == 'Baixa Renda não PPI' or linha['cota'] == 'Baixa Renda não PPI-PCD' or linha['cota'] == 'Baixa Renda não PPI-PSDS':
                total_cota_baixa_renda_nppi_semestre.update([linha['semestre_ingresso'] + '/' + 'Baixa Renda não PPI'])



            if linha['turno_tipo_curso'].find('Diurno') != -1:
                total_turno.update(['Diurno'])
                total_semestre_ingresso_turno.update([linha['semestre_ingresso'] + '/' + 'Diurno'])
                #total_semestre_ingresso_cota_turno.update([linha['semestre_ingresso'] + '/' + 'Diurno' + '/' + linha['cota']])
            elif linha['turno_tipo_curso'].find('Noturno') != -1:
                total_turno.update(['Noturno'])
                total_semestre_ingresso_turno.update([linha['semestre_ingresso'] + '/' + 'Noturno'])
                #total_semestre_ingresso_cota_turno.update([linha['semestre_ingresso'] + '/' + 'Noturno' + '/' + linha['cota']])

            if linha['turno_tipo_curso'].find('EAD') != -1:
                total_modalidade.update(['EAD' + '/' + linha['nacionalidade']])
            elif linha['turno_tipo_curso'].find('Presencial') != -1:
                total_modalidade.update(['Presencial' + '/' + linha['nacionalidade']])

            if linha['forma_saida'] == "Em curso - Ativo":
                total_ativos_e_inativos.update(['Ativos'])
            else:
                total_ativos_e_inativos.update(['Inativos'])
                total_forma_saida.update([linha['forma_saida']])


    print_all_counter_info(total_registros, variation=False)
    print_all_counter_info(total_semestre_ingresso, variation=False, titulo='total por semestre de ingresso')
    print_all_counter_info(total_forma_ingresso, variation=False, titulo='total por forma de ingresso')
    print_all_counter_info(total_forma_saida, variation=False, titulo='total por forma de saída')
    print_all_counter_info(total_ativos_e_inativos, variation=False, titulo='total ativos/inativos')
    print_all_counter_info(total_modalidade, variation=False, titulo='total por modalidade')
    print_all_counter_info(total_turno, variation=False, titulo='total por turno')
    print_all_counter_info(total_cota, variation=False, titulo='total por tipo de cota')
    #print_all_counter_info(total_semestre_ingresso_cota, variation=False, titulo='total por semestre de ingresso')
    #print_all_counter_info(total_semestre_ingresso_cota_turno, variation=False)
    print_all_counter_info(total_pne, variation=False)
    print_all_counter_info(total_semestre_ingresso_pne)

    print_all_counter_info(total_cota_universal_semestre, titulo='total estudantes não cotistas por semestre')
    print_all_counter_info(total_cota_negro_semestre, titulo='total estudantes com cota negro por semestre')
    print_all_counter_info(total_cota_indigena_semestre, titulo='total estudantes com cota indígena por semestre')
    print_all_counter_info(total_cota_alta_renda_ppi_semestre, titulo='total de estudantes Alta Renda PPI por semestre')
    print_all_counter_info(total_cota_alta_renda_nppi_semestre, titulo='total de estudantes Alta Renda não PPI por semestre')
    print_all_counter_info(total_cota_baixa_renda_ppi_semestre, titulo='total de estudantes Baixa Renda PPI por semestre')
    print_all_counter_info(total_cota_baixa_renda_nppi_semestre, titulo='total de estudantes Baixa Renda não PPI por semestre')

