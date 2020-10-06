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
        
            ## Feature Selection

            The Hospital Inpatient dataset I used had 34 columns. In my final model I used only 7 of these as features. Through exploratory data analysis, I eliminated unique identifiers and redundant information. For example, for each medical code there was an accompanying description. While useful for interrupting results, this was redundant for my model. Keeping in mind that I wanted to be implemented this model by health care providers early in the treatment process, I also eliminated columns such as ‘Length of Stay’ and ‘Total Costs’ as this data is not available until the patient has completed treatment. I also eliminated the column ‘Severity of Illness’ as this had the potential for data leakage. Data leakage is when a feature you include in your model is directly related to the target. This allows the model to ‘cheat’ by learning about the target from this feature. In this case, the severity of the illness is directly related to their risk of mortality. It makes sense that if a patient’s condition is worse, their risk of mortality is higher. 59% of the time, the severity of illness rating was the exact same as the risk of mortality rating. 

            After cleaning the remaining data, I built and ran a model using the remaining features and viewed the permutation importances. In short, permutation importances tell you the weight that a specific feature has on the predictive ability of the model. Features with higher weights are more helpful in making accurate predictions, while those with lower weights are less effective. Features can even have negative weights, meaning they are hurting the predictive capabilities of the model.
            """
        )
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """

            I used the permutation importances below to determine which features to include in my final model. 


            """
        ),
        html.Div(
            html.Img(src='assets/all_permutations.png', className='img-fluid'), 
        ),


        
        dcc.Markdown(
            """
            **Based on the results of the permutation importances and identifying that CCS Diagnosis Code and APR MDC Code were already captured by CCS Procedure Code and APR DRG Code respectfully, I decided to use the following 7 features:

                    * Age Group
                    * Type of Admission
                    * APR DRG Code
                    * CCS Procedure Code
                    * APR Medical Surgical Description
                    * Payment Typology 1
                    * Emergency Department Indicator

            """
        ),
    ]
)

layout = dbc.Row([column1, column2])
