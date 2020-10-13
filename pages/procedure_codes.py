import dash
import pandas
import os.path
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Imports from this application
from app import app

# Path to dataset
path = os.path.join(os.path.dirname(__file__), '../assets')
procedure_codes = pd.read_csv(path + '/procedure_codes.csv')

# Page layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ### CCS Procedure Codes
            """
        ),

        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in procedure_codes.columns],
            data=procedure_codes.to_dict('records'),
        )         
    ]
)

layout = dbc.Row([column1])