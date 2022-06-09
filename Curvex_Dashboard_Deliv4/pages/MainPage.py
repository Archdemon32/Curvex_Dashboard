#libraries for dash webapp
import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd   
import base64
import datetime
import io
pd.options.mode.chained_assignment = None
#register page in the dash app
dash.register_page(__name__, path="/")


upload_info= '''
#### This is a place to upload the excel file with patient's data.
'''

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
dd_split= [
    {'label': 'First Split', 'value': 'first_split'},
    {'label': 'Second Split', 'value': 'second_split'},
    {'label': 'Third Split', 'value': 'third_split'},

]
#layout
def layout():
    return dbc.Container(
    [     
        dbc.Row([
                dbc.Col(html.Div(children=[
                    # displays text on the page
                    dcc.Markdown(children=upload_info, className='text-center'),
                    html.Br()
                ]),
                    width={'size':12, 'order':1}),
            ]),
            dbc.Row([    
                dbc.Col(html.Div(children=[
                    # creates a box where the user can upload the file
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div([

                            'Drag and Drop ',
                            #html.A('Select a File')
                    ]), style={
                        
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '3px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'backgroundColor':'#262626',
                        'textColor':'#F2F2F2',
                        'textSize':'100%',
                        'width': '6'
                    },
                    multiple=True,
                    
                    ),                
                ]),
                    width={'size':5}),                
                dbc.Col(html.Div(children=[
                    html.Br(),
                    html.A(html.Button('Submit', id='split-file', n_clicks=0,style={'font-size':'29px', 
                    'width':'160px', 'height':'40px','background-color':'#F2F2F2', 'color':'#262626'}),href='/')

                ])),
            ]),
        dbc.Row([
            dbc.Col(html.Div(id='outputfile')),
            dbc.Col(html.Div(id='splitoutput')),
        ]),
        dbc.Row([
            # First Column Graph
            dbc.Col(html.Div(children=[
                html.Br(),
                html.Br(),
                html.H5('First Split', className='text-center'),
                html.Hr(),
                dcc.Graph(id='Graph1',
                        style={'height': 350},
                        ),
                html.Br(),
                html.H5('Second Split', className='text-center'),
                html.Hr(),
                dcc.Graph(id='Graph2',
                        style={'height': 350},
                        ),
                html.Br(),
                html.H5('Third Split', className='text-center'),
                html.Hr(),
                dcc.Graph(id='Graph3',
                        style={'height': 350},
                        
                        ),
            ]),
                # order 2 puts this column on the right side of the row
                width={'size': 9, 'offset': 0, 'order': 2}),
            # Second Column dropdown menu
            dbc.Col(html.Div(children=[            
                html.Br(),
                html.H6('Choose the value', className='text-center'),
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
                html.Br(),
                html.Br(),
                dcc.Textarea(
                    placeholder='Place for your notes..',
                    style={'width': '85%', 'height': 400}
                )            
            ]),
                # order 1 puts this column on the left side of the row
                width={'size': 3, 'offset': 0, 'order': 1}),                        
        ]),
    ], fluid=True)
#function that saves the data that the user uploaded into the pc 
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return html.Div([
        html.Br(),
        html.H6('Your data has been saved. Please press Submit to update the graphs'),
        dcc.Store(id="stored-data", data=df.to_csv('Graph_data.csv',index=False))
    ])
        
# first callback that takes the input from the user in a form of excel file and gives output
@callback(
    Output('outputfile','children'),
    [Input('upload-data', 'contents'), Input('upload-data','filename')],
)
# funtion that runs the parse_contents() funtion if the file inserted has some values in it 
def save_data(contents,filename):
    if contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(contents, filename)]
        return children
@callback(
    Output('splitoutput','children'),
    [Input('split-file','n_clicks')],
)
def split_data(button):  
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "split-file" in changed_id:
        df = pd.read_csv('Graph_data.csv', header=0)
        df["Tasks start and end time"].fillna( method ='ffill', inplace = True)
        first_split = df[df["Tasks start and end time"].str.contains('Task 1')]
        first_split.fillna( method='bfill', inplace=True)
        first_split.to_csv('First_split.csv', index=False, sep=',')
        second_split = df[df["Tasks start and end time"].str.contains('Task 2')]
        second_split.fillna( method='bfill', inplace=True)
        second_split.to_csv('Second_split.csv', index=False, sep=',')
        third_split = df[df["Tasks start and end time"].str.contains('Task 3')]
        third_split.fillna( method='bfill', inplace=True)
        third_split.to_csv('Third_split.csv', index=False, sep=',')   
    else:
        print("Something went wrong")
# making the graph interactive   
@callback(
    Output("Graph1", "figure"),   
    [Input("Value-Selector","value")]
)
# function to update the graph based on the choice in dropdown menu
def change_graph(value):
    csv_file=pd.read_csv('First_split.csv'.format(value))
    csv_file['Number of measurements'] = csv_file.index + 1
    fig_Delta = px.line(csv_file, x='Number of measurements', y=value)  
    return fig_Delta

@callback(
    Output("Graph2", "figure"),   
    [Input("Value-Selector","value")]
)
# function to update the graph based on the choice in dropdown menu
def change_graph(value):
    csv_file_two=pd.read_csv('Second_split.csv'.format(value))
    csv_file_two['Number of measurements'] = csv_file_two.index + 1
    fig_Delta = px.line(csv_file_two, x='Number of measurements', y=value)
    
    return fig_Delta
@callback(
    Output("Graph3", "figure"),   
    [Input("Value-Selector","value")]
)
# function to update the graph based on the choice in dropdown menu
def change_graph(value):
    csv_file_three=pd.read_csv('Third_split.csv'.format(value))
    csv_file_three['Number of measurements'] = csv_file_three.index + 1
    fig_Delta = px.line(csv_file_three, x='Number of measurements', y=value)
    
    return fig_Delta