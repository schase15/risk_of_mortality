import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Evaluation metrics/ model scores:

            After cleaning my data and selecting my features (for more on feature selection please see the “Feature Selection” page) I split my data into training, validation and test datasets. I started by running a baseline model to determine the null accuracy and f1 score. That is, the evaluation scores if we were to guess that every patient had a classification of minor risk of mortality (the most frequent target class). 

            Baseline:


            With a baseline score to beat, I trained several different types of models to see which type resulted in the best scores. The different models and scores are posted below. To see the raw code including hyperparameter tuning, please visit my GitHub page linked below. 

            Random Forest:


            XGBoost

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col([])

layout = dbc.Row([column1, column2])