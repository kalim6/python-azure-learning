import azure.functions as func
import datetime as dt
import json
import logging

app = func.FunctionApp()

@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    team = req.params.get('team')
    time = dt.datetime.now().strftime("%H:%M")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
        f"Hello, {name}. This HTTP triggered function executed successfully."
        f"\nCurrent time: {time}"
        f"\nFrom the team {team}"
    )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )