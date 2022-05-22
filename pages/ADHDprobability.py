#libraries for building the webapp page
from logging import PlaceHolder
from pydoc import classname
import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import dash_bootstrap_components as dbc
# libraries for machine learning
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import random
#libraries to save the excel file uploaded on webapp
import base64
import datetime
import io

# inserting this page into the webapp built in different code
dash.register_page(__name__,)

# Forming dataframes for the machine learning and predicting for a random user


# text displayed on the page
upload_info= '''
#### This is a place to upload the excel file with patient's data.
'''

# function defining the layout of the page
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

                            'Drag and Drop or ',
                            html.A('Select a File')
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
                    
                    
                
                

            ]),
            dbc.Row([
                dbc.Col(html.Div(id='output-file'))

            ]),
            dbc.Row([
                dbc.Col(html.Div(id='results')
                    
                ),                
                dbc.Col(html.Div(children=[
                    html.Br(),
                    # button that starts the machine learning function
                    html.Button('Submit', id='submit-value', n_clicks=0, style={'font-size':'29px', 'width':'160px', 'height':'40px','background-color':'#F2F2F2', 'color':'#262626'}),
                    html.Br()

                ]),
                    align='end',
                    width={'size':3, 'order':2}
                ),
            ]),
            
        ],fluid=True
    )

# funtion that has the algorithm for the PC to be able to predict whether the person ahs adhd based on the provided data  
def machine_learning():
    dataML=pd.read_excel(r'C:\Users\Filip\Desktop\Codes\Curvex\Samlet_Data.xlsx')
    df1=pd.read_excel(r'Person.xlsx', index_col=[0])
    
    # Modifying dataframes for the axis for ML
    x = pd.get_dummies(dataML.drop(['ADHD','Person'], axis=1))
    y = dataML['ADHD']

    #Oversampling to have a better random split due to data structure
    allzeros=dataML.loc[dataML['ADHD']==0]
    zeros2=allzeros.head(5)
    dataML=pd.concat([dataML,allzeros],axis=1)
    dataML.reset_index(drop=True)
    dataML=pd.concat([dataML,zeros2],axis=1)
    dataML.reset_index(drop=True)

    # Splitting the data for training
    xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.5)

    # Establishing the machine leaning functions and compiling the model
    model = Sequential()
    model.add(Dense(units=64, activation='relu', input_dim=len(xtrain.columns)))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='Adam', metrics='accuracy')

    # Training the model 100 times
    model.fit(xtrain, ytrain, epochs=100)

    # Specifying the output values for the model
    y_hat = model.predict(xtest)
    y_hat = [0 if val < 0.5 else 1 for val in y_hat]

    # Printing the loss and accuracy (use the accuracy on the website)
    test_loss, test_acc = model.evaluate(xtest, ytest, verbose=2)
    test_loss=round(test_loss, 2)
    test_acc=round(test_acc, 2)
    print('\nLoss for the model:', test_loss)
    print('\nAccuracy of the model:', test_acc)
        
    # Adding the new value together with the column name to the users personal excel file and predicts if the preson has adhd 
    k=model.predict(df1)
    k=[0 if val < 0.5 else 1 for val in k]
    df1['ADHD']=list(k)
    df1['UserID']= random.randint(0,1000)
    df1['Accuracy']= test_acc
    df1.to_excel("./Person.xlsx",index=False)
    adhd=df1.at[0,'ADHD']
    accuracy=df1.at[0,'Accuracy']
    percentage_acc=f"{accuracy:.0%}"
    
    # creating output based on the ADHD column, which was predicted by the machine  
    try:
        if adhd == 1:
            return html.Div([
                html.Br(),
                html.Br(),
                html.Hr(),
                html.H2('\tThe person has ADHD. The accuracy of the outcome is: ' + percentage_acc),
                html.Hr()
            ])
        elif adhd ==0:
            return html.Div([
                html.Br(),
                html.Hr(),
                html.H2('\tThe person does not have ADHD. The accuracy of the outcome is: ' + percentage_acc),
                html.Hr()
            ])
        else:
            return html.Div([
                html.H2('Something went wrong')
            ])
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
        


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
        
        html.H3('Your data has been saved. To see if the person has ADHD based on the data, please press the button.'),
        
        
        dcc.Store(id="stored-data", data=df.to_excel('Person.xlsx'))
    ])

# first callback that takes the input from the user in a form of excel file and gives output
@callback(
    Output('output-file','children'),
    [Input('upload-data', 'contents'), Input('upload-data','filename')],
)
# funtion that runs the parse_contents() funtion if the file inserted has some values in it 
def save_data(contents,filename):
    if contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(contents, filename)]
        return children
    
# second callback which takes the input from the user in a form of a button click and gives output   
@callback(
    Output('results','children'),
    [Input('submit-value','n_clicks')],
)
# function that starts the machine learning function after the button was pressed
def present_data(button):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'submit-value' in  changed_id:
        return machine_learning()
    else:
        print()
