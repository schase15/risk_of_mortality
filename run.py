# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predictions, insights, target, evaluation_scores, metrics, model_selection, feature_selection

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Patient Risk of Mortality',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Target', href='/target', className='nav-link')), 
        dbc.NavItem(dcc.Link('Evaluation Metrics', href='/metrics', className='nav-link')),
        dbc.NavItem(dcc.Link('Model Selection', href='/model_selection', className='nav-link')),
        dbc.NavItem(dcc.Link('Model Scores', href='/evaluation_scores', className='nav-link')),
        dbc.NavItem(dcc.Link('Feature Selection', href='/feature_selection', className='nav-link')),
        dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
    ],
    sticky='top',
    color='dark', 
    light=False, 
    dark=True
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Steven Chase', className='mr-2'), 
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:schase15@gmail.com'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/schase15/Build-Week-2'), 
#                     html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/<you>/'), 
#                     html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/<you>'), 
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/target':
        return target.layout
    elif pathname == '/metrics':
        return metrics.layout
    elif pathname == '/model_selection':
        return model_selection.layout
    elif pathname == '/evaluation_scores':
        return evaluation_scores.layout
    elif pathname == '/feature_selection':
        return feature_selection.layout
    elif pathname == '/insights':
        return insights.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)
