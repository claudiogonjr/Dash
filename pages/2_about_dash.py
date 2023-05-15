import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, register_page, page_registry, dash_table

PAGE = {
  'name': 'Sobre o Dash',
}

register_page(__name__, name=PAGE['name'])

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

################# BEGINNING #################

layout = html.Div([
  html.H2(PAGE['name']),
  dcc.Markdown("""Dash Plotly é um framework Python que permite criar aplicativos da web interativos e visualizações de dados de alta qualidade. 
  Com o Dash Plotly, você pode criar painéis, painéis de controle e aplicativos interativos que permitem que os usuários visualizem, 
  filtrem e analisem os dados em tempo real.

  O Dash é baseado em uma arquitetura de componentes, o que significa que você pode construir seu aplicativo ou painel usando 
  blocos modulares. Cada bloco representa uma parte do seu aplicativo, como um gráfico, um botão ou um campo de entrada. 
  Esses componentes podem ser agrupados em um layout para criar o design do seu aplicativo.

  Além disso, o Dash permite que você crie aplicativos usando o Python puro, sem precisar de conhecimentos em 
  linguagens de marcação da web, como HTML e CSS. Isso torna mais fácil para os cientistas de dados e engenheiros 
  criarem aplicativos da web interativos e compartilharem seus resultados com outras pessoas.

  Se você não se sentir confortável com HTML, não se preocupe! Você pode chegar a 95% do caminho usando apenas alguns 
  elementos e atributos, graças aos componentes pré-construídos fornecidos pelo Dash, como `html.Div`, `html.H1`, `html.P`, 
  `dcc.Graph`, `dcc.Input` e muito mais.

  Esses componentes permitem que você crie layouts, gráficos, campos de entrada e outras interações de forma simples e intuitiva, 
  sem precisar escrever HTML, CSS ou JavaScript. No entanto, se você precisar de funcionalidades mais avançadas, como animações ou 
  interações personalizadas, o Dash permite que você adicione suas próprias classes de CSS e JavaScript para personalizar ainda mais o seu aplicativo.

  Em resumo, o Dash é uma biblioteca Python acessível e intuitiva para criar aplicativos da web interativos e visualizações de 
  dados de alta qualidade, mesmo se você não tiver conhecimentos avançados em HTML, CSS ou JavaScript"""),

  html.H3('Um exemplo de código em Dash:'),
  dcc.Markdown("""
  ```python
  from dash import html

   html.Div([
    html.H1('Olá Dash'),
    html.Div([
        html.P('Dash converte classes Python em HTML'),
        html.P("Essa conversão acontece nos bastidores do front-end em JavaScript do Dash")
      ])
    ])
  ```
  """),

  html.H5('Como seria o codigo em HTML:'),
  dcc.Markdown("""
  ```html
  <div>
    <h1>Olá Dash</h1>
    <div>
        <p>Dash converte classes Python em HTML</p>
        <p>Essa conversão acontece nos bastidores do front-end em JavaScript do Dash</p>
    </div>
  </div>
```
  """),
  
  html.H3('Algumas ferramentas do Dash:'),
  html.P('Com o Dash Core Components(dcc), temos acesso a várias ferramentas e é aqui que podemos dizer que está o carro-chefe e o diferencial do Dash. Duas delas são:'),
  dcc.Markdown("""
    ##### Dash e Markdown

    O Dash suporta [Markdown](http://commonmark.org/help).

    O Markdown é uma maneira simples de escrever e formatar texto.
    
    Ele inclui uma sintaxe para coisas como texto em **negrito** e *itálico*,
    [links](http://commonmark.org/help), trechos de `código`(Como os exemplos anteriores), listas, citações, e mais.
  """),

  html.Br(),

  dcc.Markdown("""
    ##### Componetes gráficos.

    Graph em Dash é um componente que permite criar visualizações de dados interativas em seu aplicativo. Ele é construído com base na biblioteca de visualização de dados Plotly, que oferece suporte a uma ampla variedade de tipos de gráficos, como gráficos de barras, gráficos de dispersão, gráficos de linhas, gráficos de área, gráficos de caixa e muito mais.

    Para usar o componente Graph em Dash, você precisará importar o pacote `dash_core_components` e usar a classe `dcc.Graph`. Você pode personalizar seu gráfico fornecendo uma lista de dados, uma lista de layout e uma lista de configurações para o componente Graph.

    Aqui está um exemplo de gráfico usando o conjunto de dados Iris, um Dataset público do repositório UCI Machine Learning:
  """),
  dcc.Graph(figure= px.scatter(df, x="sepal_width", y="sepal_length")),

])
