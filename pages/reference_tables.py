
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ### APR Diagnosis Related Group Codes
            """
        ),  

        html.Div(
            html.Img(src='assets/diagnosis_codes-1.png', className='img-fluid'),
        ), 

        html.Div(
            html.Img(src='assets/diagnosis_codes-2.png', className='img-fluid'),
        ),

        html.Div(
            html.Img(src='assets/diagnosis_codes-3.png', className='img-fluid'),
        ),

        html.Div(
            html.Img(src='assets/diagnosis_codes-4.png', className='img-fluid'),
        ),

        html.Div(
            html.Img(src='assets/diagnosis_codes-5.png', className='img-fluid'),
        ),

        html.Div(
            html.Img(src='assets/diagnosis_codes-6.png', className='img-fluid'),
        ),

        html.Div(
            html.Img(src='assets/diagnosis_codes-7.png', className='img-fluid'),
        ),

        html.Div(
            html.Img(src='assets/diagnosis_codes-8.png', className='img-fluid'),
        ),
    ],
    md=4,
)
column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            ### CCS Procedure Codes
            """
        ),

        html.Div(
            html.Img(src='assets/procedure_codes-1.png', className='img-fluid'),
        ),
        html.Div(
            html.Img(src='assets/procedure_codes-2.png', className='img-fluid'),
        ),  
        html.Div(
            html.Img(src='assets/procedure_codes-3.png', className='img-fluid'),
        ),  
        html.Div(
            html.Img(src='assets/procedure_codes-4.png', className='img-fluid'),
        ),  
        html.Div(
            html.Img(src='assets/procedure_codes-5.png', className='img-fluid'),
        ),  
        html.Div(
            html.Img(src='assets/procedure_codes-6.png', className='img-fluid'),
        ),         
    ]
)

layout = dbc.Row([column1, column2])