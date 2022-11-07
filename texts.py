from dash import html
import dash_bootstrap_components as dbc

kiara = html.Div(children=[
    html.P("Kiara is a data orchestration engine that uses a modular approach to let users re-use tried and tested data pipelines, as well as create new ones from existing building blocks."),
    html.H5("Github Repo:",className="mb-1"),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('Kiara - https://github.com/DHARPA-Project/kiara', href="https://github.com/DHARPA-Project/kiara"),
    ], flush=True
    ),

     dbc.CardImg(src="static/images/kiara.png", top=True),
])

modules_users = html.Div(children=[
    html.P("Modules users are Kiara users who may not be comfortable with coding, but who are able to use the command line. They can access Kiara functionalities via the command-line interface, create pipelines with existing Kiara modules, and store processed data in the data registry."),
        html.Br(),
    html.H5("Tutorials",className="mb-1"),
    html.Br(),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('"Getting started with Kiara": https://dharpa.org/kiara.documentation/latest/usage/getting_started/', href="https://dharpa.org/kiara.documentation/latest/usage/getting_started/"),
        dbc.ListGroupItem('"Assembling a pipeline": https://dharpa.org/kiara.documentation/latest/extending_kiara/pipelines/assemble_pipelines/', href="https://dharpa.org/kiara.documentation/latest/extending_kiara/pipelines/assemble_pipelines/"),
    ], flush=True
    ),

    html.Br(),

    dbc.CardImg(src="static/images/modules_users.png", top=True),
])

modules_creators = html.Div(children=[
    html.P("Modules creators are Kiara users who are comfortable with coding. In addition to the functionalities available to workflow creators, they can create their own modules, by using a plugin project template."),
        html.Br(),
    html.H5("Tutorials:",className="mb-1"),
    html.Br(),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('"Creating modules": https://dharpa.org/kiara.documentation/latest/extending_kiara/creating_modules/', href="https://dharpa.org/kiara.documentation/latest/extending_kiara/creating_modules/"),
        dbc.ListGroupItem('"Assembling a pipeline": https://dharpa.org/kiara.documentation/latest/extending_kiara/pipelines/assemble_pipelines/', href="https://dharpa.org/kiara.documentation/latest/extending_kiara/pipelines/assemble_pipelines/"),
    ], flush=True
    ),

    html.Br(),
    dbc.CardImg(src="static/images/modules_creators.png", top=True),
])

app_creators = html.Div(children=[
    html.P("App creators are module creators who use low code front-end apps such as Streamlit or Dash. They can use Kiara as the pipeline execution tool for their projects via Kiara Python API."),
        html.Br(),
    html.H5("Documentation:",className="mb-1"),
    html.Br(),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('"Kiara Python API": https://dharpa.org/kiara/latest/reference/kiara/interfaces/python_api/__init__/', href="https://dharpa.org/kiara/latest/reference/kiara/interfaces/python_api/__init__/"),
    ], flush=True
    ),

    html.Br(),
    dbc.CardImg(src="static/images/app_creators.png", top=True),
])

fe_dev = html.Div(children=[
    html.P("Front-End developers can request Kiara REST API and retrieve responses formatted in JSON. Additionally, the workflow API, currently under development, is a tool enabling them to explore the possibilities in terms of Kiara workflow sessions."),
        html.Br(),
    html.H5("Documentation:",className="mb-1"),
    html.Br(),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('"Kiara Workflow Object": https://dharpa.org/kiara.documentation/latest/workflows/topic_modeling/', href="https://dharpa.org/kiara.documentation/latest/workflows/topic_modeling/"),
    ], flush=True
    ),

    html.Br(),
    dbc.CardImg(src="static/images/fe_dev.png", top=True),
])

cli = html.Div(children=[
    html.P("Operations can be performed via the command line, such as viewing the available modules and pipelines, and running them."),
    html.Br(),
    html.Br(),
    dbc.CardImg(src="static/images/cli_2.png", top=True),
    html.Br(),
    dbc.CardImg(src="static/images/cli_3.png", top=True),
])

data_registry = html.Div(children=[
    html.P("The data registry enables to store data locally. It is architectured to capture information rich metadata, such as lineage."),
    html.Br(),
    html.Br(),
    dbc.CardImg(src="static/images/data_registry.png", top=True),
])




texts_keys = {
    "Kiara": kiara,
    "Kiara Personas": kiara,
    "Modules Pipelines Users": modules_users,
    "Modules Pipelines Creators": modules_creators,
    "Pipeline-Apps Creators": app_creators,
    "Front-End Developers": fe_dev,
    "CLI": cli,
    "Data Registry": data_registry
}
