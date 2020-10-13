# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# Page layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Metrics

            As this is a classification problem, I chose to evaluate my model using two metrics: accuracy and the weighted average f1 score.
            - Accuracy tells you, out of the total number of predictions, how many of them were predicted correctly.
            - The f1 score evaluates the level of precision and recall for your model. Precision tells you, out of the total predictions for a specific class, how many of them were correct. Recall tells you, out of the total number of actual values for a specific target class, how many were correctly identified. Since this is a multi-class target, we use the average to evaluate how the model works across all categories. Additionally, because the target class is right skewed, the weighted score is used as it helps account for label imbalance. 
            
            """
        ),

    ],
)

column2 = dbc.Col(
    [
        dcc.Markdown(    
            """

            In the confusion matrix below, the columns are the predicted target class and the rows are the true target class labels. The diagonal starting with the yellow square in the upper left and going to the green square in the bottom right are all of the correct predictions. The other squares are where the model made an incorrect predication.
            - These values have been normalized by column so they represent the proportion of predictions for each class. 

            """ 
        ), 
        html.Div(
            html.Img(src='assets/confusion_matrix.png', className='img-fluid')
        )      
    ]
)

layout = dbc.Row([column1, column2])
