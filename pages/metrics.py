# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Metrics

            As this is a classification problem, trying to predict a category, I chose to evaluate my model using accuracy and the weighted average f1 score. Accuracy tells you, out of the total number of predictions, how many of them were predicted correctly. The f1 score evaluates the level of precision and recall for your model. Precision tells you, out of the total predictions for a specific class, how many of them were correct. Recall tells you, out of the total number of actual values for a specific target class, how many were correctly identified. Since this is a multi-class target, we use the average to evaluate how the model works across all categories. Additionally, because the target class is right skewed, the weighted score is used as it helps account for label imbalance. 


            """
        ),

    ],
)

layout = dbc.Row([column1])