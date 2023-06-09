# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
sites = spacex_df['Launch Site'].unique()
n_launches = spacex_df.shape[0]

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',   
                                            options=[
                                                {'label': 'All Sites', 'value': 'ALL'},
                                                {'label': sites[0], 'value': sites[0]}, 
                                                {'label': sites[1], 'value': sites[1]},
                                                {'label': sites[2], 'value': sites[2]},
                                                {'label': sites[3], 'value': sites[3]}
                                            ],
                                            value='ALL',    # default dropdown value: all sites are selected
                                            placeholder = 'Select a Launch Site here',
                                            searchable=True # enable searching launch sites via keywords
                                            ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min = 0, max=10000, step=1000,    # in Kg 
                                                value=[min_payload, max_payload],
                                                marks={0:'0', 2500:'2500', 5000:'5000', 7500:'7500', 10000:'10000'}),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(filtered_df, 
                    values='class', 
                    names='Launch Site', 
                    title='Total Success Launches by Site')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df2 = spacex_df[spacex_df['Launch Site']==entered_site]['class']
        fig = px.pie(filtered_df2, 
                    values=filtered_df2.value_counts().values, 
                    names=filtered_df2.value_counts().index, 
                    title=f'Total Success Launches for site {entered_site}')
        return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), 
              Input(component_id="payload-slider", component_property="value")])

def get_scatter_plot(entered_site, slider_range):
    if entered_site == 'ALL': 
        low, high = slider_range
        mask = (spacex_df['Payload Mass (kg)'] > low) & (spacex_df['Payload Mass (kg)'] < high)
        fig = px.scatter(spacex_df[mask], x='Payload Mass (kg)', y='class', color="Booster Version Category",
                        title='Correlation between Payload and Success for all sites')
        return fig 
    else:
        filtered_df = spacex_df[spacex_df['Launch Site']==entered_site]
        low, high = slider_range
        mask = (filtered_df['Payload Mass (kg)'] > low) & (filtered_df['Payload Mass (kg)'] < high)
        fig = px.scatter(filtered_df[mask], x='Payload Mass (kg)', y='class', color="Booster Version Category",
                        title=f'Correlation between Payload and Success for {entered_site}')
        return fig 



# Run the app
if __name__ == '__main__':
    app.run_server()
