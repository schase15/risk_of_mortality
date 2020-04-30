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
        
            ## Insights

            Besides simply the predictive capabilities of the model, we can also draw further insights by looking at how the features interact with the model and with each other. To begin with let’s look at the permutation importances for the final model.

            """
        ),

        html.Div(
            html.Img(src='assets/final_permutations.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            As mentioned before, this shows us the weight of effect that each feature has on the model’s predictions. This shows us that age group has the largest impact on categorizing the risk of mortality but tells us nothing of how it effects it. The partial dependence plot below shows us exactly how belonging to each age group effects the probability of being categorized for each risk class. 

            """
        ),

        html.Div(
            html.Img(src='assets/pdp_1_variable.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Let’s examine the first subplot for minor risk (upper left). The y-value represents the effect the age group has on the probability of being assigned a minor risk of mortality. We can see, as age increases the probability that you will be assigned a risk category of ‘minor’ decreases. This is reflected in the other three plots. They represent moderate, major and extreme risk of mortality. For each of them, probability of being assigned that risk class increases with age. 

            Again, the below graph is indicating how features are interacting with the model and its predictions. However, this time it shows how two features are interacting. The graph below looks at age group and whether the admittance was medical or surgical, and returns probabilities of being designated minor, moderate, major or extreme risk of mortality. 

            """
        ),

        html.Div(
            html.Img(src='assets/pdp_2_variable.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Looking at the plot for minor risk of mortality (upper left), we see that if the patient is young (0 to 17) and there for a medical procedure rather than surgery, they have an 80% chance of being classified as having a minor risk of mortality. Those who are in the oldest age group (70 or older), only have a 25% chance of being categorized as a minor risk. The older age group has a higher probability of being categorized as moderate (35%) or major (31%). 

            Finally, we can look at how each feature effected our final prediction for an individual in our test data. 

            Take a random patient from our test data:
            """
        ),

        html.Div(
            html.Img(src='assets/test_patient.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Using Shapley values, we can look at how the model predicted the probability of each class, and then selected the class with the highest probability as its prediction. The red arrows are the features that push the probability higher, and the blue classes push the probability lower. The length of the colored bar is the amount of impact the feature had on the probability. 

            Shapley values for Minor Risk of Mortality:
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_minor.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Shapley values for Moderate Risk of Mortality: 
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_moderate.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Shapley values for Major Risk of Mortality: 
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_major.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Shapley values for Extreme Risk of Mortality: 
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_extreme.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            In this case class with the highest probability (0.72) was the minor risk of mortality. Therefore, the model predicted that this specific patient would have a minor risk of mortality. This was also the case when we look at the actual records, so in this instance the model predicted correctly. 
            
            """
        ),
    ],
)

layout = dbc.Row([column1])