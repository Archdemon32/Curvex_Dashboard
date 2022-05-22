# importing the libraries
import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from numpy import size  
import pandas as pd   
import plotly.express as px 

# app creation in dash
app= Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])


# dictionary for Dropdown menu
dd_value_dict= [
    {'label': 'Delta', 'value': 'Delta'},
    {'label': 'Theta', 'value': 'Theta'},
    {'label': 'Low Alpha', 'value': 'Low Alpha'},
    {'label': 'High Alpha', 'value': 'High Alpha'},
    {'label': 'Low Beta', 'value': 'Low Beta'},
    {'label': 'High Beta', 'value': 'High Beta'},
    {'label': 'Low Gamma', 'value': 'Low Gamma'},
    {'label': 'Middle Gamma', 'value': 'Middle Gamma'},
    {'label': 'Cognitive Load', 'value': 'Cognitive Load'},
    {'label': 'Flow', 'value': 'Flow'},
    {'label': 'Focus', 'value': 'Focus'},
    {'label': 'Stress', 'value': 'Stress'},
]
# app layout
app.layout= dbc.Container(
    [   #create a row with 2 columns: graph - first column, dropdown menu- second
        dbc.Row([
            # First Column Graph
            dbc.Col(html.Div(children=[

                html.Br(),

                html.H4('Graphical representation of measured data', className='text-center'),
                html.Br(),

                dcc.Graph(id='Graph1',
                        style={'height': 550},
                        ),

            ]),
                # order 2 puts this column on the right side of the row
                width={'size': 9, 'offset': 0, 'order': 2}),

            # Second Column dropdown menu
            dbc.Col(html.Div(children=[

                html.Br(),
                html.Img(src= 'assets/curvexlogo.png'),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3('Choose the value'),


                dcc.Dropdown(
                    id='Value-Selector',
                    options= dd_value_dict,
                    value= 'Delta',
                    clearable= False,
                    
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                dcc.Textarea(
                    placeholder='Place for your notes..',
                    style={'width': '85%', 'height': 250}
                )            
            ]),
                # order 1 puts this column on the left side of the row
                width={'size': 3, 'offset': 0, 'order': 1}),            
            
            
        ]),
       
    
    ], fluid=True)


        
# making the graph interactive   
    
@app.callback(
    Output("Graph1", "figure"),
    [Input("Value-Selector","value")]
)
# function to update the graph based on the choice in dropdown menu
def change_graph(value):
    csv_file= pd.read_csv("Sample_file_frequency_metrics.csv".format(value))
    csv_file['Number of measurements'] = csv_file.index + 1
    fig_Delta = px.line(csv_file, x='Number of measurements', y=value)
    return fig_Delta




# running the server and restricting the access based on the login name
def running_server():
    if __name__ == '__main__':
        login_name= input("\t\tPlease enter your full name to access the data: ")
        login_name= login_name.title()
        if login_name == "Filip Gavalier":
            print("\n\t\tHello Filip Gavalier. You can see the graphical representation of the data if you click on the link above. ")
            print("\t\tTo leave the app, please press CTRL+C.\n ")
            app.run_server()
            
        else:
            print("\n\t\t Sorry "+ login_name + ". The database does not recognize this name. Try again Later. ")
            exit()
    


running_server()


