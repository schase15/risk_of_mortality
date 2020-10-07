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
        
            ## Model scores:

            After cleaning my data and selecting my features *(for more on feature selection please see the “Feature Selection” page)* I split my data into training, validation and test datasets. I started by running a baseline model to determine the null accuracy and f1 score. That is, the evaluation scores if we were to guess that every patient had a classification of minor risk of mortality (the most frequent target class). 


            With a baseline score to beat, I trained several different types of models to see which type resulted in the best scores. The different models and scores are posted to the right. 
            
            #### To see the raw code including hyperparameter tuning, please visit my GitHub repository linked below. 

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """

            ### Baseline:

                - Accuracy:                       0.57 
                - Weighted Average f1 score:      0.41

            Logistic Regression:

                - Accuracy:                       0.60
                - Weighted Average f1 score:      0.55

            Linear Support Vector Machine:

                - Accuracy:                       0.57
                - Weighted Average f1 score:      0.49

            Support Vector Classification:

                - Accuracy:                       0.64
                - Weighted Average f1 score:      0.60

            XGBoost:

                - Accuracy:                       0.66
                - Weighted Average f1 score:      0.62

            Random Forest:

                - Accuracy:                       0.69 
                - Weighted Average f1 score:      0.68
            """
        ),
    ]
)

column3 = dbc.Col(
    [
        dcc.Markdown(
            """
            ### Final test data:

            As Random Forest gave me the best validation scores, I used that to predict my test data.

            The final resulting evaluation scores are below:
            """
        ),
        html.Div(
            html.Img(src='assets/test_score.png', className='img-fluid')
        )
    ]
)

layout = dbc.Row([column1, column2, column3])
