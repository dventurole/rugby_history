#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df_rugby = pd.read_excel('Historico de jogos do Brasil_corrigido.xlsx')


# In[3]:


df_rugby.shape


# In[4]:


df_rugby.info()


# In[5]:


df_rugby.index


# In[6]:


df_rugby.head()


# In[7]:


# Criando um Dataframe apenas com registros onde a origem é BRA
df_brasil = df_rugby.loc[(df_rugby['estado_origem_time_casa'] == 'BRA') | (df_rugby['estado_origem_time_visitante'] == 'BRA')]


# In[8]:


# Eliminando registros onde a origem é BRA, mas não se tratam de seleções nacionais de Union.
df_brasil = df_brasil.loc[df_brasil['campeonato'] != 'Torneio Seven-a-side Internacionalidades']
df_brasil = df_brasil.loc[df_brasil['tipo'] != 'League']
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Brasil (Seleção Universitária)') & (df_brasil['visitante'] != 'Brasil (Seleção Universitária)')]
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Brasil (UFG)') & (df_brasil['visitante'] != 'Brasil (UFG)')]
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Brasil (USP)') & (df_brasil['visitante'] != 'Brasil (USP)')]
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Brasil Universitário') & (df_brasil['visitante'] != 'Brasil Universitário')]
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Brasil Zicosur') & (df_brasil['visitante'] != 'Brasil Zicosur')]
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Brasil Barbarians') & (df_brasil['visitante'] != 'Brasil Barbarians')]
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Seleção Paulista Universitária') & (df_brasil['visitante'] != 'Seleção Paulista Universitária')]
df_brasil = df_brasil.loc[(df_brasil['time_casa'] != 'Cobras') & (df_brasil['visitante'] != 'Cobras')]


# In[9]:


df_brasil


# In[10]:


# Construindo um novo Dataframe com as vitórias, empates e derrotas
historico_analitico_colunas = ['Jogos', 'Vitórias','Empates','Derrotas','Pto Pró','Pto Contra','Saldo','Média Pto Pró',
                               'Média Pto Contra','Pto Pró Vitórias','Pto Contra Vitórias','Saldo Pto Vitórias','Média Pto Pró Vitórias',
                               'Média Pto Contra Vitórias','Pto Pró Derrotas','Pto Contra Derrotas','Saldo Pto Derrota s','Média Pto Pró Derrotas',
                               'Média Pto Contra Derrotas','Jogos em Casa','Vitórias em Casa','Empates em casa','Derrotas em casa',
                               'Pto Pró Casa','Pto Contra Casa','Saldo Ptos Casa','Média Pto Pró Casa','Média Pto Contra Casa',
                               'Pto Pró Vitória Casa','Pto Contra Vitória Casa','Saldo Pto Vitória Casa','Média Pto Pro Vitórias Casa',
                               'Média Pto Contra Vitórias Casa','Pto Pró Derrota Casa','Pto Contra Derrota Casa','Saldo Pto Derrota Casa',
                               'Média Pto Pro Derrotas Casa','Média Pto Contra Derrotas Casa','Jogos Fora de Casa','Vitorias Fora de Casa',
                               'Empates Fora de Casa','Derrotas Fora de Casa','Pto Pró Fora','Pto Contra Fora','Saldo Fora',
                               'Média Pto Pró Fora','Média Pto Contra Fora','Pto Pró Vitória Fora','Pto Contra Vitória Fora',
                               'Saldo Pto Vitória Fora','Média Pto Pro Vitórias Fora','Média Pto Contra Vitórias Fora','Pto Pró Derrota Fora',
                               'Pto Contra Derrota Fora','Saldo Pto Derrota Fora','Média Pto Pro Derrotas Fora','Média Pto Contra Derrotas Fora']


# In[11]:


historico_analitico_index = ['Brasil XV adulto masc','Brasil XV adulto fem','Brasil XVA adulto masc','Brasil XVA adulto fem',
                             'Brasil Seven adulto masc','Brasil Seven adulto fem','Brasil Seven M18 masc']
# 'Brasil XV M18 masc', 'Brasil XV M19 masc','Brasil XV M20 masc', 'Brasil XV M21 masc', 'Brasil Seven M18 masc','Brasil Seven M20 masc','Brasil Seven M18 fem'
                             


# In[12]:


historico_analitico = pd.DataFrame('',historico_analitico_index,historico_analitico_colunas)
pd.set_option('display.max_columns', None)


# In[13]:


historico_analitico


# In[14]:


# Criando um Dataframe apenas para os resultados do Rugby XV masculino adulto do Brasil
df_brasil_xv_masc_adulto = df_brasil.query('modalidade == "XV" & genero == "Masculino" & categoria == "Adulto"')
df_brasil_xv_masc_adulto = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') | (df_brasil_xv_masc_adulto['visitante'] == 'Brasil')]


# In[15]:


df_brasil_xv_masc_adulto


# In[16]:


#Números casa - em (#), o índice de cada estatística no Dataframe
#Número de vitórias, empates e derrota em casa
vitoria_casa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].count() #21
empate_casa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & 
                                                  (df_brasil_xv_masc_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] == 0)].count() #22
derrota_casa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].count() #23

#Total de jogos em casa
jogos_casa_xvma = vitoria_casa_xvma['X'] + empate_casa_xvma['X'] + derrota_casa_xvma['X'] #20

#Quantos pontos o Brasil faz em casa #24
pontos_pro_tcasa_bra_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA')].sum()
pontos_pro_tvisitante_bra_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA')].sum()
pontos_pro_casa_xvma = pontos_pro_tcasa_bra_xvma['final_time_casa'] + pontos_pro_tvisitante_bra_xvma['final_time_visitante'] #24

#Quantos pontos o Brasil sofre em casa #25
pontos_contra_tcasa_bra_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] != 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA')].sum()
pontos_contra_tvisitante_bra_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] != 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA')].sum()
pontos_contra_casa_xvma = pontos_contra_tcasa_bra_xvma['final_time_casa'] + pontos_contra_tvisitante_bra_xvma['final_time_visitante'] #25

#Saldo de pontos em casa
saldo_casa_xvma = pontos_pro_casa_xvma - pontos_contra_casa_xvma #26

#Quantos pontos o Brasil faz quanto vence em casa #29 
#condicao_brasil_vitoria_casa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_casa_xvma = ponto_pro_vitoria_tcasa_xvma['final_time_casa'] + ponto_pro_vitoria_tvisitante_xvma['final_time_visitante'] #29

#Quantos pontos o Brasil sofre quando vence em casa #30 
ponto_contra_vitoria_tcasa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_casa_xvma = ponto_contra_vitoria_tcasa_xvma['final_time_visitante'] + ponto_contra_vitoria_tvisitante_xvma['final_time_casa'] #30

#Saldo de pontos quando o Brasil vence em casa #31
saldo_vitoria_casa_xvma = ponto_pro_vitoria_casa_xvma - ponto_contra_vitoria_casa_xvma #31

#Quantos pontos o Brasil faz quando perde em casa #34
#condicao_brasil_derrota_casa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)]

ponto_pro_derrota_tcasa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_casa_xvma = ponto_pro_derrota_tcasa_xvma['final_time_casa'] + ponto_pro_derrota_tvisitante_xvma['final_time_visitante'] #34

#Quantos pontos o Brasil sofre quando perde em casa #35
ponto_contra_derrota_tcasa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] == 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_casa_xvma = ponto_contra_derrota_tcasa_xvma['final_time_visitante'] + ponto_contra_derrota_tvisitante_xvma['final_time_casa'] #35

#Saldo de pontos quando o Brasil perde em casa #36
saldo_derrota_casa_xvma = ponto_pro_derrota_casa_xvma - ponto_contra_derrota_casa_xvma #36

#Médias
#Média de pontos que o Brasil faz nos jogos em casa #27
media_pontos_pro_casa_xvma = pontos_pro_casa_xvma/jogos_casa_xvma

#Média de pontos que o Brasil sofre nos jogos em casa #28
media_pontos_contra_casa_xvma = pontos_contra_casa_xvma/jogos_casa_xvma

#Média de pontos que o Brasil faz quando vence em casa #32
media_pontos_pro_vitoria_casa_xvma = ponto_pro_vitoria_casa_xvma/vitoria_casa_xvma #32

#Média de pontos que o Brasil sofre quando vence em casa #33
media_pontos_contra_vitoria_casa_xvma = ponto_contra_vitoria_casa_xvma/vitoria_casa_xvma #33

#Média de pontos que o Brasil faz quando perde em casa #37
media_pontos_pro_derrota_casa_xvma = ponto_pro_derrota_casa_xvma/derrota_casa_xvma #37

#Média de pontos que o Brasil sofre quando perde em casa #38
media_pontos_contra_derrota_casa_xvma = ponto_contra_derrota_casa_xvma/derrota_casa_xvma #38


# In[17]:


#Números fora de casa
#Número de vitórias, empates e derrotas fora de casa
vitoria_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].count() #40
empate_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & 
                                                  (df_brasil_xv_masc_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] == 0)].count() #41
derrota_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].count() #42

#Total de jogos fora de casa
jogos_fora_xvma = vitoria_fora_xvma['X'] + empate_fora_xvma['X'] + derrota_fora_xvma['X'] #39


#Quantos pontos o Brasil faz fora de casa #43
pontos_pro_tcasa_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA')].sum()
pontos_pro_tvisitante_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA')].sum()
pontos_pro_fora_xvma = pontos_pro_tcasa_fora_xvma['final_time_casa'] + pontos_pro_tvisitante_fora_xvma['final_time_visitante'] #43

#Quantos pontos o Brasil sofre fora de casa #44
pontos_contra_tcasa_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] != 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA')].sum()
pontos_contra_tvisitante_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] != 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA')].sum()
pontos_contra_fora_xvma = pontos_contra_tcasa_fora_xvma['final_time_casa'] + pontos_contra_tvisitante_fora_xvma['final_time_visitante'] #44

#Saldo de pontos fora de casa #45
saldo_fora_xvma = pontos_pro_fora_xvma - pontos_contra_fora_xvma #45

#Quantos pontos o Brasil faz quanto vence fora de casa #48
#condicao_brasil_vitoria_casa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_fora_xvma = ponto_pro_vitoria_tcasa_fora_xvma['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_xvma['final_time_visitante'] #48

#Quantos pontos o Brasil sofre quando vence fora de casa #49
ponto_contra_vitoria_tcasa_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_fora_xvma = ponto_contra_vitoria_tcasa_fora_xvma['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_xvma['final_time_casa'] #49

#Saldo de pontos quando o Brasil vence fora de casa #50
saldo_vitoria_fora_xvma = ponto_pro_vitoria_fora_xvma - ponto_contra_vitoria_fora_xvma #50

#Quantos pontos o Brasil faz quando perde fora de casa #53 
#condicao_brasil_derrota_casa_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)]
ponto_pro_derrota_tcasa_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_fora_xvma = ponto_pro_derrota_tcasa_fora_xvma['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_xvma['final_time_visitante']

#Quantos pontos o Brasil sofre quando perde fora de casa #54 
ponto_contra_derrota_tcasa_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_fora_xvma = df_brasil_xv_masc_adulto.loc[(df_brasil_xv_masc_adulto['visitante'] == 'Brasil') & (df_brasil_xv_masc_adulto['pais'] != 'BRA') & (df_brasil_xv_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_fora_xvma = ponto_contra_derrota_tcasa_fora_xvma['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_xvma['final_time_casa']

#Saldo de pontos quando o Brasil perde fora de casa #55
saldo_derrota_fora_xvma = ponto_pro_derrota_fora_xvma - ponto_contra_derrota_fora_xvma #55

#Médias
#Média de pontos que o Brasil faz nos jogos fora de casa #46
media_pontos_pro_fora_xvma = pontos_pro_fora_xvma/jogos_fora_xvma

#Média de pontos que o Brasil sofre nos jogos fora de casa #47
media_pontos_contra_fora_xvma = pontos_contra_fora_xvma/jogos_fora_xvma

#Média de pontos que o Brasil faz quando vence fora de casa #51
media_pontos_pro_vitoria_fora_xvma = ponto_pro_vitoria_fora_xvma/vitoria_fora_xvma #51

#Média de pontos que o Brasil sofre quando vence fora de casa #52
media_pontos_contra_vitoria_fora_xvma = ponto_contra_vitoria_fora_xvma/vitoria_fora_xvma #52

#Média de pontos que o Brasil faz quando perde fora de casa #56
media_pontos_pro_derrota_fora_xvma = ponto_pro_derrota_fora_xvma/derrota_fora_xvma #56

#Média de pontos que o Brasil sofre quando perde fora de casa #57
media_pontos_contra_derrota_fora_xvma = ponto_contra_derrota_fora_xvma/derrota_fora_xvma #57


# In[18]:


#Números consolidados - em (#), o índice de cada estatística no Dataframe
#1 a 9 - dados gerais
#10 a 14 - vitórias
#15 a 19 - derrotas
#20 a 38 - resultados em casa
#39 a 57 - resultados fora de casa
vitoria_total_xvma = vitoria_casa_xvma['X'] + vitoria_fora_xvma['X'] #2
empate_total_xvma = empate_casa_xvma['X'] + empate_fora_xvma['X'] #3
derrota_total_xvma = derrota_casa_xvma['X'] + derrota_fora_xvma['X'] #4

jogos_total_xvma = vitoria_total_xvma + empate_total_xvma + derrota_total_xvma #1

#Saldo de pontos nos jogos
pontos_pro_total_xvma = pontos_pro_casa_xvma + pontos_pro_fora_xvma #5
pontos_contra_total_xvma = pontos_contra_casa_xvma + pontos_contra_fora_xvma #6

saldo_total_xvma = pontos_pro_total_xvma - pontos_contra_total_xvma #7

#Saldo de pontos nas vitórias
pontos_pro_vitoria_xvma = ponto_pro_vitoria_casa_xvma + ponto_pro_vitoria_fora_xvma #10
pontos_contra_vitoria_xvma = ponto_contra_vitoria_casa_xvma + ponto_contra_vitoria_fora_xvma #11


saldo_vitoria_fora_xvma = ponto_pro_vitoria_fora_xvma - ponto_contra_vitoria_fora_xvma
saldo_pontos_vitoria = pontos_pro_vitoria_xvma - pontos_contra_vitoria_xvma #12

#Saldo de pontos nas derrotas
pontos_pro_derrota_xvma = ponto_pro_derrota_casa_xvma + ponto_pro_derrota_fora_xvma #15
pontos_contra_derrota_xvma = ponto_contra_derrota_casa_xvma + ponto_contra_derrota_fora_xvma #16


#saldo_derrota_fora_xvma = ponto_pro_derrota_fora_xvma - ponto_contra_derrota_fora_xvma
saldo_pontos_derrota = pontos_pro_derrota_xvma - pontos_contra_derrota_xvma #17


#Médias
media_pontos_pro_total_xvma = pontos_pro_total_xvma/jogos_total_xvma #8
media_pontos_contra_total_xvma = pontos_contra_total_xvma/jogos_total_xvma #9

media_pontos_pro_vitoria_xvma = pontos_pro_vitoria_xvma/vitoria_total_xvma #13
media_pontos_contra_vitoria_xvma = pontos_contra_vitoria_xvma/vitoria_total_xvma #14

media_pontos_pro_derrota_xvma = pontos_pro_derrota_xvma/derrota_total_xvma #18
media_pontos_contra_derrota_xvma = pontos_contra_derrota_xvma/derrota_total_xvma #19


# In[19]:


brasil_xv_masc_adulto = [jogos_total_xvma,vitoria_total_xvma,empate_total_xvma,derrota_total_xvma,pontos_pro_total_xvma, #5
                            pontos_contra_total_xvma,saldo_total_xvma,media_pontos_pro_total_xvma.round(2),media_pontos_contra_total_xvma.round(2), #9
                            pontos_pro_vitoria_xvma,pontos_contra_vitoria_xvma,saldo_pontos_vitoria,media_pontos_pro_vitoria_xvma.round(2), #13
                            media_pontos_contra_vitoria_xvma.round(2),pontos_pro_derrota_xvma,pontos_contra_derrota_xvma,saldo_pontos_derrota, #17
                            media_pontos_pro_derrota_xvma.round(2),media_pontos_contra_derrota_xvma.round(2),jogos_casa_xvma,vitoria_casa_xvma['X'], #21
                            empate_casa_xvma['X'],derrota_casa_xvma['X'],pontos_pro_casa_xvma,pontos_contra_casa_xvma,saldo_casa_xvma, #26
                            media_pontos_pro_casa_xvma.round(2),media_pontos_contra_casa_xvma.round(2),ponto_pro_vitoria_casa_xvma,ponto_contra_vitoria_casa_xvma, #30
                            saldo_vitoria_casa_xvma,media_pontos_pro_vitoria_casa_xvma['X'].round(2),media_pontos_contra_vitoria_casa_xvma['X'].round(2), #33
                            ponto_pro_derrota_casa_xvma,ponto_contra_derrota_casa_xvma,saldo_derrota_casa_xvma,media_pontos_pro_derrota_casa_xvma['X'].round(2), #37
                            media_pontos_contra_derrota_casa_xvma['X'].round(2),jogos_fora_xvma,vitoria_fora_xvma['X'],empate_fora_xvma['X'],
                            derrota_fora_xvma['X'],pontos_pro_fora_xvma,pontos_contra_fora_xvma,saldo_fora_xvma,media_pontos_pro_fora_xvma.round(2),
                            media_pontos_contra_fora_xvma.round(2),ponto_pro_vitoria_fora_xvma,ponto_contra_vitoria_fora_xvma,saldo_vitoria_fora_xvma,
                            media_pontos_pro_vitoria_fora_xvma['X'].round(2),media_pontos_contra_vitoria_fora_xvma['X'].round(2),ponto_pro_derrota_fora_xvma,
                            ponto_contra_derrota_fora_xvma,saldo_derrota_fora_xvma,media_pontos_pro_derrota_fora_xvma['X'].round(2),media_pontos_contra_derrota_fora_xvma['X'].round(2)]


# In[20]:


historico_analitico.loc['Brasil XV adulto masc'] = brasil_xv_masc_adulto


# In[21]:


# Criando um Dataframe apenas para os resultados do Rugby XV feminino adulto do Brasil
df_brasil_xv_fem_adulto = df_brasil.query('modalidade == "XV" & genero == "Feminino" & categoria == "Adulto"')
df_brasil_xv_fem_adulto = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') | (df_brasil_xv_fem_adulto['visitante'] == 'Brasil')]
df_brasil_xv_fem_adulto


# In[22]:


#Números casa - em (#), o índice de cada estatística no Dataframe
#Número de vitórias, empates e derrota em casa
vitoria_casa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].count() #21
empate_casa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & 
                                                  (df_brasil_xv_fem_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] == 0)].count() #22
derrota_casa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].count() #23

#Total de jogos em casa
jogos_casa_xvfa = vitoria_casa_xvfa['X'] + empate_casa_xvfa['X'] + derrota_casa_xvfa['X'] #20

#Quantos pontos o Brasil faz em casa #24
pontos_pro_tcasa_bra_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA')].sum()
pontos_pro_tvisitante_bra_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA')].sum()
pontos_pro_casa_xvfa = pontos_pro_tcasa_bra_xvfa['final_time_casa'] + pontos_pro_tvisitante_bra_xvfa['final_time_visitante'] #24

#Quantos pontos o Brasil sofre em casa #25
pontos_contra_tcasa_bra_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] != 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA')].sum()
pontos_contra_tvisitante_bra_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] != 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA')].sum()
pontos_contra_casa_xvfa = pontos_contra_tcasa_bra_xvfa['final_time_casa'] + pontos_contra_tvisitante_bra_xvfa['final_time_visitante'] #25

#Saldo de pontos em casa
saldo_casa_xvfa = pontos_pro_casa_xvfa - pontos_contra_casa_xvfa #26

#Quantos pontos o Brasil faz quanto vence em casa #29 
#condicao_brasil_vitoria_casa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_casa_xvfa = ponto_pro_vitoria_tcasa_xvfa['final_time_casa'] + ponto_pro_vitoria_tvisitante_xvfa['final_time_visitante'] #29

#Quantos pontos o Brasil sofre quando vence em casa #30 
ponto_contra_vitoria_tcasa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_casa_xvfa = ponto_contra_vitoria_tcasa_xvfa['final_time_visitante'] + ponto_contra_vitoria_tvisitante_xvfa['final_time_casa'] #30

#Saldo de pontos quando o Brasil vence em casa #31
saldo_vitoria_casa_xvfa = ponto_pro_vitoria_casa_xvfa - ponto_contra_vitoria_casa_xvfa #31

#Quantos pontos o Brasil faz quando perde em casa #34
#condicao_brasil_derrota_casa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)]

ponto_pro_derrota_tcasa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_casa_xvfa = ponto_pro_derrota_tcasa_xvfa['final_time_casa'] + ponto_pro_derrota_tvisitante_xvfa['final_time_visitante'] #34

#Quantos pontos o Brasil sofre quando perde em casa #35
ponto_contra_derrota_tcasa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] == 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_casa_xvfa = ponto_contra_derrota_tcasa_xvfa['final_time_visitante'] + ponto_contra_derrota_tvisitante_xvfa['final_time_casa'] #35

#Saldo de pontos quando o Brasil perde em casa #36
saldo_derrota_casa_xvfa = ponto_pro_derrota_casa_xvfa - ponto_contra_derrota_casa_xvfa #36

#Médias
#Média de pontos que o Brasil faz nos jogos em casa #27
media_pontos_pro_casa_xvfa = pontos_pro_casa_xvfa/jogos_casa_xvfa

#Média de pontos que o Brasil sofre nos jogos em casa #28
media_pontos_contra_casa_xvfa = pontos_contra_casa_xvfa/jogos_casa_xvfa

#Média de pontos que o Brasil faz quando vence em casa #32
media_pontos_pro_vitoria_casa_xvfa = ponto_pro_vitoria_casa_xvfa/vitoria_casa_xvfa #32

#Média de pontos que o Brasil sofre quando vence em casa #33
media_pontos_contra_vitoria_casa_xvfa = ponto_contra_vitoria_casa_xvfa/vitoria_casa_xvfa #33

#Média de pontos que o Brasil faz quando perde em casa #37
media_pontos_pro_derrota_casa_xvfa = ponto_pro_derrota_casa_xvfa/derrota_casa_xvfa #37

#Média de pontos que o Brasil sofre quando perde em casa #38
media_pontos_contra_derrota_casa_xvfa = ponto_contra_derrota_casa_xvfa/derrota_casa_xvfa #38


# In[23]:


#Números fora de casa
#Número de vitórias, empates e derrotas fora de casa
vitoria_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].count() #40
empate_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & 
                                                  (df_brasil_xv_fem_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] == 0)].count() #41
derrota_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].count() #42

#Total de jogos fora de casa
jogos_fora_xvfa = vitoria_fora_xvfa['X'] + empate_fora_xvfa['X'] + derrota_fora_xvfa['X'] #39


#Quantos pontos o Brasil faz fora de casa #43
pontos_pro_tcasa_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA')].sum()
pontos_pro_tvisitante_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA')].sum()
pontos_pro_fora_xvfa = pontos_pro_tcasa_fora_xvfa['final_time_casa'] + pontos_pro_tvisitante_fora_xvfa['final_time_visitante'] #43

#Quantos pontos o Brasil sofre fora de casa #44
pontos_contra_tcasa_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] != 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA')].sum()
pontos_contra_tvisitante_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] != 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA')].sum()
pontos_contra_fora_xvfa = pontos_contra_tcasa_fora_xvfa['final_time_casa'] + pontos_contra_tvisitante_fora_xvfa['final_time_visitante'] #44

#Saldo de pontos fora de casa #45
saldo_fora_xvfa = pontos_pro_fora_xvfa - pontos_contra_fora_xvfa #45

#Quantos pontos o Brasil faz quanto vence fora de casa #48
#condicao_brasil_vitoria_casa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_fora_xvfa = ponto_pro_vitoria_tcasa_fora_xvfa['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_xvfa['final_time_visitante'] #48

#Quantos pontos o Brasil sofre quando vence fora de casa #49
ponto_contra_vitoria_tcasa_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_fora_xvfa = ponto_contra_vitoria_tcasa_fora_xvfa['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_xvfa['final_time_casa'] #49

#Saldo de pontos quando o Brasil vence fora de casa #50
saldo_vitoria_fora_xvfa = ponto_pro_vitoria_fora_xvfa - ponto_contra_vitoria_fora_xvfa #50

#Quantos pontos o Brasil faz quando perde fora de casa #53 
#condicao_brasil_derrota_casa_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)]
ponto_pro_derrota_tcasa_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_fora_xvfa = ponto_pro_derrota_tcasa_fora_xvfa['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_xvfa['final_time_visitante']

#Quantos pontos o Brasil sofre quando perde fora de casa #54 
ponto_contra_derrota_tcasa_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_fora_xvfa = df_brasil_xv_fem_adulto.loc[(df_brasil_xv_fem_adulto['visitante'] == 'Brasil') & (df_brasil_xv_fem_adulto['pais'] != 'BRA') & (df_brasil_xv_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_fora_xvfa = ponto_contra_derrota_tcasa_fora_xvfa['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_xvfa['final_time_casa']

#Saldo de pontos quando o Brasil perde fora de casa #55
saldo_derrota_fora_xvfa = ponto_pro_derrota_fora_xvfa - ponto_contra_derrota_fora_xvfa #55

#Médias
#Média de pontos que o Brasil faz nos jogos fora de casa #46
media_pontos_pro_fora_xvfa = pontos_pro_fora_xvfa/jogos_fora_xvfa

#Média de pontos que o Brasil sofre nos jogos fora de casa #47
media_pontos_contra_fora_xvfa = pontos_contra_fora_xvfa/jogos_fora_xvfa

#Média de pontos que o Brasil faz quando vence fora de casa #51
media_pontos_pro_vitoria_fora_xvfa = ponto_pro_vitoria_fora_xvfa/vitoria_fora_xvfa #51

#Média de pontos que o Brasil sofre quando vence fora de casa #52
media_pontos_contra_vitoria_fora_xvfa = ponto_contra_vitoria_fora_xvfa/vitoria_fora_xvfa #52

#Média de pontos que o Brasil faz quando perde fora de casa #56
media_pontos_pro_derrota_fora_xvfa = ponto_pro_derrota_fora_xvfa/derrota_fora_xvfa #56

#Média de pontos que o Brasil sofre quando perde fora de casa #57
media_pontos_contra_derrota_fora_xvfa = ponto_contra_derrota_fora_xvfa/derrota_fora_xvfa #57


# In[24]:


#Números consolidados - em (#), o índice de cada estatística no Dataframe
#1 a 9 - dados gerais
#10 a 14 - vitórias
#15 a 19 - derrotas
#20 a 38 - resultados em casa
#39 a 57 - resultados fora de casa
vitoria_total_xvfa = vitoria_casa_xvfa['X'] + vitoria_fora_xvfa['X'] #2
empate_total_xvfa = empate_casa_xvfa['X'] + empate_fora_xvfa['X'] #3
derrota_total_xvfa = derrota_casa_xvfa['X'] + derrota_fora_xvfa['X'] #4

jogos_total_xvfa = vitoria_total_xvfa + empate_total_xvfa + derrota_total_xvfa #1

#Saldo de pontos nos jogos
pontos_pro_total_xvfa = pontos_pro_casa_xvfa + pontos_pro_fora_xvfa #5
pontos_contra_total_xvfa = pontos_contra_casa_xvfa + pontos_contra_fora_xvfa #6

saldo_total_xvfa = pontos_pro_total_xvfa - pontos_contra_total_xvfa #7

#Saldo de pontos nas vitórias
pontos_pro_vitoria_xvfa = ponto_pro_vitoria_casa_xvfa + ponto_pro_vitoria_fora_xvfa #10
pontos_contra_vitoria_xvfa = ponto_contra_vitoria_casa_xvfa + ponto_contra_vitoria_fora_xvfa #11


saldo_vitoria_fora_xvfa = ponto_pro_vitoria_fora_xvfa - ponto_contra_vitoria_fora_xvfa
saldo_pontos_vitoria = pontos_pro_vitoria_xvfa - pontos_contra_vitoria_xvfa #12

#Saldo de pontos nas derrotas
pontos_pro_derrota_xvfa = ponto_pro_derrota_casa_xvfa + ponto_pro_derrota_fora_xvfa #15
pontos_contra_derrota_xvfa = ponto_contra_derrota_casa_xvfa + ponto_contra_derrota_fora_xvfa #16


#saldo_derrota_fora_xvfa = ponto_pro_derrota_fora_xvfa - ponto_contra_derrota_fora_xvfa
saldo_pontos_derrota = pontos_pro_derrota_xvfa - pontos_contra_derrota_xvfa #17


#Médias
media_pontos_pro_total_xvfa = pontos_pro_total_xvfa/jogos_total_xvfa #8
media_pontos_contra_total_xvfa = pontos_contra_total_xvfa/jogos_total_xvfa #9

media_pontos_pro_vitoria_xvfa = pontos_pro_vitoria_xvfa/vitoria_total_xvfa #13
media_pontos_contra_vitoria_xvfa = pontos_contra_vitoria_xvfa/vitoria_total_xvfa #14

media_pontos_pro_derrota_xvfa = pontos_pro_derrota_xvfa/derrota_total_xvfa #18
media_pontos_contra_derrota_xvfa = pontos_contra_derrota_xvfa/derrota_total_xvfa #19


# In[25]:


brasil_xv_fem_adulto = [jogos_total_xvfa,vitoria_total_xvfa,empate_total_xvfa,derrota_total_xvfa,pontos_pro_total_xvfa, #5
                            pontos_contra_total_xvfa,saldo_total_xvfa,media_pontos_pro_total_xvfa.round(2),media_pontos_contra_total_xvfa.round(2), #9
                            pontos_pro_vitoria_xvfa,pontos_contra_vitoria_xvfa,saldo_pontos_vitoria,media_pontos_pro_vitoria_xvfa.round(2), #13
                            media_pontos_contra_vitoria_xvfa.round(2),pontos_pro_derrota_xvfa,pontos_contra_derrota_xvfa,saldo_pontos_derrota, #17
                            media_pontos_pro_derrota_xvfa.round(2),media_pontos_contra_derrota_xvfa.round(2),jogos_casa_xvfa,vitoria_casa_xvfa['X'], #21
                            empate_casa_xvfa['X'],derrota_casa_xvfa['X'],pontos_pro_casa_xvfa,pontos_contra_casa_xvfa,saldo_casa_xvfa, #26
                            media_pontos_pro_casa_xvfa.round(2),media_pontos_contra_casa_xvfa.round(2),ponto_pro_vitoria_casa_xvfa,ponto_contra_vitoria_casa_xvfa, #30
                            saldo_vitoria_casa_xvfa,media_pontos_pro_vitoria_casa_xvfa['X'].round(2),media_pontos_contra_vitoria_casa_xvfa['X'].round(2), #33
                            ponto_pro_derrota_casa_xvfa,ponto_contra_derrota_casa_xvfa,saldo_derrota_casa_xvfa,media_pontos_pro_derrota_casa_xvfa['X'].round(2), #37
                            media_pontos_contra_derrota_casa_xvfa['X'].round(2),jogos_fora_xvfa,vitoria_fora_xvfa['X'],empate_fora_xvfa['X'],#41
                            derrota_fora_xvfa['X'],pontos_pro_fora_xvfa,pontos_contra_fora_xvfa,saldo_fora_xvfa,media_pontos_pro_fora_xvfa.round(2), #46
                            media_pontos_contra_fora_xvfa.round(2),ponto_pro_vitoria_fora_xvfa,ponto_contra_vitoria_fora_xvfa,saldo_vitoria_fora_xvfa,#50
                            media_pontos_pro_vitoria_fora_xvfa['X'].round(2),media_pontos_contra_vitoria_fora_xvfa['X'].round(2),ponto_pro_derrota_fora_xvfa,#53
                            ponto_contra_derrota_fora_xvfa,saldo_derrota_fora_xvfa,media_pontos_pro_derrota_fora_xvfa['X'].round(2),media_pontos_contra_derrota_fora_xvfa['X'].round(2)] #57


# In[26]:


historico_analitico.loc['Brasil XV adulto fem'] = brasil_xv_fem_adulto
historico_analitico


# In[27]:


# Criando um Dataframe apenas para os resultados do Rugby XV masculino "A" adulto do Brasil
df_brasil_xv_masc_adulto_d = df_brasil.query('modalidade == "XV" & genero == "Masculino" & categoria == "Adulto"')
df_brasil_xv_masc_adulto_d = df_brasil_xv_masc_adulto_d.loc[(df_brasil_xv_masc_adulto_d['time_casa'] == 'Brasil Desenvolvimento') | (df_brasil_xv_masc_adulto_d['visitante'] == 'Brasil Desenvolvimento')]
df_brasil_xv_masc_adulto_a = df_brasil.query('modalidade == "XV" & genero == "Masculino" & categoria == "Adulto"')
df_brasil_xv_masc_adulto_a = df_brasil_xv_masc_adulto_a.loc[(df_brasil_xv_masc_adulto_a['time_casa'] == 'Brasil A') | (df_brasil_xv_masc_adulto_a['visitante'] == 'Brasil A')]
merge = [df_brasil_xv_masc_adulto_d,df_brasil_xv_masc_adulto_a]
df_brasil_xv_masc_adulto_da = pd.concat(merge)
df_brasil_xv_masc_adulto_da


# In[28]:


#Números casa - em (#), o índice de cada estatística no Dataframe
#Número de vitórias, empates e derrota em casa
vitoria_casa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count()
vitoria_casa_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count() #21
empate_casa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                  (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count()
empate_casa_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count() #22
derrota_casa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count()
derrota_casa_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count() #23

vitoria_casa_xvma_da = vitoria_casa_xvma_a + vitoria_casa_xvma_d
empate_casa_xvma_da = empate_casa_xvma_a + empate_casa_xvma_d
derrota_casa_xvma_da = derrota_casa_xvma_a + derrota_casa_xvma_d

#Total de jogos em casa
jogos_casa_xvma_a = vitoria_casa_xvma_a['X'] + empate_casa_xvma_a['X'] + derrota_casa_xvma_a['X'] #20
jogos_casa_xvma_d = vitoria_casa_xvma_d['X'] + empate_casa_xvma_d['X'] + derrota_casa_xvma_d['X'] #20
jogos_casa_xvma_da = jogos_casa_xvma_a + jogos_casa_xvma_d

#Quantos pontos o Brasil faz em casa #24
pontos_pro_tcasa_bra_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()
pontos_pro_tcasa_bra_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()

pontos_pro_tcasa_bra_xvma_da = pontos_pro_tcasa_bra_xvma_a + pontos_pro_tcasa_bra_xvma_d

pontos_pro_tvisitante_bra_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()
pontos_pro_tvisitante_bra_xvma_d = + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()

pontos_pro_tvisitante_bra_xvma_da = pontos_pro_tvisitante_bra_xvma_a + pontos_pro_tvisitante_bra_xvma_d

pontos_pro_casa_xvma_a = pontos_pro_tcasa_bra_xvma_a['final_time_casa'] + pontos_pro_tvisitante_bra_xvma_a['final_time_visitante'] #24
pontos_pro_casa_xvma_d = pontos_pro_tcasa_bra_xvma_d['final_time_casa'] + pontos_pro_tvisitante_bra_xvma_d['final_time_visitante'] #24

pontos_pro_casa_xvma_da = pontos_pro_casa_xvma_a + pontos_pro_casa_xvma_d

#Quantos pontos o Brasil sofre em casa #25
pontos_contra_tcasa_bra_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()
pontos_contra_tcasa_bra_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()

pontos_contra_tcasa_bra_xvma_da = pontos_contra_tcasa_bra_xvma_a + pontos_contra_tcasa_bra_xvma_d

pontos_contra_tvisitante_bra_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()
pontos_contra_tvisitante_bra_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA')].sum()

pontos_contra_tvisitante_bra_xvma_da = pontos_contra_tvisitante_bra_xvma_a + pontos_contra_tvisitante_bra_xvma_d

pontos_contra_casa_xvma_a = pontos_contra_tcasa_bra_xvma_a['final_time_casa'] + pontos_contra_tvisitante_bra_xvma_a['final_time_visitante'] #25
pontos_contra_casa_xvma_d = pontos_contra_tcasa_bra_xvma_d['final_time_casa'] + pontos_contra_tvisitante_bra_xvma_d['final_time_visitante'] #25

pontos_contra_casa_xvma_da = pontos_contra_casa_xvma_a + pontos_contra_casa_xvma_d

#Saldo de pontos em casa
saldo_casa_xvma_a = pontos_pro_casa_xvma_a - pontos_contra_casa_xvma_a #26
saldo_casa_xvma_d = pontos_pro_casa_xvma_d - pontos_contra_casa_xvma_d #26

saldo_casa_xvma_da = saldo_casa_xvma_a + saldo_casa_xvma_d

#Quantos pontos o Brasil faz quanto vence em casa #29
#condicao_brasil_vitoria_casa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tcasa_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_pro_vitoria_tvisitante_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_tvisitante_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_pro_vitoria_casa_xvma_a = ponto_pro_vitoria_tcasa_xvma_a['final_time_casa'] + ponto_pro_vitoria_tvisitante_xvma_a['final_time_visitante'] #29
ponto_pro_vitoria_casa_xvma_d = ponto_pro_vitoria_tcasa_xvma_d['final_time_casa'] + ponto_pro_vitoria_tvisitante_xvma_d['final_time_visitante'] #29

ponto_pro_vitoria_casa_xvma_da = ponto_pro_vitoria_casa_xvma_a + ponto_pro_vitoria_casa_xvma_d

#Quantos pontos o Brasil sofre quando vence em casa #30
ponto_contra_vitoria_tcasa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tcasa_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_contra_vitoria_tvisitante_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_tvisitante_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_contra_vitoria_casa_xvma_a = ponto_contra_vitoria_tcasa_xvma_a['final_time_visitante'] + ponto_contra_vitoria_tvisitante_xvma_a['final_time_casa'] #30
ponto_contra_vitoria_casa_xvma_d = ponto_contra_vitoria_tcasa_xvma_d['final_time_visitante'] + ponto_contra_vitoria_tvisitante_xvma_d['final_time_casa'] #30

ponto_contra_vitoria_casa_xvma_da = ponto_contra_vitoria_casa_xvma_a + ponto_contra_vitoria_casa_xvma_d

#Saldo de pontos quando o Brasil vence em casa #31
saldo_vitoria_casa_xvma_a = ponto_pro_vitoria_casa_xvma_a - ponto_contra_vitoria_casa_xvma_a #31
saldo_vitoria_casa_xvma_d = ponto_pro_vitoria_casa_xvma_d - ponto_contra_vitoria_casa_xvma_d #31

saldo_vitoria_casa_xvma_da = saldo_vitoria_casa_xvma_a + saldo_vitoria_casa_xvma_d

#Quantos pontos o Brasil faz quando perde em casa #34
#condicao_brasil_derrota_casa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)]

ponto_pro_derrota_tcasa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tcasa_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_pro_derrota_tvisitante_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_tvisitante_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_pro_derrota_casa_xvma_a = ponto_pro_derrota_tcasa_xvma_a['final_time_casa'] + ponto_pro_derrota_tvisitante_xvma_a['final_time_visitante'] #34
ponto_pro_derrota_casa_xvma_d = ponto_pro_derrota_tcasa_xvma_d['final_time_casa'] + ponto_pro_derrota_tvisitante_xvma_d['final_time_visitante'] #34

ponto_pro_derrota_casa_xvma_da = ponto_pro_derrota_casa_xvma_a + ponto_pro_derrota_casa_xvma_d

#Quantos pontos o Brasil sofre quando perde em casa #35
ponto_contra_derrota_tcasa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tcasa_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_contra_derrota_tvisitante_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_tvisitante_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] == 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_contra_derrota_casa_xvma_a = ponto_contra_derrota_tcasa_xvma_a['final_time_visitante'] + ponto_contra_derrota_tvisitante_xvma_a['final_time_casa'] #35
ponto_contra_derrota_casa_xvma_d = ponto_contra_derrota_tcasa_xvma_d['final_time_visitante'] + ponto_contra_derrota_tvisitante_xvma_d['final_time_casa'] #35

ponto_contra_derrota_casa_xvma_da = ponto_contra_derrota_casa_xvma_a + ponto_contra_derrota_casa_xvma_d

#Saldo de pontos quando o Brasil perde em casa #36
saldo_derrota_casa_xvma_a = ponto_pro_derrota_casa_xvma_a - ponto_contra_derrota_casa_xvma_a #36
saldo_derrota_casa_xvma_d = ponto_pro_derrota_casa_xvma_d - ponto_contra_derrota_casa_xvma_d #36

saldo_derrota_casa_xvma_da = saldo_derrota_casa_xvma_a + saldo_derrota_casa_xvma_d

#Médias
#Média de pontos que o Brasil faz nos jogos em casa #27
media_pontos_pro_casa_xvma_a = pontos_pro_casa_xvma_a/jogos_casa_xvma_a
media_pontos_pro_casa_xvma_d = pontos_pro_casa_xvma_d/jogos_casa_xvma_d

media_pontos_pro_casa_xvma_da = pontos_pro_casa_xvma_da/jogos_casa_xvma_da

#Média de pontos que o Brasil sofre nos jogos em casa #28
media_pontos_contra_casa_xvma_a = pontos_contra_casa_xvma_a/jogos_casa_xvma_a
media_pontos_contra_casa_xvma_d = pontos_contra_casa_xvma_d/jogos_casa_xvma_d

media_pontos_contra_casa_xvma_da = pontos_contra_casa_xvma_da/jogos_casa_xvma_da

#Média de pontos que o Brasil faz quando vence em casa #32
media_pontos_pro_vitoria_casa_xvma_a = ponto_pro_vitoria_casa_xvma_a/vitoria_casa_xvma_a #32
media_pontos_pro_vitoria_casa_xvma_d = ponto_pro_vitoria_casa_xvma_d/vitoria_casa_xvma_d #32

media_pontos_pro_vitoria_casa_xvma_da = ponto_pro_vitoria_casa_xvma_da/vitoria_casa_xvma_da

#Média de pontos que o Brasil sofre quando vence em casa #33
media_pontos_contra_vitoria_casa_xvma_a = ponto_contra_vitoria_casa_xvma_a/vitoria_casa_xvma_a #33
media_pontos_contra_vitoria_casa_xvma_d = ponto_contra_vitoria_casa_xvma_d/vitoria_casa_xvma_d #33

media_pontos_contra_vitoria_casa_xvma_da = ponto_contra_vitoria_casa_xvma_da/vitoria_casa_xvma_da

#Média de pontos que o Brasil faz quando perde em casa #37
media_pontos_pro_derrota_casa_xvma_a = ponto_pro_derrota_casa_xvma_a/derrota_casa_xvma_a #37
media_pontos_pro_derrota_casa_xvma_d = ponto_pro_derrota_casa_xvma_d/derrota_casa_xvma_d #37

media_pontos_pro_derrota_casa_xvma_da = ponto_pro_derrota_casa_xvma_da/derrota_casa_xvma_da

#Média de pontos que o Brasil sofre quando perde em casa #38
media_pontos_contra_derrota_casa_xvma_a = ponto_contra_derrota_casa_xvma_a/derrota_casa_xvma_a #38
media_pontos_contra_derrota_casa_xvma_d = ponto_contra_derrota_casa_xvma_d/derrota_casa_xvma_d #38

media_pontos_contra_derrota_casa_xvma_da = ponto_contra_derrota_casa_xvma_da/derrota_casa_xvma_da


# In[29]:


#Números fora de casa
#Número de vitórias, empates e derrotas fora de casa
vitoria_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count()
vitoria_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count() #40
empate_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                  (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count()
empate_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] == 0)].count() #41
derrota_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count()
derrota_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & 
                                                   (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].count() #42


vitoria_fora_xvma_da = vitoria_fora_xvma_a + vitoria_fora_xvma_d
empate_fora_xvma_da = empate_fora_xvma_a + empate_fora_xvma_d
derrota_fora_xvma_da = derrota_fora_xvma_a + derrota_fora_xvma_d

#Total de jogos fora de casa
jogos_fora_xvma_a = vitoria_fora_xvma_a['X'] + empate_fora_xvma_a['X'] + derrota_fora_xvma_a['X'] #39
jogos_fora_xvma_d = vitoria_fora_xvma_d['X'] + empate_fora_xvma_d['X'] + derrota_fora_xvma_d['X'] #39

jogos_fora_xvma_da = jogos_fora_xvma_a + jogos_fora_xvma_d

#Quantos pontos o Brasil faz fora de casa #43
pontos_pro_tcasa_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()
pontos_pro_tcasa_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()

pontos_pro_tvisitante_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()
pontos_pro_tvisitante_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()

pontos_pro_fora_xvma_a = pontos_pro_tcasa_fora_xvma_a['final_time_casa'] + pontos_pro_tvisitante_fora_xvma_a['final_time_visitante'] #43
pontos_pro_fora_xvma_d = pontos_pro_tcasa_fora_xvma_d['final_time_casa'] + pontos_pro_tvisitante_fora_xvma_d['final_time_visitante'] #43

pontos_pro_fora_xvma_da = pontos_pro_fora_xvma_a + pontos_pro_fora_xvma_d

#Quantos pontos o Brasil sofre fora de casa #44
pontos_contra_tcasa_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()
pontos_contra_tcasa_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()

pontos_contra_tvisitante_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()
pontos_contra_tvisitante_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['time_casa'] != 'Brasil A') & (df_brasil_xv_masc_adulto_da['visitante'] != 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA')].sum()

pontos_contra_fora_xvma_a = pontos_contra_tcasa_fora_xvma_a['final_time_casa'] + pontos_contra_tvisitante_fora_xvma_a['final_time_visitante'] #44
pontos_contra_fora_xvma_d = pontos_contra_tcasa_fora_xvma_d['final_time_casa'] + pontos_contra_tvisitante_fora_xvma_d['final_time_visitante'] #44

pontos_contra_fora_xvma_da = pontos_contra_fora_xvma_a + pontos_contra_fora_xvma_d

#Saldo de pontos fora de casa #45
saldo_fora_xvma_a = pontos_pro_fora_xvma_a - pontos_contra_fora_xvma_a #45
saldo_fora_xvma_d = pontos_pro_fora_xvma_d - pontos_contra_fora_xvma_d #45

saldo_fora_xvma_da = saldo_fora_xvma_a + saldo_fora_xvma_d

#Quantos pontos o Brasil faz quanto vence fora de casa #48
#condicao_brasil_vitoria_casa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tcasa_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_pro_vitoria_tvisitante_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_tvisitante_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_pro_vitoria_fora_xvma_a = ponto_pro_vitoria_tcasa_fora_xvma_a['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_xvma_a['final_time_visitante'] #48
ponto_pro_vitoria_fora_xvma_d = ponto_pro_vitoria_tcasa_fora_xvma_d['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_xvma_d['final_time_visitante'] #48

ponto_pro_vitoria_fora_xvma_da = ponto_pro_vitoria_fora_xvma_a + ponto_pro_vitoria_fora_xvma_d

#Quantos pontos o Brasil sofre quando vence fora de casa #49
ponto_contra_vitoria_tcasa_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tcasa_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_contra_vitoria_tvisitante_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_tvisitante_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_contra_vitoria_fora_xvma_a = ponto_contra_vitoria_tcasa_fora_xvma_a['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_xvma_a['final_time_casa'] #49
ponto_contra_vitoria_fora_xvma_d = ponto_contra_vitoria_tcasa_fora_xvma_d['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_xvma_d['final_time_casa'] #49

ponto_contra_vitoria_fora_xvma_da = ponto_contra_vitoria_fora_xvma_a + ponto_contra_vitoria_fora_xvma_d

#Saldo de pontos quando o Brasil vence fora de casa #50
saldo_vitoria_fora_xvma_a = ponto_pro_vitoria_fora_xvma_a - ponto_contra_vitoria_fora_xvma_a #50
saldo_vitoria_fora_xvma_d = ponto_pro_vitoria_fora_xvma_d - ponto_contra_vitoria_fora_xvma_d #50

saldo_vitoria_fora_xvma_da = saldo_vitoria_fora_xvma_a + saldo_vitoria_fora_xvma_d

#Quantos pontos o Brasil faz quando perde fora de casa #53 
#condicao_brasil_derrota_casa_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)]
ponto_pro_derrota_tcasa_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tcasa_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_pro_derrota_tvisitante_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_tvisitante_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_pro_derrota_fora_xvma_a = ponto_pro_derrota_tcasa_fora_xvma_a['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_xvma_a['final_time_visitante']
ponto_pro_derrota_fora_xvma_d = ponto_pro_derrota_tcasa_fora_xvma_d['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_xvma_d['final_time_visitante']

ponto_pro_derrota_fora_xvma_da = ponto_pro_derrota_fora_xvma_a + ponto_pro_derrota_fora_xvma_d

#Quantos pontos o Brasil sofre quando perde fora de casa #54 
ponto_contra_derrota_tcasa_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tcasa_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['time_casa'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] < 0)].sum()

ponto_contra_derrota_tvisitante_fora_xvma_a = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil A') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_tvisitante_fora_xvma_d = df_brasil_xv_masc_adulto_da.loc[(df_brasil_xv_masc_adulto_da['visitante'] == 'Brasil Desenvolvimento') & (df_brasil_xv_masc_adulto_da['pais'] != 'BRA') & (df_brasil_xv_masc_adulto_da['diferenca_pontos_final'] > 0)].sum()

ponto_contra_derrota_fora_xvma_a = ponto_contra_derrota_tcasa_fora_xvma_a['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_xvma_a['final_time_casa']
ponto_contra_derrota_fora_xvma_d = ponto_contra_derrota_tcasa_fora_xvma_d['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_xvma_d['final_time_casa']

ponto_contra_derrota_fora_xvma_da = ponto_contra_derrota_fora_xvma_a + ponto_contra_derrota_fora_xvma_d

#Saldo de pontos quando o Brasil perde fora de casa #55
saldo_derrota_fora_xvma_a = ponto_pro_derrota_fora_xvma_a - ponto_contra_derrota_fora_xvma_a #55
saldo_derrota_fora_xvma_d = ponto_pro_derrota_fora_xvma_d - ponto_contra_derrota_fora_xvma_d #55

saldo_derrota_fora_xvma_da = saldo_derrota_fora_xvma_a + saldo_derrota_fora_xvma_d

#Médias
#Média de pontos que o Brasil faz nos jogos fora de casa #46
media_pontos_pro_fora_xvma_a = pontos_pro_fora_xvma_a/jogos_fora_xvma_a
media_pontos_pro_fora_xvma_d = pontos_pro_fora_xvma_d/jogos_fora_xvma_d

media_pontos_pro_fora_xvma_da = pontos_pro_fora_xvma_da/jogos_fora_xvma_da

#Média de pontos que o Brasil sofre nos jogos fora de casa #47
media_pontos_contra_fora_xvma_a = pontos_contra_fora_xvma_a/jogos_fora_xvma_a
media_pontos_contra_fora_xvma_d = pontos_contra_fora_xvma_d/jogos_fora_xvma_d

media_pontos_contra_fora_xvma_da = pontos_contra_fora_xvma_da/jogos_fora_xvma_da

#Média de pontos que o Brasil faz quando vence fora de casa #51
media_pontos_pro_vitoria_fora_xvma_a = ponto_pro_vitoria_fora_xvma_a/vitoria_fora_xvma_a #51
media_pontos_pro_vitoria_fora_xvma_d = ponto_pro_vitoria_fora_xvma_d/vitoria_fora_xvma_d #51

media_pontos_pro_vitoria_fora_xvma_da = ponto_pro_vitoria_fora_xvma_da/vitoria_fora_xvma_da

#Média de pontos que o Brasil sofre quando vence fora de casa #52
media_pontos_contra_vitoria_fora_xvma_a = ponto_contra_vitoria_fora_xvma_a/vitoria_fora_xvma_a #52
media_pontos_contra_vitoria_fora_xvma_d = ponto_contra_vitoria_fora_xvma_d/vitoria_fora_xvma_d #52

media_pontos_contra_vitoria_fora_xvma_da = ponto_contra_vitoria_fora_xvma_da/vitoria_fora_xvma_da

#Média de pontos que o Brasil faz quando perde fora de casa #56
media_pontos_pro_derrota_fora_xvma_a = ponto_pro_derrota_fora_xvma_a/derrota_fora_xvma_a #56
media_pontos_pro_derrota_fora_xvma_d = ponto_pro_derrota_fora_xvma_d/derrota_fora_xvma_d #56

media_pontos_pro_derrota_fora_xvma_da = ponto_pro_derrota_fora_xvma_da/derrota_fora_xvma_da

#Média de pontos que o Brasil sofre quando perde fora de casa #57
media_pontos_contra_derrota_fora_xvma_a = ponto_contra_derrota_fora_xvma_a/derrota_fora_xvma_a #57
media_pontos_contra_derrota_fora_xvma_d = ponto_contra_derrota_fora_xvma_d/derrota_fora_xvma_d #57

media_pontos_contra_derrota_fora_xvma_da = ponto_contra_derrota_fora_xvma_da/derrota_fora_xvma_da


# In[30]:


#Números consolidados - em (#), o índice de cada estatística no Dataframe
#1 a 9 - dados gerais
#10 a 14 - vitórias
#15 a 19 - derrotas
#20 a 38 - resultados em casa
#39 a 57 - resultados fora de casa
vitoria_total_xvma_a = vitoria_casa_xvma_a['X'] + vitoria_fora_xvma_a['X'] #2
empate_total_xvma_a = empate_casa_xvma_a['X'] + empate_fora_xvma_a['X'] #3
derrota_total_xvma_a = derrota_casa_xvma_a['X'] + derrota_fora_xvma_a['X'] #4

vitoria_total_xvma_d = vitoria_casa_xvma_d['X'] + vitoria_fora_xvma_d['X'] #2
empate_total_xvma_d = empate_casa_xvma_d['X'] + empate_fora_xvma_d['X'] #3
derrota_total_xvma_d = derrota_casa_xvma_d['X'] + derrota_fora_xvma_d['X'] #4

vitoria_total_xvma_da = vitoria_total_xvma_a + vitoria_total_xvma_d #2
empate_total_xvma_da = empate_total_xvma_a + empate_total_xvma_d #3
derrota_total_xvma_da = derrota_total_xvma_a + derrota_total_xvma_d #4


jogos_total_xvma_a = vitoria_total_xvma_a + empate_total_xvma_a + derrota_total_xvma_a #1
jogos_total_xvma_d = vitoria_total_xvma_d + empate_total_xvma_d + derrota_total_xvma_d #1

jogos_total_xvma_da = jogos_total_xvma_a + jogos_total_xvma_d

#Saldo de pontos nos jogos
pontos_pro_total_xvma_a = pontos_pro_casa_xvma_a + pontos_pro_fora_xvma_a #5
pontos_contra_total_xvma_a = pontos_contra_casa_xvma_a + pontos_contra_fora_xvma_a #6

pontos_pro_total_xvma_d = pontos_pro_casa_xvma_d + pontos_pro_fora_xvma_d #5
pontos_contra_total_xvma_d = pontos_contra_casa_xvma_d + pontos_contra_fora_xvma_d #6

pontos_pro_total_xvma_da = pontos_pro_total_xvma_a + pontos_pro_total_xvma_d #5
pontos_contra_total_xvma_da = pontos_contra_total_xvma_a + pontos_contra_total_xvma_d #6

saldo_total_xvma_a = pontos_pro_total_xvma_a - pontos_contra_total_xvma_a #7
saldo_total_xvma_d = pontos_pro_total_xvma_d - pontos_contra_total_xvma_d #7

saldo_total_xvma_da = pontos_pro_total_xvma_da - pontos_contra_total_xvma_da

#Saldo de pontos nas vitórias
pontos_pro_vitoria_xvma_a = ponto_pro_vitoria_casa_xvma_a + ponto_pro_vitoria_fora_xvma_a #10
pontos_contra_vitoria_xvma_a = ponto_contra_vitoria_casa_xvma_a + ponto_contra_vitoria_fora_xvma_a #11

pontos_pro_vitoria_xvma_d = ponto_pro_vitoria_casa_xvma_d + ponto_pro_vitoria_fora_xvma_d #10
pontos_contra_vitoria_xvma_d = ponto_contra_vitoria_casa_xvma_d + ponto_contra_vitoria_fora_xvma_d #11

pontos_pro_vitoria_xvma_da = pontos_pro_vitoria_xvma_a + pontos_pro_vitoria_xvma_d #10
pontos_contra_vitoria_xvma_da = pontos_contra_vitoria_xvma_a + pontos_contra_vitoria_xvma_d #11

saldo_vitoria_fora_xvma_a = ponto_pro_vitoria_fora_xvma_a - ponto_contra_vitoria_fora_xvma_a #12 
saldo_pontos_vitoria_a = pontos_pro_vitoria_xvma_a - pontos_contra_vitoria_xvma_a #12

saldo_vitoria_fora_xvma_d = ponto_pro_vitoria_fora_xvma_d - ponto_contra_vitoria_fora_xvma_d
saldo_pontos_vitoria_d = pontos_pro_vitoria_xvma_d - pontos_contra_vitoria_xvma_d #12

saldo_vitoria_fora_xvma_da = saldo_vitoria_fora_xvma_a + saldo_vitoria_fora_xvma_d
saldo_pontos_vitoria_da = saldo_pontos_vitoria_a + saldo_pontos_vitoria_d

#Saldo de pontos nas derrotas
pontos_pro_derrota_xvma_a = ponto_pro_derrota_casa_xvma_a + ponto_pro_derrota_fora_xvma_a #15
pontos_contra_derrota_xvma_a = ponto_contra_derrota_casa_xvma_a + ponto_contra_derrota_fora_xvma_a #16

pontos_pro_derrota_xvma_d = ponto_pro_derrota_casa_xvma_d + ponto_pro_derrota_fora_xvma_d #15
pontos_contra_derrota_xvma_d = ponto_contra_derrota_casa_xvma_d + ponto_contra_derrota_fora_xvma_d #16

pontos_pro_derrota_xvma_da = pontos_pro_derrota_xvma_a + pontos_pro_derrota_xvma_d
pontos_contra_derrota_xvma_da = pontos_contra_derrota_xvma_a + pontos_contra_derrota_xvma_d

#saldo_derrota_fora_xvma_a = ponto_pro_derrota_fora_xvma_a - ponto_contra_derrota_fora_xvma_a
saldo_pontos_derrota_a = pontos_pro_derrota_xvma_a - pontos_contra_derrota_xvma_a #17
saldo_pontos_derrota_d = pontos_pro_derrota_xvma_d - pontos_contra_derrota_xvma_d #17

saldo_pontos_derrota_da = saldo_pontos_derrota_a + saldo_pontos_derrota_d

#Médias
media_pontos_pro_total_xvma_a = pontos_pro_total_xvma_a/jogos_total_xvma_a #8
media_pontos_contra_total_xvma_a = pontos_contra_total_xvma_a/jogos_total_xvma_a #9

media_pontos_pro_total_xvma_d = pontos_pro_total_xvma_d/jogos_total_xvma_d #8
media_pontos_contra_total_xvma_d = pontos_contra_total_xvma_d/jogos_total_xvma_d #9

media_pontos_pro_total_xvma_da = pontos_pro_total_xvma_da/jogos_total_xvma_da #8
media_pontos_contra_total_xvma_da = pontos_contra_total_xvma_da/jogos_total_xvma_da #9

media_pontos_pro_vitoria_xvma_a = pontos_pro_vitoria_xvma_a/vitoria_total_xvma_a #13
media_pontos_contra_vitoria_xvma_a = pontos_contra_vitoria_xvma_a/vitoria_total_xvma_a #14

media_pontos_pro_vitoria_xvma_d = pontos_pro_vitoria_xvma_d/vitoria_total_xvma_d #13
media_pontos_contra_vitoria_xvma_d = pontos_contra_vitoria_xvma_d/vitoria_total_xvma_d #14

media_pontos_pro_vitoria_xvma_da = pontos_pro_vitoria_xvma_da/vitoria_total_xvma_da #13
media_pontos_contra_vitoria_xvma_da = pontos_contra_vitoria_xvma_da/vitoria_total_xvma_da #14

media_pontos_pro_derrota_xvma_a = pontos_pro_derrota_xvma_a/derrota_total_xvma_a #18
media_pontos_contra_derrota_xvma_a = pontos_contra_derrota_xvma_a/derrota_total_xvma_a #19

media_pontos_pro_derrota_xvma_d = pontos_pro_derrota_xvma_d/derrota_total_xvma_d #18
media_pontos_contra_derrota_xvma_d = pontos_contra_derrota_xvma_d/derrota_total_xvma_d #19

media_pontos_pro_derrota_xvma_da = pontos_pro_derrota_xvma_da/derrota_total_xvma_da #18
media_pontos_contra_derrota_xvma_da = pontos_contra_derrota_xvma_da/derrota_total_xvma_da #19


# In[31]:


brasil_xv_masc_adulto_da = [jogos_total_xvma_da,vitoria_total_xvma_da,empate_total_xvma_da,derrota_total_xvma_da,pontos_pro_total_xvma_da, #5
                            pontos_contra_total_xvma_da,saldo_total_xvma_da,media_pontos_pro_total_xvma_da.round(2),media_pontos_contra_total_xvma_da.round(2), #9
                            pontos_pro_vitoria_xvma_da,pontos_contra_vitoria_xvma_da,saldo_pontos_vitoria_da,media_pontos_pro_vitoria_xvma_da.round(2), #13
                            media_pontos_contra_vitoria_xvma_da.round(2),pontos_pro_derrota_xvma_da,pontos_contra_derrota_xvma_da,saldo_pontos_derrota_da, #17
                            media_pontos_pro_derrota_xvma_da.round(2),media_pontos_contra_derrota_xvma_da.round(2),jogos_casa_xvma_da,vitoria_casa_xvma_da['X'], #21
                            empate_casa_xvma_da['X'],derrota_casa_xvma_da['X'],pontos_pro_casa_xvma_da,pontos_contra_casa_xvma_da,saldo_casa_xvma_da, #26
                            media_pontos_pro_casa_xvma_da.round(2),media_pontos_contra_casa_xvma_da.round(2),ponto_pro_vitoria_casa_xvma_da,ponto_contra_vitoria_casa_xvma_da, #30
                            saldo_vitoria_casa_xvma_da,media_pontos_pro_vitoria_casa_xvma_da['X'].round(2),media_pontos_contra_vitoria_casa_xvma_da['X'].round(2), #33
                            ponto_pro_derrota_casa_xvma_da,ponto_contra_derrota_casa_xvma_da,saldo_derrota_casa_xvma_da,media_pontos_pro_derrota_casa_xvma_da['X'].round(2), #37
                            media_pontos_contra_derrota_casa_xvma_da['X'].round(2),jogos_fora_xvma_da,vitoria_fora_xvma_da['X'],empate_fora_xvma_da['X'],
                            derrota_fora_xvma_da['X'],pontos_pro_fora_xvma_da,pontos_contra_fora_xvma_da,saldo_fora_xvma_da,media_pontos_pro_fora_xvma_da.round(2),
                            media_pontos_contra_fora_xvma_da.round(2),ponto_pro_vitoria_fora_xvma_da,ponto_contra_vitoria_fora_xvma_da,saldo_vitoria_fora_xvma_da,
                            media_pontos_pro_vitoria_fora_xvma_da['X'].round(2),media_pontos_contra_vitoria_fora_xvma_da['X'].round(2),ponto_pro_derrota_fora_xvma_da,
                            ponto_contra_derrota_fora_xvma_da,saldo_derrota_fora_xvma_da,media_pontos_pro_derrota_fora_xvma_da['X'].round(2),media_pontos_contra_derrota_fora_xvma_da['X'].round(2)]
brasil_xv_masc_adulto_da


# In[32]:


historico_analitico.loc['Brasil XVA adulto masc'] = brasil_xv_masc_adulto_da
historico_analitico


# In[33]:


# Criando um Dataframe apenas para os resultados do Rugby XV feminino "A" adulto do Brasil
df_brasil_xv_fem_adulto_a = df_brasil.query('modalidade == "XV" & genero == "Feminino" & categoria == "Adulto"')
df_brasil_xv_fem_adulto_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') | (df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A')]
df_brasil_xv_fem_adulto_a


# In[34]:


#Números casa - em (#), o índice de cada estatística no Dataframe
#Número de vitórias, empates e derrota em casa
vitoria_casa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].count() #21
empate_casa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & 
                                                  (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] == 0)].count() #22
derrota_casa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].count() #23

#Total de jogos em casa
jogos_casa_xvfa_a = vitoria_casa_xvfa_a['X'] + empate_casa_xvfa_a['X'] + derrota_casa_xvfa_a['X'] #20

#Quantos pontos o Brasil fa_az em casa #24
pontos_pro_tcasa_bra_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA')].sum()
pontos_pro_tvisitante_bra_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA')].sum()
pontos_pro_casa_xvfa_a = pontos_pro_tcasa_bra_xvfa_a['final_time_casa'] + pontos_pro_tvisitante_bra_xvfa_a['final_time_visitante'] #24

#Quantos pontos o Brasil sofre em casa #25
pontos_contra_tcasa_bra_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] != 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA')].sum()
pontos_contra_tvisitante_bra_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] != 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA')].sum()
pontos_contra_casa_xvfa_a = pontos_contra_tcasa_bra_xvfa_a['final_time_casa'] + pontos_contra_tvisitante_bra_xvfa_a['final_time_visitante'] #25

#Saldo de pontos em casa
saldo_casa_xvfa_a = pontos_pro_casa_xvfa_a - pontos_contra_casa_xvfa_a #26

#Quantos pontos o Brasil fa_az quanto vence em casa #29 
#condicao_brasil_vitoria_casa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_casa_xvfa_a = ponto_pro_vitoria_tcasa_xvfa_a['final_time_casa'] + ponto_pro_vitoria_tvisitante_xvfa_a['final_time_visitante'] #29

#Quantos pontos o Brasil sofre quando vence em casa #30 
ponto_contra_vitoria_tcasa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_casa_xvfa_a = ponto_contra_vitoria_tcasa_xvfa_a['final_time_visitante'] + ponto_contra_vitoria_tvisitante_xvfa_a['final_time_casa'] #30

#Saldo de pontos quando o Brasil vence em casa #31
saldo_vitoria_casa_xvfa_a = ponto_pro_vitoria_casa_xvfa_a - ponto_contra_vitoria_casa_xvfa_a #31

#Quantos pontos o Brasil fa_az quando perde em casa #34
#condicao_brasil_derrota_casa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)]

ponto_pro_derrota_tcasa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_casa_xvfa_a = ponto_pro_derrota_tcasa_xvfa_a['final_time_casa'] + ponto_pro_derrota_tvisitante_xvfa_a['final_time_visitante'] #34

#Quantos pontos o Brasil sofre quando perde em casa #35
ponto_contra_derrota_tcasa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] == 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_casa_xvfa_a = ponto_contra_derrota_tcasa_xvfa_a['final_time_visitante'] + ponto_contra_derrota_tvisitante_xvfa_a['final_time_casa'] #35

#Saldo de pontos quando o Brasil perde em casa #36
saldo_derrota_casa_xvfa_a = ponto_pro_derrota_casa_xvfa_a - ponto_contra_derrota_casa_xvfa_a #36

#Médias
#Média de pontos que o Brasil fa_az nos jogos em casa #27
media_pontos_pro_casa_xvfa_a = pontos_pro_casa_xvfa_a/jogos_casa_xvfa_a

#Média de pontos que o Brasil sofre nos jogos em casa #28
media_pontos_contra_casa_xvfa_a = pontos_contra_casa_xvfa_a/jogos_casa_xvfa_a

#Média de pontos que o Brasil fa_az quando vence em casa #32
media_pontos_pro_vitoria_casa_xvfa_a = ponto_pro_vitoria_casa_xvfa_a/vitoria_casa_xvfa_a #32

#Média de pontos que o Brasil sofre quando vence em casa #33
media_pontos_contra_vitoria_casa_xvfa_a = ponto_contra_vitoria_casa_xvfa_a/vitoria_casa_xvfa_a #33

#Média de pontos que o Brasil fa_az quando perde em casa #37
media_pontos_pro_derrota_casa_xvfa_a = ponto_pro_derrota_casa_xvfa_a/derrota_casa_xvfa_a #37

#Média de pontos que o Brasil sofre quando perde em casa #38
media_pontos_contra_derrota_casa_xvfa_a = ponto_contra_derrota_casa_xvfa_a/derrota_casa_xvfa_a #38


# In[35]:


#Números fora de casa
#Número de vitórias, empates e derrotas fora de casa
vitoria_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].count() + df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].count() #40
empate_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & 
                                                  (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] == 0)].count() + df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] == 0)].count() #41
derrota_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].count() + df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & 
                                                   (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].count() #42

#Total de jogos fora de casa
jogos_fora_xvfa_a = vitoria_fora_xvfa_a['X'] + empate_fora_xvfa_a['X'] + derrota_fora_xvfa_a['X'] #39


#Quantos pontos o Brasil faz fora de casa #43
pontos_pro_tcasa_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA')].sum()
pontos_pro_tvisitante_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA')].sum()
pontos_pro_fora_xvfa_a = pontos_pro_tcasa_fora_xvfa_a['final_time_casa'] + pontos_pro_tvisitante_fora_xvfa_a['final_time_visitante'] #43

#Quantos pontos o Brasil sofre fora de casa #44
pontos_contra_tcasa_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] != 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA')].sum()
pontos_contra_tvisitante_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] != 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA')].sum()
pontos_contra_fora_xvfa_a = pontos_contra_tcasa_fora_xvfa_a['final_time_casa'] + pontos_contra_tvisitante_fora_xvfa_a['final_time_visitante'] #44

#Saldo de pontos fora de casa #45
saldo_fora_xvfa_a = pontos_pro_fora_xvfa_a - pontos_contra_fora_xvfa_a #45

#Quantos pontos o Brasil faz quanto vence fora de casa #48
#condicao_brasil_vitoria_casa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_fora_xvfa_a = ponto_pro_vitoria_tcasa_fora_xvfa_a['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_xvfa_a['final_time_visitante'] #48

#Quantos pontos o Brasil sofre quando vence fora de casa #49
ponto_contra_vitoria_tcasa_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_fora_xvfa_a = ponto_contra_vitoria_tcasa_fora_xvfa_a['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_xvfa_a['final_time_casa'] #49

#Saldo de pontos quando o Brasil vence fora de casa #50
saldo_vitoria_fora_xvfa_a = ponto_pro_vitoria_fora_xvfa_a - ponto_contra_vitoria_fora_xvfa_a #50

#Quantos pontos o Brasil fa_az quando perde fora de casa #53 
#condicao_brasil_derrota_casa_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)]
ponto_pro_derrota_tcasa_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_fora_xvfa_a = ponto_pro_derrota_tcasa_fora_xvfa_a['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_xvfa_a['final_time_visitante']

#Quantos pontos o Brasil sofre quando perde fora de casa #54 
ponto_contra_derrota_tcasa_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['time_casa'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_fora_xvfa_a = df_brasil_xv_fem_adulto_a.loc[(df_brasil_xv_fem_adulto_a['visitante'] == 'Brasil A') & (df_brasil_xv_fem_adulto_a['pais'] != 'BRA') & (df_brasil_xv_fem_adulto_a['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_fora_xvfa_a = ponto_contra_derrota_tcasa_fora_xvfa_a['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_xvfa_a['final_time_casa']

#Saldo de pontos quando o Brasil perde fora de casa #55
saldo_vitoria_fora_xvfa_a = ponto_pro_derrota_fora_xvfa_a - ponto_contra_derrota_fora_xvfa_a #55

#Médias
#Média de pontos que o Brasil fa_az nos jogos fora de casa #46
media_pontos_pro_fora_xvfa_a = pontos_pro_fora_xvfa_a/jogos_fora_xvfa_a

#Média de pontos que o Brasil sofre nos jogos fora de casa #47
media_pontos_contra_fora_xvfa_a = pontos_contra_fora_xvfa_a/jogos_fora_xvfa_a

#Média de pontos que o Brasil fa_az quando vence fora de casa #51
media_pontos_pro_vitoria_fora_xvfa_a = ponto_pro_vitoria_fora_xvfa_a/vitoria_fora_xvfa_a #51

#Média de pontos que o Brasil sofre quando vence fora de casa #52
media_pontos_contra_vitoria_fora_xvfa_a = ponto_contra_vitoria_fora_xvfa_a/vitoria_fora_xvfa_a #52

#Média de pontos que o Brasil fa_az quando perde fora de casa #56
media_pontos_pro_derrota_fora_xvfa_a = ponto_pro_derrota_fora_xvfa_a/derrota_fora_xvfa_a #56

#Média de pontos que o Brasil sofre quando perde fora de casa #57
media_pontos_contra_derrota_fora_xvfa_a = ponto_contra_derrota_fora_xvfa_a/derrota_fora_xvfa_a #57


# In[36]:


#Números consolidados - em (#), o índice de cada estatística no Dataframe
#1 a 9 - dados gerais
#10 a 14 - vitórias
#15 a 19 - derrotas
#20 a 38 - resultados em casa
#39 a 57 - resultados fora de casa
vitoria_total_xvfa_a = vitoria_casa_xvfa_a['X'] + vitoria_fora_xvfa_a['X'] #2
empate_total_xvfa_a = empate_casa_xvfa_a['X'] + empate_fora_xvfa_a['X'] #3
derrota_total_xvfa_a = derrota_casa_xvfa_a['X'] + derrota_fora_xvfa_a['X'] #4

jogos_total_xvfa_a = vitoria_total_xvfa_a + empate_total_xvfa_a + derrota_total_xvfa_a #1

#Saldo de pontos nos jogos
pontos_pro_total_xvfa_a = pontos_pro_casa_xvfa_a + pontos_pro_fora_xvfa_a #5
pontos_contra_total_xvfa_a = pontos_contra_casa_xvfa_a + pontos_contra_fora_xvfa_a #6

saldo_total_xvfa_a = pontos_pro_total_xvfa_a - pontos_contra_total_xvfa_a #7

#Saldo de pontos nas vitórias
pontos_pro_vitoria_xvfa_a = ponto_pro_vitoria_casa_xvfa_a + ponto_pro_vitoria_fora_xvfa_a #10
pontos_contra_vitoria_xvfa_a = ponto_contra_vitoria_casa_xvfa_a + ponto_contra_vitoria_fora_xvfa_a #11


saldo_vitoria_fora_xvfa_a = ponto_pro_vitoria_fora_xvfa_a - ponto_contra_vitoria_fora_xvfa_a
saldo_pontos_vitoria = pontos_pro_vitoria_xvfa_a - pontos_contra_vitoria_xvfa_a #12

#Saldo de pontos nas derrotas
pontos_pro_derrota_xvfa_a = ponto_pro_derrota_casa_xvfa_a + ponto_pro_derrota_fora_xvfa_a #15
pontos_contra_derrota_xvfa_a = ponto_contra_derrota_casa_xvfa_a + ponto_contra_derrota_fora_xvfa_a #16


#saldo_derrota_fora_xvfa_a = ponto_pro_derrota_fora_xvfa_a - ponto_contra_derrota_fora_xvfa_a
saldo_pontos_derrota = pontos_pro_derrota_xvfa_a - pontos_contra_derrota_xvfa_a #17


#Médias
media_pontos_pro_total_xvfa_a = pontos_pro_total_xvfa_a/jogos_total_xvfa_a #8
media_pontos_contra_total_xvfa_a = pontos_contra_total_xvfa_a/jogos_total_xvfa_a #9

media_pontos_pro_vitoria_xvfa_a = pontos_pro_vitoria_xvfa_a/vitoria_total_xvfa_a #13
media_pontos_contra_vitoria_xvfa_a = pontos_contra_vitoria_xvfa_a/vitoria_total_xvfa_a #14

media_pontos_pro_derrota_xvfa_a = pontos_pro_derrota_xvfa_a/derrota_total_xvfa_a #18
media_pontos_contra_derrota_xvfa_a = pontos_contra_derrota_xvfa_a/derrota_total_xvfa_a #19


# In[37]:


brasil_xv_fem_adulto_a = [jogos_total_xvfa_a,vitoria_total_xvfa_a,empate_total_xvfa_a,derrota_total_xvfa_a,pontos_pro_total_xvfa_a, #5
                            pontos_contra_total_xvfa_a,saldo_total_xvfa_a,media_pontos_pro_total_xvfa_a.round(2),media_pontos_contra_total_xvfa_a.round(2), #9
                            pontos_pro_vitoria_xvfa_a,pontos_contra_vitoria_xvfa_a,saldo_pontos_vitoria,media_pontos_pro_vitoria_xvfa_a.round(2), #13
                            media_pontos_contra_vitoria_xvfa_a.round(2),pontos_pro_derrota_xvfa_a,pontos_contra_derrota_xvfa_a,saldo_pontos_derrota, #17
                            media_pontos_pro_derrota_xvfa_a.round(2),media_pontos_contra_derrota_xvfa_a.round(2),jogos_casa_xvfa_a,vitoria_casa_xvfa_a['X'], #21
                            empate_casa_xvfa_a['X'],derrota_casa_xvfa_a['X'],pontos_pro_casa_xvfa_a,pontos_contra_casa_xvfa_a,saldo_casa_xvfa_a, #26
                            media_pontos_pro_casa_xvfa_a.round(2),media_pontos_contra_casa_xvfa_a.round(2),ponto_pro_vitoria_casa_xvfa_a,ponto_contra_vitoria_casa_xvfa_a, #30
                            saldo_vitoria_casa_xvfa_a,media_pontos_pro_vitoria_casa_xvfa_a['X'].round(2),media_pontos_contra_vitoria_casa_xvfa_a['X'].round(2), #33
                            ponto_pro_derrota_casa_xvfa_a,ponto_contra_derrota_casa_xvfa_a,saldo_derrota_casa_xvfa_a,media_pontos_pro_derrota_casa_xvfa_a['X'].round(2), #37
                            media_pontos_contra_derrota_casa_xvfa_a['X'].round(2),jogos_fora_xvfa_a,vitoria_fora_xvfa_a['X'],empate_fora_xvfa_a['X'],
                            derrota_fora_xvfa_a['X'],pontos_pro_fora_xvfa_a,pontos_contra_fora_xvfa_a,saldo_fora_xvfa_a,media_pontos_pro_fora_xvfa_a.round(2),
                            media_pontos_contra_fora_xvfa_a.round(2),ponto_pro_vitoria_fora_xvfa_a,ponto_contra_vitoria_fora_xvfa_a,saldo_vitoria_fora_xvfa_a,
                            media_pontos_pro_vitoria_fora_xvfa_a['X'].round(2),media_pontos_contra_vitoria_fora_xvfa_a['X'].round(2),ponto_pro_derrota_fora_xvfa_a,
                            ponto_contra_derrota_fora_xvfa_a,saldo_vitoria_fora_xvfa_a,media_pontos_pro_derrota_fora_xvfa_a['X'].round(2),media_pontos_contra_derrota_fora_xvfa_a['X'].round(2)]
brasil_xv_fem_adulto_a


# In[38]:


historico_analitico.loc['Brasil XVA adulto fem'] = brasil_xv_fem_adulto_a
historico_analitico


# In[39]:


# Criando um Dataframe apenas para os resultados do Rugby Sevens masculino adulto do Brasil
df_brasil_seven_masc_adulto = df_brasil.query('modalidade == "Seven" & genero == "Masculino" & categoria == "Adulto"')
df_brasil_seven_masc_adulto = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') | (df_brasil_seven_masc_adulto['visitante'] == 'Brasil')]
#pd.set_option('display.max_columns', None)
df_brasil_seven_masc_adulto


# In[40]:


#Números casa - em (#), o índice de cada estatística no Dataframe
#Número de vitórias, empates e derrota em casa
vitoria_casa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].count() #21
empate_casa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & 
                                                  (df_brasil_seven_masc_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] == 0)].count() #22
derrota_casa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].count() #23

#Total de jogos em casa
jogos_casa_sma = vitoria_casa_sma['X'] + empate_casa_sma['X'] + derrota_casa_sma['X'] #20

#Quantos pontos o Brasil faz em casa #24
pontos_pro_tcasa_bra_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA')].sum()
pontos_pro_tvisitante_bra_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA')].sum()
pontos_pro_casa_sma = pontos_pro_tcasa_bra_sma['final_time_casa'] + pontos_pro_tvisitante_bra_sma['final_time_visitante'] #24

#Quantos pontos o Brasil sofre em casa #25
pontos_contra_tcasa_bra_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] != 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA')].sum()
pontos_contra_tvisitante_bra_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] != 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA')].sum()
pontos_contra_casa_sma = pontos_contra_tcasa_bra_sma['final_time_casa'] + pontos_contra_tvisitante_bra_sma['final_time_visitante'] #25

#Saldo de pontos em casa
saldo_casa_sma = pontos_pro_casa_sma - pontos_contra_casa_sma #26

#Quantos pontos o Brasil faz quanto vence em casa #29 
#condicao_brasil_vitoria_casa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_casa_sma = ponto_pro_vitoria_tcasa_sma['final_time_casa'] + ponto_pro_vitoria_tvisitante_sma['final_time_visitante'] #29

#Quantos pontos o Brasil sofre quando vence em casa #30 
ponto_contra_vitoria_tcasa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_casa_sma = ponto_contra_vitoria_tcasa_sma['final_time_visitante'] + ponto_contra_vitoria_tvisitante_sma['final_time_casa'] #30

#Saldo de pontos quando o Brasil vence em casa #31
saldo_vitoria_casa_sma = ponto_pro_vitoria_casa_sma - ponto_contra_vitoria_casa_sma #31

#Quantos pontos o Brasil faz quando perde em casa #34
#condicao_brasil_derrota_casa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)]

ponto_pro_derrota_tcasa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_casa_sma = ponto_pro_derrota_tcasa_sma['final_time_casa'] + ponto_pro_derrota_tvisitante_sma['final_time_visitante'] #34

#Quantos pontos o Brasil sofre quando perde em casa #35
ponto_contra_derrota_tcasa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] == 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_casa_sma = ponto_contra_derrota_tcasa_sma['final_time_visitante'] + ponto_contra_derrota_tvisitante_sma['final_time_casa'] #35

#Saldo de pontos quando o Brasil perde em casa #36
saldo_derrota_casa_sma = ponto_pro_derrota_casa_sma - ponto_contra_derrota_casa_sma #36

#Médias
#Média de pontos que o Brasil faz nos jogos em casa #27
media_pontos_pro_casa_sma = pontos_pro_casa_sma/jogos_casa_sma

#Média de pontos que o Brasil sofre nos jogos em casa #28
media_pontos_contra_casa_sma = pontos_contra_casa_sma/jogos_casa_sma

#Média de pontos que o Brasil faz quando vence em casa #32
media_pontos_pro_vitoria_casa_sma = ponto_pro_vitoria_casa_sma/vitoria_casa_sma #32

#Média de pontos que o Brasil sofre quando vence em casa #33
media_pontos_contra_vitoria_casa_sma = ponto_contra_vitoria_casa_sma/vitoria_casa_sma #33

#Média de pontos que o Brasil faz quando perde em casa #37
media_pontos_pro_derrota_casa_sma = ponto_pro_derrota_casa_sma/derrota_casa_sma #37

#Média de pontos que o Brasil sofre quando perde em casa #38
media_pontos_contra_derrota_casa_sma = ponto_contra_derrota_casa_sma/derrota_casa_sma #38


# In[41]:


#Números fora de casa
#Número de vitórias, empates e derrotas fora de casa
vitoria_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].count() #40
empate_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & 
                                                  (df_brasil_seven_masc_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] == 0)].count() #41
derrota_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].count() #42

#Total de jogos fora de casa
jogos_fora_sma = vitoria_fora_sma['X'] + empate_fora_sma['X'] + derrota_fora_sma['X'] #39


#Quantos pontos o Brasil faz fora de casa #43
pontos_pro_tcasa_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA')].sum()
pontos_pro_tvisitante_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA')].sum()
pontos_pro_fora_sma = pontos_pro_tcasa_fora_sma['final_time_casa'] + pontos_pro_tvisitante_fora_sma['final_time_visitante'] #43

#Quantos pontos o Brasil sofre fora de casa #44
pontos_contra_tcasa_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] != 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA')].sum()
pontos_contra_tvisitante_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] != 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA')].sum()
pontos_contra_fora_sma = pontos_contra_tcasa_fora_sma['final_time_casa'] + pontos_contra_tvisitante_fora_sma['final_time_visitante'] #44

#Saldo de pontos fora de casa #45
saldo_fora_sma = pontos_pro_fora_sma - pontos_contra_fora_sma #45

#Quantos pontos o Brasil faz quanto vence fora de casa #48
#condicao_brasil_vitoria_casa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_fora_sma = ponto_pro_vitoria_tcasa_fora_sma['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_sma['final_time_visitante'] #48

#Quantos pontos o Brasil sofre quando vence fora de casa #49
ponto_contra_vitoria_tcasa_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_fora_sma = ponto_contra_vitoria_tcasa_fora_sma['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_sma['final_time_casa'] #49

#Saldo de pontos quando o Brasil vence fora de casa #50
saldo_vitoria_fora_sma = ponto_pro_vitoria_fora_sma - ponto_contra_vitoria_fora_sma #50

#Quantos pontos o Brasil faz quando perde fora de casa #53 
#condicao_brasil_derrota_casa_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)]
ponto_pro_derrota_tcasa_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_fora_sma = ponto_pro_derrota_tcasa_fora_sma['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_sma['final_time_visitante']

#Quantos pontos o Brasil sofre quando perde fora de casa #54 
ponto_contra_derrota_tcasa_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_fora_sma = df_brasil_seven_masc_adulto.loc[(df_brasil_seven_masc_adulto['visitante'] == 'Brasil') & (df_brasil_seven_masc_adulto['pais'] != 'BRA') & (df_brasil_seven_masc_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_fora_sma = ponto_contra_derrota_tcasa_fora_sma['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_sma['final_time_casa']

#Saldo de pontos quando o Brasil perde fora de casa #55
saldo_vitoria_fora_sma = ponto_pro_derrota_fora_sma - ponto_contra_derrota_fora_sma #55

#Médias
#Média de pontos que o Brasil faz nos jogos fora de casa #46
media_pontos_pro_fora_sma = pontos_pro_fora_sma/jogos_fora_sma

#Média de pontos que o Brasil sofre nos jogos fora de casa #47
media_pontos_contra_fora_sma = pontos_contra_fora_sma/jogos_fora_sma

#Média de pontos que o Brasil faz quando vence fora de casa #51
media_pontos_pro_vitoria_fora_sma = ponto_pro_vitoria_fora_sma/vitoria_fora_sma #51

#Média de pontos que o Brasil sofre quando vence fora de casa #52
media_pontos_contra_vitoria_fora_sma = ponto_contra_vitoria_fora_sma/vitoria_fora_sma #52

#Média de pontos que o Brasil faz quando perde fora de casa #56
media_pontos_pro_derrota_fora_sma = ponto_pro_derrota_fora_sma/derrota_fora_sma #56

#Média de pontos que o Brasil sofre quando perde fora de casa #57
media_pontos_contra_derrota_fora_sma = ponto_contra_derrota_fora_sma/derrota_fora_sma #57


# In[42]:


#Números consolidados - em (#), o índice de cada estatística no Dataframe
#1 a 9 - dados gerais
#10 a 14 - vitórias
#15 a 19 - derrotas
#20 a 38 - resultados em casa
#39 a 57 - resultados fora de casa
vitoria_total_sma = vitoria_casa_sma['X'] + vitoria_fora_sma['X'] #2
empate_total_sma = empate_casa_sma['X'] + empate_fora_sma['X'] #3
derrota_total_sma = derrota_casa_sma['X'] + derrota_fora_sma['X'] #4

jogos_total_sma = vitoria_total_sma + empate_total_sma + derrota_total_sma #1

#Saldo de pontos nos jogos
pontos_pro_total_sma = pontos_pro_casa_sma + pontos_pro_fora_sma #5
pontos_contra_total_sma = pontos_contra_casa_sma + pontos_contra_fora_sma #6

saldo_total_sma = pontos_pro_total_sma - pontos_contra_total_sma #7

#Saldo de pontos nas vitórias
pontos_pro_vitoria_sma = ponto_pro_vitoria_casa_sma + ponto_pro_vitoria_fora_sma #10
pontos_contra_vitoria_sma = ponto_contra_vitoria_casa_sma + ponto_contra_vitoria_fora_sma #11


saldo_vitoria_fora_sma = ponto_pro_vitoria_fora_sma - ponto_contra_vitoria_fora_sma
saldo_pontos_vitoria = pontos_pro_vitoria_sma - pontos_contra_vitoria_sma #12

#Saldo de pontos nas derrotas
pontos_pro_derrota_sma = ponto_pro_derrota_casa_sma + ponto_pro_derrota_fora_sma #15
pontos_contra_derrota_sma = ponto_contra_derrota_casa_sma + ponto_contra_derrota_fora_sma #16


#saldo_derrota_fora_sma = ponto_pro_derrota_fora_sma - ponto_contra_derrota_fora_sma
saldo_pontos_derrota = pontos_pro_derrota_sma - pontos_contra_derrota_sma #17


#Médias
media_pontos_pro_total_sma = pontos_pro_total_sma/jogos_total_sma #8
media_pontos_contra_total_sma = pontos_contra_total_sma/jogos_total_sma #9

media_pontos_pro_vitoria_sma = pontos_pro_vitoria_sma/vitoria_total_sma #13
media_pontos_contra_vitoria_sma = pontos_contra_vitoria_sma/vitoria_total_sma #14

media_pontos_pro_derrota_sma = pontos_pro_derrota_sma/derrota_total_sma #18
media_pontos_contra_derrota_sma = pontos_contra_derrota_sma/derrota_total_sma #19


# In[43]:


brasil_seven_adulto_masc = [jogos_total_sma,vitoria_total_sma,empate_total_sma,derrota_total_sma,pontos_pro_total_sma, #5
                            pontos_contra_total_sma,saldo_total_sma,media_pontos_pro_total_sma.round(2),media_pontos_contra_total_sma.round(2), #9
                            pontos_pro_vitoria_sma,pontos_contra_vitoria_sma,saldo_pontos_vitoria,media_pontos_pro_vitoria_sma.round(2), #13
                            media_pontos_contra_vitoria_sma.round(2),pontos_pro_derrota_sma,pontos_contra_derrota_sma,saldo_pontos_derrota, #17
                            media_pontos_pro_derrota_sma.round(2),media_pontos_contra_derrota_sma.round(2),jogos_casa_sma,vitoria_casa_sma['X'], #21
                            empate_casa_sma['X'],derrota_casa_sma['X'],pontos_pro_casa_sma,pontos_contra_casa_sma,saldo_casa_sma, #26
                            media_pontos_pro_casa_sma.round(2),media_pontos_contra_casa_sma.round(2),ponto_pro_vitoria_casa_sma,ponto_contra_vitoria_casa_sma, #30
                            saldo_vitoria_casa_sma,media_pontos_pro_vitoria_casa_sma['X'].round(2),media_pontos_contra_vitoria_casa_sma['X'].round(2), #33
                            ponto_pro_derrota_casa_sma,ponto_contra_derrota_casa_sma,saldo_derrota_casa_sma,media_pontos_pro_derrota_casa_sma['X'].round(2), #37
                            media_pontos_contra_derrota_casa_sma['X'].round(2),jogos_fora_sma,vitoria_fora_sma['X'],empate_fora_sma['X'],
                            derrota_fora_sma['X'],pontos_pro_fora_sma,pontos_contra_fora_sma,saldo_fora_sma,media_pontos_pro_fora_sma.round(2),
                            media_pontos_contra_fora_sma.round(2),ponto_pro_vitoria_fora_sma,ponto_contra_vitoria_fora_sma,saldo_vitoria_fora_sma,
                            media_pontos_pro_vitoria_fora_sma['X'].round(2),media_pontos_contra_vitoria_fora_sma['X'].round(2),ponto_pro_derrota_fora_sma,
                            ponto_contra_derrota_fora_sma,saldo_vitoria_fora_sma,media_pontos_pro_derrota_fora_sma['X'].round(2),media_pontos_contra_derrota_fora_sma['X'].round(2)]


# In[44]:


historico_analitico.loc['Brasil Seven adulto masc'] = brasil_seven_adulto_masc
historico_analitico


# In[45]:


# Criando um Dataframe apenas para os resultados do Rugby Sevens feminino adulto do Brasil
df_brasil_seven_fem_adulto = df_brasil.query('modalidade == "Seven" & genero == "Feminino" & categoria == "Adulto"')
df_brasil_seven_fem_adulto = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') | (df_brasil_seven_fem_adulto['visitante'] == 'Brasil')]
#pd.set_option('display.max_columns', None)
df_brasil_seven_fem_adulto


# In[46]:


#Números casa - em (#), o índice de cada estatística no Dataframe
#Número de vitórias, empates e derrota em casa
vitoria_casa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].count() #21
empate_casa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & 
                                                  (df_brasil_seven_fem_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] == 0)].count() #22
derrota_casa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].count() #23

#Total de jogos em casa
jogos_casa_sfa = vitoria_casa_sfa['X'] + empate_casa_sfa['X'] + derrota_casa_sfa['X'] #20

#Quantos pontos o Brasil faz em casa #24
pontos_pro_tcasa_bra_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA')].sum()
pontos_pro_tvisitante_bra_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA')].sum()
pontos_pro_casa_sfa = pontos_pro_tcasa_bra_sfa['final_time_casa'] + pontos_pro_tvisitante_bra_sfa['final_time_visitante'] #24

#Quantos pontos o Brasil sofre em casa #25
pontos_contra_tcasa_bra_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] != 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA')].sum()
pontos_contra_tvisitante_bra_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] != 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA')].sum()
pontos_contra_casa_sfa = pontos_contra_tcasa_bra_sfa['final_time_casa'] + pontos_contra_tvisitante_bra_sfa['final_time_visitante'] #25

#Saldo de pontos em casa
saldo_casa_sfa = pontos_pro_casa_sfa - pontos_contra_casa_sfa #26

#Quantos pontos o Brasil faz quanto vence em casa #29 
#condicao_brasil_vitoria_casa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_casa_sfa = ponto_pro_vitoria_tcasa_sfa['final_time_casa'] + ponto_pro_vitoria_tvisitante_sfa['final_time_visitante'] #29

#Quantos pontos o Brasil sofre quando vence em casa #30 
ponto_contra_vitoria_tcasa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_casa_sfa = ponto_contra_vitoria_tcasa_sfa['final_time_visitante'] + ponto_contra_vitoria_tvisitante_sfa['final_time_casa'] #30

#Saldo de pontos quando o Brasil vence em casa #31
saldo_vitoria_casa_sfa = ponto_pro_vitoria_casa_sfa - ponto_contra_vitoria_casa_sfa #31

#Quantos pontos o Brasil faz quando perde em casa #34
#condicao_brasil_derrota_casa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)]

ponto_pro_derrota_tcasa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_casa_sfa = ponto_pro_derrota_tcasa_sfa['final_time_casa'] + ponto_pro_derrota_tvisitante_sfa['final_time_visitante'] #34

#Quantos pontos o Brasil sofre quando perde em casa #35
ponto_contra_derrota_tcasa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] == 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_casa_sfa = ponto_contra_derrota_tcasa_sfa['final_time_visitante'] + ponto_contra_derrota_tvisitante_sfa['final_time_casa'] #35

#Saldo de pontos quando o Brasil perde em casa #36
saldo_derrota_casa_sfa = ponto_pro_derrota_casa_sfa - ponto_contra_derrota_casa_sfa #36

#Médias
#Média de pontos que o Brasil faz nos jogos em casa #27
media_pontos_pro_casa_sfa = pontos_pro_casa_sfa/jogos_casa_sfa

#Média de pontos que o Brasil sofre nos jogos em casa #28
media_pontos_contra_casa_sfa = pontos_contra_casa_sfa/jogos_casa_sfa

#Média de pontos que o Brasil faz quando vence em casa #32
media_pontos_pro_vitoria_casa_sfa = ponto_pro_vitoria_casa_sfa/vitoria_casa_sfa #32

#Média de pontos que o Brasil sofre quando vence em casa #33
media_pontos_contra_vitoria_casa_sfa = ponto_contra_vitoria_casa_sfa/vitoria_casa_sfa #33

#Média de pontos que o Brasil faz quando perde em casa #37
media_pontos_pro_derrota_casa_sfa = ponto_pro_derrota_casa_sfa/derrota_casa_sfa #37

#Média de pontos que o Brasil sofre quando perde em casa #38
media_pontos_contra_derrota_casa_sfa = ponto_contra_derrota_casa_sfa/derrota_casa_sfa #38


# In[47]:


#Números fora de casa
#Número de vitórias, empates e derrotas fora de casa
vitoria_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].count() + df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].count() #40
empate_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & 
                                                  (df_brasil_seven_fem_adulto['diferenca_pontos_final'] == 0)].count() + df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] == 0)].count() #41
derrota_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].count() + df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & 
                                                   (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].count() #42

#Total de jogos fora de casa
jogos_fora_sfa = vitoria_fora_sfa['X'] + empate_fora_sfa['X'] + derrota_fora_sfa['X'] #39


#Quantos pontos o Brasil faz fora de casa #43
pontos_pro_tcasa_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA')].sum()
pontos_pro_tvisitante_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA')].sum()
pontos_pro_fora_sfa = pontos_pro_tcasa_fora_sfa['final_time_casa'] + pontos_pro_tvisitante_fora_sfa['final_time_visitante'] #43

#Quantos pontos o Brasil sofre fora de casa #44
pontos_contra_tcasa_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] != 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA')].sum()
pontos_contra_tvisitante_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] != 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA')].sum()
pontos_contra_fora_sfa = pontos_contra_tcasa_fora_sfa['final_time_casa'] + pontos_contra_tvisitante_fora_sfa['final_time_visitante'] #44

#Saldo de pontos fora de casa #45
saldo_fora_sfa = pontos_pro_fora_sfa - pontos_contra_fora_sfa #45

#Quantos pontos o Brasil faz quanto vence fora de casa #48
#condicao_brasil_vitoria_casa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_fora_sfa = ponto_pro_vitoria_tcasa_fora_sfa['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_sfa['final_time_visitante'] #48

#Quantos pontos o Brasil sofre quando vence fora de casa #49
ponto_contra_vitoria_tcasa_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_fora_sfa = ponto_contra_vitoria_tcasa_fora_sfa['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_sfa['final_time_casa'] #49

#Saldo de pontos quando o Brasil vence fora de casa #50
saldo_vitoria_fora_sfa = ponto_pro_vitoria_fora_sfa - ponto_contra_vitoria_fora_sfa #50

#Quantos pontos o Brasil faz quando perde fora de casa #53 
#condicao_brasil_derrota_casa_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)]
ponto_pro_derrota_tcasa_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_fora_sfa = ponto_pro_derrota_tcasa_fora_sfa['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_sfa['final_time_visitante']

#Quantos pontos o Brasil sofre quando perde fora de casa #54 
ponto_contra_derrota_tcasa_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['time_casa'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_fora_sfa = df_brasil_seven_fem_adulto.loc[(df_brasil_seven_fem_adulto['visitante'] == 'Brasil') & (df_brasil_seven_fem_adulto['pais'] != 'BRA') & (df_brasil_seven_fem_adulto['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_fora_sfa = ponto_contra_derrota_tcasa_fora_sfa['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_sfa['final_time_casa']

#Saldo de pontos quando o Brasil perde fora de casa #55
saldo_derrota_fora_sfa = ponto_pro_derrota_fora_sfa - ponto_contra_derrota_fora_sfa #55

#Médias
#Média de pontos que o Brasil faz nos jogos fora de casa #46
media_pontos_pro_fora_sfa = pontos_pro_fora_sfa/jogos_fora_sfa

#Média de pontos que o Brasil sofre nos jogos fora de casa #47
media_pontos_contra_fora_sfa = pontos_contra_fora_sfa/jogos_fora_sfa

#Média de pontos que o Brasil faz quando vence fora de casa #51
media_pontos_pro_vitoria_fora_sfa = ponto_pro_vitoria_fora_sfa/vitoria_fora_sfa #51

#Média de pontos que o Brasil sofre quando vence fora de casa #52
media_pontos_contra_vitoria_fora_sfa = ponto_contra_vitoria_fora_sfa/vitoria_fora_sfa #52

#Média de pontos que o Brasil faz quando perde fora de casa #56
media_pontos_pro_derrota_fora_sfa = ponto_pro_derrota_fora_sfa/derrota_fora_sfa #56

#Média de pontos que o Brasil sofre quando perde fora de casa #57
media_pontos_contra_derrota_fora_sfa = ponto_contra_derrota_fora_sfa/derrota_fora_sfa #57


# In[48]:


#Números consolidados - em (#), o índice de cada estatística no Dataframe
#1 a 9 - dados gerais
#10 a 14 - vitórias
#15 a 19 - derrotas
#20 a 38 - resultados em casa
#39 a 57 - resultados fora de casa
vitoria_total_sfa = vitoria_casa_sfa['X'] + vitoria_fora_sfa['X'] #2
empate_total_sfa = empate_casa_sfa['X'] + empate_fora_sfa['X'] #3
derrota_total_sfa = derrota_casa_sfa['X'] + derrota_fora_sfa['X'] #4

jogos_total_sfa = vitoria_total_sfa + empate_total_sfa + derrota_total_sfa #1

#Saldo de pontos nos jogos
pontos_pro_total_sfa = pontos_pro_casa_sfa + pontos_pro_fora_sfa #5
pontos_contra_total_sfa = pontos_contra_casa_sfa + pontos_contra_fora_sfa #6

saldo_total_sfa = pontos_pro_total_sfa - pontos_contra_total_sfa #7

#Saldo de pontos nas vitórias
pontos_pro_vitoria_sfa = ponto_pro_vitoria_casa_sfa + ponto_pro_vitoria_fora_sfa #10
pontos_contra_vitoria_sfa = ponto_contra_vitoria_casa_sfa + ponto_contra_vitoria_fora_sfa #11


saldo_vitoria_fora_sfa = ponto_pro_vitoria_fora_sfa - ponto_contra_vitoria_fora_sfa
saldo_pontos_vitoria = pontos_pro_vitoria_sfa - pontos_contra_vitoria_sfa #12

#Saldo de pontos nas derrotas
pontos_pro_derrota_sfa = ponto_pro_derrota_casa_sfa + ponto_pro_derrota_fora_sfa #15
pontos_contra_derrota_sfa = ponto_contra_derrota_casa_sfa + ponto_contra_derrota_fora_sfa #16


#saldo_derrota_fora_sfa = ponto_pro_derrota_fora_sfa - ponto_contra_derrota_fora_sfa
saldo_pontos_derrota = pontos_pro_derrota_sfa - pontos_contra_derrota_sfa #17


#Médias
media_pontos_pro_total_sfa = pontos_pro_total_sfa/jogos_total_sfa #8
media_pontos_contra_total_sfa = pontos_contra_total_sfa/jogos_total_sfa #9

media_pontos_pro_vitoria_sfa = pontos_pro_vitoria_sfa/vitoria_total_sfa #13
media_pontos_contra_vitoria_sfa = pontos_contra_vitoria_sfa/vitoria_total_sfa #14

media_pontos_pro_derrota_sfa = pontos_pro_derrota_sfa/derrota_total_sfa #18
media_pontos_contra_derrota_sfa = pontos_contra_derrota_sfa/derrota_total_sfa #19


# In[49]:


brasil_seven_adulto_fem = [jogos_total_sfa,vitoria_total_sfa,empate_total_sfa,derrota_total_sfa,pontos_pro_total_sfa, #5
                            pontos_contra_total_sfa,saldo_total_sfa,media_pontos_pro_total_sfa.round(2),media_pontos_contra_total_sfa.round(2), #9
                            pontos_pro_vitoria_sfa,pontos_contra_vitoria_sfa,saldo_pontos_vitoria,media_pontos_pro_vitoria_sfa.round(2), #13
                            media_pontos_contra_vitoria_sfa.round(2),pontos_pro_derrota_sfa,pontos_contra_derrota_sfa,saldo_pontos_derrota, #17
                            media_pontos_pro_derrota_sfa.round(2),media_pontos_contra_derrota_sfa.round(2),jogos_casa_sfa,vitoria_casa_sfa['X'], #21
                            empate_casa_sfa['X'],derrota_casa_sfa['X'],pontos_pro_casa_sfa,pontos_contra_casa_sfa,saldo_casa_sfa, #26
                            media_pontos_pro_casa_sfa.round(2),media_pontos_contra_casa_sfa.round(2),ponto_pro_vitoria_casa_sfa,ponto_contra_vitoria_casa_sfa, #30
                            saldo_vitoria_casa_sfa,media_pontos_pro_vitoria_casa_sfa['X'].round(2),media_pontos_contra_vitoria_casa_sfa['X'].round(2), #33
                            ponto_pro_derrota_casa_sfa,ponto_contra_derrota_casa_sfa,saldo_derrota_casa_sfa,media_pontos_pro_derrota_casa_sfa['X'].round(2), #37
                            media_pontos_contra_derrota_casa_sfa['X'].round(2),jogos_fora_sfa,vitoria_fora_sfa['X'],empate_fora_sfa['X'],
                            derrota_fora_sfa['X'],pontos_pro_fora_sfa,pontos_contra_fora_sfa,saldo_fora_sfa,media_pontos_pro_fora_sfa.round(2),
                            media_pontos_contra_fora_sfa.round(2),ponto_pro_vitoria_fora_sfa,ponto_contra_vitoria_fora_sfa,saldo_vitoria_fora_sfa,
                            media_pontos_pro_vitoria_fora_sfa['X'].round(2),media_pontos_contra_vitoria_fora_sfa['X'].round(2),ponto_pro_derrota_fora_sfa,
                            ponto_contra_derrota_fora_sfa,saldo_derrota_fora_sfa,media_pontos_pro_derrota_fora_sfa['X'].round(2),media_pontos_contra_derrota_fora_sfa['X'].round(2)]


# In[50]:


historico_analitico.loc['Brasil Seven adulto fem'] = brasil_seven_adulto_fem
historico_analitico


# In[51]:


# Criando um Dataframe apenas para os resultados do Rugby Sevens masculino M18 do Brasil
df_brasil_seven_masc_m18 = df_brasil.query('modalidade == "Seven" & genero == "Masculino" & categoria == "M18"')
df_brasil_seven_masc_m18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') | (df_brasil_seven_masc_m18['visitante'] == 'Brasil')]
#pd.set_option('display.max_columns', None)
df_brasil_seven_masc_m18


# In[52]:


#Números casa - em (#), o índice de cada estatística no Dataframe
#Número de vitórias, empates e derrota em casa
vitoria_casa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].count() + df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].count() #21
empate_casa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & 
                                                  (df_brasil_seven_masc_m18['diferenca_pontos_final'] == 0)].count() + df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] == 0)].count() #22
derrota_casa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].count() + df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].count() #23

#Total de jogos em casa
jogos_casa_smm18 = vitoria_casa_smm18['X'] + empate_casa_smm18['X'] + derrota_casa_smm18['X'] #20

#Quantos pontos o Brasil faz em casa #24
pontos_pro_tcasa_bra_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA')].sum()
pontos_pro_tvisitante_bra_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA')].sum()
pontos_pro_casa_smm18 = pontos_pro_tcasa_bra_smm18['final_time_casa'] + pontos_pro_tvisitante_bra_smm18['final_time_visitante'] #24

#Quantos pontos o Brasil sofre em casa #25
pontos_contra_tcasa_bra_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] != 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA')].sum()
pontos_contra_tvisitante_bra_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] != 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA')].sum()
pontos_contra_casa_smm18 = pontos_contra_tcasa_bra_smm18['final_time_casa'] + pontos_contra_tvisitante_bra_smm18['final_time_visitante'] #25

#Saldo de pontos em casa
saldo_casa_smm18 = pontos_pro_casa_smm18 - pontos_contra_casa_smm18 #26

#Quantos pontos o Brasil faz quanto vence em casa #29 
#condicao_brasil_vitoria_casa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_casa_smm18 = ponto_pro_vitoria_tcasa_smm18['final_time_casa'] + ponto_pro_vitoria_tvisitante_smm18['final_time_visitante'] #29

#Quantos pontos o Brasil sofre quando vence em casa #30 
ponto_contra_vitoria_tcasa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_casa_smm18 = ponto_contra_vitoria_tcasa_smm18['final_time_visitante'] + ponto_contra_vitoria_tvisitante_smm18['final_time_casa'] #30

#Saldo de pontos quando o Brasil vence em casa #31
saldo_vitoria_casa_smm18 = ponto_pro_vitoria_casa_smm18 - ponto_contra_vitoria_casa_smm18 #31

#Quantos pontos o Brasil faz quando perde em casa #34
#condicao_brasil_derrota_casa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)]

ponto_pro_derrota_tcasa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_casa_smm18 = ponto_pro_derrota_tcasa_smm18['final_time_casa'] + ponto_pro_derrota_tvisitante_smm18['final_time_visitante'] #34

#Quantos pontos o Brasil sofre quando perde em casa #35
ponto_contra_derrota_tcasa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] == 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_casa_smm18 = ponto_contra_derrota_tcasa_smm18['final_time_visitante'] + ponto_contra_derrota_tvisitante_smm18['final_time_casa'] #35

#Saldo de pontos quando o Brasil perde em casa #36
saldo_derrota_casa_smm18 = ponto_pro_derrota_casa_smm18 - ponto_contra_derrota_casa_smm18 #36

#Médias
#Média de pontos que o Brasil faz nos jogos em casa #27
media_pontos_pro_casa_smm18 = pontos_pro_casa_smm18/jogos_casa_smm18

#Média de pontos que o Brasil sofre nos jogos em casa #28
media_pontos_contra_casa_smm18 = pontos_contra_casa_smm18/jogos_casa_smm18

#Média de pontos que o Brasil faz quando vence em casa #32
media_pontos_pro_vitoria_casa_smm18 = ponto_pro_vitoria_casa_smm18/vitoria_casa_smm18 #32

#Média de pontos que o Brasil sofre quando vence em casa #33
media_pontos_contra_vitoria_casa_smm18 = ponto_contra_vitoria_casa_smm18/vitoria_casa_smm18 #33

#Média de pontos que o Brasil faz quando perde em casa #37
media_pontos_pro_derrota_casa_smm18 = ponto_pro_derrota_casa_smm18/derrota_casa_smm18 #37

#Média de pontos que o Brasil sofre quando perde em casa #38
media_pontos_contra_derrota_casa_smm18 = ponto_contra_derrota_casa_smm18/derrota_casa_smm18 #38


# In[53]:


#Números fora de casa
#Número de vitórias, empates e derrotas fora de casa
vitoria_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].count() + df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].count() #40
empate_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & 
                                                  (df_brasil_seven_masc_m18['diferenca_pontos_final'] == 0)].count() + df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] == 0)].count() #41
derrota_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].count() + df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & 
                                                   (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].count() #42

#Total de jogos fora de casa
jogos_fora_smm18 = vitoria_fora_smm18['X'] + empate_fora_smm18['X'] + derrota_fora_smm18['X'] #39


#Quantos pontos o Brasil faz fora de casa #43
pontos_pro_tcasa_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA')].sum()
pontos_pro_tvisitante_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA')].sum()
pontos_pro_fora_smm18 = pontos_pro_tcasa_fora_smm18['final_time_casa'] + pontos_pro_tvisitante_fora_smm18['final_time_visitante'] #43

#Quantos pontos o Brasil sofre fora de casa #44
pontos_contra_tcasa_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] != 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA')].sum()
pontos_contra_tvisitante_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] != 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA')].sum()
pontos_contra_fora_smm18 = pontos_contra_tcasa_fora_smm18['final_time_casa'] + pontos_contra_tvisitante_fora_smm18['final_time_visitante'] #44

#Saldo de pontos fora de casa #45
saldo_fora_smm18 = pontos_pro_fora_smm18 - pontos_contra_fora_smm18 #45

#Quantos pontos o Brasil faz quanto vence fora de casa #48
#condicao_brasil_vitoria_casa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)]
ponto_pro_vitoria_tcasa_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_pro_vitoria_tvisitante_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_pro_vitoria_fora_smm18 = ponto_pro_vitoria_tcasa_fora_smm18['final_time_casa'] + ponto_pro_vitoria_tvisitante_fora_smm18['final_time_visitante'] #48

#Quantos pontos o Brasil sofre quando vence fora de casa #49
ponto_contra_vitoria_tcasa_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_contra_vitoria_tvisitante_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_contra_vitoria_fora_smm18 = ponto_contra_vitoria_tcasa_fora_smm18['final_time_visitante'] + ponto_contra_vitoria_tvisitante_fora_smm18['final_time_casa'] #49

#Saldo de pontos quando o Brasil vence fora de casa #50
saldo_vitoria_fora_smm18 = ponto_pro_vitoria_fora_smm18 - ponto_contra_vitoria_fora_smm18 #50

#Quantos pontos o Brasil faz quando perde fora de casa #53 
#condicao_brasil_derrota_casa_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)]
ponto_pro_derrota_tcasa_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_pro_derrota_tvisitante_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_pro_derrota_fora_smm18 = ponto_pro_derrota_tcasa_fora_smm18['final_time_casa'] + ponto_pro_derrota_tvisitante_fora_smm18['final_time_visitante']

#Quantos pontos o Brasil sofre quando perde fora de casa #54 
ponto_contra_derrota_tcasa_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['time_casa'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] < 0)].sum()
ponto_contra_derrota_tvisitante_fora_smm18 = df_brasil_seven_masc_m18.loc[(df_brasil_seven_masc_m18['visitante'] == 'Brasil') & (df_brasil_seven_masc_m18['pais'] != 'BRA') & (df_brasil_seven_masc_m18['diferenca_pontos_final'] > 0)].sum()
ponto_contra_derrota_fora_smm18 = ponto_contra_derrota_tcasa_fora_smm18['final_time_visitante'] + ponto_contra_derrota_tvisitante_fora_smm18['final_time_casa']

#Saldo de pontos quando o Brasil perde fora de casa #55
saldo_derrota_fora_smm18 = ponto_pro_derrota_fora_smm18 - ponto_contra_derrota_fora_smm18 #55

#Médias
#Média de pontos que o Brasil faz nos jogos fora de casa #46
media_pontos_pro_fora_smm18 = pontos_pro_fora_smm18/jogos_fora_smm18

#Média de pontos que o Brasil sofre nos jogos fora de casa #47
media_pontos_contra_fora_smm18 = pontos_contra_fora_smm18/jogos_fora_smm18

#Média de pontos que o Brasil faz quando vence fora de casa #51
media_pontos_pro_vitoria_fora_smm18 = ponto_pro_vitoria_fora_smm18/vitoria_fora_smm18 #51

#Média de pontos que o Brasil sofre quando vence fora de casa #52
media_pontos_contra_vitoria_fora_smm18 = ponto_contra_vitoria_fora_smm18/vitoria_fora_smm18 #52

#Média de pontos que o Brasil faz quando perde fora de casa #56
media_pontos_pro_derrota_fora_smm18 = ponto_pro_derrota_fora_smm18/derrota_fora_smm18 #56

#Média de pontos que o Brasil sofre quando perde fora de casa #57
media_pontos_contra_derrota_fora_smm18 = ponto_contra_derrota_fora_smm18/derrota_fora_smm18 #57


# In[54]:


#Números consolidados - em (#), o índice de cada estatística no Dataframe
#1 a 9 - dados gerais
#10 a 14 - vitórias
#15 a 19 - derrotas
#20 a 38 - resultados em casa
#39 a 57 - resultados fora de casa
vitoria_total_smm18 = vitoria_casa_smm18['X'] + vitoria_fora_smm18['X'] #2
empate_total_smm18 = empate_casa_smm18['X'] + empate_fora_smm18['X'] #3
derrota_total_smm18 = derrota_casa_smm18['X'] + derrota_fora_smm18['X'] #4

jogos_total_smm18 = vitoria_total_smm18 + empate_total_smm18 + derrota_total_smm18 #1

#Saldo de pontos nos jogos
pontos_pro_total_smm18 = pontos_pro_casa_smm18 + pontos_pro_fora_smm18 #5
pontos_contra_total_smm18 = pontos_contra_casa_smm18 + pontos_contra_fora_smm18 #6

saldo_total_smm18 = pontos_pro_total_smm18 - pontos_contra_total_smm18 #7

#Saldo de pontos nas vitórias
pontos_pro_vitoria_smm18 = ponto_pro_vitoria_casa_smm18 + ponto_pro_vitoria_fora_smm18 #10
pontos_contra_vitoria_smm18 = ponto_contra_vitoria_casa_smm18 + ponto_contra_vitoria_fora_smm18 #11


saldo_vitoria_fora_smm18 = ponto_pro_vitoria_fora_smm18 - ponto_contra_vitoria_fora_smm18
saldo_pontos_vitoria = pontos_pro_vitoria_smm18 - pontos_contra_vitoria_smm18 #12

#Saldo de pontos nas derrotas
pontos_pro_derrota_smm18 = ponto_pro_derrota_casa_smm18 + ponto_pro_derrota_fora_smm18 #15
pontos_contra_derrota_smm18 = ponto_contra_derrota_casa_smm18 + ponto_contra_derrota_fora_smm18 #16


#saldo_derrota_fora_smm18 = ponto_pro_derrota_fora_smm18 - ponto_contra_derrota_fora_smm18
saldo_pontos_derrota = pontos_pro_derrota_smm18 - pontos_contra_derrota_smm18 #17


#Médias
media_pontos_pro_total_smm18 = pontos_pro_total_smm18/jogos_total_smm18 #8
media_pontos_contra_total_smm18 = pontos_contra_total_smm18/jogos_total_smm18 #9

media_pontos_pro_vitoria_smm18 = pontos_pro_vitoria_smm18/vitoria_total_smm18 #13
media_pontos_contra_vitoria_smm18 = pontos_contra_vitoria_smm18/vitoria_total_smm18 #14

media_pontos_pro_derrota_smm18 = pontos_pro_derrota_smm18/derrota_total_smm18 #18
media_pontos_contra_derrota_smm18 = pontos_contra_derrota_smm18/derrota_total_smm18 #19


# In[55]:


brasil_seven_masc_m18 = [jogos_total_smm18,vitoria_total_smm18,empate_total_smm18,derrota_total_smm18,pontos_pro_total_smm18, #5
                            pontos_contra_total_smm18,saldo_total_smm18,media_pontos_pro_total_smm18.round(2),media_pontos_contra_total_smm18.round(2), #9
                            pontos_pro_vitoria_smm18,pontos_contra_vitoria_smm18,saldo_pontos_vitoria,media_pontos_pro_vitoria_smm18.round(2), #13
                            media_pontos_contra_vitoria_smm18.round(2),pontos_pro_derrota_smm18,pontos_contra_derrota_smm18,saldo_pontos_derrota, #17
                            media_pontos_pro_derrota_smm18.round(2),media_pontos_contra_derrota_smm18.round(2),jogos_casa_smm18,vitoria_casa_smm18['X'], #21
                            empate_casa_smm18['X'],derrota_casa_smm18['X'],pontos_pro_casa_smm18,pontos_contra_casa_smm18,saldo_casa_smm18, #26
                            media_pontos_pro_casa_smm18.round(2),media_pontos_contra_casa_smm18.round(2),ponto_pro_vitoria_casa_smm18,ponto_contra_vitoria_casa_smm18, #30
                            saldo_vitoria_casa_smm18,media_pontos_pro_vitoria_casa_smm18['X'].round(2),media_pontos_contra_vitoria_casa_smm18['X'].round(2), #33
                            ponto_pro_derrota_casa_smm18,ponto_contra_derrota_casa_smm18,saldo_derrota_casa_smm18,media_pontos_pro_derrota_casa_smm18['X'].round(2), #37
                            media_pontos_contra_derrota_casa_smm18['X'].round(2),jogos_fora_smm18,vitoria_fora_smm18['X'],empate_fora_smm18['X'],
                            derrota_fora_smm18['X'],pontos_pro_fora_smm18,pontos_contra_fora_smm18,saldo_fora_smm18,media_pontos_pro_fora_smm18.round(2),
                            media_pontos_contra_fora_smm18.round(2),ponto_pro_vitoria_fora_smm18,ponto_contra_vitoria_fora_smm18,saldo_vitoria_fora_smm18,
                            media_pontos_pro_vitoria_fora_smm18['X'].round(2),media_pontos_contra_vitoria_fora_smm18['X'].round(2),ponto_pro_derrota_fora_smm18,
                            ponto_contra_derrota_fora_smm18,saldo_derrota_fora_smm18,media_pontos_pro_derrota_fora_smm18['X'].round(2),media_pontos_contra_derrota_fora_smm18['X'].round(2)]
brasil_seven_masc_m18


# In[56]:


historico_analitico.loc['Brasil Seven M18 masc'] = brasil_seven_masc_m18
historico_analitico

