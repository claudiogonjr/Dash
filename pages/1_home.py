import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, register_page, page_registry, dash_table

PAGE = {
  'path': '/',
  'name': 'Início',
}

register_page(__name__, path=PAGE['path'], name=PAGE['name'])

df = pd.read_parquet('data/dataset_clean.parquet')

def get_grouped_data(df, groupby: str, sum: str='emissao', drop: str='ano'):
  return df.groupby(groupby, sort=False).sum(sum).drop(drop, axis=1).squeeze().sort_values(ascending=False)

emission_per_year = pd.read_parquet('./data/emission_per_year.parquet')
emission_per_uf = get_grouped_data(df, 'sigla_uf')
emission_per_emission_type = get_grouped_data(df, 'tipo_emissao')
emission_per_gas = get_grouped_data(df, 'gas').head(10)
emission_per_eco_activity = get_grouped_data(df, 'atividade_economica')

################# BEGINNING #################
layout = html.Div([
  html.H2('☁️ Emissões de Gases de Efeito Estufa no Brasil (2000-2019)'),
  html.Hr(),

  html.P('Os gráficos a seguir foram criados com base em um conjunto de dados de 20 anos de emissões de gases de efeito estufa (GEE) no Brasil (2000-2019), fornecendo mais de 1 milhão de registros para os setores de Agricultura, Energia, Indústria, Resíduos e Mudança do Uso da Terra em escala nacional. e níveis subnacionais. foi desenvolvido pelo Observatório do Clima, uma iniciativa da sociedade civil brasileira, com base nas diretrizes do IPCC e nos Inventários Nacionais Brasileiros incorporados a fatores e processos de emissão específicos do país.'),
  dash_table.DataTable(
    data=df.head(1_000).to_dict('records'),
    columns=[{"name": i, "id": i, 'selectable': True} for i in df.columns],
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    page_action="native",
    page_current= 0,
    page_size= 10,
  ),
  html.P('OBS 1: Todos os valores de emissão estão na escala de toneladas (t).'),
  html.P('OBS 2: Originalmente o dataset veio com registros desde 1970 (3.2 Mi de registros), porém filtramos os dados a partir de 2000 (1.2 Mi de registros) por questões de economia de performance e tempo. Por este motivo, a maior parte dos dados apresentados nesta página são entre 2000-2019.'),
  html.Hr(),

  html.H3('- Emissão de Gases de Efeito Estufa (1970-2019)'),
  html.P('Apresentação da evolução no índice de emissão de Gases de Efeito Estufa (GEE) ao longo do tempo. Esse índice mede a quantidade de gases que são liberados na atmosfera e que contribuem para o aquecimento global. Quanto maior o índice, maior é a quantidade de GEE emitida.'),
  dcc.Graph(figure=px.line(emission_per_year)),
  html.Hr(),
])
