from pydoc import classname
import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd   

#register page in the dash app
dash.register_page(__name__,)

# text for the webpage contents
gamma_info = '''

###### The fastest ones are called Gamma waves, and they indicate the brain is engaged in “higher” cognitive states such as peace and altruism. This state is also present when the brain is processing a lot of information and passing it between regions.
'''
beta_info = '''

###### Beta waves are engaged when attention is being used to outwardly cognitive tasks that involve the senses. In this state, the mind is alert, focused, good at making judgment decisions, and solving problems.
'''
alpha_info = '''

###### Alpha waves indicate passive and calm thought activity, and that a person is comfortable in the present moment. The brain is awake, yet resting, and is engaged with coordination, clarity, and alertness. This is a great time for learning to take place.
'''
theta_info = '''

###### Theta waves are prevalent in sleep and meditation. They indicate learning, memory, intuition, and imagination.
'''
delta_info = '''

###### Delta waves are the slowest, and they are indicative of meditation and dreamless sleep. When the brain is actively engaged in a delta rhythm, there is little external awareness, which gives the mind and body a chance to heal and regenerate.
'''
flow_info = '''

###### Flow is measured based on the amount of workload and immersion in a task, and is particularly noticed when you regulate your cognitive load and focus based on the increased task difficulty.
'''
focus_info = '''

###### Levels of focus reflect the intensity of concentration and attention you have in a specific task and is the opposite of mind wandering. The more you fixate on a task and concentrate on it, your levels of focus rise.
'''
cognitiveload_info = '''

###### When we workout at the gym, we lift weight in the form of dumbbells to do workouts - the same applies to the brain and all the processing it does every second. We want to balance our cognitive load, such that it does not remain too high for too long a period, but for analyzing and solving difficult tasks, we could notice our cognitive load rising, and also notice the cognitive load drop when we are inactive/relaxing.
'''
stress_info = '''

###### A state of mental or emotional strain or tension resulting from adverse or demanding circumstances.
'''
rawegg_info = '''

###### Raw EEG data is captured when an electrode captures neuron activity, the raw EEG data part is the electrical activity taking place in the electrodes proximity. The raw EEG data itself is a complex waveform of not simply brainwave activity, but the electrical activity of nearby muscles, electrode motion interference and what is called “ambient noise” (caused by electrical supplies and appliances in the room).
# '''


# layout for the page
def layout():
    return dbc.Container(
        [   
            dbc.Row(dbc.Col(html.Div(children=[
                html.Br(),
                html.H5('Information about different frequency and metrics data', className='text-center'),
                html.Br(),

            ]))),
            dbc.Row(dbc.Col(html.Div(children=[
                
                
                html.H4('Frequency Values', className='text-center'),
                
                html.Br(),

            ]))),
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Br(),
                    dcc.Markdown(children=gamma_info),
                    
                    
                ]),
                    width={'size': 9, 'offset': 0, 'order': 2}),
                
                dbc.Col(html.Div(children=[
                    html.H3('Gamma', className='text-center'),
                    
                ]),
                
                    width={'size': 2, 'offset': 0, 'order': 1}),   
                

            ]),
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(children=beta_info),
                    
                    
                ]),
                    width={'size': 9, 'offset': 0, 'order': 1}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.H3('Beta', className='text-center'),
                    

                ]),
                    width={'size': 2, 'offset': 0, 'order': 2}),   
                

            ]), 
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(children=alpha_info),                   
                ]),
                    width={'size': 9, 'offset': 0, 'order': 2}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.H3('Alpha', className='text-center'),
                ]),
                    width={'size': 2, 'offset': 0, 'order': 1}),   
                

            ]),
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(children=theta_info),
                    
                    
                ]),
                    width={'size': 9, 'offset': 0, 'order': 1}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    
                    html.H3('Theta', className='text-center'),
                    

                ]),
                    width={'size': 2, 'offset': 0, 'order': 2}),   
                

            ]), 
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(children=delta_info),                   
                ]),
                    width={'size': 9, 'offset': 0, 'order': 2}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.H3('Delta', className='text-center'),
                ]),
                    width={'size': 2, 'offset': 0, 'order': 1}),   
                

            ]),
            dbc.Row(dbc.Col(html.Div(children=[
                
                html.Br(),
                html.Br(),
                html.H4('Metrics Values', className='text-center'),
                
                html.Br(),

            ]))),
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Br(),
                    dcc.Markdown(children=flow_info),
                    
                    
                ]),
                    width={'size': 9, 'offset': 0, 'order': 1}),
                
                dbc.Col(html.Div(children=[
                    
                    html.H3('Flow', className='text-center'),
                    

                ]),
                    width={'size': 2, 'offset': 0, 'order': 2}),   
                

            ]), 
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(children=focus_info),                   
                ]),
                    width={'size': 9, 'offset': 0, 'order': 2}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.H3('Focus', className='text-center'),
                ]),
                    width={'size': 2, 'offset': 0, 'order': 1}),   
                

            ]),
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(children=cognitiveload_info),
                    
                    
                ]),
                    width={'size': 9, 'offset': 0, 'order': 1}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.H3('Cognitive Load', className='text-center'),
                    

                ]),
                    width={'size': 2, 'offset': 0, 'order': 2}),   
                

            ]), 
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown(children=stress_info),                   
                ]),
                    width={'size': 9, 'offset': 0, 'order': 2}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    
                    html.H3('Stress', className='text-center'),
                    
                ]),
                    width={'size': 2, 'offset': 0, 'order': 1}),   
                

            ]),                          
            dbc.Row([
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    
                    dcc.Markdown(children=rawegg_info),
                    html.Br(),
                    
                ]),
                    width={'size': 9, 'offset': 0, 'order': 1}),
                
                dbc.Col(html.Div(children=[
                    html.Hr(style={'height':'6px'}),
                    html.Br(),
                    html.H3('Raw EGG', className='text-center'),
                    

                ]),
                    width={'size': 2, 'offset': 0, 'order': 2}),   
                

            ]),

        ], fluid=True)