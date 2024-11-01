import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

#------------------------DATA------------------------

data_MCQ160F_nd_eda = pd.read_csv('data_MCQ160F_nd_eda.csv')
logistic_regression_results = pd.read_csv('results.csv')

target_column = 'Had_stroke'
data_MCQ160F_nd_eda[target_column].replace({1: 'Yes', 2: 'No'}, inplace=True)


def change_numeric_to_categorical_variables(data, col_names, start_column, end_column):
    data['Gender'].replace({1: 'Male', 2: 'Female'}, inplace=True)
    data['Have_diabetes'].replace({1: 'Yes', 2: 'No', 3: 'Borderline'}, inplace=True)
    data['Birth_country'].replace({1: 'USA', 2: 'Others'}, inplace=True)
    data['Marital_status'].replace({1: 'Married', 2: 'Widowed', 3: 'Divorced', 4: 'Separated', 5: 'Never married', 6: 'Living with partner',}, inplace=True)
    data['Annual_family_income'].replace({1: '0-4.99k', 2: '5-9k', 3: '10-14.99k', 4: '15-19.99k', 5: '20-24.99k', 6: '25-34.99k',
                                                                     7: '35-44.99k', 8: '45-54.99k', 9: '55-64.99k', 10: '65-74.99k', 12: '20k and over',
                                                                     13: 'under 20k', 14: '75-99.99k', 15: '100k and over'}, inplace=True)
    data['Race'].replace({1: 'Mexican American', 2: 'Other Hispanic', 3: 'Non-Hispanic White', 4: 'Non-Hispanic Black',
                                                      6: 'Non-Hispanic Asian', 7: 'Other Race'}, inplace=True)
    data['Education_level'].replace({1: 'Less than 9th grade', 2: '9-11th grade', 3: 'High school graduate', 4: 'Some college or AA degree',
                                                                5: 'College graduate or above'}, inplace=True)
    data['Work_type_last_week'].replace({1: 'Working', 2: 'Working (not at work)', 3: 'Looking for work', 4: 'Not working'}, inplace=True)
    for col in col_names[start_column:end_column]:
            data[col].replace({1: 'Yes', 2: 'No'}, inplace=True)
    return data


col_names = data_MCQ160F_nd_eda.columns.values
data_MCQ160F_nd_eda = change_numeric_to_categorical_variables(data_MCQ160F_nd_eda, col_names, 1, 10)


# Excluding NA values

data_MCQ160F_noNA = data_MCQ160F_nd_eda.dropna()


#------------------------PLOTS FEATURES------------------------

features_count_plots = ['Had_stroke', 'Gender', 'Had_high_blood_pressure', 'Have_high_cholesterol', 'Have_diabetes_close_relative', 'Have_diabetes',
                        'Limited_work_can_do', 'Moderate_work_activity', 'Moderate_recreational_activities', 'Walk_or_bicycle',
                        'Birth_country', 'Work_type_last_week', 'Marital_status', 'Annual_family_income', 'Race', 'Education_level', 'Age_group']
numerical_features = ['Minutes_sedentary_activity', 'Creatinine_refrigerated_serum', 'Age_at_screening']
facet_columns = ['Limited_work_can_do', 'Had_high_blood_pressure', 'Have_high_cholesterol']
physical_activities = ['Work_type_last_week', 'Walk_or_bicycle', 'Moderate_recreational_activities', 'Moderate_work_activity']

Work_type_last_week = ['Looking for work','Not working','Working','Working (not at work)']
looking_for_work = 2
not_working = 8
working = 1
working_not_at_work = 2
Walk_or_bicycle = ['Walk or bicycle', "Do not walk or bicycle"]
Walk_or_bicycle_Yes = 2
Walk_or_bicycle_No = 4
Moderate_recreational_activities = ['Do recreation activities', "Do not do recreational activities"]
Moderate_recreational_activities_Yes = 2
Moderate_recreational_activities_No = 5
Moderate_work_activity = ['Do moderate work activity', "Do not do moderate work activity"]
Moderate_work_activity_Yes = 3
Moderate_work_activity_No = 4


#------------------------DASHBOARD------------------------

app = dash.Dash()


app.layout = html.Div(children=[
    html.H1(
        children='Project Dashboard',
        style={
        'textAlign': 'center'
        }
    ),
    html.H2(children='Stroke Findings',
        style={
        'textAlign': 'center'
        }
    ),
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='xaxis',
                    options=[{'label': i, 'value': i} for i in features_count_plots],
                    value='Had_stroke'
                )],
                style={'width': '48%', 'display': 'inline-block'}
            ),
            dcc.Graph(id='feature-graphic')
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='xaxis2',
                    options=[{'label': i, 'value': i} for i in features_count_plots],
                    value='Age_group'
                )],
                style={'width': '48%', 'display': 'inline-block'}
            ),
            dcc.Graph(id='feature-graphic2')
        ],
        style={'width': '48%', 'align': 'right', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='numerical_hist1',
                figure={
                    'data':[
                        go.Histogram(
                            x=data_MCQ160F_nd_eda[data_MCQ160F_nd_eda['Had_stroke']=="Yes"]['Minutes_sedentary_activity'],
                            opacity=0.75,
                            name='Had stroke',
                            nbinsx=20
                        ),
                        go.Histogram(
                            x=data_MCQ160F_nd_eda[data_MCQ160F_nd_eda['Had_stroke']=="No"]['Minutes_sedentary_activity'],
                            opacity=0.75,
                            name='Did not have stroke',
                            nbinsx=20
                        ),        
                    ],
                    'layout': go.Layout(title="Minutes sedentary activity by stroke class")
                })
            ],
        style={'width': '48%', 'display': 'inline-block'}
        ),
        html.Div([
            dcc.Graph(
                id='numerical_hist2',
                figure={
                    'data':[
                        go.Histogram(
                            x=data_MCQ160F_nd_eda[data_MCQ160F_nd_eda['Had_stroke']=="Yes"]['Creatinine_refrigerated_serum'],
                            opacity=0.75,
                            name='Had stroke',
                            nbinsx=20
                        ),
                        go.Histogram(
                            x=data_MCQ160F_nd_eda[data_MCQ160F_nd_eda['Had_stroke']=="No"]['Creatinine_refrigerated_serum'],
                            opacity=0.75,
                            name='Did not have stroke',
                            nbinsx=20
                        ),        
                    ],
                    'layout': go.Layout(title="Creatinine refrigerated serum (mg/dL) by stroke class")
                })
            ],
        style={'width': '48%', 'align': 'right', 'display': 'inline-block'},
        ),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='xaxis3',
                    options=[{'label': i, 'value': i} for i in numerical_features],
                    value='Creatinine_refrigerated_serum'                    
                )
            ],
            style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id='yaxis3',
                    options=[{'label': i, 'value': i} for i in numerical_features],
                    value='Age_at_screening'
                )
            ],
            style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id='facet_col3',
                    options=[{'label': i, 'value': i} for i in facet_columns],
                    value='Limited_work_can_do'
                )
            ],
            style={'width': '48%', 'display': 'inline-block'}),
            dcc.Graph(id='feature-graphic3')
        ]),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='xaxis4',
                    options=[{'label': i, 'value': i} for i in physical_activities],
                    value='Work_type_last_week'
                )],
                style={'width': '100%', 'display': 'inline-block'}
            ),
            dcc.Graph(id='feature-graphic4')
        ],
        style={'width': '100%', 'display': 'inline-block'}),

        html.Div([
            dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in logistic_regression_results.columns
        ],
        data=logistic_regression_results.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 20,
        ),
            html.Div(id='datatable-interactivity-container')
        ])
    ])
])

@app.callback(
    [Output('feature-graphic', 'figure')],
    [Input('xaxis', 'value')]
)
def update_graph(xaxis_name):
    return [
        px.histogram(data_MCQ160F_nd_eda, x=xaxis_name, title='{} variable values count'.format(xaxis_name), category_orders={
            "Annual_family_income": ['under 20k', '20k and over','0-4.99k', '5-9k', '10-14.99k', '15-19.99k', '20-24.99k', '25-34.99k',
                '35-44.99k', '45-54.99k', '55-64.99k', '65-74.99k', '75-99.99k', '100k and over'],
            "Education_level": ['Less than 9th grade', '9-11th grade', 'High school graduate', 'Some college or AA degree', 'College graduate or above'],
            "Age_group": ["20-30", "31-40", "41-50", "51-60", "61-70", "Greater than 70"],
        })
    ]

@app.callback(
    [Output('feature-graphic2', 'figure')],
    [Input('xaxis2', 'value')]
)
def update_graph(xaxis_name):
    return [
        px.histogram(data_MCQ160F_nd_eda, x=xaxis_name, title='{} variable values count'.format(xaxis_name), category_orders={
            "Annual_family_income": ['under 20k', '20k and over','0-4.99k', '5-9k', '10-14.99k', '15-19.99k', '20-24.99k', '25-34.99k',
                '35-44.99k', '45-54.99k', '55-64.99k', '65-74.99k', '75-99.99k', '100k and over'],
            "Education_level": ['Less than 9th grade', '9-11th grade', 'High school graduate', 'Some college or AA degree', 'College graduate or above'],
            "Age_group": ["20-30", "31-40", "41-50", "51-60", "61-70", "Greater than 70"],
        })
    ]

@app.callback(
    [Output('feature-graphic3', 'figure')],
    [Input('xaxis3', 'value')],
    [Input('yaxis3', 'value')],
    [Input('facet_col3', 'value')]
)
def update_graph(xaxis_name, yaxis_name, facet_col):
    return [px.scatter(data_MCQ160F_noNA, x=xaxis_name, y=yaxis_name, color="Had_stroke", facet_col=facet_col, opacity=0.75, title='{} vs {} per {} category'.format(xaxis_name, yaxis_name, facet_col))]

@app.callback(
    [Output('feature-graphic4', 'figure')],
    [Input('xaxis4', 'value')]
)
def update_graph(xaxis_name):
    if xaxis_name == 'Work_type_last_week':
        trace1 = go.Bar(x=Work_type_last_week, y=[looking_for_work, not_working, working, working_not_at_work],
            base=0,
            marker_color='crimson',
            name='Had stroke')
        trace2 = go.Bar(x=Work_type_last_week, y=[100 - looking_for_work, 100 - not_working, 100 - working, 100 - working_not_at_work],
            base=[-(100 - looking_for_work), -(100 - not_working), -(100 - working), -(100 - working_not_at_work)],
            marker_color='lightslategrey',
            name='Did not have stroke')
    if xaxis_name == 'Walk_or_bicycle':
        trace1 = go.Bar(x=Walk_or_bicycle, y=[Walk_or_bicycle_Yes, Walk_or_bicycle_No],
            base=0,
            marker_color='crimson',
            name='Had stroke')
        trace2 = go.Bar(x=Walk_or_bicycle, y=[100 - Walk_or_bicycle_Yes, 100 - Walk_or_bicycle_No],
            base=[-(100 - Walk_or_bicycle_Yes), -(100 - Walk_or_bicycle_No)],
            marker_color='lightslategrey',
            name='Did not have stroke')
    if xaxis_name == 'Moderate_recreational_activities':
        trace1 = go.Bar(x=Moderate_recreational_activities, y=[Moderate_recreational_activities_Yes, Moderate_recreational_activities_No],
            base=0,
            marker_color='crimson',
            name='Had stroke')
        trace2 = go.Bar(x=Moderate_recreational_activities, y=[100 - Moderate_recreational_activities_Yes, 100 - Moderate_recreational_activities_No],
            base=[-(100 - Moderate_recreational_activities_Yes), -(100 - Moderate_recreational_activities_No)],
            marker_color='lightslategrey',
            name='Did not have stroke')
    if xaxis_name == 'Moderate_work_activity':
        trace1 = go.Bar(x=Moderate_work_activity, y=[Moderate_work_activity_Yes, Moderate_work_activity_No],
            base=0,
            marker_color='crimson',
            name='Had stroke')
        trace2 = go.Bar(x=Moderate_work_activity, y=[100 - Moderate_work_activity_Yes, 100 - Moderate_work_activity_No],
            base=[-(100 - Moderate_work_activity_Yes), -(100 - Moderate_work_activity_No)],
            marker_color='lightslategrey',
            name='Did not have stroke')
    layout = go.Layout(title="Distribution of Stroke Class per {} Class".format(xaxis_name))
    return [go.Figure(data=[trace1, trace2], layout=layout)]

@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    Input('datatable-interactivity', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@app.callback(
    Output('datatable-interactivity-container', "children"),
    Input('datatable-interactivity', "derived_virtual_data"),
    Input('datatable-interactivity', "derived_virtual_selected_rows"))
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = logistic_regression_results if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["Feature"],
                        "y": dff[column],
                        "type": "bar",
                        "marker": {"color": colors},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": column}
                    },
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )
    for column in ["Odds Ratio", "2.5% CI", "97.5% CI", "p-values"] if column in dff
    ]


if __name__ == '__main__':
    app.run_server(port=4567)
