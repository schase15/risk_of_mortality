# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports
import joblib
import sklearn
import category_encoders as ce
import numpy as np
import pandas as pd

# Imports from this application
from app import app

# # Load pipeline
pipeline = joblib.load('assets/pipeline.joblib')

# input_labels = ['Age Group', 'Type of Admission',	'APR DRG Code',	'CCS Procedure Code',	'APR Medical Surgical Description',	'Payment Typology 1',	'Emergency Department Indicator' ]

# input_vals = [1, 'Emergency', 254, 0, 'Medical', 'Medicaid', 'Y']

# test_input = pd.DataFrame(dict(zip(input_labels, input_vals)), index=[0])

# test = pipeline.predict(test_input)


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            Fill out the patient information below using the drop down menus.

            Use the Reference tables to get the numeric codes for Procedure Type and Diagnosis

            """
        ),

        dcc.Markdown(
            """
            ##### Age Group:
            """
        ),

        dcc.Dropdown(
            id='age',
            options= [
                {'label': '0 to 17', 'value': 1},
                {'label': '18 to 29', 'value': 2},
                {'label': '30 to 49', 'value': 3},
                {'label': '50 to 69', 'value': 4},
                {'label': '70 or Older', 'value': 5},
            ],
            value=1,
            className='mb-4'
        ),

        dcc.Markdown(
            """
            ##### Type of Admission:
            """
        ),

        dcc.Dropdown(
            id='admission',
            options= [
                {'label': 'Emergency', 'value': 'Emergency'},
                {'label': 'Elective', 'value': 'Elective'},
                {'label': 'Newborn', 'value': 'Newborn'},
                {'label': 'Urgent', 'value': 'Urgent'},
                {'label': 'Trauma', 'value': 'Trauma'},
                {'label': 'Not Available', 'value': 'Not Available'},
            ],
            value='Emergency',
            className='mb-4'
        ),

        dcc.Markdown(
            """
            ##### Medical or Surgical Admittance:
            """
        ),

        dcc.Dropdown(
            id='surgical',
            options= [
                {'label': 'Medical', 'value': 'Medical'},
                {'label': 'Surgical', 'value': 'Surgical'},
            ],
            value='Medical',
            className='mb-4'
        ),

        dcc.Markdown(
            """
            ##### Emergency Room Department:
            """
        ),

        dcc.Dropdown(
            id='emergency_room',
            options= [
                {'label': 'Y', 'value': 'Y'},
                {'label': 'N', 'value': 'N'},
            ],
            value='Y',
            className='mb-4'
        ),

        dcc.Markdown(
            """
            ##### Method of Payment:
            """
        ),

        dcc.Dropdown(
            id='payment',
            options= [
                {'label': 'Medicare', 'value': 'Medicare'},
                {'label': 'Medicaid', 'value': 'Medicaid'},
                {'label': 'Private Health Insurance', 'value': 'Private Health Insurance'},
                {'label': 'Blue Cross/Blue Shield', 'value': 'Blue Cross/Blue Shield'},
                {'label': 'Self-Pay', 'value': 'Self-Pay'},
                {'label': 'Managed Care, Unspecified', 'value': 'Managed Care, Unspecified'},
                {'label': 'Miscellaneous/Other', 'value': 'Miscellaneous/Other'},
                {'label': 'Federal/State/Local/VA', 'value': 'Federal/State/Local/VA'},
                {'label': 'Department of Corrections', 'value': 'Department of Corrections'},
                {'label': 'Unknown', 'value': 'Unknown'},
            ],
            value='Medicare',
            className='mb-4'
        ),

        dcc.Markdown(
            """
            ##### Patient Diagnosis:
            """
        ),
        dcc.Link(
            'Click to access reference codes', 
            href='/reference_tables', 
            className='nav-link',
            # target='_blank',
            style= {'color': 'blue'}
        ),

        dcc.Input(
            id='diagnosis',
            placeholder='Enter a numeric APR DRG Code...',
            type='number',
            value='',
            className='mb-4'
        ),

        dcc.Markdown(
            """
            ##### Patient Procedure:
            """
        ),

        dcc.Link(
            'Click to access reference codes', 
            href='/reference_tables', 
            className='nav-link',
            # target='_blank',
            style= {'color': 'blue'}
        ),

        dcc.Input(
            id='procedure',
            placeholder='Enter a numeric CCS Procedure Code...',
            type='number',
            value='',
            className='mb-4'
        ),

        dcc.Markdown(
            """
            ### The Risk of Mortality for Your Patient is:

            """
        ),

        html.Div(
            id= 'prediction-content',
            style= {
                'textAlign': 'center',
                'color': 'red',
                'fontSize': 72
            }
        )        

    ],
)


@app.callback(
    Output('prediction-content', 'children'),
    [Input('age', 'value'),
    Input('admission', 'value'),
    Input('diagnosis', 'value'),
    Input('procedure', 'value'),
    Input('surgical', 'value'),
    Input('payment', 'value'),
    Input('emergency_room', 'value')]
)

def predict(age, admission, diagnosis, procedure, surgical, payment, emergency_room):
    df = pd.DataFrame(
        columns=['Age Group',
                'Type of Admission',
                'APR DRG Code',
                'CCS Prodecure Code', 
                'APR Medical Surgical Description',
                'Payment Typology 1',
                'Emergency Department Indicator'],
        data=[[age, admission, diagnosis, procedure, surgical, payment, emergency_room]]
    )
    y_pred=pipeline.predict(df)[0]
    if (y_pred == 1):
        return 'Minor'
    elif (y_pred == 2):
        return 'Moderate'
    elif (y_pred == 3):
        return 'Major'
    else:
        return 'Extreme'





layout = dbc.Row([column1])