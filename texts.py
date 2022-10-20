from dash import html
import dash_bootstrap_components as dbc

workflow_creators = html.Div(children=[
    html.P("Workflow creators are Kiara users who may or may not be comfortable with coding. They can access Kiara functionalities via the command-line interface, create pipelines with existing Kiara modules, and store processed data in the data registry."),
        html.Br(),
    html.H5("Tutorials:",className="mb-1"),
    html.Br(),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('"Getting started with Kiara"', href="https://dharpa.org/kiara.documentation/latest/usage/getting_started/"),
        dbc.ListGroupItem('"Assembling a pipeline"', href="https://dharpa.org/kiara.documentation/latest/extending_kiara/pipelines/assemble_pipelines/"),
    ], flush=True
    ),
])

modules_creators = html.Div(children=[
    html.P("Modules creators are Kiara users who are comfortable with coding. In addition to the functionalities available to workflow creators, they can create their own modules, by using a plugin project template."),
        html.Br(),
    html.H5("Tutorials:",className="mb-1"),
    html.Br(),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('"Writing your own kiara module"', href="https://dharpa.org/kiara.documentation/latest/extending_kiara/creating_modules/the_basics/#setting-up-development-environment"),
        dbc.ListGroupItem('"Assembling a pipeline"', href="https://dharpa.org/kiara.documentation/latest/extending_kiara/pipelines/assemble_pipelines/"),
    ], flush=True
    ),
])

kiara = html.Div(children=[
    html.P("Kiara is a data orchestration engine that uses a modular approach to let users re-use tried and tested data pipelines, as well as create new ones from existing building blocks."),
    html.H5("Github Repo:",className="mb-1"),

    dbc.ListGroup(
    [
        dbc.ListGroupItem('Kiara', href="https://github.com/DHARPA-Project/kiara"),
    ], flush=True
    ),
])

texts_keys = {
    "Kiara": kiara,
    "Workflow Creators": workflow_creators,
    "Modules Creators": modules_creators,
}