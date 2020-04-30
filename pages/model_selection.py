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
        
            ## Model Selection

            Having defined my target and evaluation metrics, I then set out to explore different types of models to determine which would return the highest evaluation metrics. As this is a classification problem, I chose to explore Random Forest, XGBoost and Support Vector Machine. Additionally, I explored two linear classification models, Logistic Regression and Linear Support Vector Machine. Through experimentation I determined that Random Forest gave me the best results.
            
            For more details on the results of my various models, please view the “Model Scores” page. 


            """
        ),
    ],
    # md=4,
)

layout = dbc.Row([column1])