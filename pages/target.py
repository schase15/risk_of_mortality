
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
        
            ## Target

            While working in a hospital, there is always a lot of pressure to make prudent decisions. Afterall, the decision you make could be the difference between life and death for your patient. Ideally each patient would receive the full resources of the hospital immediately upon being admitted. However, realistically this is not the case. Hospitals have limited resources and doctors can only be at one place at a time. This requires that a level of urgency is assigned to patients so that more patients can be successfully treated. Those with critical conditions must be seen and treated immediately, while those who can afford to, must wait. In common practice this ranking of urgency is called triage. 

            My goal was to create a model that can take patient information that is available early in the admittance process and return a risk of mortality. With an accurate ranking of this risk, healthcare providers have a crucial piece of information as to which patients they need to prioritize. 

            To accomplish this, I used the 2017 Hospital Inpatient Discharge dataset for the State of New York. This dataset had a wealth of information about every patient who was admitted to a hospital in the State of New York in 2017. Included was a column called “Risk of Mortality” which I set as my target while I trained my model. Risk of Mortality had the target classes of minor, moderate, major and extreme which I label encoded to the ordinal rank of 1, 2, 3 and 4 respectively. As we see below, the distribution of risk of mortality across the patients is skewed right with the majority of inpatients having a minor risk of mortality. To accomplish this, I used the 2017 Hospital Inpatient Discharge dataset for the State of New York. This dataset had a wealth of information about every patient who was admitted to a hospital in the State of New York in 2017. Included was a column called “Risk of Mortality” which I set as my target while I trained my model. Risk of Mortality had the target classes of minor, moderate, major and extreme which I label encoded to the ordinal rank of 1, 2, 3 and 4 respectively. As we see below, the distribution of risk of mortality across the patients is skewed right with the majority of inpatients having a minor risk of mortality. 


            """
        ),
    ],
    md=4,
)

column2 = dbc.Col([])

layout = dbc.Row([column1, column2])