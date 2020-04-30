# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Determine the Risk of Mortality for Your Patient

            Using basic diagnostic information gathered early in the treatment process, determine the risk of mortality for your particular patient.
            
            Having an accurate prediction of risk will allow you to prioritize higher risk patient and allocate hospital resources more effectively. 

            """
        ),
        dcc.Link(dbc.Button('Predict Risk', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Div(
            html.Img(src='assets/hospital-room.png', className= 'img-fluid')
        )
    ]
)

layout = dbc.Row([column1, column2])
