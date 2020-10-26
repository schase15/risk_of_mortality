### Dash web application that predicts a patient's risk of mortality based on diagnosis and other metrics available early in the patient intake process.

This application uses a trained random forest model to predict the Risk of Mortality for a specific patient. The model takes the following input and returns a prediction of four risk levels.

**Input**:
- Age Group
- Type of Admission
- APR DRG Code
- CCS Procedure Code
- APR Medical Surgical Description
- Payment Typology 1
- Emergency Department Indicator

**Output**
Risk of Mortality:
- Minor
- Moderate
- Major
- Extreme

The `Build Week 2` [notebook](/notebooks/'Build Week 2.ipynb') includes the code used to create and test the final model as well as code exploring various other model types and interations.

The data used to train this model can be found on the New York State Health Department's website, [here](https://health.data.ny.gov/dataset/Hospital-Inpatient-Discharges-SPARCS-De-Identified/22g3-z7e7)

Read more on the accompanying blog post: [Modeling to Predict Patient's Risk of Mortality](http://steventchase.com/2020-05-01-risk-of-mortality/)

Visit the application website to predict your patient's risk: [Here](https://risk-of-mortality.herokuapp.com/)
