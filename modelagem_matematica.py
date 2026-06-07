# ==============================================================================
# FIAP - Engenharia de Software
# Disciplina: DIFFERENTIATED PROBLEM SOLVING
# Professor: Lucas Mendes Marques Gonçalves
# Global Solution 2026
#
# INTEGRANTES DO GRUPO
# RM 571182 - Luiz Ademario
# RM 569592 - Gustavo Noleto
# RM 568616 - Lucas Gaspar
#
# PROJETO: SpaceLaunch Optimizer - Modelagem Matemática do Mercado Espacial
# ==============================================================================

import math
import matplotlib.pyplot as plt

print("=====================================================================")
print("          SpaceLaunch Optimizer - MODELAGEM MATEMÁTICA                ")
print("=====================================================================")
print()

# ==============================================================================
# MODELO 1 - FUNÇÃO AFIM (1º GRAU)
# Função: y = 6000 * x + 15000
# Variáveis:
#   x (Domínio): Peso da carga útil (satélite) em kg -> [0, +infinito)
#   y (Imagem): Custo total do lançamento em USD
# ==============================================================================

print("---------------------------------------------------------------------")
print("MODELO 1: Função Afim (Custo por Peso da Carga)")
print("Equação: y = 6000x + 15000")
print("---------------------------------------------------------------------")

coef_angular_a = 6000
coef_linear_b = 15000 
print(f"-> Coeficiente Angular (a) = {coef_angular_a}")
print(f"   Significado: Cada 1 kg adicionado ao satélite aumenta o custo em U$ {coef_angular_a},00")
print(f"-> Coeficiente Linear (b) = {coef_linear_b}")
print(f"   Significado: Custo fixo inicial (mesmo se o peso for zero) = U$ {coef_linear_b},00")
print()
print(f"Análise de Crescimento: Como a = {coef_angular_a} (maior que zero), a função é CRESCENTE.")
print()

pesos_satelite = [1, 2, 3, 4, 5, 6, 8, 10, 12]

print("TABELA DE VALORES (Modelo 1):")
print(f"{'Peso (x em kg)':<15} | {'Custo Total (y em USD)':<20}")
print("-" * 40)

for peso in pesos_satelite:
    custo_calculado = (6000 * peso) + 15000
    print(f"{peso:<15} | U$ {custo_calculado:<18,.2f}")
print()

eixo_x_modelo1 = list(range(0, 14))
eixo_y_modelo1 = []
for x in eixo_x_modelo1:
    y = (6000 * x) + 15000
    eixo_y_modelo1.append(y)

plt.figure(figsize=(7, 5))
plt.plot(eixo_x_modelo1, eixo_y_modelo1, color="blue", marker="o", linestyle="-", label="y = 6000x + 15000")
plt.title("Modelo 1: Função Afim\nCusto de Lançamento por Peso da Carga (Rideshare)")
plt.xlabel("Peso da Carga Útil (kg)")
plt.ylabel("Custo Total do Lançamento (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_modelo1_afim.png")
plt.close()
print("[INFO] Gráfico do Modelo 1 gerado com sucesso: grafico_modelo1_afim.png")
print()


# ==============================================================================
# MODELO 2 - FUNÇÃO QUADRÁTICA (2º GRAU)
# Função Ajustada da Economia: E(n) = -2.5*n^2 + 35*n - 32.5
# Variáveis:
#   n (Domínio): Número de equipes compartilhando o voo [1, 10]
#   E(n) (Imagem): Porcentagem de economia em relação ao lançamento solo
# ==============================================================================

print("---------------------------------------------------------------------")
print("MODELO 2: Função de 2º Grau (Economia do Modelo de Lançamento Compartilhado)")
print("Equação Ajustada: E(n) = -2.5n² + 35n - 32.5")
print("---------------------------------------------------------------------")

custo_voo_solo = 14000
a2 = -2.5
b2 = 35.0
c2 = -32.5

print(f"Custo Base do Lançamento Individual (Solo): USD {custo_voo_solo}")
print("Análise de Concavidade: Como o coeficiente 'a' (-2.5) é NEGATIVO, a parábola tem concavidade para BAIXO.")
print("Isso indica a existência de um PONTO MÁXIMO de economia econômica.")
print()

n_vertice = -b2 / (2 * a2)
economia_maxima = (a2 * (n_vertice ** 2)) + (b2 * n_vertice) + c2

delta_parabola = (b2 ** 2) - (4 * a2 * c2)

print(f"-> Estudo do Vértice:")
print(f"   Xv (Número ideal de equipes): {n_vertice:.1f} equipes")
print(f"   Yv (Economia Máxima Teórica): {economia_maxima:.2f}%")
print(f"-> Delta da Função: {delta_parabola:.2f} (Como delta > 0, possui duas raízes reais)")
print("   Justificativa de Negócio: Após 7 equipes, a complexidade logística e adaptadores")
print("   reduzem o ganho marginal de economia por participante.")
print()

print("SIMULAÇÃO DE CENÁRIOS (OrbitShare):")
print(f"{'Equipes (n)':<12} | {'Custo Total':<14} | {'Custo/Equipe':<14} | {'Economia Real %':<15}")
print("-" * 65)

lista_equipes = [1, 2, 3, 4, 5, 6, 8, 10]

n_grafico_m2 = []
custo_total_m2 = []
custo_equipe_m2 = []
economia_real_m2 = []

for n in lista_equipes:
    c_total = 10000 + (4000 * n)
    c_equipe = c_total / n
    
    if n == 1:
        eco_porcentagem = 0.0
    else:
        eco_porcentagem = (1 - (c_equipe / custo_voo_solo)) * 100
        
    n_grafico_m2.append(n)
    custo_total_m2.append(c_total)
    custo_equipe_m2.append(c_equipe)
    economia_real_m2.append(eco_porcentagem)
    
    print(f"{n:<12} | U$ {c_total:<11,.0f} | U$ {c_equipe:<11,.0f} | {eco_porcentagem:<14.1f}%")
print()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(n_grafico_m2, custo_total_m2, color="red", marker="o", label="Custo Total da Missão")
ax1.plot(n_grafico_m2, custo_equipe_m2, color="blue", marker="s", label="Custo Individual por Equipe")
ax1.axhline(y=custo_voo_solo, color="gray", linestyle="--", label=f"Custo Voo Solo (USD {custo_voo_solo})")
ax1.set_title("Análise de Custos: Total vs Por Equipe")
ax1.set_xlabel("Número de Equipes (n)")
ax1.set_ylabel("Valor em Dólares (USD)")
ax1.legend()
ax1.grid(True)

n_continuo = []
economia_continua = []
temp_n = 1.0
while temp_n <= 10.0:
    n_continuo.append(temp_n)
    eco_quad = (a2 * (temp_n ** 2)) + (b2 * temp_n) + c2
    if eco_quad < 0:
        eco_quad = 0.0
    economia_continua.append(eco_quad)
    temp_n += 0.1

ax2.plot(n_continuo, economia_continua, color="green", label="Curva Teórica da Economia")
ax2.scatter(n_grafico_m2, economia_real_m2, color="red", zorder=5, label="Pontos Reais da Simulação")
ax2.scatter([n_vertice], [economia_maxima], color="purple", s=100, zorder=6, label=f"Vértice (Máximo: {economia_maxima:.1f}%)")
ax2.set_title("Curva de Economia Percentual (2º Grau)")
ax2.set_xlabel("Número de Equipes (n)")
ax2.set_ylabel("Economia (%)")
ax2.legend()
ax2.grid(True)

plt.suptitle("Modelo 2 - Análise Econômica da Plataforma OrbitShare", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("grafico_modelo2_quadratica.png")
plt.close()
print("[INFO] Gráfico do Modelo 2 gerado com sucesso: grafico_modelo2_quadratica.png")
print()


# ==============================================================================
# MODELO 3 - FUNÇÃO EXPONENCIAL
# Equação: S(t) = 100 * e^(0.28 * t)
# Variáveis:
#   t (Domínio): Anos decorridos após 2015 (t=0 -> ano 2015)
#   S(t) (Imagem): Quantidade de satélites lançados por ano mundialmente
# ==============================================================================

print("---------------------------------------------------------------------")
print("MODELO 3: Função Exponencial (Crescimento do Mercado Espacial)")
print("Equação: S(t) = 100 * e^(0.28t)")
print("---------------------------------------------------------------------")

S0 = 100
taxa_crescimento_r = 0.28

print(f"-> Tamanho de Mercado em 2015 (t=0): {S0} satélites lançados.")
print(f"-> Taxa de Crescimento Contínuo (r): {taxa_crescimento_r * 100:.0f}% ao ano.")
print("Análise de Comportamento: Como a base (e) é aproximadamente 2.718 e o expoente r > 0,")
print("a curva cresce de forma exponencial, caracterizando um mercado em BOOM tecnológico.")
print()

tempo_dobrar = math.log(2) / taxa_crescimento_r
print(f"-> Tempo de Dobramento Calculado: {tempo_dobrar:.2f} anos.")
print(f"   Significado Crítico: A cada {tempo_dobrar:.1f} anos, o volume de satélites lançados DOBRA,")
print("   o que justifica a urgência comercial de lançar o software SpaceLaunch Optimizer hoje (2026).")
print()

print("PROJEÇÃO DE MERCADO ATÉ 2030:")
print(f"{'Ano Calendário':<14} | {'Tempo (t)':<10} | {'Satélites/Ano':<18} | {'Market Share Estimado (15%)'}")
print("-" * 75)

anos_estudo = [2015, 2017, 2019, 2021, 2023, 2025, 2026, 2027, 2030]
valores_satelites_plot = []

for ano in anos_estudo:
    t = ano - 2015
    calculo_satelites = S0 * math.exp(taxa_crescimento_r * t)
    valores_satelites_plot.append(calculo_satelites)
    
    usuarios_plataforma = calculo_satelites * 0.15
    print(f"{ano:<14} | {t:<10} | {calculo_satelites:<18,.0f} | {usuarios_plataforma:,.0f} potenciais clientes")

print()

eixo_t_completo = list(range(0, 16))
eixo_anos_completo = []
eixo_s_completo = []

for t in eixo_t_completo:
    eixo_anos_completo.append(2015 + t)
    eixo_s_completo.append(S0 * math.exp(taxa_crescimento_r * t))

plt.figure(figsize=(7, 5))
plt.plot(eixo_anos_completo, eixo_s_completo, color="darkorange", marker="d", linestyle="-", label="S(t) = 100 * e^(0.28t)")
plt.axvline(x=2026, color="purple", linestyle="--", label="Ano Atual (2026)")

sat_2026 = S0 * math.exp(taxa_crescimento_r * (2026 - 2015))
plt.scatter([2026], [sat_2026], color="red", s=120, zorder=5)

plt.title("Modelo 3: Análise Exponencial\nEvolução do Volume de Pequenos Satélites Lançados")
plt.xlabel("Ano Cronológico")
plt.ylabel("Satélites Lançados por Ano")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_modelo3_exponencial.png")
plt.close()
print("[INFO] Gráfico do Modelo 3 gerado com sucesso: grafico_modelo3_exponencial.png")
print()

print("=====================================================================")
print("  EXECUÇÃO COMPLETA: Todos os modelos e gráficos salvos com sucesso! ")
print("  Pronto para anexar no Relatório Técnico da Global Solution 2026.    ")
print("=====================================================================")