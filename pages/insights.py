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

            Besides the predictive capabilities of the model, we can also draw further insights by looking at how the features interact with the model and with each other. To begin with let’s look at the permutation importances for the final model.

            """
        ),

        html.Div(
            html.Img(src='assets/final_permutations.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            As mentioned before, this shows us the weight of effect that each feature has on the model’s predictions. This shows us that 'age group' has the largest impact on categorizing the risk of mortality but tells us nothing of how it effects it. The partial dependence plot below shows us exactly how belonging to each age group effects the probability of being categorized for each risk class. 

            """
        ),

        html.Div(
            html.Img(src='assets/pdp_1_variable.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Let’s examine the first subplot for 'minor risk' (upper left). The y-value represents the effect the age group has on the probability of being assigned a minor risk of mortality. We can see, as age increases the probability that you will be assigned a risk category of ‘minor’ decreases. This is reflected in the other three plots. They represent 'moderate', 'major' and 'extreme' risk of mortality. For each of them, probability of being assigned that risk class increases with age. 

            Again, the below graph is indicating how features are interacting with the model and its predictions. However, this time it shows how two features are interacting to influence the mortality risk prediciton. The graph below looks at age group and whether the admittance was medical or surgical, and returns probabilities of being designated 'minor', 'moderate', 'major' or 'extreme' risk of mortality. 

            """
        ),

        html.Div(
            html.Img(src='assets/pdp_2_variable.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Now let's examine the plot for 'minor risk' of mortality (upper left). We can see that if the patient is young (0 to 17) and admitted to the hospital for a medical procedure rather than surgery, they have an 80% chance of being classified as having a 'minor risk' of mortality. If they are admitted to the hospital for surgery, then the probability of being predicted as a 'minor risk' of mortality drops to 64% while it increases for the higher risk levels. Those who are in the oldest age group (70 or older) and are at the hospital for medical admittance only have a 25% chance of being categorized as a 'minor risk'. 
            From these partial dependence plots we can see that the risk increases both with age, as well as with a surgical admittance versus a medical admittance.  
            Finally, we can look at one individual in our test data to see how each feature effected our final prediction.

            **Take a random patient from our test data:**
            """
        ),

        html.Div(
            html.Img(src='assets/test_patient.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            Using Shapley values, we can look at how the model predicted the probability of each class, and then selected the class with the highest probability as its prediction. The red arrows are the features that push the probability for that class higher, and the blue arrows push the probability lower. The length of the colored bar is the amount of impact the feature had on influencing the prediction. 

            __Shapley values for Minor Risk of Mortality:__
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_minor.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            __Shapley values for Moderate Risk of Mortality:__ 
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_moderate.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            __Shapley values for Major Risk of Mortality:__ 
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_major.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            __Shapley values for Extreme Risk of Mortality:__
            """
        ),

        html.Div(
            html.Img(src='assets/shapley_extreme.png', className='img-fluid')
        ),

        dcc.Markdown(
            """
            For this individual, the class with the highest probability (0.72) was the 'minor risk of mortality'. Therefore, the model predicted that this specific patient would have a 'minor risk of mortality'. This prediction matched the actual records, so in this instance the model predicted correctly.
            You can tell that the model arrived at this correct prediction because the indivudual was young, paid with Medicaid, was a medical admittance and did not undergo a procedure (CCS Procedure 0). Some features that lowered the probability of it being a 'minor risk' were; that it was an emergency department admittance and that it was a digestive system diagnosis (APR DRG 254).
            
            """
        ),
    ],
)

layout = dbc.Row([column1])
