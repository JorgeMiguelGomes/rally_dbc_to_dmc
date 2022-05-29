# -*- coding: utf-8 -*-
# Developed with 🤍 by VOST Portugal
# Code by Jorge Gomes 
# KML files by Nuno Peixoto 
# Geojson conversion by Paulo Henriques
# Infrastructure by João Pina


# Vodafone Rally de Portugal 2022 - Spectator Zones Public 
# This app will be embed at the official site. 

# -----------------------------------------------
#                  LIBRARIES
# -----------------------------------------------

# Import Core Libraries

import pandas as pd 
import plotly.express as px
import json 

# Import Dash and Dash Bootstrap Components
import dash
import dash_daq as daq
from dash import Input, Output, dcc, html, dash_table, callback
import dash_bootstrap_components as dbc




# -----------------------------------------------
#              APP STARTS HERE
# -----------------------------------------------


app = dash.Dash(__name__,title='VODAFONE RALLY DE PORTUGAL',suppress_callback_exceptions=True,update_title=None,
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
	)


app.css.config.serve_locally = False 
app.scripts.config.serve_locally = False 

server = app.server

# Google Analytics 

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
		<script async src="https://www.googletagmanager.com/gtag/js?id=G-R4DT982P80"></script>
		<script>
  			window.dataLayer = window.dataLayer || [];
 			function gtag(){dataLayer.push(arguments);}
  			gtag('js', new Date());

  			gtag('config', 'G-R4DT982P80');
		</script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""



# -----------------------------------------------
#                   CARD STYLING 
# -----------------------------------------------

card_head_style = {"background": "#1F2B45","color":"white","font-size":"24px","font":"bold"}
card_text_style = {"color":"#1F2B45","font":"bold"}


# -----------------------------------------------
#              GET DATA
# -----------------------------------------------

df_access = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQFfzz_Hbd_j_GnR_iDqFdnTxb8XmI6E-8EBehky5HJE5tP57ddT6oOw7chLB1Cl2E8IcJjd4u7uG4k/pub?gid=761969903&single=true&output=csv')


# -----------------------------------------------
#              APP LAYOUT DESIGN
# -----------------------------------------------


app.layout = html.Div(
	[
		html.Hr(style={'margin_top':'35px'}),
		html.Div(
			[
				dbc.Col(
					html.Img(src="/assets/logo-vodafone-rally-de-portugal-2022.png"),
				xs=12, sm=12, md=12, lg=12, xl=12,
				),
			],
		style={"align":"center"},
		),

		html.Hr(style={'margin_bottom':'35px'}),
		dbc.Row(
			[
				dbc.Col(
					[
						html.H6("DIA / DAY",style={'margin-left':'20px'}),
						dbc.Col(
		                    dcc.Dropdown(
		                        id='dropdown_dia',
		                        options=[{'label': i, 'value': i} for i in df_access['day'].unique()],
		                        placeholder='Escolha / Select',
		                        value="2022/05/19",
		                        className="dropdown",
		                        multi=False
		                    ),
		                 ),
					],
					xs=12, sm=12, md=3, lg=3, xl=2,
				),
				dbc.Col(
					[
						html.H6("Super Especial / Special Stage",style={'margin-left':'20px'}),
						dbc.Col(
		                    dcc.Dropdown(
		                        id='dropdown_ss',
		                        className="dropdown",
		                        placeholder='Escolha / Select',
		                        value="Shakedown",
		                        multi=False
		                    ),
		                 ),
					],
					xs=12, sm=12, md=3, lg=3, xl=2,
				),
				dbc.Col(
					[
						html.H6("ZE",style={'margin-left':'20px'}),
						dbc.Col(
		                    dcc.Dropdown(
		                        id='dropdown_ze',
		                        className="dropdown",
		                        placeholder='Escolha / Select',
		                        value="ZE1",
		                        multi=False
		                    ),
		                 ),
					],
					xs=12, sm=12, md=12, lg=4, xl=4,
				),
			],
		),
		html.Hr(),
		dbc.Row(
			[
				dbc.Col(
					dbc.Card(
	                    [
	                    	dbc.CardHeader(id="common_name", style=card_head_style),
	                        dbc.CardBody(
	                            [
	                                html.H6("Zona Espectáculo", className="card-title"),
	                                html.H4(id="ze_name",style=card_text_style),
	                            ],

	                    	),
	                    ],
	             	),
	            xs=12, sm=12, md=12, lg=4, xl=4,
				),
				dbc.Col(
					dbc.Card(
	                    [
	                    	dbc.CardHeader("Tipo de Acesso", style=card_head_style),
	                        dbc.CardBody(
	                            [
	                                html.H6("Access Type", className="card-title"),
	                                html.H4(id="track_type",style=card_text_style),
	                            ],

	                    	),
	                    ],
	             	),
	            xs=12, sm=12, md=12, lg=3, xl=4,
				),
				dbc.Col(
					dbc.Card(
	                    [
	                    	dbc.CardHeader("Link Waze", style=card_head_style),
	                        dbc.CardBody(
	                            [
	                                html.H6("Waze Link", className="card-title"),
	                                html.H4(id="link_waze",style=card_text_style),
	                            ],

	                    	),
	                    ],
	             	),
	            xs=12, sm=12, md=12, lg=3, xl=4,
				),
			],
		className="g-0",
		),
		dbc.Row(
			[
				dbc.Col(
					[
						dbc.Col(
							dcc.Graph(id="location_map"),
							),
					],
				xs=12, sm=12, md=12, lg=3, xl=4,
				),
				dbc.Col(
					[
						dbc.Col(
							dcc.Graph(id="location_ze_map"),
							),
					],
				xs=12, sm=12, md=12, lg=3, xl=4,
				),
			],
		),
		dbc.Row(
			[
				dbc.Col(
					[
					html.Hr(style={"margin-left":"25px","margin-top":"50px","margin-bottom":"50px","align-text":"center"}),
					html.A("Developed with 🤍 by VOST Portugal", href='https://vost.pt', target="_blank",style={"align":"center"}),
					html.A(" with the support of Waze Portugal", href='https://mobile.twitter.com/wazeportugal', target="_blank",style={"align":"center"})
					],

				),
			],
		)
		
	],
)




@app.callback(
    Output(component_id="dropdown_ss", component_property="options"),
    Input(component_id="dropdown_dia", component_property="value"),
    #prevent_initial_call=True
)

def update_ze_dropdown(value):


	df_access = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQFfzz_Hbd_j_GnR_iDqFdnTxb8XmI6E-8EBehky5HJE5tP57ddT6oOw7chLB1Cl2E8IcJjd4u7uG4k/pub?gid=761969903&single=true&output=csv')
	df_dropdown_ze = df_access[df_access['day']== value]
	return [{'label': i, 'value': i} for i in df_dropdown_ze['common_name'].unique()]

@app.callback(
    Output(component_id="dropdown_ze", component_property="options"),
    Input(component_id="dropdown_ss", component_property="value"),
    #prevent_initial_call=True
)

def update_ze_dropdown(value):


	df_access = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQFfzz_Hbd_j_GnR_iDqFdnTxb8XmI6E-8EBehky5HJE5tP57ddT6oOw7chLB1Cl2E8IcJjd4u7uG4k/pub?gid=761969903&single=true&output=csv')
	df_dropdown_ze = df_access[df_access['common_name']== value]
	return [{'label': i, 'value': i} for i in df_dropdown_ze['ze_name'].unique()]

@app.callback(
	Output(component_id="common_name", component_property="children"),
	Output(component_id="ze_name", component_property="children"),
	Output(component_id="track_type", component_property="children"),
	Output(component_id="link_waze", component_property="children"),
	Output(component_id="location_map", component_property="figure"),
	Output(component_id="location_ze_map", component_property="figure"),
    Input(component_id="dropdown_dia", component_property="value"),
    Input(component_id="dropdown_ss", component_property="value"),
    Input(component_id="dropdown_ze", component_property="value"),
    #prevent_initial_call=True

)

def update_card(day_value,ss_value,ze_value):

	# DATA TREATMENT AND FILTERING 
	df_access = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQFfzz_Hbd_j_GnR_iDqFdnTxb8XmI6E-8EBehky5HJE5tP57ddT6oOw7chLB1Cl2E8IcJjd4u7uG4k/pub?gid=761969903&single=true&output=csv')
	
	df_filter_dropdown_01 = df_access[df_access['day']== day_value]

	df_filter_dropdown_02 = df_filter_dropdown_01[df_filter_dropdown_01['common_name']== ss_value]

	df_filter_dropdown_03 = df_filter_dropdown_02[df_filter_dropdown_02['ze_name']== ze_value]
	
	# CARD VALUES
	ze_name_card = df_filter_dropdown_03['ze_name'].values[0]



	common_name_card = df_filter_dropdown_03['common_name'].values[0]

	track_type_card = df_filter_dropdown_03['type_of_track'].values[0]

	# BUILD MAP ALL ZE from SS


	location_map_graph = px.scatter_mapbox(df_filter_dropdown_02,
									lat='latitude',
									lon='longitude',
									size='area_01_sq',
									color='ze_name',
									zoom=10,
									mapbox_style='open-street-map',
									color_discrete_sequence=["#C71115","#F54E04","#F54E04","#F54E04","#F54E04","#F54E04","#F54E04"],
									labels={"ze_name":"ZE #"}
									)
	location_map_graph.update_layout(margin={"r":0,"t":15,"l":0,"b":15},showlegend=True)

	location_map_graph.update_layout(legend=dict(
	    orientation="h",
	    yanchor="bottom",
	    y=1.02,
	    xanchor="right",
	    x=1
	))


	# BUILD MAP FOR CHOOSEN ZE

	# Define ZE Geojson source
	source_geo = f"assets/zegeojson/" \
	f"{ze_name_card}" \
	f".geojson" \
	
	
	# Open geojson file with doors layout 
	with open(source_geo) as response:
		ze_area = json.load(response)

	# Define Map Center

	center_lat = df_filter_dropdown_03['latitude'].values[0]
	center_lon = df_filter_dropdown_03['longitude'].values[0]


	location_ze_map = px.choropleth_mapbox(df_filter_dropdown_03, geojson=ze_area,locations='ze_name',featureidkey='properties.Name',color='occupancy',
									color_continuous_scale="Reds",                           
									mapbox_style="open-street-map",
									center=dict(lon=center_lon, lat=center_lat),
									zoom=16,
									opacity=0.6
									
	)

	location_ze_map.update_layout(margin={"r":0,"t":15,"l":0,"b":15},coloraxis_showscale=False)


	# Get Link for ZE 

	waze_link = df_filter_dropdown_03['link_waze'].values[0]

	waze_link_return = html.A(common_name_card+" / "+ze_name_card,href=waze_link, target="_blank")

	# html.A("Developed with 🤍 by VOST Portugal", href='https://vost.pt', target="_blank",style={"align":"center"}),



	

	return common_name_card,ze_name_card, track_type_card, waze_link_return, location_map_graph, location_ze_map

	


# -------------------------------------------------------------------------------------
# --------------------------------  START THE APP -------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == "__main__":
	app.run_server(host='0.0.0.0', debug=True)


# The End

