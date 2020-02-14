import csv
import codecs
from collections import Counter, OrderedDict

'''
['JCOL', 'matricula', 'nome', 'periodo_estudo', 'motivos', 'curso_nivel',
 'curso_nome', 'campus', 'periodo_ingresso_unb', 'forma_ingresso',
 'sexo', 'cpf', 'isencao_vestibular', 'teve_abatimento', 'cor', 
 'escola_em_tipo', 'escola_em_nome', 'escola_em_cidade', 'escola_em_uf', 
 'fez_pre_vestibular', 'faz_outro_curso_superior', 'outro_curso_superior_ies', 
 'fez_outro_curso_superior', 'situacao_prof_corrente', 'situacao_prof_anterior', 
 'contribui_p_rendafam', 'cidade_moradia_sae', 'endereco_moradia_sae', 
 'endereco_moradia_sigra', 'email', 'com_quem_reside', 'situacao_residencia_familia', 
 'estado_civil_estudante', 'pai_nome', 'pai_situacao', 'pai_cpf', 'pai_cidade', 
 'pai_endereco', 'pai_endereco_uf', 'pai_escolaridade', 'pai_profissao', 'pai_remuneracao', 
 'mae_nome', 'mae_situacao', 'mae_cpf', 'mae_cidade', 'mae_endereco', 'mae_endereco_uf', 
 'mae_escolaridade', 'mae_profissao', 'mae_remuneracao', 'transporte_usado', 'justificativa', 
 'pontuacao_vinculo_emprego_estudante', 'pontuacao_cidade_estudante', 
 'pontuacao_vinculo_emprego_pai', 'pontuacao_vinculo_emprego_mae', 
 'pontuacao_vinculo_emprego_mantenedor', 'pontuacao_fx_renda', 'pontuacao_parecer', 
 'pontuacao_grupo', 'pontuacao_assistente_social']

Região Centro-Oeste — (Goiás, Mato Grosso e Mato Grosso do Sul) e o Distrito Federal
Região Nordeste — (Alagoas, Bahia, Ceará, Maranhão, Paraíba, Pernambuco, Piauí, Rio Grande do Norte e Sergipe)
Região Norte — (Acre, Amapá, Amazonas, Pará, Rondônia, Roraima e Tocantins)
Região Sudeste — (Espírito Santo, Minas Gerais, Rio de Janeiro e São Paulo)
Região Sul — (Paraná, Rio Grande do Sul e Santa Catarina)

'''

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




def print_all_counter_info(counterObj, sigma=True, variation=True):
    print('===============================================')
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
total_gr = Counter()
total_fi = Counter()

total_fi_dupla_hab = Counter()
total_fi_refugiado = Counter()
total_fi_vest = Counter()
total_fi_matcor = Counter()
total_fi_enem = Counter()
total_fi_sisu = Counter()
total_fi_tranf = Counter()
total_fi_pas = Counter()
total_fi_mudanca_curso = Counter()
total_fi_funai = Counter()
total_fi_duplo_curso = Counter()
total_fi_mudanca_turno = Counter()
total_fi_transf_obr = Counter()
total_fi_dupla_dip = Counter()
total_fi_registro_dip = Counter()
total_fi_pec_g = Counter()
total_fi_port_dip_curso_sup = Counter()
total_fi_mudanca_hab = Counter()

total_regiao_nordeste = Counter()
total_regiao_norte = Counter()
total_regiao_centro_o = Counter()
total_regiao_sudeste = Counter()
total_regiao_sul = Counter()

total_sexo_masculino = Counter()
total_sexo_feminino = Counter()

total_cor = Counter()

total_cor_parda = Counter()
total_cor_branca = Counter()
total_cor_preta = Counter()
total_cor_amarela = Counter()
total_cor_indigena = Counter()

total_periodo = Counter()

total_sexo = Counter()
total_curso_nv = Counter()
total_curso_nome = Counter()

total_estudos_novos = Counter()
total_cpf = Counter()

cpf_controller = {}


with open('old_sae_nfo.csv') as f:
    dados = csv.DictReader(f, delimiter='\t')
    fields = dados.fieldnames
    fields.append('estudo_novo')
    fields.append('curso_area')
    dados = list(dados)

    for linha in dados:
        linha['estudo_novo'] = False
        linha['curso_area'] = ''
        linha = fixers(linha)
        total_registros.update(['t'])
        total_sexo.update([linha['sexo']])
        total_curso_nome.update([linha['curso_nome']])
        total_cor.update([linha['cor']])
        total_periodo.update([linha['periodo_estudo']])
        total_cpf.update([linha['cpf']])

        
        if linha['curso_nivel'] == 'Graduação':
            if not cpf_controller.get(linha['cpf']):
                cpf_controller[linha['cpf']] = True
                linha['estudo_novo'] = True
                total_estudos_novos.update([linha['periodo_estudo']])

            total_gr.update(['t_gr'])

            if linha['cor'] == 'Parda':
                total_cor_parda.update([linha['periodo_estudo'] + '/' + linha['cor']])
            elif linha['cor'] == 'Branca':
                total_cor_branca.update([linha['periodo_estudo'] + '/' + linha['cor']])
            elif linha['cor'] == 'Preta':
                total_cor_preta.update([linha['periodo_estudo'] + '/' + linha['cor']])
            elif linha['cor'] == 'Amarela':
                total_cor_amarela.update([linha['periodo_estudo'] + '/' + linha['cor']])
            elif linha['cor'] == 'Indígena':
                total_cor_indigena.update([linha['periodo_estudo'] + '/' + linha['cor']])

            if linha['sexo'] == 'Masculino':
                total_sexo_masculino.update([linha['periodo_estudo'] + '/' + 'M'])
            elif linha['sexo'] == 'Feminino':
                total_sexo_feminino.update([linha['periodo_estudo'] + '/' + 'F'])

            if linha['escola_em_uf'] == 'Centro-Oeste':
                total_regiao_centro_o.update([linha['periodo_estudo'] + '/' + linha['escola_em_uf']])
            elif linha['escola_em_uf'] == 'Sudeste':
                total_regiao_sudeste.update([linha['periodo_estudo'] + '/' + linha['escola_em_uf']])
            elif linha['escola_em_uf'] == 'Nordeste':
                total_regiao_nordeste.update([linha['periodo_estudo'] + '/' + linha['escola_em_uf']])
            elif linha['escola_em_uf'] == 'Norte':
                total_regiao_norte.update([linha['periodo_estudo'] + '/' + linha['escola_em_uf']])
            elif linha['escola_em_uf'] == 'Sul':
                total_regiao_sul.update([linha['periodo_estudo'] + '/' + linha['escola_em_uf']])

            if linha['forma_ingresso'] == 'Dupla Habilitação':
                total_fi_dupla_hab.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Refugiado':
                total_fi_refugiado.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Vestibular':
                total_fi_vest.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Matrícula Cortesia':
                total_fi_matcor.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Enem':
                total_fi_enem.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Sisu-Sistema de Seleção Unificada':
                total_fi_sisu.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Transferência Facultativa':
                total_fi_tranf.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Programa de Avaliação Seriada':
                total_fi_pas.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Mudança de Curso':
                total_fi_mudanca_curso.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Convênio Funai':
                total_fi_funai.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Duplo Curso':
                total_fi_duplo_curso.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Mudança de Turno':
                total_fi_mudanca_turno.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Transferência Obrigatória':
                total_fi_transf_obr.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Dupla Diplomação':
                total_fi_dupla_dip.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Registro de Diploma':
                total_fi_registro_dip.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Acordo Cultural-PEC-G':
                total_fi_pec_g.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Portador Diplom Curso Superior':
                total_fi_port_dip_curso_sup.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
            elif linha['forma_ingresso'] == 'Mudança de Habilitação':
                total_fi_mudanca_hab.update([linha['periodo_estudo'] + '/' + linha['forma_ingresso']])
    
    with open('saida_csv.csv', 'w') as output_f:
        w = csv.DictWriter(output_f, fields, delimiter='\t')
        w.writeheader()
        w.writerows(dados)
        
    
    print_counter(total_registros)
    print_counter(total_gr)
    print('Total_entries:', len(total_cpf.keys()))
    print(total_gr['t_gr'] / total_registros['t'])
    print(total_curso_nome.keys())
    #print_all_counter_info(total_fi_vest)
    #print_all_counter_info(total_fi_enem)
    #print_all_counter_info(total_fi_sisu)
    #print_all_counter_info(total_fi_pas)
    #print_all_counter_info(total_regiao_centro_o)
    #print_all_counter_info(total_regiao_nordeste)
    #print_all_counter_info(total_regiao_norte)
    #print_all_counter_info(total_regiao_sudeste)
    #print_all_counter_info(total_regiao_sul)
    #print_all_counter_info(total_sexo_feminino)
    #print_all_counter_info(total_sexo_masculino)
    #print_all_counter_info(total_cor_parda)
    #print_all_counter_info(total_cor_branca)
    #print_all_counter_info(total_cor_preta)
    #print_all_counter_info(total_cor_amarela)
    #print_all_counter_info(total_cor_indigena)
    #print(len(total_cpf.keys()))

    print('Estudos Novos...')
    print_counter(total_estudos_novos)
    print_sigma_counter(total_estudos_novos)
    print('')
    print('Total Estudos por período...')
    print_counter(total_periodo)
    print_sigma_counter(total_periodo)

    #print_periodo_relative(total_cor_parda, total_periodo)
    #print_periodo_relative(total_cor_branca, total_periodo)
    #print_periodo_relative(total_cor_preta, total_periodo)
    #print_periodo_relative(total_cor_amarela, total_periodo)
    #print_periodo_relative(total_cor_indigena, total_periodo)