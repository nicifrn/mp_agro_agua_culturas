# Plano de trabalho - Calculadora de necessidade de água das culturas

**Estudantes:** Teófilo (@teofilo) e @Zeke-Maker - Técnico Integrado em Informática

**Orientadores:** Prof. Bruno Gomes (@brunogomesifrn) e Entony (@franciscoentony) - NIC/IFRN

**Repositório:** https://github.com/nicifrn/mp_agro_agua_culturas

**Período:** 16/10/2026 a 10/12/2026: 8 sprints de 1 semana (de sexta a quinta-feira). As duas primeiras são de aprendizado de Python.

**Projeto pai:** AgroAgreste, observatório territorial da agricultura familiar no Agreste do Rio Grande do Norte (resumo em [`docs/projeto_agroagreste.md`](projeto_agroagreste.md)).

**Trabalho escrito:** um **artigo**, no **formato de TCC do NIC**, seguindo as normas de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).

> **Leiam este documento inteiro antes de começar a Sprint 1.** Ele é a referência completa do trabalho de vocês: tudo o que vocês vão aprender, programar, pesquisar e escrever está aqui, sprint por sprint. As *issues* do GitHub são o resumo de cada semana e sempre apontam para a seção correspondente deste documento. Se uma *issue* e este documento parecerem dizer coisas diferentes, **vale este documento**.

---

## Sumário

- [1. Como usar este documento e o quadro de tarefas](#como-usar)
- [2. A ideia do trabalho](#ideia)
- [3. Decisões já tomadas](#decisoes)
- [4. Cronograma](#cronograma)
- [5. Como trabalhar no repositório (fluxo do NIC)](#fluxo-git)
- [6. Como vocês dois trabalham juntos](#dupla)
- [7. A estrutura de pastas que vocês vão construir](#estrutura)
- [8. Combinados que valem para todas as sprints](#combinados)
- [9. Como escrever o artigo](#escrita-geral)
- [Sprint 1 - Aprender Python, parte 1](#sprint-1-dev)
- [Sprint 2 - Aprender Python, parte 2](#sprint-2-dev)
- [Sprint 3 - Os dados de clima da NASA POWER](#sprint-3-dev)
- [Sprint 4 - A evapotranspiração pelo método de Hargreaves-Samani](#sprint-4-dev)
- [Sprint 5 - A validação com Penman-Monteith](#sprint-5-dev)
- [Sprint 6 - A necessidade de água da mandioca e do feijão](#sprint-6-dev)
- [Sprint 7 - O balanço hídrico mensal e os gráficos](#sprint-7-dev)
- [Sprint 8 - O programa completo, o README e o fechamento](#sprint-8-dev)
- [10. Quadro-resumo](#quadro-resumo)
- [11. Riscos e planos B](#riscos)
- [12. Se sobrar tempo](#extras)
- [13. Referências mínimas do artigo](#referencias-minimas)

---

<a id="como-usar"></a>
## 1. Como usar este documento e o quadro de tarefas

### As *issues* e o quadro (kanban)

Eu cadastrei as tarefas de vocês como *issues* no repositório. **Cada *issue* é dos dois**: ela aparece com os dois como responsáveis, e vocês se organizam para dividir o trabalho (a [seção 6](#dupla) explica como). Toda semana tem:

- **uma *issue* com a etiqueta `Desenvolvimento`**: o que vocês vão aprender ou programar;
- **uma *issue* com a etiqueta `Escrita`**: o que vocês vão pesquisar e escrever no artigo. Em seis semanas ela é a entrega de uma parte do texto. Em duas semanas (Sprints 1 e 6) não há entrega de seção nova, e a *issue* é uma tarefa menor: na Sprint 1, preparar o documento e fichar leituras; na Sprint 6, colocar no documento as tabelas com os números da validação. Essas tarefas pequenas existem para o texto não ficar parado, porque **quem deixa os Resultados para o fim não entrega**.

As *issues* de uma semana estão agrupadas em um **marco** (*milestone*) com o nome e a data da sprint, por exemplo `Sprint 04 - Hargreaves-Samani (06/11 a 12/11)`. A página **Milestones** do repositório mostra quanto de cada sprint já foi concluído.

O **quadro do projeto** (aba *Projects* do repositório) tem quatro colunas:

| Coluna | Quando o card fica aqui |
|---|---|
| **A fazer** | a tarefa ainda não começou |
| **Em andamento** | vocês estão trabalhando nela. **Movam o card assim que começarem** |
| **Em revisão** | vocês terminaram e avisaram os orientadores |
| **Concluído** | os orientadores aprovaram e fecharam a *issue* |

### Como cada sprint está organizada neste documento

Cada sprint tem duas partes, **Desenvolvimento** e **Escrita**, e cada uma tem um endereço próprio (`#sprint-4-dev`, `#sprint-4-escrita`), que é para onde as *issues* apontam.

A parte de desenvolvimento tem sempre os mesmos blocos:

- **O que vocês vão entregar**: em uma frase, o que precisa estar funcionando no fim da semana;
- **Sugestão de divisão**: uma forma de repartir a semana entre os dois;
- **Passo a passo**: a lista numerada do que fazer, na ordem. Sigam na ordem, sem pular;
- **Como saber que deu certo**: o que vocês devem ver na tela ou no arquivo. Se não virem isso, ainda não terminou;
- **Entrega da sprint**: a lista de conferência que também está na *issue*.

**Neste documento eu não dou os programas prontos.** Eu digo o que cada programa precisa fazer, em que ordem, quais funções usar e o que pesquisar. Quem escreve o código são vocês, e é isso que faz o trabalho ser de vocês. As fórmulas aparecem completas, porque são o objeto de estudo e vão para o artigo; os trechos de Python são **peças** (uma chamada de função, um esqueleto com comentários), não a solução montada.

### Como entregar

**Desenvolvimento:**

1. abram um *pull request* (PR) da *branch* da sprint para a `develop`, seguindo a [seção 5](#fluxo-git), com `Closes #N` na descrição (o número N de cada sprint está indicado na própria sprint);
2. comentem na *issue*: `@brunogomesifrn @franciscoentony entrega da Sprint N pronta para revisão - PR #X`;
3. movam o card para **Em revisão**.

Quando um de nós aprovar e fizer o *merge* do PR, a *issue* fecha sozinha e o card vai para **Concluído**. Se pedirmos ajustes, façam os ajustes na mesma *branch* (o PR se atualiza sozinho) e comentem de novo.

**Escrita:**

1. escrevam no documento do Google Drive (veja a [seção 9](#escrita-geral));
2. nomeiem a versão no histórico do Drive (*Arquivo → Histórico de versões → Nomear versão atual*), por exemplo `Entrega 1 - Introdução - 29/10`;
3. comentem na *issue*: `@brunogomesifrn @franciscoentony Introdução pronta para revisão - versão "Entrega 1 - Introdução - 29/10"`;
4. movam o card para **Em revisão**.

Nós comentamos no próprio documento do Drive. Quando a seção estiver aprovada, fechamos a *issue*.

### Regras de ouro

- **Entreguem no prazo, mesmo incompleto.** Trabalho pela metade dá para revisar; trabalho que não chega, não. Na *issue*, digam o que ficou faltando.
- **Terminaram antes? Não comecem a próxima sprint.** Usem o tempo para entender melhor o que fizeram e para adiantar a escrita.
- **Travaram mais de 40 minutos no mesmo erro? Parem e peçam ajuda.** Primeiro um ao outro; depois, comentem na *issue* da semana, marcando nós dois, com: o que estavam tentando fazer, o comando que rodaram e **a mensagem de erro inteira, copiada e colada** (não um resumo, nem um print cortado). Pedir ajuda depois de 40 minutos não é desistir, é administrar o tempo.

---

<a id="ideia"></a>
## 2. A ideia do trabalho

### O problema

Uma planta "sua", como a gente. A água sai pelas folhas (isso se chama **transpiração**) e também evapora do solo em volta (**evaporação**). Somadas, as duas são a **evapotranspiração**, medida em milímetros de água por dia, como a chuva. Em um dia quente, seco e com vento, a plantação perde muito mais água do que em um dia nublado e frio.

Se a chuva de um mês é **menor** do que a água que a plantação perdeu, falta água (**déficit**): a planta sofre, e o agricultor só colhe bem se irrigar. Se a chuva é **maior**, sobra água (**excedente**). Saber em quais meses falta água para a mandioca e para o feijão ajuda a escolher a época de plantar e a planejar o uso da água, e esse é justamente um dos temas de **Educação Ambiental** do projeto AgroAgreste: o uso consciente da água.

### Como se calcula

O cálculo tem três passos, todos descritos no **manual FAO-56**, da Organização das Nações Unidas para a Alimentação e a Agricultura (FAO), que é a referência mundial no assunto:

1. **ET₀, a evapotranspiração de referência:** quanto de água uma grama baixa e bem regada perderia naquele dia, naquele lugar. Depende só do clima;
2. **Kc, o coeficiente de cultura:** um número que diz quanto uma cultura específica perde **em relação à grama**. Muda conforme a fase da planta: pequeno logo depois do plantio, maior quando a planta está crescida, e cai de novo perto da colheita;
3. **ETc, a necessidade de água da cultura:** `ETc = Kc × ET₀`. Comparando a ETc com a chuva, vocês obtêm o **balanço**: `chuva - ETc`. Negativo é déficit; positivo é excedente.

### O ponto que faz disto um artigo

O método **padrão** para calcular a ET₀ é o de **Penman-Monteith**, que precisa de temperatura, umidade do ar, vento e radiação solar. Muitas vezes esses dados não existem, principalmente em municípios pequenos sem estação meteorológica completa. Existe um método mais simples, o de **Hargreaves-Samani**, que precisa **só da temperatura** e é fácil de programar. A pergunta é se ele é bom o suficiente.

A pergunta que o trabalho de vocês responde é:

> **O método de Hargreaves-Samani, que usa só a temperatura, estima a evapotranspiração de Nova Cruz (RN) com erro pequeno em relação ao método padrão da FAO? E, usando essa estimativa, em quais meses do ciclo falta água para a mandioca e para o feijão?**

Para responder, vocês vão:

| O que fazer | Como |
|---|---|
| **Obter o clima** | dados diários de temperatura, chuva, umidade, vento e radiação de 2015 a 2024, da API gratuita da NASA POWER |
| **Calcular a ET₀ com Hargreaves-Samani** | programando vocês mesmos a fórmula do FAO-56, passo a passo |
| **Validar** | comparando com a ET₀ de Penman-Monteith calculada pela biblioteca `pyet` sobre os mesmos dados: erro médio, erro absoluto médio e correlação |
| **Testar** | testes automatizados com `pytest`, usando os exemplos numéricos publicados no próprio FAO-56 |
| **Calcular a necessidade de água** | a ETc da mandioca e do feijão, com os Kc do FAO-56 |
| **Comparar com a chuva** | tabela e gráfico mensal de chuva contra ETc, com o déficit ou excedente de cada mês |

### O que este trabalho **não** é

**Não é "fazer o AgroAgreste".** O observatório é o **contexto** que justifica a pergunta; o objeto do trabalho de vocês é uma **calculadora validada**, que depois pode virar um indicador do observatório. Vocês não mexem no código da plataforma.

**Não é um sistema de irrigação.** Vocês não vão dizer ao agricultor quanto irrigar no dia: vão mostrar, mês a mês, onde a chuva não dá conta da necessidade da cultura. É um indicador para planejamento e para Educação Ambiental.

### O que o trabalho de vocês tem a favor

1. **Ele produz números**, e números conferidos: a fórmula de vocês é testada contra os exemplos do FAO-56 e validada contra o método padrão.
2. **Ele fala da região de vocês**, com dados reais, e de duas culturas da agricultura familiar potiguar.
3. **Ele é útil para quem não tem estação meteorológica completa**: se o Hargreaves-Samani funcionar bem, qualquer município com um termômetro consegue estimar a necessidade de água.

---

<a id="decisoes"></a>
## 3. Decisões já tomadas

Para vocês não perderem tempo escolhendo:

| Item | Decisão |
|---|---|
| Linguagem | **Python 3** |
| Onde vocês trabalham | **computadores do laboratório (Windows)**. Não é possível instalar programas, mas o `pip install` e o Git funcionam |
| Editor | **VS Code** |
| Bibliotecas | `requests` (baixar da API), `pandas` (tabelas), `matplotlib` (gráficos), `pyet` (Penman-Monteith, para validar) e `pytest` (testes). Todas pelo `pip` |
| Fonte do clima | **NASA POWER**, API gratuita e sem cadastro |
| Município principal | **Nova Cruz (RN)**, do Agreste Potiguar |
| Município de comparação | **Canguaretama (RN)**, a cidade de vocês |
| Período | **de 01/01/2015 a 31/12/2024** (10 anos completos) |
| Culturas | **mandioca** e **feijão**, com os valores do FAO-56 |
| Data de plantio | **1º de abril** de cada ano, começo da estação chuvosa na região |
| Armazenamento | **arquivos CSV**. O volume (10 anos × 365 dias × 2 municípios, umas 7.300 linhas) cabe folgadamente em CSV, abre no Excel para conferência e não precisa de banco de dados |
| Repositório | `nicifrn/mp_agro_agua_culturas`, só de vocês dois, seguindo a política de desenvolvimento do NIC ([seção 5](#fluxo-git)) |
| Texto | **artigo**, no **formato de TCC do NIC**, em um documento do Google Drive que eu compartilho com vocês |
| O que **não** entra | banco de dados, Django, Docker, inteligência artificial, irrigação, chuva efetiva, dados de pessoas. O que for relevante vira "trabalho futuro" no artigo |

### Por que Nova Cruz, e não Canguaretama?

O projeto AgroAgreste trata do **Agreste Potiguar**. Canguaretama, pela divisão regional do IBGE, fica na mesorregião **Leste Potiguar** (microrregião do Litoral Sul), e não no Agreste. O município do Agreste mais perto de Canguaretama é **Nova Cruz**, a uns 35 km a oeste. Por isso Nova Cruz é o município principal do trabalho.

Canguaretama entra como **comparação**: é perto, mas mais perto do mar, e chove mais. Comparar os dois mostra como a necessidade de água muda em poucos quilômetros, o que é um resultado interessante e fala da cidade de vocês. Na Sprint 2 vocês vão conferir essa classificação na API do IBGE, com o próprio código.

### As coordenadas

A NASA POWER pede a latitude e a longitude do ponto. Use as das sedes dos municípios:

| Município | Código IBGE | Latitude | Longitude |
|---|---|---|---|
| Nova Cruz | 2408300 | -6.4778 | -35.4339 |
| Canguaretama | 2402204 | -6.3800 | -35.1281 |

Latitude negativa quer dizer **sul** do Equador; longitude negativa, **oeste** de Greenwich.

### Uso de inteligência artificial

- **Pode:** usar uma ferramenta de IA para entender uma mensagem de erro ou um conceito, como fariam com um colega.
- **Não pode:** pedir para a IA escrever os programas ou o texto do artigo. O código e o texto têm de ser de vocês, e vocês precisam saber explicar cada linha na apresentação.
- **Nunca:** colocar no artigo uma referência que vocês não abriram e leram. Ferramentas de IA inventam referências com naturalidade.

---

<a id="cronograma"></a>
## 4. Cronograma

Cada sprint vai de **sexta a quinta-feira**. O prazo de tudo é a **quinta-feira** que fecha a sprint.

| Sprint | Período | Desenvolvimento | Escrita |
|---|---|---|---|
| 1 | 16/10 a 22/10 | **Aprender Python, parte 1:** Git, ambiente, variáveis, condições, repetições e funções | Preparar o documento e fichar as leituras da Introdução |
| 2 | 23/10 a 29/10 | **Aprender Python, parte 2:** listas, dicionários, CSV, `pandas`, gráficos, API e testes | **Entrega 1:** Introdução e Objetivo geral |
| 3 | 30/10 a 05/11 | Os dados de clima da NASA POWER | **Entrega 2:** Referencial 2.1 e 2.2 |
| 4 | 06/11 a 12/11 | A ET₀ por Hargreaves-Samani, com testes | **Entrega 3:** Referencial 2.3, 2.4 e 2.5 |
| 5 | 13/11 a 19/11 | A validação com Penman-Monteith | **Entrega 4:** Metodologia e Materiais e Métodos |
| 6 | 20/11 a 26/11 | A necessidade de água da mandioca e do feijão | Tarefa curta: tabelas da validação no documento |
| 7 | 27/11 a 03/12 | O balanço hídrico mensal e os gráficos | **Entrega 5:** Resultados e Discussão |
| 8 | 04/12 a 10/12 | O programa completo, o README e o fechamento | **Entrega 6:** Conclusão, Objetivos específicos, Resumo e Título |

**Tudo termina em 10/12.**

**Feriados:** 02/11 (segunda, Sprint 3) e 20/11 (sexta, primeiro dia da Sprint 6). Nenhum prazo cai em feriado, mas nessas duas semanas o laboratório fica fechado um dia: **a semana tem um dia útil a menos**, então comecem cedo.

**Três avisos sobre o cronograma:**

1. **As duas primeiras semanas são de aprendizado, mas não são férias.** Os exercícios são todos sobre clima e chuva, de propósito: o que vocês aprenderem ali vai ser usado direto nas Sprints 3 a 8.
2. **Os Resultados vencem em 03/12, na mesma semana dos gráficos.** Por isso a Sprint 6 já manda colocar as tabelas da validação no documento, e a Sprint 7 manda terminar o balanço e os gráficos **até segunda-feira, 30/11**: a terça, a quarta e a quinta ficam para escrever.
3. **A última semana é cheia.** A Conclusão precisa estar escrita até **segunda-feira, 07/12**, para sobrar a terça, a quarta e a quinta para o Resumo, o *Abstract*, o Título e a revisão final.

---

<a id="fluxo-git"></a>
## 5. Como trabalhar no repositório (fluxo do NIC)

O NIC tem uma política de desenvolvimento que vale para todos os projetos. Abaixo está o que ela significa no trabalho de vocês.

### 5.1 As *branches*

| *Branch* | Para que serve | Quem mexe |
|---|---|---|
| `main` | versão estável e aprovada | só os orientadores, no fim do trabalho |
| `develop` | onde as sprints aprovadas vão se juntando. É a *branch* padrão do repositório | ninguém envia direto: só entra por PR aprovado |
| `feature/...` | **uma por sprint**, onde vocês dois trabalham | vocês |

Os nomes das *branches* das sprints já estão definidos em cada sprint (por exemplo, `feature/hargreaves`). Se precisarem corrigir algo de uma sprint que já foi aprovada, usem `fix/` (por exemplo, `fix/dia-do-ano`).

### 5.2 O ciclo de cada sprint (os dois na mesma *branch*)

**No começo da sprint** (sexta-feira), **um de vocês** cria a *branch* da semana a partir da `develop` atualizada e a envia para o GitHub:

```
git checkout develop
git pull
git checkout -b feature/nome-da-sprint
git push -u origin feature/nome-da-sprint
```

**O outro**, na própria máquina, busca a *branch* que o colega criou:

```
git checkout develop
git pull
git checkout feature/nome-da-sprint
```

**Toda vez que forem começar a trabalhar**, puxem o que o colega enviou:

```
git pull
```

**Ao fim de cada dia**, enviem o trabalho. Código que só existe na máquina do laboratório não foi entregue, e a máquina pode ser formatada:

```
git status
git add (os arquivos que vocês mexeram)
git commit -m "feat: adiciona cálculo da radiação extraterrestre"
git push
```

**Antes de todo `git add`, olhem o `git status`.** Se aparecer `.venv/` ou `__pycache__/`, o `.gitignore` está errado: corrijam antes de continuar.

> **O `git push` foi recusado** com a mensagem `rejected ... fetch first`? É porque o colega enviou algo antes. Rodem `git pull` e depois `git push` de novo. Se o `git pull` disser `CONFLICT`, é porque vocês dois mexeram nas **mesmas linhas do mesmo arquivo**: parem, abram o arquivo no VS Code (ele mostra as duas versões, com os botões *Accept Current Change* e *Accept Incoming Change*), decidam **juntos** qual fica, salvem, e façam `git add`, `git commit` e `git push`. A regra da [seção 6](#dupla) existe para isso quase nunca acontecer.

**No fim da sprint**, abram o PR (seção 5.4).

### 5.3 Mensagens de *commit*

Os *commits* devem ser **pequenos, objetivos e frequentes**: pelo menos 2 por semana **para cada um de vocês**. Usem o padrão abaixo, com a mensagem em português e o verbo no presente:

```
feat: adiciona cálculo da ET0 por Hargreaves-Samani
fix: corrige dia do ano em ano bissexto
docs: registra configuração da máquina
test: adiciona testes com os exemplos do FAO-56
refactor: separa as funções de cálculo em um módulo
```

| Prefixo | Quando usar |
|---|---|
| `feat:` | algo novo funcionando (um script, uma função, um exercício) |
| `fix:` | correção de algo que estava errado |
| `docs:` | documentação, diário, `README.md`, prints, tabelas de resultado |
| `test:` | testes |
| `refactor:` | reorganizar código sem mudar o que ele faz |

**Mensagens proibidas pela política do NIC:** `ajustes`, `mudanças`, `update`, `correções`. Se vocês não conseguem dizer em uma frase o que o *commit* faz, ele está grande demais.

### 5.4 O *pull request* do fim da sprint

1. Confiram se tudo foi enviado (`git status` deve dizer `nothing to commit`) e se o colega também enviou tudo.
2. Rodem os testes (a partir da Sprint 2): `python -m pytest`. Todos precisam passar.
3. No GitHub, abram o repositório. Vai aparecer uma faixa amarela com o botão **Compare & pull request**. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a *branch* da sprint**.
4. Preencham a descrição. O repositório já traz um modelo com os campos que a política do NIC exige:
   - **Objetivo:** o que esta sprint entrega, em uma ou duas frases;
   - **O que foi feito:** a lista do que foi implementado, **com o nome de quem fez cada parte**;
   - **Possíveis impactos:** o que muda para quem roda o projeto (um script novo, uma pasta nova, uma biblioteca nova);
   - **Evidências de teste:** a saída do `pytest` (copiada do terminal), as tabelas e os prints;
   - **Issue:** `Closes #N`, com o número indicado na sprint.
5. Em **Reviewers**, marquem `brunogomesifrn` e `franciscoentony`.
6. Comentem na *issue* e movam o card para **Em revisão** (veja a [seção 1](#como-usar)).

Basta **um** de vocês abrir o PR. **Vocês não fazem o *merge* do próprio PR, e um não aprova o PR do outro**: a política do NIC exige que um revisor aprove antes da integração, e os revisores são os orientadores. A revisão cruzada da [seção 6](#dupla) é feita **antes** de abrir o PR, rodando o código do colega, e não pelo botão de aprovação. **Um PR por sprint**: não acumulem duas sprints no mesmo PR.

### 5.5 Testes

A política do NIC pede que toda funcionalidade tenha testes compatíveis com a sua complexidade. No trabalho de vocês, os testes ficam na pasta `tests/` e usam a biblioteca **`pytest`**, que vocês aprendem na Sprint 2. Um teste é uma função cujo nome começa com `test_` e que usa o comando `assert`:

```python
def test_amplitude():
    assert amplitude(33.0, 22.0) == 11.0
```

Se a condição do `assert` for **verdadeira**, o teste passa. Se for **falsa**, o `pytest` mostra qual teste falhou, o valor esperado e o valor obtido.

Rodem sempre **a partir da raiz do repositório**, com o `.venv` ativo, assim:

```
python -m pytest
```

(Com `python -m` na frente, o Python enxerga os arquivos da raiz, e os *imports* dos testes funcionam.) O `pytest` procura sozinho, em todas as pastas do repositório, os arquivos cujo nome começa com `test_` (ele ignora a `.venv`).

### 5.6 Segurança

Nunca enviem para o repositório senhas, *tokens*, chaves ou arquivos `.env`. Neste trabalho vocês não precisam de nenhum deles: a API da NASA POWER não pede cadastro.

---

<a id="dupla"></a>
## 6. Como vocês dois trabalham juntos

Cada *issue* é dos dois. **Vocês decidem como dividir**, e em cada sprint há uma **sugestão de divisão** para ajudar. Três regras valem sempre:

1. **Um arquivo, um dono por vez.** Na sexta-feira, combinem quem mexe em qual arquivo naquela semana e anotem no comentário da *issue* (por exemplo: `Nome 1: calculos.py; Nome 2: tests/test_calculos.py`). Duas pessoas editando o mesmo arquivo no mesmo dia geram conflito no Git. Se precisar mudar o arquivo do colega, peçam a ele.
2. **Revisão cruzada antes do PR.** Antes de abrir o PR, cada um baixa o trabalho do outro (`git pull`) e **roda o código do colega na própria máquina**. É a forma mais barata de descobrir o "só funciona no meu computador": caminho de arquivo fixo, biblioteca instalada só de um lado, arquivo que não foi enviado.
3. **Os dois precisam entender tudo.** Vocês vão apresentar juntos e assinar um artigo só. No acompanhamento semanal, podemos pedir a um de vocês para explicar a parte do outro. Isso não é armadilha, é o combinado.

Uma forma que funciona bem para quem está aprendendo: **um escreve a função, o outro escreve o teste dela**, e na semana seguinte vocês trocam. Assim os dois programam e os dois testam.

No **diário** ([seção 8](#combinados)), cada um escreve as próprias três linhas.

---

<a id="estrutura"></a>
## 7. A estrutura de pastas que vocês vão construir

Vocês não precisam criar tudo de uma vez: cada sprint cria a sua parte. Esta é a figura final, para vocês saberem aonde estão indo. Tudo fica **na raiz do repositório** `mp_agro_agua_culturas/`:

```
mp_agro_agua_culturas/
├── .github/
│   └── pull_request_template.md  ← já existe (modelo do PR)
├── aprendizado/
│   ├── clima_exemplo.csv         ← já existe (dados de março de 2024, para os exercícios)
│   ├── semana1/                  ← exercícios da Sprint 1
│   └── semana2/                  ← exercícios da Sprint 2
├── dados/
│   ├── brutos/                   ← o que veio da NASA, sem mexer (Sprint 3)
│   ├── clima_nova_cruz.csv       ← Sprint 3
│   ├── clima_canguaretama.csv    ← Sprint 3
│   └── culturas.csv              ← os valores do FAO-56 (Sprint 6)
├── tests/
│   ├── test_calculos.py          ← Sprints 4 e 6
│   └── test_balanco.py           ← Sprint 7
├── resultados/                   ← tabelas geradas pelos scripts (Sprints 4 a 7)
├── graficos/                     ← figuras do artigo (Sprints 5 a 7)
├── docs/
│   ├── 01_descricao_geral.md     ← este documento (já existe)
│   ├── projeto_agroagreste.md    ← já existe
│   ├── orientacoes_escrita_tcc.md ← já existe
│   ├── ambiente.md               ← Sprint 1
│   ├── diario.md                 ← Sprint 1 em diante
│   ├── leituras.md               ← Sprint 1 em diante
│   └── evidencias/               ← prints de tela
├── calculos.py                   ← as funções de cálculo (Sprints 4, 6 e 7)
├── verificar_ambiente.py         ← Sprint 1
├── baixar_clima.py               ← Sprint 3
├── calcular_et0.py               ← Sprint 4
├── validar_et0.py                ← Sprint 5
├── calcular_etc.py               ← Sprint 6
├── balanco.py                    ← Sprint 7
├── rodar_tudo.py                 ← Sprint 8
├── .gitignore
├── requirements.txt
└── README.md
```

A ideia da organização: **as funções de cálculo** (fórmulas) ficam todas em `calculos.py`, que é o arquivo testado pelo `pytest`. **Os scripts** (`baixar_clima.py`, `calcular_et0.py`...) leem os arquivos, chamam as funções e gravam os resultados. Separar "fazer a conta" de "ler e gravar arquivo" é o que permite testar as contas.

---

<a id="combinados"></a>
## 8. Combinados que valem para todas as sprints

- **Rodem tudo a partir da raiz do repositório:** `python calcular_et0.py`, e não de dentro de outra pasta. Todos os caminhos dos programas (`dados/`, `resultados/`) partem da raiz.
- **Diário (`docs/diario.md`):** no fim de cada sprint, **cada um** escreve 3 linhas: o que funcionou, o que deu errado e o que aprendeu. Leva cinco minutos e vai escrever a Conclusão por vocês no fim do trabalho. Usem este formato:

  ```
  ## Sprint 4 - 06/11 a 12/11
  ### (nome do primeiro)
  - Funcionou: ...
  - Deu errado: ...
  - Aprendi: ...
  ### (nome do segundo)
  - Funcionou: ...
  - Deu errado: ...
  - Aprendi: ...
  ```

- **Nunca apaguem dado bruto.** O que veio da NASA fica em `dados/brutos/` do jeito que veio. Os scripts leem dali e gravam em outro lugar.
- **Anotem todo erro e toda surpresa.** Neste trabalho, **surpresa é resultado**. Se um mês saiu com déficit enorme, se o Hargreaves errou mais em algum período do ano, isso vai para o artigo.
- **Prints (`docs/evidencias/`):** sempre que algo funcionar (ou falhar de um jeito interessante), tirem um print (`Win + Shift + S`). Deem nomes que digam o que é: `s04_pytest_passando.png`.
- **Acompanhamento semanal:** no começo de cada sprint, vocês mostram aos orientadores o que fizeram na anterior, **rodando na tela**. A partir da Sprint 4, "está funcionando" não basta: tem que ter número.

---

<a id="escrita-geral"></a>
## 9. Como escrever o artigo

### 9.1 Onde escrever: o documento compartilhado no Google Drive

Na Sprint 1 eu compartilho com vocês um documento do Google Drive que **já está no formato de TCC do NIC** (capa, folha de rosto, resumo, sumário e as seções). O trabalho de vocês é um **artigo**: o formato é o do TCC, mas o texto é mais curto e mais direto (veja o tamanho na seção 9.3). Vocês não criam arquivo novo nem trabalham em cópia local.

- **Escrevam sempre no documento compartilhado.** Nada de escrever no Word e colar depois: o histórico do Drive é o que nos permite ver o que mudou de uma semana para outra, e quem escreveu o quê.
- **Não criem cópias** ("Artigo v2", "Artigo final"). O Drive já guarda tudo em **Arquivo → Histórico de versões**.
- **Marquem cada entrega no histórico:** *Arquivo → Histórico de versões → Nomear versão atual*, com um rótulo como `Entrega 1 - Introdução - 29/10`.
- **Avisem na *issue* quando entregarem**, como explicado na [seção 1](#como-usar).
- **Comentário se responde, não se apaga.** Respondam a cada comentário dizendo o que fizeram e só então marquem como resolvido.
- **Resolvam todos os comentários da entrega anterior antes de avisar sobre a próxima.**
- **Figuras e tabelas** vão dentro do documento, no lugar certo, com a identificação em cima e a fonte embaixo.
- **Não deem acesso ao documento a outras pessoas.**

**Como dois autores escrevem um texto só:** dividam as subseções de cada entrega entre os dois (anotem a divisão no comentário da *issue*) e, antes de entregar, **cada um lê a parte do outro inteira** e corrige o que estiver confuso. O texto final tem de parecer escrito por uma pessoa só: mesma forma de chamar as coisas (sempre "ET₀", sempre "Hargreaves-Samani"), mesmo tempo verbal.

### 9.2 As normas

Todas as regras de escrita e de ABNT estão em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): estrutura, citações, referências, figuras, tabelas, formatação e linguagem. **Leiam esse arquivo inteiro na Sprint 1.** Ele foi escrito para o TCC e vale para o artigo do mesmo jeito; a única diferença é o tamanho de cada seção. Este plano não repete as regras da ABNT; ele diz **o que pesquisar e o que escrever** em cada seção.

> **Importante:** o que está neste plano são **orientações**, não o texto pronto. Não copiem estas frases para o artigo. Elas dizem sobre o que é cada parágrafo; o texto tem de ser escrito por vocês, com as suas palavras e com as referências que leram.

### 9.3 A estrutura do artigo

```
1 INTRODUÇÃO
1.1 Objetivo geral
1.2 Objetivos específicos
2 REFERENCIAL TEÓRICO
2.1 Agricultura familiar, água e Educação Ambiental no semiárido
2.2 Evapotranspiração e necessidade de água das culturas
2.3 Métodos de estimativa da evapotranspiração de referência
2.4 Dados climáticos da NASA POWER
2.5 Trabalhos relacionados
3 METODOLOGIA
3.1 Classificação da pesquisa
3.2 Área de estudo e período
3.3 Etapas do trabalho
4 MATERIAIS E MÉTODOS
4.1 Materiais
4.2 Obtenção dos dados
4.3 Cálculo e validação da ET₀
4.4 Necessidade de água das culturas e balanço
5 RESULTADOS E DISCUSSÃO
5.1 O clima de Nova Cruz e Canguaretama
5.2 Validação do método de Hargreaves-Samani
5.3 Necessidade de água da mandioca e do feijão
5.4 Balanço hídrico mensal
5.5 Limitações
6 CONCLUSÃO
REFERÊNCIAS
```

Tamanho de referência da parte textual (da Introdução à Conclusão): **de 12 a 18 páginas**, mais ou menos assim: Introdução, 2; Referencial, 4 a 5; Metodologia e Materiais e Métodos, 3 a 4; Resultados, 4 a 6; Conclusão, 1.

### 9.4 As três perguntas de pesquisa

O trabalho gira em torno de três perguntas, que saem da pergunta principal da [seção 2](#ideia). Elas aparecem na Metodologia, organizam os Resultados e são respondidas na Conclusão:

1. qual é o **erro** da ET₀ calculada por Hargreaves-Samani em relação à de Penman-Monteith, nos dados diários e nos totais mensais, em Nova Cruz e em Canguaretama?
2. quanto de água a **mandioca** e o **feijão** precisam, mês a mês, plantados em 1º de abril?
3. em quais meses do ciclo de cada cultura a chuva **não dá conta** da necessidade de água, e quanto falta?

### 9.5 Regras que valem para o texto inteiro

- **Toda afirmação técnica precisa de referência.**
- **Não empilhem citações.** Expliquem com as suas palavras e amarrem ao trabalho.
- **Documentação oficial** (NASA POWER, `pyet`, Python) serve para descrever a ferramenta, não para fundamentar conceito. Para conceito, usem livro, manual da FAO ou artigo.
- **Nada de blog, Stack Overflow ou site sem autoria** nas Referências.
- **Nunca citem uma referência que vocês não leram.**
- **Criem a seção "Referências" no primeiro dia** e acrescentem cada obra assim que lerem.
- **Meta:** de 10 a 15 referências (lista mínima na [seção 13](#referencias-minimas)).
- **Fichamento:** tudo o que vocês lerem vai para `docs/leituras.md`, no formato abaixo. É ele que transforma leitura em texto:

  ```
  ## ALLEN et al. (1998)
  - Quem fichou: (nome)
  - Referência completa (ABNT): ...
  - Onde achei: (endereço)
  - Ideia principal, com as minhas palavras: ...
  - Trecho que posso citar (com página): "..." (p. X)
  - Vou usar na seção: 2.2 e 2.3
  ```

---

# Sprint 1: 16/10 a 22/10/2026

<a id="sprint-1-dev"></a>
## Sprint 1 · Desenvolvimento: aprender Python, parte 1

**Branch:** `feature/aprendizado-semana1` · **No PR:** `Closes #1`

**O que vocês vão entregar:** o Git configurado nas duas máquinas, o repositório clonado, o ambiente virtual com as bibliotecas, o programa que confere o ambiente e **seis exercícios de Python feitos por cada um**, todos sobre temperatura e chuva.

**Esta semana e a próxima são de aprendizado.** Vocês não precisam saber Python para começar: precisam assistir às aulas indicadas, digitar os exemplos junto com o professor e fazer os exercícios. **Cada um faz todos os exercícios**, na própria pasta: quem só olha o colega programar não aprende.

**Sugestão de divisão:** os passos 1 a 6 vocês fazem juntos, na sexta (um cria a *branch* e o `requirements.txt`, o outro cria o `.gitignore` e o `verificar_ambiente.py`). Os exercícios, cada um faz os seus. Na quinta, cada um roda os exercícios do outro (revisão cruzada).

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 16/10 | passos 1 a 6 (Git, repositório, ambiente, verificação) |
| segunda, 19/10 | passo 7 (aulas do Mundo 1) e exercícios 1 e 2 |
| terça, 20/10 | aulas de condições e exercício 3 |
| quarta, 21/10 | aulas de repetição (Mundo 2) e exercícios 4 a 6 |
| quinta, 22/10 | revisão cruzada, diário, *commits* e PR; a escrita da semana |

### Passo a passo

**1. Aprendam o básico de Git e GitHub.** Assistam às aulas iniciais do Curso de Git e GitHub do Curso em Vídeo (https://www.cursoemvideo.com/curso/curso-de-git-e-github/), até a parte em que o repositório é enviado para o GitHub. Depois leiam a [seção 5](#fluxo-git) e a [seção 6](#dupla) deste documento inteiras.

**2. Configurem o Git**, cada um na sua máquina do laboratório (uma vez só por máquina), com o mesmo e-mail da conta do GitHub. Abram o Prompt de Comando (tecla `Win`, digitem `cmd`, Enter):

```
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email-do-github@exemplo.com"
```

**3. Aceitem o convite do repositório.** Cada um recebeu por e-mail um convite para o `nicifrn/mp_agro_agua_culturas`. Aceitem (ou abram https://github.com/nicifrn/mp_agro_agua_culturas/invitations). Aceitem também o convite do quadro do projeto, que chega no mesmo e-mail.

**4. Clonem o repositório**, cada um na sua máquina:

```
cd %USERPROFILE%
git clone https://github.com/nicifrn/mp_agro_agua_culturas.git
cd mp_agro_agua_culturas
```

Na primeira vez que o Git falar com o GitHub, abre uma janela do navegador pedindo login. Entrem com a conta e autorizem. Depois **um** de vocês cria a *branch* da sprint e o **outro** a busca, como explicado na [seção 5.2](#fluxo-git). Abram a pasta `mp_agro_agua_culturas` no VS Code (*File → Open Folder*). A partir de agora, **é sempre essa pasta que vocês abrem**.

**5. Criem o ambiente virtual e instalem as bibliotecas.** O ambiente virtual é uma "caixa" só deste projeto, onde as bibliotecas ficam instaladas sem bagunçar o Python da máquina. Cada um, na própria máquina, na raiz do repositório, **no Prompt de Comando** (e não no PowerShell):

```
python -m venv .venv
.venv\Scripts\activate
pip install requests pandas matplotlib pyet pytest
```

Depois de ativar, o começo da linha passa a mostrar `(.venv)`. **Se não mostrar, o ambiente não está ativo**, e o que vocês instalarem vai para o lugar errado. Toda vez que abrirem um terminal novo, ativem de novo.

**Só um de vocês** gera a lista das bibliotecas e a envia: `pip freeze > requirements.txt`. O outro, depois do `git pull`, pode conferir que está tudo igual com `pip install -r requirements.txt`.

> No terminal do VS Code (`` Ctrl + ` ``), abram o seletor de terminal (setinha ao lado do `+`) e escolham **Command Prompt**. No PowerShell, o `activate` costuma dar erro de "execução de scripts desabilitada".
>
> Se o comando `python` não for reconhecido, tentem `py`. Se o `py` funcionar, usem `py` no lugar de `python` em todos os comandos deste documento, e anotem isso no diário.

**6. Criem as pastas, o `.gitignore` e o programa que confere o ambiente.**

1. Criem as pastas `aprendizado\semana1`, `aprendizado\semana2`, `dados\brutos`, `tests`, `resultados`, `graficos` e `docs\evidencias` (veja a [seção 7](#estrutura)). *Pesquisem:* o comando `mkdir` no Windows. O Git não guarda pastas vazias; por isso, coloquem dentro de cada pasta vazia um arquivo vazio chamado `.gitkeep`.
2. Criem o arquivo `.gitignore` na raiz, com este conteúdo:

   ```
   .venv/
   __pycache__/
   *.pyc
   .pytest_cache/
   ```

3. Escrevam `verificar_ambiente.py`, o primeiro programa de vocês. Ele mostra, um por linha, a versão do Python e a versão de cada biblioteca instalada. É curto (umas 8 linhas). Ele precisa:
   1. importar o módulo `sys` e mostrar `sys.version`;
   2. importar `requests`, `pandas`, `matplotlib`, `pyet` e `pytest`;
   3. mostrar, para cada uma, o nome e a versão, que fica guardada em `nome_da_biblioteca.__version__`.

   *Pesquisem:* o comando `import` e a função `print` com vários valores separados por vírgula. Rodem com `python verificar_ambiente.py`. Se der `ModuleNotFoundError`, o ambiente virtual não está ativo.

4. Criem `docs/ambiente.md` com a configuração das duas máquinas (tecla `Win`, digitem "Sobre o seu PC": anotem "Processador", "RAM instalada", "Edição" e "Versão" do Windows) e a saída do `verificar_ambiente.py`.

**7. Assistam às aulas de Python.** Usem o **Curso de Python 3 do Curso em Vídeo** (gratuito, com o professor Gustavo Guanabara):

- **Mundo 1** (https://www.cursoemvideo.com/curso/python-3-mundo-1/): das aulas iniciais até as **condições** (primeiros comandos, tipos primitivos, operadores aritméticos, módulos e condições);
- **Mundo 2** (https://www.cursoemvideo.com/curso/python-3-mundo-2/): as aulas de **condições aninhadas** e de **repetição** (`for` e `while`).

**Digitem os exemplos junto com as aulas**, no VS Code, em vez de só assistir. É digitando e errando que se aprende. Os exercícios do próprio curso são ótimos, mas não são obrigatórios: os obrigatórios são os seis abaixo.

**8. Façam os seis exercícios.** Cada um cria a própria pasta, `aprendizado\semana1\<seu-primeiro-nome>\` (sem acento e em minúsculas, por exemplo `aprendizado\semana1\teofilo\`), e salva um arquivo por exercício. Para cada um há **o que o programa faz**, **o que pesquisar** e **um teste**: rodem com os valores do teste e confiram se a saída bate.

| Exercício | O que o programa faz | Pesquisem | Teste |
|---|---|---|---|
| `ex01_conversao.py` | pede uma temperatura em graus Celsius e mostra em graus Fahrenheit. A fórmula é `F = C × 9 / 5 + 32` | `input`, `float`, `print` | 30 → 86.0 |
| `ex02_media_amplitude.py` | pede a temperatura máxima e a mínima de um dia e mostra a **média** das duas e a **amplitude** (máxima menos mínima) | operadores aritméticos | 33 e 22 → média 27.5 e amplitude 11.0 |
| `ex03_dia_chuvoso.py` | pede a chuva do dia, em milímetros, e mostra `dia chuvoso` se for de 1 mm ou mais, e `dia seco` se for menos | `if` e `else` | 0.5 → dia seco; 8.62 → dia chuvoso |
| `ex04_semana_de_chuva.py` | a chuva dos 7 primeiros dias de março de 2024 em Nova Cruz está na lista `[8.62, 0.88, 2.11, 1.71, 15.56, 6.27, 8.06]`. Escreva-a no código e mostre o **total**, a **maior** chuva e **quantos dias secos** (menos de 1 mm) houve, usando um `for` | listas, `for`, contador, acumulador | total 43.21, maior 15.56, 1 dia seco |
| `ex05_graus_radianos.py` | pede uma latitude em graus e minutos e mostra o valor em **radianos**. Primeiro converta para graus decimais (`graus + minutos / 60`); depois, para radianos (`graus × π / 180`). Se a latitude for sul, o valor é negativo | `math.pi`, `round` | 13° 44' norte → 0.24; 22° 54' sul → -0.4 |
| `ex06_funcoes.py` | crie três funções: `amplitude(tmax, tmin)`, `media(a, b)` e `classificar_dia(chuva)` (que **devolve** o texto `"chuvoso"` ou `"seco"`). Chame as três para os valores dos testes acima e mostre os resultados | `def` e `return` | os mesmos valores dos exercícios 2 e 3 |

No `ex04`, arredonde o total para duas casas (`round(total, 2)`). Somas de números decimais no computador às vezes dão `43.209999999`, e isso é normal: os números decimais não são exatos no computador. Anotem no diário que vocês viram isso.

> **O exercício 5 não é à toa:** os valores do teste são do **Exemplo 7 do manual FAO-56**, e a conversão de graus para radianos vai ser a primeira função do cálculo da evapotranspiração, na Sprint 4.

**9. Revisão cruzada, diário e PR.** Na quinta, cada um roda os seis exercícios do colega (`python aprendizado\semana1\<nome>\ex04_semana_de_chuva.py`) e confere os testes. Criem `docs/diario.md` com as três linhas de cada um ([seção 8](#combinados)). Façam os *commits* (cada um os seus) e abram o PR para a `develop` com `Closes #1`, colando em **Evidências de teste** a saída do `verificar_ambiente.py`.

### Como saber que deu certo

- O terminal mostra `(.venv)` no começo da linha, nas duas máquinas.
- `python verificar_ambiente.py` mostra a versão do Python e das cinco bibliotecas.
- Cada um tem seis exercícios na sua pasta, e todos dão a saída do teste.
- O `git status` **não** mostra `.venv/` nem `__pycache__/`.

### Entrega da sprint

- [ ] Git configurado nas duas máquinas e repositório clonado.
- [ ] *Branch* `feature/aprendizado-semana1` criada por um e buscada pelo outro.
- [ ] Ambiente virtual com as cinco bibliotecas e `requirements.txt` enviado.
- [ ] Estrutura de pastas e `.gitignore`.
- [ ] `verificar_ambiente.py` funcionando e `docs/ambiente.md` preenchido.
- [ ] Os seis exercícios de **cada um**, em `aprendizado/semana1/<nome>/`, conferidos pelo colega.
- [ ] `docs/diario.md` com as três linhas de cada um.
- [ ] PR aberto para a `develop`, com `Closes #1`.

### Erros comuns

- **`'python' não é reconhecido`:** usem `py` (veja o passo 5).
- **O `activate` não funciona:** vocês estão no PowerShell. Troquem para o Command Prompt.
- **`TypeError: can't multiply sequence by non-int of type 'float'`:** o `input` devolve texto. Convertam com `float(...)` antes de fazer contas.
- **`IndentationError`:** o Python usa os espaços no começo da linha para saber o que está dentro do `if`, do `for` e do `def`. Usem 4 espaços, sempre.

<a id="sprint-1-escrita"></a>
## Sprint 1 · Escrita: preparar o documento e fichar as leituras da Introdução

**O que vocês vão entregar:** o documento do artigo aberto e preparado, as normas lidas e as leituras da Introdução fichadas. Nesta semana não há entrega de seção.

**Sugestão de divisão:** os passos 1 a 4 juntos; no passo 5, cada um fica com metade das leituras.

### Passo a passo

**1. Abram o documento do artigo** que eu compartilhei com vocês no Google Drive (o convite chega no e-mail). Preencham a capa e a folha de rosto com os nomes de vocês, o curso, o nome dos orientadores e o título provisório: *Necessidade de água da mandioca e do feijão em Nova Cruz (RN): uma calculadora baseada no método de Hargreaves-Samani*.

**2. Criem a seção "REFERÊNCIAS"** no fim do documento, ainda vazia. A partir de hoje, toda obra que vocês lerem entra nela no mesmo dia.

**3. Leiam as normas.** Leiam [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) inteiro, com atenção especial a: estrutura do trabalho, Introdução, objetivo geral, como citar e como referenciar.

**4. Leiam o resumo do projeto pai** em [`docs/projeto_agroagreste.md`](projeto_agroagreste.md). Ele é o ponto de partida da Introdução.

**5. Pesquisem, leiam e fichem em `docs/leituras.md`** (no formato da [seção 9.5](#escrita-geral); este arquivo entra no PR de desenvolvimento da semana):

- **a Lei nº 11.326, de 24 de julho de 2006**, que define agricultor familiar: procurem no portal da legislação federal (`planalto.gov.br`) e leiam o artigo 3º;
- **a produção de mandioca e de feijão em Nova Cruz:** no **SIDRA do IBGE** (`sidra.ibge.gov.br`), abram a **tabela 5457** (Produção Agrícola Municipal), escolham o ano mais recente, o município Nova Cruz (RN) e as culturas mandioca e feijão, e anotem a **área plantada** (hectares) e a **quantidade produzida** (toneladas). Anotem também o ano dos dados e a data da consulta. Número concreto vale mais que adjetivo;
- **o Semiárido brasileiro:** procurem no site da **SUDENE** (`gov.br/sudene`) a delimitação oficial do Semiárido mais recente e verifiquem se **Nova Cruz** e **Canguaretama** estão na lista de municípios. Anotem o resultado e o documento oficial (número da resolução e ano);
- **o uso da água na agricultura:** no relatório **Conjuntura dos Recursos Hídricos no Brasil**, da **Agência Nacional de Águas e Saneamento Básico (ANA)** (`gov.br/ana`), procurem qual porcentagem da água retirada no Brasil vai para a irrigação. Anotem o número e o ano do relatório;
- **a Lei nº 9.795, de 27 de abril de 1999**, que institui a Política Nacional de Educação Ambiental: leiam os artigos 1º e 2º (o que é Educação Ambiental);
- **o manual FAO-56:** ALLEN, R. G. *et al.* *Crop evapotranspiration: guidelines for computing crop water requirements*. Roma: FAO, 1998 (FAO Irrigation and Drainage Paper 56). Ele está disponível gratuitamente no site da FAO (`fao.org`): procurem pelo título. Está em inglês; usem o tradutor do navegador para ajudar, mas anotem os termos técnicos em inglês também. Leiam o **capítulo 1** (*Introduction to evapotranspiration*): é curto e explica, com figuras, tudo o que está na [seção 2](#ideia) deste plano.

### Como saber que deu certo

- O documento do Drive tem capa, folha de rosto e a seção de Referências criadas.
- O `docs/leituras.md` tem pelo menos **6 obras fichadas**, cada uma com a referência completa no formato ABNT e o nome de quem fichou.
- Vocês têm anotados: a área plantada e a produção de mandioca e feijão de Nova Cruz, a situação dos dois municípios no Semiárido e a porcentagem de água usada na irrigação, cada um com a fonte e a data da consulta.

### Entrega

- [ ] Documento do Drive com capa, folha de rosto, título provisório e seção de Referências.
- [ ] `docs/orientacoes_escrita_tcc.md` e `docs/projeto_agroagreste.md` lidos pelos dois.
- [ ] Pelo menos 6 obras fichadas em `docs/leituras.md`, com referência ABNT.
- [ ] Os números do IBGE, da SUDENE e da ANA anotados com a fonte e a data.
- [ ] As obras lidas lançadas na seção de Referências do documento.

Para entregar, comentem na *issue* dizendo quantas obras fichou cada um e movam o card para **Em revisão**.

---

# Sprint 2: 23/10 a 29/10/2026

<a id="sprint-2-dev"></a>
## Sprint 2 · Desenvolvimento: aprender Python, parte 2

**Branch:** `feature/aprendizado-semana2` · **No PR:** `Closes #3`

**O que vocês vão entregar:** seis exercícios de cada um, agora com listas, dicionários, arquivos CSV, a biblioteca `pandas`, um gráfico, uma consulta a uma API de verdade e os primeiros testes com `pytest`.

Esta semana é a ponte entre o aprendizado e o trabalho: **cada exercício é uma versão pequena de algo que vocês vão fazer nas Sprints 3 a 8**, com os dados reais de março de 2024 em Nova Cruz, que já estão no repositório, em `aprendizado/clima_exemplo.csv`. Abram esse arquivo no VS Code e vejam: uma linha por dia, com a data, a temperatura máxima, a mínima, a média e a chuva.

**Sugestão de divisão:** cada um faz todos os exercícios, na própria pasta. Na quinta, revisão cruzada.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 23/10 | passo 1 (aulas do Mundo 3) e exercício 7 |
| segunda, 26/10 | exercícios 8 e 9 (CSV e `pandas`) |
| terça, 27/10 | exercícios 10 e 11 (gráfico e API) |
| quarta, 28/10 | exercício 12 (funções e testes) |
| quinta, 29/10 | revisão cruzada, diário e PR; a Introdução vence hoje |

### Passo a passo

**1. Assistam às aulas do Mundo 3** do Curso em Vídeo (https://www.cursoemvideo.com/curso/python-3-mundo-3/): **listas**, **dicionários**, **funções** e **módulos**. Digitem os exemplos junto.

**2. Façam os seis exercícios,** cada um em `aprendizado\semana2\<seu-primeiro-nome>\`:

**`ex07_dicionario.py`:** crie um dicionário em que a chave é o nome do município e o valor é uma tupla com a latitude e a longitude (os valores estão na [seção 3](#decisoes)). Percorra o dicionário com um `for` e mostre uma linha por município: `Nova Cruz: latitude -6.4778, longitude -35.4339`. *Pesquisem:* dicionários e o método `.items()`.

**`ex08_ler_csv.py`:** leia o `aprendizado/clima_exemplo.csv` com o módulo `csv` (que já vem com o Python) e mostre o **total de chuva de março** e o **número de dias secos** (chuva menor que 1 mm). *Pesquisem:* `open(..., encoding="utf-8")`, `csv.DictReader`, e lembrem que o que vem do arquivo é texto (usem `float`). **Teste:** total 160.0 mm e 6 dias secos.

**`ex09_pandas.py`:** faça a mesma coisa com o `pandas`, que é como vocês vão trabalhar daqui para frente, e mais um pouco. Mostre:

1. o total de chuva e a média da temperatura máxima do mês;
2. quantos dias tiveram máxima **acima de 33 °C** (filtro);
3. uma coluna nova, `amplitude`, com a máxima menos a mínima de cada dia, e a média dela;
4. o dia mais chuvoso e quanto choveu nele.

*Pesquisem:* `pd.read_csv`, selecionar uma coluna (`tabela["chuva"]`), `.sum()`, `.mean()`, filtro com colchetes (`tabela[tabela["tmax"] > 33]`), `len`, criar coluna nova, `.idxmax()` e `.loc`. **Teste:** chuva 160.0; máxima média 31.82; 8 dias acima de 33 °C; amplitude média 8.17; dia mais chuvoso 2024-03-29, com 16.69 mm (arredondem para duas casas).

Comparem o `ex08` com o `ex09`: o que deu menos trabalho? Anotem no diário. É por isso que o trabalho usa `pandas`.

**`ex10_grafico.py`:** com o `matplotlib`, faça um gráfico de **barras** com a chuva de cada dia de março. Escrevam o nome dos eixos (`Dia` e `Chuva (mm)`) e salvem a figura como `grafico_marco.png` na própria pasta do exercício. *Pesquisem:* `import matplotlib.pyplot as plt`, `plt.bar`, `plt.xlabel`, `plt.ylabel`, `plt.savefig`. Abram a figura e confiram: a barra mais alta tem de ser a do dia 29.

**`ex11_api_ibge.py`:** consulte uma API de verdade. A API de Localidades do IBGE devolve os dados de um município a partir do código dele:

```
https://servicodados.ibge.gov.br/api/v1/localidades/municipios/2408300
```

Abram esse endereço no navegador primeiro e vejam a resposta: é um texto no formato **JSON**, que o Python transforma em dicionários dentro de dicionários. Depois, no programa, consultem os dois municípios (Nova Cruz, `2408300`, e Canguaretama, `2402204`) e mostrem, de cada um, o **nome**, a **microrregião** e a **mesorregião**. *Pesquisem:* `requests.get`, `resposta.status_code`, `resposta.json()` e como acessar um dicionário dentro de outro (`dados["microrregiao"]["nome"]`). **Teste:** Nova Cruz está na mesorregião Agreste Potiguar; Canguaretama, na Leste Potiguar. Foi com essa consulta que eu escolhi Nova Cruz como município principal ([seção 3](#decisoes)).

**`ex12` (funções e testes):** este exercício tem **dois arquivos**, e é o primeiro contato de vocês com testes automatizados:

1. `funcoes_<nome>.py` (por exemplo, `funcoes_teofilo.py`), com três funções: `amplitude(tmax, tmin)`, `classificar_dia(chuva)` e `graus_para_radianos(graus)` (esta última recebe graus decimais e devolve radianos, como no exercício 5). As funções **devolvem** o resultado com `return`; não usam `input` nem `print`;
2. `test_funcoes_<nome>.py`, na mesma pasta, que importa as três funções (`from funcoes_teofilo import amplitude, ...`) e tem **pelo menos cinco testes**, um por função e mais dois de casos diferentes (um dia de chuva exatamente igual a 1 mm; uma latitude sul).

Para comparar números decimais, não usem `==`: usem `pytest.approx`, assim:

```python
assert graus_para_radianos(13 + 44 / 60) == pytest.approx(0.240, abs=0.001)
```

O `abs=0.001` quer dizer "aceito uma diferença de até 0,001". *Pesquisem:* "pytest primeiros passos" e `pytest.approx`. Rodem, da raiz do repositório:

```
python -m pytest aprendizado
```

O `pytest` mostra um ponto verde para cada teste que passou. Depois **façam um teste falhar de propósito** (troquem o valor esperado) e vejam como o `pytest` mostra o erro. Voltem ao valor certo.

> **Por que o nome do arquivo leva o nome de vocês?** Porque o `pytest` não aceita dois arquivos de teste com o mesmo nome em pastas diferentes deste tipo, e um importaria as funções do outro. Com o nome de cada um, não há confusão.

**3. Revisão cruzada, diário e PR.** Na quinta, cada um roda os exercícios do colega e o `python -m pytest aprendizado`. Escrevam o diário, façam os *commits* e abram o PR com `Closes #3`, colando em **Evidências de teste** a saída do `pytest` e o gráfico do `ex10`.

### Como saber que deu certo

- Os exercícios 8 e 9 dão os números dos testes.
- O `grafico_marco.png` de cada um mostra 31 barras, com eixos nomeados.
- O `ex11` mostra Canguaretama na mesorregião Leste Potiguar.
- `python -m pytest aprendizado` mostra pelo menos 10 testes passando (5 de cada um).

### Entrega da sprint

- [ ] Aulas do Mundo 3 (listas, dicionários, funções e módulos) assistidas pelos dois.
- [ ] Os exercícios 7 a 12 de **cada um**, em `aprendizado/semana2/<nome>/`.
- [ ] `grafico_marco.png` de cada um.
- [ ] Testes com `pytest` passando, e a falha proposital vista e desfeita.
- [ ] Revisão cruzada feita e diário atualizado.
- [ ] PR aberto para a `develop`, com `Closes #3`.

### Erros comuns

- **`FileNotFoundError` no `ex08` ou no `ex09`:** vocês rodaram o programa de dentro de outra pasta. Rodem da raiz do repositório, com o caminho `aprendizado/clima_exemplo.csv`.
- **`KeyError: 'chuva'`:** o nome da coluna está escrito diferente do cabeçalho do CSV. Confiram com `print(tabela.columns)`.
- **`ModuleNotFoundError: No module named 'funcoes_teofilo'`:** o arquivo de teste não está na mesma pasta das funções, ou o nome do arquivo está diferente do nome no `import`.
- **`requests.exceptions.ConnectionError`:** sem internet, ou o endereço está digitado errado. Testem o endereço no navegador.

<a id="sprint-2-escrita"></a>
## Sprint 2 · Escrita: Introdução e Objetivo geral (Entrega 1)

**Prazo:** 29/10/2026

**O que vocês vão entregar:** a Introdução, em cinco blocos de parágrafos, e o Objetivo geral. Cerca de 2 páginas.

**Sugestão de divisão:** um escreve os blocos 1 e 2; o outro, os blocos 3, 4 e 5. O objetivo geral, juntos. Antes de entregar, cada um lê e corrige a parte do outro.

A Introdução segue a sequência de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): contextualização, problemática, caminho para a solução, apresentação da solução e vínculo com o projeto. Escrevam nessa ordem.

### Bloco 1: Contextualização (1 a 2 parágrafos)

**Usem as leituras da Sprint 1:** a Lei nº 11.326/2006, os números do IBGE e a delimitação do Semiárido.

**Escrevam sobre:** a agricultura familiar no Agreste potiguar e a importância da mandioca e do feijão (com os números de Nova Cruz); o clima da região, com chuva concentrada em poucos meses do ano; e a água como recurso escasso e disputado, com o número da ANA sobre o uso da água na agricultura. Fechem com a ideia de que **saber quanto de água uma plantação precisa** é a base para usar bem a água que existe.

### Bloco 2: Problemática (1 a 2 parágrafos)

**Escrevam sobre:** o problema concreto. A necessidade de água de uma cultura depende da **evapotranspiração**, e o método padrão para calculá-la (Penman-Monteith, do manual FAO-56) precisa de temperatura, umidade, vento e radiação solar. Esses dados nem sempre existem: muitos municípios pequenos não têm estação meteorológica completa. Sem esses dados, o agricultor e as instituições ficam sem um número para planejar a época de plantio e o uso da água.

Terminem com a pergunta que ainda não tem resposta para a região de vocês: **um método mais simples, que usa só a temperatura, dá um resultado próximo o bastante do padrão para ser usado?**

### Bloco 3: Caminho para a solução (1 parágrafo)

**Escrevam sobre:** as alternativas: métodos simplificados de estimativa da evapotranspiração, como o de **Hargreaves-Samani**, que usa só a temperatura; e bases de dados climáticos gratuitas que cobrem qualquer ponto do planeta, como a **NASA POWER**. Juntas, as duas tornam possível estimar a necessidade de água de qualquer município, desde que o método simplificado seja validado.

Digam também o que o trabalho **não** faz: não recomenda quanto irrigar, não considera o tipo de solo nem a chuva que escorre sem infiltrar. **Recorte declarado é recorte defendido.**

### Bloco 4: Apresentação da solução (1 a 2 parágrafos)

Escrevam **no futuro** ("será desenvolvida..."); na revisão final, na Sprint 8, vocês passam para o passado.

**Escrevam sobre:** o que será construído e como será avaliado: uma calculadora em Python que obtém dez anos de dados diários da NASA POWER para Nova Cruz e Canguaretama, calcula a ET₀ por Hargreaves-Samani, **valida** o resultado contra o método de Penman-Monteith (calculado pela biblioteca `pyet`), calcula a necessidade de água da mandioca e do feijão com os coeficientes do FAO-56 e compara essa necessidade com a chuva, mês a mês. Digam que as fórmulas são conferidas por **testes automatizados** com os exemplos do próprio FAO-56.

Registrem que o trabalho usa apenas **dados públicos**, sem nenhum participante de pesquisa e sem dados pessoais, o que dispensa a submissão ao Comitê de Ética em Pesquisa.

### Bloco 5: Vínculo com o projeto e escopo (1 parágrafo)

**Escrevam sobre:** o vínculo com o projeto AgroAgreste ([`docs/projeto_agroagreste.md`](projeto_agroagreste.md)), que prevê indicadores ambientais e ações de Educação Ambiental sobre o uso consciente da água. Expliquem que a calculadora é construída **de forma independente** e que a **incorporação ao observatório é trabalho futuro**.

Fechem a Introdução com um parágrafo curto dizendo como o texto está organizado.

### 1.1 Objetivo geral

Uma **única frase**, com **uma única ação principal**, no modelo de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md):

> "O objetivo principal do presente trabalho consiste no [ação] de [o quê] para [finalidade]."

- a ação pode ser **desenvolver e validar** (aqui as duas formam uma coisa só: uma calculadora validada) ou **avaliar**;
- digam **o quê** (a necessidade de água da mandioca e do feijão, ou o método de Hargreaves-Samani), **onde** (Nova Cruz, RN) e **para quê** (apoiar o planejamento do uso da água);
- **não** empilhem ações ("baixar, calcular, comparar e gerar gráficos" são tarefas, não objetivos).

**Teste:** leiam o objetivo e depois o título provisório. Os dois têm de falar da mesma coisa.

### 1.2 Objetivos específicos

Deixem só o título e a frase "(a ser escrito na Sprint 8)". Eles ficam para o fim de propósito: precisam descrever o que foi **realmente** feito.

### Entrega

- [ ] Os cinco blocos da Introdução, na ordem, com citações.
- [ ] Os números de Nova Cruz (IBGE) e da ANA no texto, com a fonte.
- [ ] Objetivo geral em uma frase, com uma ação principal.
- [ ] Seção 1.2 com "(a ser escrito na Sprint 8)".
- [ ] Obras citadas lançadas nas Referências.
- [ ] Versão nomeada no histórico: `Entrega 1 - Introdução - 29/10`.

Para entregar, comentem na *issue* com o nome da versão e movam o card para **Em revisão**.

---

# Sprint 3: 30/10 a 05/11/2026

<a id="sprint-3-dev"></a>
## Sprint 3 · Desenvolvimento: os dados de clima da NASA POWER

**Branch:** `feature/dados-nasa` · **No PR:** `Closes #5`

**O que vocês vão entregar:** um script que baixa da NASA POWER dez anos de dados diários de clima de Nova Cruz e de Canguaretama, guarda o que veio sem mexer, converte para CSV com nomes em português, confere os dados com testes e faz o primeiro gráfico do trabalho. E o `README.md` do repositório.

**Sugestão de divisão:** um escreve o `baixar_clima.py` (passos 2 a 4); o outro escreve os testes dos dados e a exploração (passos 5 e 6). O `README.md`, quem terminar primeiro.

**Divida a semana assim** (segunda, 02/11, é feriado):

| Dia | O que fazer |
|---|---|
| sexta, 30/10 | passo 1 (entender a API) e passo 2 (baixar) |
| terça, 03/11 | passos 3 e 4 (converter e guardar os municípios) |
| quarta, 04/11 | passos 5 e 6 (testes e exploração) |
| quinta, 05/11 | passo 7 (`README.md`, diário e PR) |

### Passo a passo

**1. Entendam a API antes de programar.** A NASA POWER é um serviço gratuito da agência espacial americana que entrega dados de clima de qualquer ponto do planeta. Abram este endereço no navegador (é uma linha só):

```
https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2M_MAX,T2M_MIN,PRECTOTCORR,RH2M,WS2M,ALLSKY_SFC_SW_DWN&community=AG&longitude=-35.4339&latitude=-6.4778&start=20240301&end=20240303&format=JSON
```

A resposta é um JSON. Procurem nela:

- **`geometry` → `coordinates`:** três números. Os dois primeiros são a longitude e a latitude; o **terceiro é a altitude** do ponto, em metros. Vocês vão precisar dela na Sprint 5;
- **`properties` → `parameter`:** um dicionário com um item por variável, e dentro de cada um, um valor por dia (a chave é a data no formato `AAAAMMDD`);
- **`parameters`:** a descrição e a unidade de cada variável.

Comparem os três dias com o `aprendizado/clima_exemplo.csv`: são os mesmos números. Montem no diário esta tabela, preenchendo a unidade de cada uma a partir da resposta:

| Variável da NASA | O que é | Unidade | Nome que vocês vão usar |
|---|---|---|---|
| `T2M` | temperatura média do ar a 2 m | | `tmedia_nasa` |
| `T2M_MAX` | temperatura máxima | | `tmax` |
| `T2M_MIN` | temperatura mínima | | `tmin` |
| `PRECTOTCORR` | chuva (precipitação corrigida) | | `chuva` |
| `RH2M` | umidade relativa do ar a 2 m | | `umidade` |
| `WS2M` | velocidade do vento a 2 m | | `vento` |
| `ALLSKY_SFC_SW_DWN` | radiação solar que chega à superfície | | `radiacao` |

O `community=AG` pede os dados no formato da comunidade agrícola (com a radiação já em MJ/m² por dia, que é a unidade do FAO-56). As quatro últimas variáveis não entram no Hargreaves-Samani: elas são para o Penman-Monteith da Sprint 5. Baixem tudo agora, de uma vez.

**2. Escrevam `baixar_clima.py`, primeira parte: baixar e guardar o bruto.** Uma função `baixar(latitude, longitude, inicio, fim)` que:

1. monta a chamada com `requests.get`, passando o endereço base (`https://power.larc.nasa.gov/api/temporal/daily/point`) e os parâmetros em um **dicionário** (`params=...`), em vez de montar o endereço juntando texto;
2. usa `timeout=120` (a resposta de dez anos demora alguns segundos);
3. confere se deu certo com `resposta.raise_for_status()`;
4. devolve `resposta.json()`.

O programa chama a função para os dois municípios, de `20150101` a `20241231`, e grava cada resposta **do jeito que veio** em `dados/brutos/nasa_nova_cruz.json` e `dados/brutos/nasa_canguaretama.json`. **Se o arquivo já existir, não baixa de novo**: assim o trabalho fica reproduzível (a NASA às vezes revisa os dados) e vocês não sobrecarregam o serviço. *Pesquisem:* `json.dump` e `json.load`, `os.path.exists`.

**3. Segunda parte: converter para CSV.** Uma função `json_para_tabela(dados)` que:

1. cria um `DataFrame` a partir de `dados["properties"]["parameter"]` (cada variável vira uma coluna, cada data vira uma linha);
2. transforma o índice em datas de verdade, com `pd.to_datetime(..., format="%Y%m%d")`, e dá a ele o nome `data`;
3. troca os nomes das colunas pelos da tabela do passo 1 (*pesquisem:* `rename` com um dicionário);
4. troca o valor **-999** por "vazio" (`numpy.nan`). É o código que a NASA usa para dado faltante (está em `header` → `fill_value`). Se vocês fizerem conta com -999, a média do mês despenca, e ninguém percebe;
5. cria a coluna **`tmedia`**, com a média da máxima e da mínima: `(tmax + tmin) / 2`. É assim que o FAO-56 (equação 9) define a temperatura média do dia para os cálculos, e é ela que vocês vão usar daqui para frente (a `tmedia_nasa` fica só para comparação).

O programa grava `dados/clima_nova_cruz.csv` e `dados/clima_canguaretama.csv`.

**4. Guardem os dados dos municípios em `dados/municipios.csv`**, com as colunas `municipio,codigo_ibge,latitude,longitude,altitude`. A latitude, a longitude e o código estão na [seção 3](#decisoes); a altitude é o terceiro número de `geometry` → `coordinates` de cada JSON. Os scripts das próximas sprints leem a latitude e a altitude daqui, em vez de repetir os números no código.

**5. Escrevam os testes dos dados, em `tests/test_dados.py`.** São testes que conferem se os CSV estão certos, e vão continuar rodando até o fim do trabalho. Para cada um dos dois municípios:

1. o CSV tem **3.653 linhas** de dados. *Pensem antes de rodar:* 10 anos de 365 dias dão 3.650. De onde vêm os outros 3? (Escrevam a resposta como comentário no teste.);
2. as datas começam em 2015-01-01, terminam em 2024-12-31 e **não pulam nenhum dia** (*pesquisem:* `pd.date_range` e comparem com o índice);
3. **não há valor vazio** em nenhuma coluna (*pesquisem:* `.isna().sum()`);
4. em todos os dias, `tmin <= tmax`;
5. em todos os dias, `chuva >= 0`.

Rodem com `python -m pytest`. Se o teste 3 falhar, **não apaguem os dias vazios**: anotem quantos são e em quais datas, e comentem na *issue* com essa lista (o plano B está na [seção 11](#riscos)).

**6. Explorem os dados.** Escrevam `explorar_clima.py`, que lê os dois CSV e:

1. calcula o **total de chuva de cada ano** de cada município e grava em `resultados/chuva_anual.csv` (*pesquisem:* `resample("YE")` ou `groupby(tabela.index.year)`);
2. calcula a **chuva média de cada mês** (a média dos dez janeiros, dos dez fevereiros...) de cada município;
3. faz um gráfico de **barras lado a lado**, com os 12 meses no eixo horizontal e a chuva média no vertical, uma barra para cada município, e salva em `graficos/chuva_mensal.png`. *Pesquisem:* "matplotlib barras lado a lado" (`numpy.arange` e um deslocamento para cada município) e `plt.legend`.

Olhem o gráfico e anotem no diário: em quais meses chove mais? Em quais quase não chove? Qual dos dois municípios chove mais no ano? Qual foi o **ano mais seco** e o **ano mais chuvoso** de Nova Cruz no período? Vocês vão precisar desses dois anos na Sprint 7.

> **Um cuidado para o artigo:** a NASA POWER não mede a chuva em Nova Cruz com um pluviômetro: ela **estima** a partir de satélites e modelos, em uma grade de quadrados de dezenas de quilômetros de lado. *Pesquisem:* "NASA POWER resolução espacial" e anotem no diário o tamanho do quadrado. Isso vai para as limitações do artigo, e é a razão de dois municípios a 35 km de distância poderem ter números diferentes (ou iguais).

**7. Escrevam o `README.md`** do repositório (se o GitHub já tiver criado um, substituam o conteúdo), com as quatro partes que a política do NIC exige:

1. **o que é este projeto**, em três linhas;
2. **responsáveis:** vocês dois e os orientadores, com os usuários do GitHub;
3. **instalação:** como criar o ambiente virtual e instalar com `pip install -r requirements.txt`;
4. **como rodar:** por enquanto, `python baixar_clima.py`, `python explorar_clima.py` e `python -m pytest`. A cada sprint vocês acrescentam o que for novo.

Atualizem o diário, façam os *commits* (incluindo os JSON brutos, que são pequenos) e abram o PR com `Closes #5`.

### Como saber que deu certo

- `dados/brutos/` tem os dois JSON, e rodar o `baixar_clima.py` de novo não baixa outra vez.
- `dados/clima_nova_cruz.csv` abre no Excel, com a coluna `data` e as colunas em português.
- `python -m pytest` mostra os testes dos dados passando para os dois municípios.
- `graficos/chuva_mensal.png` mostra 12 grupos de 2 barras, com legenda e eixos nomeados.

### Entrega da sprint

- [ ] `baixar_clima.py` com `baixar()` e `json_para_tabela()`, sem baixar de novo o que já existe.
- [ ] JSON brutos em `dados/brutos/` e CSV dos dois municípios em `dados/`.
- [ ] `-999` trocado por vazio e coluna `tmedia` = (tmax + tmin) / 2.
- [ ] `dados/municipios.csv` com latitude, longitude e altitude.
- [ ] `tests/test_dados.py` com os cinco testes, passando.
- [ ] `resultados/chuva_anual.csv` e `graficos/chuva_mensal.png`.
- [ ] Tabela das variáveis, ano mais seco e mais chuvoso e resolução da NASA POWER anotados no diário.
- [ ] `README.md` com as quatro partes.
- [ ] PR aberto para a `develop`, com `Closes #5`.

### Erros comuns

- **`ReadTimeout`:** a NASA demorou a responder. Rodem de novo; se repetir, aumentem o `timeout`.
- **`KeyError: 'properties'`:** a resposta veio com erro (por exemplo, uma data inválida). Abram o JSON gravado e leiam a mensagem que está em `messages`.
- **As datas viraram números no CSV:** faltou o `pd.to_datetime` no índice.

<a id="sprint-3-escrita"></a>
## Sprint 3 · Escrita: Referencial Teórico, seções 2.1 e 2.2 (Entrega 2)

**Prazo:** 05/11/2026

**O que vocês vão entregar:** as duas primeiras seções do Referencial, cerca de 2 páginas.

**Explicação em vídeo (assistam antes de começar):** https://youtu.be/8Qztq1Q5vb0

**Sugestão de divisão:** um escreve a 2.1; o outro, a 2.2. Cada um lê e corrige a seção do colega antes da entrega.

Escrevam **apenas sobre o que reaparece** na Metodologia ou nos Resultados.

### 2.1 Agricultura familiar, água e Educação Ambiental no semiárido (cerca de 0,75 página)

**Pesquisem:** o conceito de agricultura familiar (Lei nº 11.326/2006); a mandioca e o feijão na agricultura familiar do Nordeste (procurem publicações da **Embrapa Mandioca e Fruticultura** e da **Embrapa Arroz e Feijão**, que são gratuitas, no portal `embrapa.br`); a irregularidade das chuvas no Semiárido (procurem publicações do **Instituto Nacional do Semiárido (INSA)** e da SUDENE); e o uso consciente da água como tema de Educação Ambiental (Lei nº 9.795/1999).

**Escrevam:** por que a mandioca e o feijão importam para a agricultura familiar da região; como a chuva concentrada em poucos meses define a época de plantar; e por que conhecer a necessidade de água das culturas é um conteúdo de Educação Ambiental, e não só de agronomia: é o que permite falar de uso consciente da água com números.

### 2.2 Evapotranspiração e necessidade de água das culturas (cerca de 1,25 página)

**Pesquisem:** os capítulos 1, 2, 5 e 6 do manual **FAO-56** (Allen *et al.*, 1998). Procurem também um livro de agrometeorologia em português: *Agrometeorologia: fundamentos e aplicações práticas*, de Pereira, Angelocci e Sentelhas (biblioteca do campus ou Google Livros), tem um capítulo sobre evapotranspiração.

**Escrevam:**

- o que é **evaporação**, **transpiração** e **evapotranspiração**, e por que se mede em milímetros por dia;
- o que é a **evapotranspiração de referência (ET₀)**: a superfície de referência (uma grama hipotética, baixa e bem regada) e por que ela depende só do clima;
- o que é o **coeficiente de cultura (Kc)** e por que ele muda ao longo do ciclo: as **quatro fases** (inicial, desenvolvimento, intermediária e final) e os três valores tabelados (Kc inicial, Kc intermediário e Kc final). Uma **figura** da curva do Kc, redesenhada por vocês no draw.io (`app.diagrams.net`) a partir da figura do FAO-56, ajuda muito o leitor (citem a fonte embaixo: "Fonte: adaptado de Allen *et al.* (1998)");
- a **evapotranspiração da cultura**, `ETc = Kc × ET₀`, e o **balanço** entre a chuva e a ETc, com o que significa déficit e excedente.

### Entrega

- [ ] Seções 2.1 e 2.2, com toda afirmação técnica referenciada.
- [ ] ET₀, Kc e ETc definidos com as suas palavras, com a fórmula da ETc.
- [ ] Figura da curva do Kc, com fonte.
- [ ] Comentários da Entrega 1 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 2 - Referencial 2.1 e 2.2 - 05/11`.

Para entregar, comentem na *issue* com o nome da versão e movam o card para **Em revisão**.

---

# Sprint 4: 06/11 a 12/11/2026

<a id="sprint-4-dev"></a>
## Sprint 4 · Desenvolvimento: a evapotranspiração pelo método de Hargreaves-Samani

**Branch:** `feature/hargreaves` · **No PR:** `Closes #7`

**O que vocês vão entregar:** as funções do cálculo da ET₀ por Hargreaves-Samani, escritas por vocês a partir das equações do FAO-56, conferidas por testes com os exemplos do próprio manual, e a ET₀ diária de dez anos dos dois municípios.

**Esta é a sprint mais importante do trabalho.** É aqui que a fórmula do artigo vira código, e é aqui que vocês provam, com testes, que o código está certo.

**Sugestão de divisão:** a regra "um escreve a função, o outro escreve o teste". Um escreve as funções em `calculos.py`; o outro escreve `tests/test_calculos.py` **ao mesmo tempo**, a partir das mesmas equações e dos exemplos do FAO-56. Quando os dois juntarem, os testes dizem se a função está certa. No meio da semana, troquem: quem escreveu funções escreve o `calcular_et0.py`.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 06/11 | passo 1 (entender as equações) e passo 2 (conversões e dia do ano) |
| segunda, 09/11 | passo 3 (radiação extraterrestre) e seus testes |
| terça, 10/11 | passo 4 (Hargreaves-Samani) e seus testes |
| quarta, 11/11 | passo 5 (`calcular_et0.py`) |
| quinta, 12/11 | passo 6 (diário e PR) |

### Passo a passo

**1. Entendam as equações antes de programar.** No FAO-56, abram o **capítulo 3** (*Meteorological data*) e localizem as equações 20 a 25 (radiação extraterrestre) e a **equação 52** (Hargreaves). O método de Hargreaves-Samani é:

```
ET₀ = 0,0023 × (Tmédia + 17,8) × √(Tmáx − Tmín) × Ra
```

em que as temperaturas estão em °C e **Ra** é a **radiação extraterrestre**, convertida para milímetros por dia. A Ra é a energia do Sol que chega ao **topo da atmosfera**, e depende só de duas coisas: a **latitude** do lugar e o **dia do ano**. Não precisa de nenhum dado medido: é pura geometria entre a Terra e o Sol. É por isso que o método só precisa da temperatura.

O cálculo da Ra tem cinco passos, cada um uma equação do FAO-56:

| Passo | Equação do FAO-56 | Fórmula |
|---|---|---|
| latitude em radianos (φ) | 22 | `φ = π / 180 × graus` |
| distância relativa Terra-Sol (dr) | 23 | `dr = 1 + 0,033 × cos(2π / 365 × J)` |
| declinação solar (δ) | 24 | `δ = 0,409 × sen(2π / 365 × J − 1,39)` |
| ângulo do pôr do sol (ωs) | 25 | `ωs = arccos(−tan(φ) × tan(δ))` |
| radiação extraterrestre (Ra), em MJ/m² por dia | 21 | `Ra = (24 × 60 / π) × 0,0820 × dr × [ωs × sen(φ) × sen(δ) + cos(φ) × cos(δ) × sen(ωs)]` |

**J** é o **dia do ano**: 1 para 1º de janeiro, 365 (ou 366, em ano bissexto) para 31 de dezembro. O 0,0820 é a constante solar, em MJ/m² por minuto.

Para usar a Ra no Hargreaves-Samani, ela precisa estar em **milímetros por dia**: pela equação 20, multiplica-se por **0,408**.

**Leiam também o Exemplo 8 do FAO-56** (*Determination of extraterrestrial radiation*): ele faz essa conta passo a passo para a latitude 20° sul no dia 3 de setembro. Os números do exemplo vão ser os testes de vocês.

**2. Comecem pelas funções simples**, em `calculos.py`:

| Função | O que devolve | Pesquisem |
|---|---|---|
| `graus_para_radianos(graus)` | o ângulo em radianos (vocês já fizeram no `ex12`) | `math.pi` |
| `dia_do_ano(data)` | o número do dia no ano, recebendo um `datetime.date` | `data.timetuple().tm_yday` |

E os primeiros testes, em `tests/test_calculos.py` (importando de `calculos`):

- **Exemplo 7 do FAO-56:** 13° 44' norte dá 0,240 rad; 22° 54' sul dá -0,400 rad (com `pytest.approx(..., abs=0.001)`);
- **dia do ano:** 3 de setembro de 2026 é o dia **246** (é o J do Exemplo 8); 3 de setembro de 2024 é o dia **247** (2024 é bissexto: o 29 de fevereiro empurra todos os dias seguintes); 1º de janeiro é sempre 1; 31 de dezembro de 2024 é 366.

**3. Escrevam as funções da radiação extraterrestre**, uma por equação: `distancia_relativa(j)`, `declinacao_solar(j)`, `angulo_por_do_sol(lat_rad, declinacao)` e `radiacao_extraterrestre(lat_graus, j)` (esta última chama as outras e devolve a Ra em MJ/m² por dia). E uma `mj_para_mm(valor)`, que multiplica por 0,408.

*Pesquisem:* `math.cos`, `math.sin`, `math.tan` e `math.acos`. **Cuidado: as funções do `math` trabalham em radianos**, nunca em graus. É o erro mais comum desta sprint.

Testes, com os valores do **Exemplo 8** (latitude -20°, J = 246):

| Grandeza | Valor esperado | Tolerância |
|---|---|---|
| `dr` | 0,985 | 0,001 |
| `δ` | 0,120 rad | 0,001 |
| `ωs` | 1,527 rad | 0,001 |
| `Ra` | 32,2 MJ/m² por dia | 0,1 |
| `Ra` em mm | 13,1 mm por dia | 0,1 |

**4. Escrevam `et0_hargreaves(tmax, tmin, tmedia, ra_mm)`**, com a equação 52. Duas regras:

- se `tmax` for **menor** que `tmin`, a função não calcula: ela **levanta um erro** com `raise ValueError("tmax menor que tmin")`. Raiz quadrada de número negativo não existe, e um dado assim é sinal de problema nos dados, não algo para esconder. *Pesquisem:* `raise` e `pytest.raises`;
- a função recebe a Ra **já em milímetros**.

Testes:

1. **um caso calculado à mão:** escolham um dia do `dados/clima_nova_cruz.csv`, calculem a Ra e a ET₀ desse dia **na calculadora**, passo a passo, anotem a conta em `docs/conta_a_mao.md`, e escrevam o teste com o valor que deu na calculadora. Se o teste falhar, ou a conta à mão ou a função está errada: descubram qual;
2. **`tmax` menor que `tmin`** levanta `ValueError`;
3. **comparação com a biblioteca `pyet`:** a `pyet` também tem o Hargreaves (`pyet.hargreaves`). Leiam os 31 primeiros dias do CSV de Nova Cruz, calculem a ET₀ com a função de vocês e com `pyet.hargreaves(tmedia, tmax, tmin, lat=...)`, e confiram que a diferença de cada dia é menor que **0,1 mm**. Atenção a dois detalhes da `pyet`: ela recebe colunas do `pandas` com as datas no índice (não números soltos), e a **latitude em radianos**. *Pesquisem:* a documentação da `pyet` (`pyet.readthedocs.io`), página do Hargreaves.

Se a diferença do teste 3 for pequena mas não zero, é normal: anotem no diário quanto foi (a `pyet` arredonda algumas constantes de um jeito um pouco diferente).

**5. Escrevam `calcular_et0.py`**, o script que usa as funções. Para cada município, ele:

1. lê o `dados/clima_<municipio>.csv` e a latitude em `dados/municipios.csv`;
2. calcula, para cada dia, a Ra em mm e a ET₀ por Hargreaves-Samani (*pesquisem:* percorrer as linhas com `itertuples`, ou `apply` com `axis=1`);
3. grava `resultados/et0_<municipio>.csv`, com as colunas `data`, `ra_mm` e `et0_hs`;
4. mostra a **ET₀ média por dia** e o **total médio por ano**.

Comparem com a chuva média anual da Sprint 3 e anotem no diário: no total do ano, a ET₀ é maior ou menor que a chuva? E em quais meses?

**6. Feche a sprint.** Rodem `python -m pytest` (os testes dos dados e os do cálculo). Atualizem o `README.md` e o diário, façam os *commits* e abram o PR com `Closes #7`, colando a saída do `pytest`.

### Como saber que deu certo

- `python -m pytest` mostra todos os testes passando: os do Exemplo 7, do dia do ano, do Exemplo 8, da conta à mão, do `ValueError` e da comparação com a `pyet`.
- `resultados/et0_nova_cruz.csv` e `resultados/et0_canguaretama.csv` têm 3.653 linhas, sem valor vazio.
- A ET₀ diária fica sempre entre 0 e 10 mm (valores fora disso indicam erro de unidade).

### Entrega da sprint

- [ ] `calculos.py` com as conversões, o dia do ano, as quatro funções da radiação e o `et0_hargreaves`.
- [ ] `tests/test_calculos.py` com os testes dos Exemplos 7 e 8, do dia do ano e do Hargreaves.
- [ ] Conta à mão registrada em `docs/conta_a_mao.md` e usada em um teste.
- [ ] Comparação com `pyet.hargreaves` com diferença menor que 0,1 mm.
- [ ] `calcular_et0.py` gerando a ET₀ diária dos dois municípios.
- [ ] Diário com a comparação ET₀ × chuva.
- [ ] PR aberto para a `develop`, com `Closes #7`.

### Erros comuns

- **Ra com valores absurdos (negativos, ou perto de zero):** vocês usaram graus em vez de radianos em alguma função do `math`.
- **`ValueError: math domain error` no `acos`:** o valor dentro do `acos` saiu do intervalo de -1 a 1. Quase sempre é a latitude em graus em vez de radianos.
- **ET₀ por volta de 30 mm por dia:** vocês usaram a Ra em MJ, sem multiplicar por 0,408.

<a id="sprint-4-escrita"></a>
## Sprint 4 · Escrita: Referencial Teórico, seções 2.3, 2.4 e 2.5 (Entrega 3)

**Prazo:** 12/11/2026

**O que vocês vão entregar:** as três últimas seções do Referencial, cerca de 2,5 páginas, incluindo o quadro de trabalhos relacionados.

**Sugestão de divisão:** um escreve a 2.3 (que conversa com o código desta semana); o outro, a 2.4. A 2.5, metade cada (um trabalho relacionado cada, e o quadro juntos).

### 2.3 Métodos de estimativa da evapotranspiração de referência (cerca de 1 página)

**Pesquisem:** o capítulo 2 do FAO-56 (por que Penman-Monteith é o método padrão) e o capítulo 3, equação 52 (Hargreaves); o artigo original de **Hargreaves e Samani (1985)**, *Reference crop evapotranspiration from temperature*, publicado na revista *Applied Engineering in Agriculture* (procurem pelo título no Google Acadêmico); e outros métodos que usam só temperatura, como o de **Thornthwaite** e o de **Camargo**, para dar panorama.

**Escrevam:** o que é o **método de Penman-Monteith** (as variáveis de que ele precisa, sem deduzir a fórmula) e por que a FAO o adota como padrão; o que é o **método de Hargreaves-Samani**, a fórmula completa (é a que vocês programaram), e o papel da **radiação extraterrestre**, que vem da latitude e do dia do ano; e as **vantagens e desvantagens** de um método que usa só temperatura: precisa de menos dados, mas não "vê" a umidade nem o vento. Digam o que a literatura diz sobre **onde** o Hargreaves-Samani costuma errar mais (climas úmidos, litorâneos ou com muito vento): isso vai ajudar a explicar os resultados de Canguaretama.

### 2.4 Dados climáticos da NASA POWER (cerca de 0,5 página)

**Pesquisem:** a documentação da NASA POWER (`power.larc.nasa.gov/docs`): de onde vêm os dados (reanálise e satélites), a resolução da grade e as variáveis. Procurem no Google Acadêmico trabalhos brasileiros que **compararam a NASA POWER com estações do INMET**, de preferência no Nordeste (termos: "NASA POWER INMET comparação", "NASA POWER Nordeste").

**Escrevam:** o que é a NASA POWER, de onde vêm os dados, a resolução espacial e o que os trabalhos de validação encontraram (a NASA POWER costuma acertar melhor a temperatura do que a chuva?). Feche dizendo por que ela foi escolhida: gratuita, sem cadastro, cobre qualquer ponto e tem todas as variáveis do Penman-Monteith, o que permite a validação deste trabalho.

### 2.5 Trabalhos relacionados (cerca de 1 página)

**Pesquisem:** trabalhos que **compararam o Hargreaves-Samani com o Penman-Monteith** no Brasil, de preferência no Nordeste ou no Semiárido, e trabalhos que calcularam a **necessidade de água ou o balanço hídrico** de mandioca ou feijão. Onde procurar: Google Acadêmico, SciELO (`scielo.br`), a *Revista Brasileira de Engenharia Agrícola e Ambiental* (*Agriambi*) e a *Revista Brasileira de Agrometeorologia*. Termos úteis: "Hargreaves-Samani Penman-Monteith Nordeste", "evapotranspiração de referência métodos empíricos", "necessidade hídrica mandioca", "balanço hídrico feijão".

**Escrevam:** de **2 a 3 trabalhos**, um parágrafo curto cada, dizendo onde foi feito, que métodos comparou, **que medida de erro usou** e o que encontrou. Fechem com um **quadro comparativo** entre eles e o trabalho de vocês, com as colunas: local, período, fonte dos dados, métodos comparados, medidas de erro e resultado principal.

**Esse quadro mostra o que o trabalho de vocês acrescenta**: provavelmente, a validação para Nova Cruz e Canguaretama com dados da NASA POWER, uma calculadora em código aberto com testes automatizados e a ligação com um indicador de Educação Ambiental.

### Regras que valem para o referencial inteiro

- **Documentação oficial** (NASA POWER, `pyet`) serve para descrever a ferramenta, **não** para fundamentar conceito.
- **Nunca citem uma referência que vocês não leram.**
- Ao fim desta entrega, vocês devem ter **pelo menos 8 referências** na lista.

### Entrega

- [ ] Seções 2.3, 2.4 e 2.5, com toda afirmação técnica referenciada.
- [ ] Fórmula do Hargreaves-Samani completa, com o significado de cada termo.
- [ ] Quadro comparativo dos trabalhos relacionados com o de vocês.
- [ ] Comentários da Entrega 2 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 3 - Referencial 2.3 a 2.5 - 12/11`.

Para entregar, comentem na *issue* com o nome da versão e movam o card para **Em revisão**.

---

# Sprint 5: 13/11 a 19/11/2026

<a id="sprint-5-dev"></a>
## Sprint 5 · Desenvolvimento: a validação com Penman-Monteith

**Branch:** `feature/validacao-pm` · **No PR:** `Closes #9`

**O que vocês vão entregar:** a ET₀ dos dois municípios calculada também pelo método padrão da FAO (Penman-Monteith), com a biblioteca `pyet`; as três medidas de erro do Hargreaves-Samani, por dia e por mês; os gráficos da validação; e a análise de em quais meses o método simples erra mais.

**A ideia, em uma frase:** a ET₀ de Penman-Monteith é a "resposta certa"; vocês medem o quanto a ET₀ de Hargreaves-Samani se afasta dela.

**Sugestão de divisão:** um escreve as funções das medidas de erro e os testes delas (passos 2 e 3); o outro escreve o cálculo do Penman-Monteith (passo 1). Depois, um faz a tabela e o outro os gráficos (passos 4 e 5). A análise por mês (passo 6), juntos.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 13/11 | passo 1 (Penman-Monteith com a `pyet`) |
| segunda, 16/11 | passos 2 e 3 (medidas de erro e testes) |
| terça, 17/11 | passo 4 (tabela da validação) |
| quarta, 18/11 | passos 5 e 6 (gráficos e erro por mês) |
| quinta, 19/11 | passo 7 (diário e PR) e a escrita da semana |

### Passo a passo

**1. Calculem a ET₀ de Penman-Monteith com a `pyet`.** O Penman-Monteith do FAO-56 (equação 6) usa muito mais dados do que o Hargreaves-Samani: temperatura, umidade, vento, radiação solar e a altitude. Vocês **não** vão programar essa fórmula: a biblioteca `pyet` já faz isso, e ela é a referência contra a qual a fórmula de vocês vai ser medida.

Escrevam `validar_et0.py`. Para cada município, ele:

1. lê o `dados/clima_<municipio>.csv` com as datas no índice (*pesquisem:* `pd.read_csv` com `index_col="data"` e `parse_dates=True`), a ET₀ de Hargreaves-Samani de `resultados/et0_<municipio>.csv`, e a latitude e a altitude de `dados/municipios.csv`;
2. calcula a ET₀ de Penman-Monteith com `pyet.pm_fao56`, passando, pelo nome: a temperatura média (`tmedia`), o vento (`wind`), a radiação solar (`rs`), a máxima (`tmax`), a mínima (`tmin`), a umidade relativa (`rh`), a altitude (`elevation`) e a latitude **em radianos** (`lat`);
3. junta as duas ET₀ em uma tabela com as colunas `data`, `et0_hs` e `et0_pm` e grava em `resultados/validacao_<municipio>.csv`.

*Pesquisem:* a página do `pm_fao56` na documentação da `pyet` (`pyet.readthedocs.io`), para conferir o nome e a unidade de cada parâmetro. A radiação tem de estar em MJ/m² por dia (é por isso que vocês baixaram com `community=AG`), e o vento, em metros por segundo a 2 metros de altura.

**Confiram:** a `et0_pm` não pode ter dias vazios, e os valores têm de estar na mesma faixa da `et0_hs` (alguns milímetros por dia). Se vierem vazios, algum parâmetro está com o nome errado.

**2. Escrevam as medidas de erro, em `calculos.py`.** São três funções, e cada uma recebe duas listas (ou colunas) do mesmo tamanho: a **estimada** (Hargreaves-Samani) e a **de referência** (Penman-Monteith):

| Função | O que calcula | Como se lê |
|---|---|---|
| `erro_medio(estimado, referencia)` | a média de `estimado - referencia` | se for **positivo**, o Hargreaves-Samani **superestima** (calcula mais água do que o padrão); se for negativo, subestima. Também se chama **viés** |
| `erro_absoluto_medio(estimado, referencia)` | a média de `|estimado - referencia|` | o tamanho típico do erro, **sem** deixar os erros para cima e para baixo se cancelarem. Em inglês, *MAE* |
| `correlacao(estimado, referencia)` | o coeficiente de correlação de Pearson (*r*) | de -1 a 1. Perto de 1: quando um sobe, o outro sobe junto, mesmo que um seja sempre maior |

Escrevam as duas primeiras **com um `for`** (ou com operações do `pandas`, se preferirem), para entender a conta. A correlação pode usar o `pandas` (`serie1.corr(serie2)`). *Pesquisem:* "erro médio absoluto", "viés" e "correlação de Pearson", e o que cada uma mostra que as outras não mostram.

**Por que as três?** Porque cada uma responde uma pergunta diferente. Um método pode ter erro médio quase zero (erra para cima no verão e para baixo no inverno, e os erros se cancelam) e mesmo assim errar muito em cada dia. Só olhando as três juntas vocês sabem o que está acontecendo.

**3. Testem as medidas de erro**, em `tests/test_calculos.py`, com contas que dá para fazer de cabeça:

- estimado `[2, 4, 6]` e referência `[1, 4, 8]`: o erro médio é `(1 + 0 - 2) / 3`, e o erro absoluto médio é `(1 + 0 + 2) / 3`. Calculem os dois valores e escrevam os testes;
- `[1, 2, 3]` contra `[2, 4, 6]`: correlação **1** (um é o dobro do outro: sobem juntos);
- `[1, 2, 3]` contra `[3, 2, 1]`: correlação **-1**.

**4. Montem a tabela da validação.** No `validar_et0.py`, para cada município, calculem as três medidas em **duas escalas**:

- **diária:** dia a dia, os 3.653 dias;
- **mensal:** primeiro somem a ET₀ de cada mês (*pesquisem:* `resample("ME").sum()`), e depois comparem os 120 totais mensais.

Acrescentem também a **média diária** de cada método e o **erro relativo**: o erro absoluto médio dividido pela média do Penman-Monteith, em porcentagem. Gravem em `resultados/validacao.csv`, com as colunas `municipio`, `escala`, `media_hs`, `media_pm`, `erro_medio`, `erro_absoluto_medio`, `erro_relativo_pct` e `correlacao`. Arredondem para duas casas (três na correlação).

Olhem a tabela e anotem no diário: o Hargreaves-Samani superestima ou subestima? O erro é maior por dia ou por mês? Por que a escala mensal tende a ter correlação maior? (Dica: nos totais do mês, os erros de dias diferentes se compensam em parte.) O erro é parecido nos dois municípios?

**5. Façam os gráficos da validação**, com o `matplotlib`, para cada município:

- **dispersão:** cada ponto é um dia, com a ET₀ de Penman-Monteith no eixo horizontal e a de Hargreaves-Samani no vertical. Desenhem também a **reta 1:1** (a linha onde os dois seriam iguais): os pontos acima dela são dias em que o Hargreaves-Samani superestimou. Salvem em `graficos/dispersao_<municipio>.png`. *Pesquisem:* `plt.scatter` (com `s=4` e `alpha=0.4`, porque são muitos pontos) e `plt.plot` para a reta;
- **série mensal:** os 120 totais mensais dos dois métodos, em duas linhas, com a data no eixo horizontal. Salvem em `graficos/et0_mensal_<municipio>.png`.

Nomeiem os eixos com a unidade (`ET₀ Penman-Monteith (mm/dia)`). **Não coloquem título dentro da imagem**: pela ABNT, o título vai no documento, em cima da figura.

**6. Descubram em que época do ano o Hargreaves-Samani erra mais.** Calculem o **erro médio de cada mês do ano** (a média de todos os janeiros, de todos os fevereiros...) e gravem em `resultados/erro_por_mes.csv`. Façam também a **umidade média** e o **vento médio** de cada mês do ano. Comparem: o erro é maior nos meses mais úmidos? Nos de mais vento? O Hargreaves-Samani não usa nenhum dos dois, então é natural que ele erre mais quando esses fatores mudam muito. Anotem no diário o que vocês encontraram: é um dos melhores parágrafos dos Resultados.

**7. Fechem a sprint.** Rodem `python -m pytest`, atualizem o `README.md` e o diário, façam os *commits* e abram o PR com `Closes #9`, colando a saída do `pytest`, a tabela da validação e os gráficos de dispersão.

### Como saber que deu certo

- `resultados/validacao.csv` tem 4 linhas (2 municípios × 2 escalas), sem valor vazio.
- Os testes das medidas de erro passam.
- Os gráficos de dispersão mostram uma "nuvem" de pontos ao redor da reta 1:1.
- O diário diz se o Hargreaves-Samani superestima ou subestima, e em quais meses erra mais.

### Entrega da sprint

- [ ] `validar_et0.py` calculando a ET₀ de Penman-Monteith com `pyet.pm_fao56`.
- [ ] `erro_medio`, `erro_absoluto_medio` e `correlacao` em `calculos.py`, com testes.
- [ ] `resultados/validacao.csv` com as escalas diária e mensal dos dois municípios.
- [ ] Gráficos de dispersão e da série mensal dos dois municípios.
- [ ] `resultados/erro_por_mes.csv` e a relação com umidade e vento anotada no diário.
- [ ] PR aberto para a `develop`, com `Closes #9`.

### Erros comuns

- **`et0_pm` toda vazia:** algum parâmetro do `pm_fao56` está com o nome errado, ou a latitude está em graus.
- **`TypeError` dentro da `pyet`:** vocês passaram números soltos ou listas, e não colunas do `pandas` com as datas no índice.
- **A correlação deu exatamente 1:** vocês compararam uma coluna com ela mesma.

<a id="sprint-5-escrita"></a>
## Sprint 5 · Escrita: Metodologia e Materiais e Métodos (Entrega 4)

**Prazo:** 19/11/2026

**O que vocês vão entregar:** as seções 3 e 4 do artigo, cerca de 3 a 4 páginas no total.

**Sugestão de divisão:** um escreve a seção 3 e a 4.1; o outro, as seções 4.2 e 4.3. A 4.4, juntos.

Metodologia e Materiais e Métodos dizem **como** o trabalho foi feito, com detalhe suficiente para outra pessoa repetir. Verbos no passado e linguagem impessoal ("foram obtidos dados diários..."). O que ainda não aconteceu (a necessidade de água das culturas e o balanço) vocês escrevem **como planejado**, e completam na Sprint 6 e na revisão final.

**Pasta com metodologias prontas para consulta:** https://drive.google.com/drive/folders/1OwAjk47aQWuRKLf-ktesizSax9csEtXO?usp=sharing

### 3.1 Classificação da pesquisa

**Pesquisem:** Gil (2017) e Prodanov e Freitas (2013), com as referências completas em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md). Leiam os capítulos de classificação antes de escrever.

**Escrevam:** a classificação pelos quatro critérios, **justificando cada uma** com uma frase ligada ao trabalho:

- **natureza:** aplicada, porque produz uma ferramenta e um indicador para um problema concreto do território;
- **objetivos:** descritiva, porque descreve a necessidade de água das culturas e o desempenho de um método de estimativa;
- **abordagem:** quantitativa, porque os resultados são valores medidos e comparados com medidas de erro;
- **procedimentos:** pesquisa bibliográfica e **estudo de caso** (Nova Cruz e Canguaretama), com **dados secundários** públicos.

### 3.2 Área de estudo e período

**Escrevam:** onde ficam Nova Cruz e Canguaretama (mesorregião, distância entre as duas, coordenadas, altitude da NASA POWER e situação no Semiárido, das leituras da Sprint 1), por que Nova Cruz é o município principal (é do Agreste, recorte do AgroAgreste) e por que Canguaretama entra na comparação. Digam o período (2015 a 2024) e por que dez anos completos: um ano só poderia ser atípico. Um **mapa de localização** ajuda: façam um print do mapa do IBGE (`cidades.ibge.gov.br`, página de cada município) ou montem um no draw.io, sempre com a fonte.

### 3.3 Etapas do trabalho

**Escrevam:** as etapas, na ordem: obtenção dos dados, cálculo da ET₀, validação, cálculo da necessidade de água das culturas, balanço hídrico. Façam um **fluxograma** no draw.io com essas etapas, mostrando o que entra e o que sai de cada uma (por exemplo: "temperatura e latitude → ET₀ de Hargreaves-Samani"). Registrem que não há participantes de pesquisa nem dados pessoais.

### 4.1 Materiais

Vale a analogia de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): **lista de ingredientes** mais **modo de preparo**. Para **cada** ferramenta, digam **o que é** (uma frase), **para que foi usada** e a **versão** (do `docs/ambiente.md`): Python, `requests`, `pandas`, `matplotlib`, `pyet`, `pytest`, a API da NASA POWER e o manual FAO-56. Uma tabela resolve. Digam também a configuração da máquina e o endereço do repositório (https://github.com/nicifrn/mp_agro_agua_culturas).

### 4.2 Obtenção dos dados

**Escrevam:** a API da NASA POWER, as variáveis (a tabela do passo 1 da Sprint 3, com as unidades), o período, a comunidade `AG`, o tratamento do valor -999, a definição da temperatura média pela equação 9 do FAO-56, e os testes automáticos que conferem os dados (número de dias, ausência de vazios, `tmin <= tmax`).

### 4.3 Cálculo e validação da ET₀

**Escrevam:**

- as equações da radiação extraterrestre (21 a 25) e do Hargreaves-Samani (52) do FAO-56, numeradas no texto (*pesquisem:* como escrever equações no Google Docs, em *Inserir → Equação*);
- como as funções foram **testadas**: os Exemplos 7 e 8 do FAO-56, a conta à mão e a comparação com a `pyet`, e quantos testes passaram;
- o Penman-Monteith calculado pela `pyet` como referência, com as variáveis usadas;
- as três medidas de erro, **com as fórmulas** (*pesquisem:* a fórmula do erro médio, do erro absoluto médio e do coeficiente de Pearson, em um livro de estatística ou em um dos trabalhos relacionados que vocês leram), e as duas escalas (diária e mensal).

### 4.4 Necessidade de água das culturas e balanço (como planejado)

**Escrevam:** as culturas (mandioca e feijão), a data de plantio (1º de abril, começo da estação chuvosa), que os valores de Kc e a duração das fases vêm das tabelas 11 e 12 do FAO-56, e que a necessidade de água será comparada com a chuva mês a mês. Os valores exatos vocês completam na Sprint 6.

### Entrega

- [ ] Seções 3.1 a 3.3, com o fluxograma e o mapa de localização.
- [ ] Seções 4.1 a 4.3, com as equações numeradas e as fórmulas das medidas de erro.
- [ ] Seção 4.4 como planejado.
- [ ] Comentários da Entrega 3 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 4 - Metodologia e Materiais e Métodos - 19/11`.

Para entregar, comentem na *issue* com o nome da versão e movam o card para **Em revisão**.

---

# Sprint 6: 20/11 a 26/11/2026

<a id="sprint-6-dev"></a>
## Sprint 6 · Desenvolvimento: a necessidade de água da mandioca e do feijão

**Branch:** `feature/necessidade-agua` · **No PR:** `Closes #11`

**O que vocês vão entregar:** os valores de Kc das duas culturas tirados do FAO-56, a função que dá o Kc de cada dia do ciclo, e a necessidade de água (ETc) diária da mandioca e do feijão, plantados em 1º de abril de cada ano, nos dois municípios.

**Atenção:** sexta, 20/11, é feriado. A semana começa na segunda.

**Sugestão de divisão:** os dois leem o capítulo 6 do FAO-56 juntos e preenchem o `culturas.csv` juntos (passo 1). Depois, um escreve a `kc_do_dia` e o outro escreve os testes dela (passos 2 e 3). O `calcular_etc.py` (passos 4 e 5), um faz a mandioca e o outro o feijão, e depois juntam.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| segunda, 23/11 | passo 1 (as tabelas do FAO-56) e passo 2 (`kc_do_dia`) |
| terça, 24/11 | passo 3 (testes) e passo 4 (`calcular_etc.py`) |
| quarta, 25/11 | passo 5 (totais por ciclo e gráfico do Kc) |
| quinta, 26/11 | passo 6 (diário e PR) e a escrita da semana |

### Passo a passo

**1. Tirem os valores do FAO-56 e guardem em `dados/culturas.csv`.** Abram o **capítulo 6** do FAO-56 (*ETc - single crop coefficient*) e localizem:

- a **Tabela 11**, com a **duração das quatro fases** de cada cultura, em dias (*initial*, *development*, *mid-season* e *late season*);
- a **Tabela 12**, com os **três valores de Kc** de cada cultura (*Kc ini*, *Kc mid* e *Kc end*).

Usem estas linhas das tabelas:

| Cultura | Nome no FAO-56 | Qual linha da Tabela 11 |
|---|---|---|
| mandioca | *Cassava*, primeiro ano (*year 1*) | a de *year 1*, regiões tropicais, estação chuvosa |
| feijão | *Beans, dry* | a linha cujo total é de **110 dias** |

Criem o `dados/culturas.csv`:

```
cultura,nome_fao,dias_inicial,dias_desenvolvimento,dias_intermediaria,dias_final,kc_ini,kc_mid,kc_end
mandioca,Cassava year 1,...
feijao,"Beans, dry",...
```

(o nome do feijão vai entre aspas porque tem vírgula). **Confiram os números duas vezes, cada um sozinho, e comparem**: um número copiado errado aqui estraga todo o resultado e nenhum teste pega. Anotem no diário a página do FAO-56 de cada tabela, para citar no artigo.

Leiam também as notas da Tabela 12 e anotem no diário: **para que clima** os valores de Kc *mid* e *end* foram tabelados (umidade e vento)? O FAO-56 ensina a ajustá-los para outros climas (equação 62); vocês não vão fazer esse ajuste (é a extra E2 da [seção 12](#extras)), e isso vai para as limitações.

> **Sobre a mandioca:** o ciclo real da mandioca dura de 12 a 18 meses, mas o FAO-56 traz o primeiro ano separado, com a duração da Tabela 11. Vocês vão calcular a necessidade de água desse primeiro período, que é o que vai de abril até a estação seca. Escrevam isso no diário: vai para as limitações.

**2. Escrevam `kc_do_dia(dia_do_ciclo, cultura)` em `calculos.py`.** O `cultura` é um dicionário com uma linha do `culturas.csv` (as durações e os três Kc). O `dia_do_ciclo` conta os dias desde o plantio: **0 é o dia do plantio**. A função segue a curva do Kc do FAO-56 (figura 25 do capítulo 6), com quatro trechos:

| Fase | Dias do ciclo | Kc |
|---|---|---|
| inicial | de 0 até o fim da fase inicial | constante, igual ao `kc_ini` |
| desenvolvimento | os dias seguintes, pela duração da fase | **sobe em linha reta** do `kc_ini` até o `kc_mid` |
| intermediária | os dias seguintes, pela duração da fase | constante, igual ao `kc_mid` |
| final | os dias seguintes, pela duração da fase | **desce em linha reta** do `kc_mid` até o `kc_end` |
| depois do fim do ciclo, ou antes do plantio | | não há cultura: a função devolve `None` |

Para os dois trechos em linha reta, a conta é a mesma (é uma interpolação linear, como na equação 66 do FAO-56):

```
Kc = Kc_do_começo_da_fase + (Kc_do_fim_da_fase − Kc_do_começo_da_fase) × (dias já passados na fase / duração da fase)
```

*Pesquisem:* "interpolação linear" e `if`/`elif` com vários limites. **Dica:** calculem antes, em variáveis, o dia em que cada fase termina (`fim_inicial`, `fim_desenvolvimento`...): o código fica muito mais fácil de ler.

Escrevam também `fase_do_dia(dia_do_ciclo, cultura)`, que devolve o nome da fase (`"inicial"`, `"desenvolvimento"`, `"intermediaria"`, `"final"` ou `None`). Vai servir nos gráficos.

**3. Testem a `kc_do_dia`**, em `tests/test_calculos.py`. Montem nos testes uma cultura **inventada**, com números fáceis (por exemplo, 10 dias em cada fase, `kc_ini` 0,4, `kc_mid` 1,2 e `kc_end` 0,6), para poder calcular as respostas de cabeça:

- no dia 0 e no último dia da fase inicial, o Kc é o `kc_ini`;
- **no meio da fase de desenvolvimento**, o Kc é a média do `kc_ini` e do `kc_mid`;
- em qualquer dia da fase intermediária, o Kc é o `kc_mid`;
- no último dia do ciclo, o Kc é igual (ou muito próximo) ao `kc_end`;
- no dia seguinte ao fim do ciclo, e em um dia negativo, a função devolve `None`;
- a `fase_do_dia` devolve a fase certa nesses mesmos dias.

Pensem com cuidado nos dias **de fronteira** (o último dia de uma fase e o primeiro da seguinte): é onde quase todos os erros aparecem. Escrevam no teste, como comentário, qual regra vocês escolheram para eles.

**4. Escrevam `calcular_etc.py`.** Para cada município e cada cultura, e para **cada ano de 2015 a 2024**:

1. o plantio é em **1º de abril** daquele ano;
2. para cada dia do ciclo, calculem o `dia_do_ciclo`, a fase, o Kc, a ETc com a ET₀ de Hargreaves-Samani (`etc = kc × et0_hs`) e, **também**, a ETc com a ET₀ de Penman-Monteith (`etc_pm = kc × et0_pm`), e copiem a chuva do dia;
3. gravem tudo em `resultados/etc_<municipio>_<cultura>.csv`, com as colunas `data`, `safra` (o ano do plantio), `dia_do_ciclo`, `fase`, `kc`, `et0_hs`, `etc`, `etc_pm` e `chuva`.

*Pesquisem:* `datetime.date(ano, 4, 1)`, a diferença entre duas datas (`(data - plantio).days`) e `pd.concat` para juntar as tabelas dos dez anos.

> **Por que calcular também a `etc_pm`?** Porque a pergunta que importa para o agricultor não é "o Hargreaves-Samani erra quanto na ET₀?", e sim "**esse erro muda a conclusão** sobre faltar ou sobrar água?". Com as duas ETc, vocês vão poder responder isso na Sprint 7.

**5. Calculem os totais de cada ciclo e façam o gráfico do Kc.**

1. Para cada município, cultura e safra, somem a ETc e a chuva do ciclo inteiro e gravem em `resultados/ciclo_<municipio>_<cultura>.csv` (`safra`, `etc_total`, `etc_pm_total`, `chuva_total`, `diferenca` = chuva menos ETc). Mostrem na tela a média dos dez anos. *Pesquisem:* `groupby("safra").sum()`.
2. Façam o gráfico da **curva do Kc** das duas culturas (dia do ciclo no eixo horizontal, Kc no vertical, uma linha por cultura) e salvem em `graficos/kc_culturas.png`. Comparem com a figura 25 do FAO-56: o formato tem de ser o mesmo.

Anotem no diário: em quantos dos dez anos a chuva do ciclo foi maior que a ETc total, para cada cultura? Qual das duas culturas precisa de mais água no ciclo? E por dia?

**6. Fechem a sprint.** Rodem `python -m pytest`, atualizem o `README.md` e o diário, façam os *commits* e abram o PR com `Closes #11`, colando a saída do `pytest`, o `culturas.csv` e o gráfico do Kc.

### Como saber que deu certo

- `dados/culturas.csv` tem as duas culturas, conferido pelos dois.
- Os testes da `kc_do_dia` passam, inclusive os dos dias de fronteira.
- `graficos/kc_culturas.png` tem o formato da curva do FAO-56 (reta, subida, reta, descida).
- `resultados/etc_nova_cruz_mandioca.csv` tem 10 ciclos, todos começando em 1º de abril, e nenhuma linha com Kc vazio.

### Entrega da sprint

- [ ] `dados/culturas.csv` com os valores das Tabelas 11 e 12 do FAO-56, conferidos pelos dois.
- [ ] `kc_do_dia` e `fase_do_dia` em `calculos.py`, com testes (inclusive dos dias de fronteira).
- [ ] `calcular_etc.py` gerando a ETc diária (com Hargreaves-Samani e com Penman-Monteith) das duas culturas nos dois municípios.
- [ ] Totais por ciclo em `resultados/ciclo_<municipio>_<cultura>.csv`.
- [ ] `graficos/kc_culturas.png`.
- [ ] Diário com as observações sobre os ciclos e as limitações (clima das tabelas e ciclo da mandioca).
- [ ] PR aberto para a `develop`, com `Closes #11`.

<a id="sprint-6-escrita"></a>
## Sprint 6 · Escrita: colocar no documento as tabelas da validação

**Prazo:** 26/11/2026

**O que vocês vão entregar:** as tabelas e figuras da validação já dentro do documento, nos lugares certos dos Resultados, e a seção 4.4 completa. Nesta semana não há entrega de seção nova: é a tarefa que impede os Resultados de ficarem para a última hora.

**Sugestão de divisão:** um faz os passos 1 a 3; o outro, os passos 4 e 5.

### Passo a passo

**1. Criem no documento os títulos da seção 5** (5.1 a 5.5, como na [seção 9.3](#escrita-geral)), ainda sem texto.

**2. Montem em 5.2 a Tabela "Validação da ET₀ de Hargreaves-Samani"**, com o conteúdo do `resultados/validacao.csv`: uma linha por município e escala, com as médias, o erro médio, o erro absoluto médio, o erro relativo e a correlação. Usem **vírgula** como separador decimal e o mesmo número de casas em cada coluna. Identificação em cima, centralizada; fonte embaixo ("Fonte: dados da pesquisa (2026)."), como em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).

**3. Insiram em 5.2 os gráficos de dispersão** dos dois municípios e, em 5.1, o gráfico da chuva média mensal (Sprint 3), cada um com a identificação em cima e a fonte embaixo.

**4. Escrevam só uma frase** antes de cada tabela e figura, anunciando-a ("A Tabela X apresenta..."). A discussão vem na Sprint 7.

**5. Completem a seção 4.4** com os valores do `culturas.csv` (em uma tabela, citando as Tabelas 11 e 12 do FAO-56 com a página), a regra da curva do Kc (com a fórmula da interpolação) e o cálculo da ETc com as duas ET₀.

### Entrega

- [ ] Títulos 5.1 a 5.5 no documento.
- [ ] Tabela da validação em 5.2, com identificação, fonte e vírgula decimal.
- [ ] Gráficos de dispersão em 5.2 e da chuva mensal em 5.1.
- [ ] Seção 4.4 completa, com a tabela dos valores do FAO-56.
- [ ] Comentários da Entrega 4 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Sprint 6 - tabelas da validação - 26/11`.

Para entregar, comentem na *issue* com o nome da versão e movam o card para **Em revisão**.

---

# Sprint 7: 27/11 a 03/12/2026

<a id="sprint-7-dev"></a>
## Sprint 7 · Desenvolvimento: o balanço hídrico mensal e os gráficos

**Branch:** `feature/balanco` · **No PR:** `Closes #13`

**O que vocês vão entregar:** a tabela e o gráfico mensal que comparam a chuva com a necessidade de água de cada cultura, em cada município, com o déficit ou o excedente de cada mês; a comparação entre um ano seco e um ano chuvoso; e a resposta à pergunta "o erro do Hargreaves-Samani muda a conclusão?".

É nesta semana que a calculadora vira resultado.

**Atenção ao calendário:** os Resultados vencem na quinta, 03/12. **O balanço e os gráficos precisam estar prontos até segunda, 30/11.**

**Sugestão de divisão:** um escreve as funções do balanço e os testes (passos 1 e 2); o outro escreve o `balanco.py` (passo 3). Os gráficos (passos 4 e 5), um faz os do balanço e o outro o do ano seco e chuvoso. O passo 6, juntos.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 27/11 | passos 1 a 3 (funções, testes e tabela mensal) |
| segunda, 30/11 | passos 4 e 5 (gráficos) |
| terça, 01/12 | passo 6 (o erro do Hargreaves-Samani muda a conclusão?) |
| quarta e quinta, 02 e 03/12 | escrita dos Resultados; passo 7 (diário e PR) |

### Passo a passo

**1. Escrevam as funções do balanço, em `calculos.py`:**

- `balanco(chuva, etc)`: devolve `chuva - etc`, em milímetros;
- `situacao(valor_do_balanco)`: devolve `"deficit"` se o balanço for negativo, e `"excedente"` se for zero ou positivo.

**2. Testem as duas**, em `tests/test_balanco.py`: chuva 120 e ETc 80 dão balanço 40 e excedente; chuva 30 e ETc 95 dão balanço -65 e déficit; chuva igual à ETc dá balanço 0 e excedente.

**3. Escrevam `balanco.py`, a tabela mensal.** Para cada município e cada cultura, a partir de `resultados/etc_<municipio>_<cultura>.csv`:

1. somem a chuva, a ETc e a ETc de Penman-Monteith **por mês de cada safra** (os dias do ciclo que caem em abril de 2015, em maio de 2015...). *Pesquisem:* `groupby` por duas colunas (`safra` e o mês da data);
2. calculem o balanço e a situação de cada mês de cada safra;
3. agora, **para cada mês do ciclo** (abril, maio, junho...), calculem a **média dos dez anos** da chuva, da ETc e do balanço, e **contem em quantos dos dez anos houve déficit** naquele mês;
4. gravem em `resultados/balanco_mensal_<municipio>_<cultura>.csv`, com as colunas `mes`, `chuva_media`, `etc_media`, `balanco_medio`, `situacao` e `anos_com_deficit`.

A coluna `anos_com_deficit` é a mais útil para quem planta: "em 8 dos 10 anos faltou água em setembro" diz muito mais do que a média sozinha. Anotem no diário, para cada cultura e município: em quais meses do ciclo falta água na média? Em quais falta em quase todos os anos? O feijão, que termina em julho, passa pela estação seca?

> **Atenção ao primeiro e ao último mês do ciclo:** eles não têm todos os dias (o feijão, por exemplo, não ocupa julho inteiro). A ETc e a chuva desses meses são só dos dias do ciclo. Isso está certo, mas deixem escrito no diário e no artigo, para ninguém comparar esse mês com um mês cheio.

**4. Façam os gráficos do balanço.** Para cada município e cada cultura, um gráfico de **barras lado a lado**: os meses do ciclo no eixo horizontal, e duas barras por mês, a **chuva média** e a **ETc média**. Onde a barra da ETc passa a da chuva, falta água. Salvem em `graficos/balanco_<municipio>_<cultura>.png` (são quatro gráficos). Usem a mesma escala no eixo vertical nos quatro (*pesquisem:* `plt.ylim`), para que dê para comparar um com o outro.

**5. Comparem um ano seco com um ano chuvoso.** Na Sprint 3, vocês anotaram o ano mais seco e o mais chuvoso de Nova Cruz. Façam o mesmo gráfico do passo 4 **só para a mandioca em Nova Cruz**, uma vez com a safra do ano mais seco e outra com a do ano mais chuvoso, lado a lado na mesma figura (*pesquisem:* `plt.subplots(1, 2)`). Salvem em `graficos/ano_seco_chuvoso.png`. É a figura que mostra que a média esconde a variação: um ano ruim é muito pior que a média.

**6. Respondam: o erro do Hargreaves-Samani muda a conclusão?** No `balanco.py`, calculem também o balanço mensal com a `etc_pm` (a necessidade de água com a ET₀ de Penman-Monteith) e comparem com o balanço feito com a `etc`. Para cada município e cultura, contem:

- em quantos meses-safra (cada mês de cada um dos dez ciclos) a **situação mudou** (era déficit com um método e excedente com o outro);
- a diferença média, em milímetros, entre os dois balanços.

Gravem em `resultados/comparacao_metodos.csv`. **Esta é a conclusão prática da validação:** se a situação quase nunca muda, o método simples serve para o indicador do observatório, mesmo errando um pouco na ET₀; se muda com frequência, não serve. Anotem no diário em quais meses ela muda: provavelmente nos meses em que a chuva e a ETc estão muito próximas.

**7. Fechem a sprint.** Rodem `python -m pytest`, atualizem o `README.md` e o diário, façam os *commits* e abram o PR com `Closes #13`, colando a saída do `pytest`, as tabelas de balanço mensal de Nova Cruz e os gráficos.

### Como saber que deu certo

- `python -m pytest` passa, com os testes do balanço.
- Existem quatro tabelas `balanco_mensal_*.csv` e quatro gráficos `balanco_*.png`, com a mesma escala vertical.
- `graficos/ano_seco_chuvoso.png` mostra os dois anos lado a lado.
- `resultados/comparacao_metodos.csv` diz quantas vezes a situação mudou entre os dois métodos.

### Entrega da sprint

- [ ] `balanco` e `situacao` em `calculos.py`, com `tests/test_balanco.py`.
- [ ] `balanco.py` gerando as quatro tabelas mensais, com `anos_com_deficit`.
- [ ] Os quatro gráficos de balanço, com a mesma escala.
- [ ] Gráfico do ano seco e do ano chuvoso da mandioca em Nova Cruz.
- [ ] `resultados/comparacao_metodos.csv`, com as mudanças de situação entre Hargreaves-Samani e Penman-Monteith.
- [ ] PR aberto para a `develop`, com `Closes #13`.

### Erros comuns

- **Meses fora do ciclo aparecendo na tabela:** vocês somaram a chuva do ano inteiro, e não só dos dias do ciclo. Filtrem as linhas com `kc` preenchido.
- **Os meses aparecem fora de ordem no gráfico:** ordenem pelo número do mês, e não pelo nome.

<a id="sprint-7-escrita"></a>
## Sprint 7 · Escrita: Resultados e Discussão (Entrega 5)

**Prazo:** 03/12/2026

**O que vocês vão entregar:** a seção 5 completa, de 4 a 6 páginas. É a seção mais importante do artigo.

**Sugestão de divisão:** um escreve a 5.1 e a 5.2 (clima e validação); o outro, a 5.3 e a 5.4 (culturas e balanço). A 5.5, juntos. Cada um lê e corrige a parte do outro.

> **Regra sem exceção:** toda figura ou tabela é **anunciada no texto antes** de aparecer e **explicada depois**. Nada de duas figuras seguidas sem texto entre elas. Organizem a seção respondendo às **três perguntas de pesquisa**, na ordem.

### 5.1 O clima de Nova Cruz e Canguaretama

A chuva média de cada mês (gráfico da Sprint 3), o total anual médio dos dois municípios, e o ano mais seco e o mais chuvoso. **Discutam:** como a chuva se concentra em poucos meses, e o que isso significa para quem planta.

### 5.2 Validação do método de Hargreaves-Samani (pergunta 1)

A tabela da validação e os gráficos de dispersão (já no documento desde a Sprint 6). **Discutam:** o Hargreaves-Samani superestima ou subestima? O erro é aceitável? Comparem os números de vocês com os dos **trabalhos relacionados** do Referencial: o erro foi parecido com o que eles encontraram? Expliquem por que a escala mensal tem correlação maior. Mostrem em **quais meses** o método erra mais (o `erro_por_mes.csv`) e relacionem com a umidade e o vento, ligando com o que a literatura diz (seção 2.3): resultado ligado à teoria vale o dobro. Comparem também os dois municípios: o erro é diferente em Canguaretama, mais perto do mar?

### 5.3 Necessidade de água da mandioca e do feijão (pergunta 2)

A curva do Kc das duas culturas, a tabela da ETc total de cada ciclo (média dos dez anos e variação entre os anos) e a comparação entre as culturas. **Discutam:** qual precisa de mais água no ciclo inteiro, e qual precisa de mais água **por dia**; em que fase do ciclo a necessidade é maior.

### 5.4 Balanço hídrico mensal (pergunta 3)

Os gráficos e as tabelas de balanço mensal, a coluna `anos_com_deficit` e o gráfico do ano seco e do ano chuvoso. **Discutam:**

- em quais meses do ciclo falta água para cada cultura, quanto falta e em quantos anos;
- a diferença entre a média e um ano seco: o que o planejamento precisa considerar;
- a diferença entre Nova Cruz e Canguaretama;
- **a comparação entre os métodos** (o `comparacao_metodos.csv`): o erro do Hargreaves-Samani muda a conclusão sobre déficit ou excedente? Em quantos meses? Esta é a resposta prática da validação, e merece um parágrafo inteiro.

Fechem com o que isso significa para o **uso consciente da água**: é o gancho para a Educação Ambiental e para o indicador do AgroAgreste.

### 5.5 Limitações

Curta e honesta:

- os dados da NASA POWER são **estimativas** em uma grade de dezenas de quilômetros, e não medições de estação no município;
- os valores de Kc do FAO-56 foram usados **sem o ajuste** para o clima local;
- a mandioca foi calculada só no **primeiro período** do FAO-56, e não no ciclo completo;
- o balanço usa a **chuva total**, e não a chuva efetiva (a parte que de fato infiltra no solo), e não considera o tipo de solo;
- a data de plantio é **fixa** (1º de abril), e na prática ela varia com o começo das chuvas.

### Entrega

- [ ] Seções 5.1 a 5.5, com os números de `resultados/`.
- [ ] Todos os gráficos inseridos, cada um anunciado antes e explicado depois, com fonte.
- [ ] As três perguntas de pesquisa respondidas, na ordem.
- [ ] Comparação com os trabalhos relacionados na 5.2.
- [ ] Comentários da Sprint 6 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 5 - Resultados - 03/12`.

Para entregar, comentem na *issue* com o nome da versão e movam o card para **Em revisão**.

---

# Sprint 8: 04/12 a 10/12/2026

<a id="sprint-8-dev"></a>
## Sprint 8 · Desenvolvimento: o programa completo, o README e o fechamento

**Branch:** `feature/fechamento` · **No PR:** `Closes #15`

**O que vocês vão entregar:** um programa que refaz o trabalho inteiro com um comando, a **calculadora** que qualquer pessoa pode usar para um município, uma cultura e uma safra, o indicador pronto para o AgroAgreste, o `README.md` completo e testado do zero, e a apresentação.

**Sugestão de divisão:** um faz o `rodar_tudo.py` e o indicador (passos 1 e 3); o outro faz a calculadora (passo 2). O `README.md` e a reprodução do zero (passos 4 e 5), um escreve e o **outro testa**: é o teste de verdade. A apresentação, juntos.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 04/12 | passos 1 e 2 (`rodar_tudo.py` e calculadora) |
| segunda, 07/12 | passo 3 (indicador); a Conclusão do artigo tem de estar pronta hoje |
| terça, 08/12 | passos 4 e 5 (`README.md` e reprodução do zero) |
| quarta e quinta, 09 e 10/12 | passos 6 a 8 (limpeza, apresentação e PR) e o fechamento do texto |

### Passo a passo

**1. Escrevam `rodar_tudo.py`.** Um programa que roda, **na ordem**, todas as etapas: baixar o clima, calcular a ET₀, validar, calcular a ETc e o balanço. Para isso, organizem cada script com uma função `principal()` e o bloco `if __name__ == "__main__": principal()` no fim. O `rodar_tudo.py` importa cada script e chama a `principal()` de cada um, mostrando o nome da etapa e quanto tempo ela levou (*pesquisem:* `time.perf_counter`). No fim, mostra o tempo total. Anotem esse tempo no diário: ele vai para o artigo, porque mostra que o observatório consegue atualizar o indicador em segundos.

**2. Escrevam a calculadora, `calculadora.py`.** É a ferramenta que dá nome ao trabalho: a pessoa escolhe o município, a cultura e a safra, e recebe a tabela e o gráfico. Ela é chamada assim:

```
python calculadora.py --municipio "Nova Cruz" --cultura feijao --safra 2024
```

e:

1. lê os parâmetros com o `argparse` (*pesquisem:* `argparse.ArgumentParser` e `add_argument`). Se o município ou a cultura não existirem nos arquivos de `dados/`, mostra uma mensagem clara com as opções válidas;
2. usa as funções de `calculos.py` (e não copia as contas!) para calcular, dia a dia, a ET₀, o Kc e a ETc do ciclo daquela safra;
3. mostra na tela uma tabela mensal (mês, chuva, ETc, balanço, situação) e o total do ciclo;
4. salva o gráfico mensal da safra em `graficos/calculadora_<municipio>_<cultura>_<safra>.png`.

**3. Gerem o indicador para o AgroAgreste.** Juntem as quatro tabelas `balanco_mensal_*.csv` em um arquivo só, `resultados/indicador_balanco_hidrico.csv`, com as colunas `municipio`, `cultura`, `mes`, `chuva_media_mm`, `etc_media_mm`, `balanco_medio_mm`, `situacao` e `anos_com_deficit`. Escrevam `docs/indicador.md` explicando, em uma tabela, o que é cada coluna, a unidade, de onde vem e o período. É esse arquivo que a equipe do observatório vai usar para montar o painel: escrevam pensando em quem nunca viu o trabalho de vocês.

**4. Completem o `README.md`.** Ele precisa permitir que outra pessoa repita tudo. Escrevam na ordem em que a pessoa faria:

1. o que é o projeto e o que ele calcula;
2. o que precisa ter: Python 3 e acesso à internet (para a NASA POWER);
3. como criar o ambiente virtual e instalar (`pip install -r requirements.txt`);
4. como rodar tudo de uma vez (`python rodar_tudo.py`) e cada etapa separada;
5. como usar a calculadora, com um exemplo;
6. como rodar os testes (`python -m pytest`);
7. o que tem em cada pasta e em cada arquivo de `resultados/`;
8. de onde vêm os dados (NASA POWER e FAO-56), com as referências;
9. os responsáveis.

**5. Testem o README do zero.** Quem **não** escreveu o README clona o repositório **em outra pasta** (`git clone ... teste_readme`), apaga as pastas `dados/brutos`, `resultados` e `graficos` da cópia (para os dados serem baixados e tudo ser recalculado) e segue o texto, passo a passo, sem usar nada que não esteja escrito nele. Cada vez que precisar de algo que não está no README, avisa o colega, que acrescenta. No fim, os números dos `resultados/` da cópia têm de ser **iguais** aos do repositório. Anotem no diário quanto tempo levou e o que faltava.

**6. Limpem o repositório.** Rodem `git status` e confiram: nada de `.venv/`, `__pycache__/` ou `.pytest_cache/`. Apaguem arquivos de teste soltos que não fazem parte do trabalho.

**7. Montem a apresentação.** Dez minutos, de 8 a 10 slides no Google Apresentações, salvos na mesma pasta do Drive do artigo, e **os dois apresentam**: o problema (uso da água, com um número da região), o que é evapotranspiração (com a analogia da planta que "sua"), os dados, a validação (a tabela e um gráfico de dispersão), o balanço de uma cultura, o ano seco e o ano chuvoso, e o que isso significa para o AgroAgreste. Terminem com uma demonstração da calculadora, rodando.

**8. Abram o PR** com `Closes #15`, com a saída do `pytest`, a do `rodar_tudo.py` e um exemplo da calculadora. Depois do *merge*, os orientadores levam a `develop` para a `main` e publicam a versão `v1.0`.

### Como saber que deu certo

- `python rodar_tudo.py` refaz tudo, mostrando o tempo de cada etapa.
- `python calculadora.py --municipio "Nova Cruz" --cultura feijao --safra 2024` mostra a tabela mensal e salva o gráfico.
- `resultados/indicador_balanco_hidrico.csv` e `docs/indicador.md` existem e se explicam.
- O colega conseguiu seguir o `README.md` do zero e chegou aos mesmos números.
- `python -m pytest` passa, e o `git status` está limpo.

### Entrega da sprint

- [ ] `rodar_tudo.py` com o tempo de cada etapa.
- [ ] `calculadora.py` com `argparse`, usando as funções de `calculos.py`.
- [ ] `resultados/indicador_balanco_hidrico.csv` e `docs/indicador.md`.
- [ ] `README.md` completo e testado do zero por quem não o escreveu.
- [ ] Repositório limpo.
- [ ] Apresentação de 10 minutos na pasta do Drive.
- [ ] PR aberto para a `develop`, com `Closes #15`.

<a id="sprint-8-escrita"></a>
## Sprint 8 · Escrita: Conclusão, Objetivos específicos, Resumo e Título (Entrega 6)

**Prazo:** 10/12/2026 · **A Conclusão precisa estar pronta na segunda, 07/12.**

**O que vocês vão entregar:** a Conclusão, os Objetivos específicos, o Resumo, o *Abstract*, as palavras-chave, o Título definitivo e o texto inteiro revisado.

**Sugestão de divisão:** um escreve a Conclusão; o outro, os Objetivos específicos e o Resumo. O *Abstract* e o Título, juntos. A revisão final, **cada um lê o texto inteiro**.

### 6 Conclusão (cerca de 1 página, até 07/12)

Curta e direta. Nada de resultado, conceito ou citação que não tenha aparecido antes. **Escrevam, nesta ordem:**

1. **o problema e o objetivo geral**, dizendo que foi alcançado, **com número**: "[...] uma vez que a ET₀ estimada por Hargreaves-Samani apresentou erro absoluto médio de X mm por dia e correlação de Y em relação ao método de Penman-Monteith, e o balanço indicou déficit hídrico para a mandioca nos meses de...";
2. **a resposta direta às três perguntas de pesquisa**, uma ou duas frases cada;
3. **as contribuições:** a calculadora em código aberto, com testes automatizados baseados no FAO-56; a validação do método simples para Nova Cruz e Canguaretama; e o indicador de balanço hídrico pronto para o AgroAgreste, que também serve de material de Educação Ambiental sobre o uso da água;
4. **as dificuldades reais**, do `docs/diario.md`: aprender Python em duas semanas, os radianos, o dia do ano bissexto, os dias de fronteira da curva do Kc, ler um manual técnico em inglês;
5. **trabalhos futuros**, concretos: integrar o indicador ao AgroAgreste (o principal); comparar com dados de uma **estação do INMET** da região; ajustar o Kc para o clima local (equação 62 do FAO-56); usar a **chuva efetiva**; estender para outros municípios do Agreste e outras culturas; e **calibrar** o coeficiente do Hargreaves-Samani para a região.

**Não escrevam** que "o método de Hargreaves-Samani é bom" sem dizer em que medida, em qual escala e em quais municípios. E não generalizem para "o Nordeste" o que vocês mediram em dois municípios e dez anos.

### 1.2 Objetivos específicos

De 4 a 5 itens, verbo no infinitivo, minúscula no início, ponto e vírgula no fim de cada um e ponto no último, **na mesma ordem** das etapas da Metodologia e das subseções dos Resultados. Cada um tem de ser **verificável**: na Conclusão, vocês mostraram com número que foi atingido. "Instalar uma biblioteca" é tarefa, não objetivo.

O que os itens devem cobrir (escrevam com as suas palavras): a obtenção dos dados climáticos; a implementação e o teste do Hargreaves-Samani; a validação contra o Penman-Monteith; o cálculo da necessidade de água das duas culturas; e o balanço hídrico mensal.

### Resumo, *Abstract* e palavras-chave

Escrito **por último**, depois do texto aprovado. Parágrafo único, de 150 a 250 palavras (é um artigo), impessoal, sem citações, sem siglas pouco conhecidas e sem menção a figuras ou tabelas (NBR 6028:2021). Uma ou duas frases para cada item:

1. **contexto e problema:** a água na agricultura familiar do Agreste e a falta de dados para o método padrão;
2. **objetivo:** o que o trabalho desenvolveu e validou;
3. **método:** NASA POWER, dez anos, Hargreaves-Samani validado contra Penman-Monteith, Kc do FAO-56, duas culturas, dois municípios;
4. **resultados:** os números principais (o erro e a correlação; os meses de déficit de cada cultura);
5. **conclusão:** se o método simples serve para o indicador, e o encaminhamento para o AgroAgreste.

**Coloquem números no resumo.** Resumo sem número é resumo fraco.

O ***Abstract*** é a versão em inglês. Os termos técnicos têm forma consagrada (*reference evapotranspiration*, *crop coefficient*, *crop water requirement*, *water balance*): usem-nas, e não a tradução literal. Não entreguem tradução automática sem revisar.

**Palavras-chave:** de 3 a 5, separadas por ponto e vírgula, no campo de: evapotranspiração; Hargreaves-Samani; necessidade hídrica; agricultura familiar; Educação Ambiental.

### Título

Deve indicar **o que foi feito** e **em que contexto**, coerente com o objetivo geral: o objeto (necessidade de água ou evapotranspiração), as culturas, o método (se couber) e o lugar (Nova Cruz, RN, ou Agreste potiguar). Subtítulo separado por dois-pontos, se precisar. Evitem títulos genéricos ("Calculadora de água") e não prometam mais do que o artigo mede. Proponham **três opções** na *issue*; nós escolhemos uma com vocês na revisão.

### Revisão final

- [ ] A Introdução (bloco 4) e a Metodologia estão no **passado** (o que estava "planejado" foi atualizado com o que foi feito)?
- [ ] O objetivo geral, as perguntas de pesquisa, os objetivos específicos, as subseções dos Resultados e a Conclusão falam das mesmas coisas, na mesma ordem?
- [ ] Todos os números do Resumo, dos Resultados e da Conclusão são **exatamente** os dos arquivos de `resultados/`?
- [ ] As equações estão numeradas e citadas no texto?
- [ ] Os valores do FAO-56 estão citados com a tabela e a página?
- [ ] Toda tabela e figura é citada no texto antes de aparecer, tem identificação em cima e fonte embaixo?
- [ ] Os gráficos informam a unidade nos eixos?
- [ ] As limitações estão declaradas?
- [ ] As siglas (FAO, NASA, IBGE, ANA, SUDENE, ET₀, ETc) estão por extenso na primeira vez?
- [ ] O texto está impessoal e no passado?
- [ ] O endereço do repositório (https://github.com/nicifrn/mp_agro_agua_culturas) está citado em Materiais e Métodos?
- [ ] O texto parece escrito por uma pessoa só (mesmos termos, mesmo tempo verbal)?
- [ ] Todos os comentários foram respondidos e resolvidos?
- [ ] A versão final foi nomeada no histórico: `Entrega 6 - versão final - 10/12`?

Para entregar, comentem na *issue* com o nome da versão e as três opções de título, e movam o card para **Em revisão**.

---

<a id="quadro-resumo"></a>
## 10. Quadro-resumo

| Sprint | Período | Desenvolvimento | Escrita | Conceitos novos |
|---|---|---|---|---|
| 1 | 16/10 a 22/10 | Aprender Python 1 | Preparar o documento e fichar | Git, ambiente virtual, variáveis, `if`, `for`, funções |
| 2 | 23/10 a 29/10 | Aprender Python 2 | Introdução e Objetivo geral | listas, dicionários, CSV, `pandas`, gráficos, API, `pytest` |
| 3 | 30/10 a 05/11 | Dados da NASA POWER | Referencial 2.1 e 2.2 | JSON, dado bruto, dado faltante, testes de dados |
| 4 | 06/11 a 12/11 | Hargreaves-Samani | Referencial 2.3 a 2.5 | radiação extraterrestre, radianos, testes com o FAO-56 |
| 5 | 13/11 a 19/11 | Validação com Penman-Monteith | Metodologia e Materiais e Métodos | erro médio, erro absoluto médio, correlação |
| 6 | 20/11 a 26/11 | Necessidade de água das culturas | Tabelas da validação | Kc, fases da cultura, interpolação linear |
| 7 | 27/11 a 03/12 | Balanço hídrico mensal | Resultados e Discussão | déficit, excedente, ano seco e chuvoso |
| 8 | 04/12 a 10/12 | Programa completo, calculadora e README | Conclusão, Resumo e Título | `argparse`, reprodutibilidade |

---

<a id="riscos"></a>
## 11. Riscos e planos B

| Risco | Sinal de alerta | O que fazer |
|---|---|---|
| O Python não "entra" em duas semanas | Sprint 2 chegando à quarta com exercícios faltando | Entreguem o que fizeram, com o diário dizendo onde travaram. Na Sprint 3, o que um não souber, os dois fazem juntos, lado a lado (um digita, o outro acompanha, e trocam a cada hora) |
| A API da NASA POWER fora do ar | Sprint 3, erro de conexão repetido | Tentem em outro horário. Se continuar por mais de um dia, comentem na *issue* com o erro inteiro, e eu envio os JSON baixados por mim para vocês colocarem em `dados/brutos/` (o programa não baixa de novo o que já existe) |
| Dias vazios (-999) nos dados | Sprint 3, teste de vazios falhando | Anotem as datas na *issue*. Se forem poucos dias, o `pyet` e o Hargreaves pulam esses dias, e vocês declaram quantos foram. Não inventem valores |
| Os testes do Exemplo 8 não passam | Sprint 4 | Confiram, nesta ordem: radianos em todas as funções do `math`; o J do dia 3 de setembro (246); a latitude negativa (sul) |
| A `pyet` dá resultado vazio ou estranho | Sprint 5 | Confiram os nomes dos parâmetros na documentação e a latitude em radianos |
| A curva do Kc sai com "degraus" | Sprint 6 | Confiram a interpolação nos dias de fronteira, com os testes da cultura inventada |
| O tempo aperta na Sprint 7 | segunda, 30/11, sem os gráficos | Façam primeiro Nova Cruz (o município principal) e as duas culturas; Canguaretama entra no texto só com a tabela |
| A calculadora atrasa | Sprint 8 | Entreguem o `rodar_tudo.py`, o indicador e o README. A calculadora vira trabalho futuro no texto |

**Se algo tiver de ser cortado, cortem largura, não profundidade.** É melhor um município e duas culturas bem validados do que dois municípios mal conferidos. O que **não** pode faltar é o Hargreaves-Samani testado com o FAO-56, a validação contra o Penman-Monteith e o balanço mensal de Nova Cruz: isso é o trabalho.

---

<a id="extras"></a>
## 12. Se sobrar tempo (opcional)

Só depois de a sprint da semana estar entregue. Cada extra que vocês fizerem vira um parágrafo a mais nos Resultados.

- **E1.** **Calibrar** o Hargreaves-Samani para Nova Cruz: testar outros valores no lugar do 0,0023 e ver qual deixa o erro médio mais perto de zero. Cuidado: calibrem com os anos de 2015 a 2019 e confiram o erro em 2020 a 2024 (calibrar e conferir nos mesmos anos engana).
- **E2.** **Ajustar o Kc** intermediário e final para o clima local, com a equação 62 do FAO-56 (usa a umidade mínima e o vento médio), e ver se o balanço muda.
- **E3.** Testar **outras datas de plantio** (1º de março, 1º de maio) e mostrar qual deixa menos meses com déficit.
- **E4.** Acrescentar o **ciclo completo da mandioca**, juntando o primeiro e o segundo ano do FAO-56.
- **E5.** Fazer a calculadora para **qualquer coordenada**, baixando os dados da NASA POWER na hora.

---

<a id="referencias-minimas"></a>
## 13. Referências mínimas do artigo

- **2 obras de metodologia científica:** Gil (2017) e Prodanov e Freitas (2013), em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md);
- **o manual FAO-56** (Allen *et al.*, 1998): é a referência central do trabalho;
- **o artigo de Hargreaves e Samani (1985)**;
- **1 livro de agrometeorologia** em português (por exemplo, Pereira, Angelocci e Sentelhas);
- **a documentação da NASA POWER** e **1 trabalho que validou a NASA POWER** no Brasil;
- **a documentação da `pyet`**;
- **2 a 3 trabalhos relacionados** (seção 2.5);
- **1 publicação da Embrapa** sobre mandioca ou feijão;
- **a legislação e as fontes institucionais:** Lei nº 11.326/2006, Lei nº 9.795/1999, IBGE (tabela 5457 do SIDRA), a delimitação do Semiárido da SUDENE e o relatório da ANA.

Registrem a referência completa de **tudo** o que lerem, na seção de Referências do documento do Drive, desde o primeiro dia.
