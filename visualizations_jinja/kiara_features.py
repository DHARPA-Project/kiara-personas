from dash import html

def create_viz(height):
    
    kiara_features = html.Iframe(srcDoc=f"""
            <!DOCTYPE html>
            <meta charset="utf-8">
            <title>kiara-features</title>
            <link rel="stylesheet" type="text/css" href="../assets/viz/kiara-features/inspector.css">
            <head></head>
            <body>
            <script src="https://cdn.jsdelivr.net/npm/d3@6"></script>
            <script type="module">

            import define from "../assets/viz/kiara-features/index.js";
            import {{Runtime, Library, Inspector}} from "../assets/viz/kiara-features/runtime.js";


            const runtime = new Runtime();
            const main = runtime.module(define, name => {{

                if (name === "style") {{
                    return new Inspector(document.head)
                }} 

                if (name === "viewof kiaraFeats") {{   
                    var elem = document.createElement('div')
                    elem.setAttribute('id','chart')
                    document.body.appendChild(elem)
                    return new Inspector(document.querySelector("#chart"));
                }} 

                if (name === 'clicked') {{
                    return {{
                        fulfilled(value) {{ 
                            const clickedFeat = parent.document.getElementById('clicked-feat')

                            if (clickedFeat) {{
                                clickedFeat.value = value 
                                parent.document.getElementById('button-test').click();
                            }}

                            else {{
                                clickedFeat.value = "Kiara"
                            }}
                            

                            }},
                    }};
                }}
            }});

            
            </script>
            """,style={'width':'100%'},height=height)
        
       
        
    return kiara_features