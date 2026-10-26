import azure.functions as func
import logging
import json

# Create the Azure Function App
app = func.FunctionApp()

# ------------------------------------------------------------------
# Mock data (pretending this is a database)
# Keys are media IDs
# Values are the details for each movie/TV show
# ------------------------------------------------------------------
media = {
    "1": {
        "title": "Interstellar",
        "type": "Movie",
        "year": 2014
    },
    "2": {
        "title": "Breaking Bad",
        "type": "TV Show",
        "year": 2008
    },
    "3": {
        "title": "The Dark Knight",
        "type": "Movie",
        "year": 2008
    },
    "4": {
        "title": "The Last of Us",
        "type": "TV Show",
        "year": 2023
    },
    "5": {
        "title": "Dune: Part Two",
        "type": "Movie",
        "year": 2024
    },
    "6": {
        "title": "Game of Thrones",
        "type": "TV Show",
        "year": 2011
    },
    "7": {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "type": "Movie",
        "year": 2001
    },
    "8": {
        "title": "Stranger Things",
        "type": "TV Show",
        "year": 2016
    }
}


# ------------------------------------------------------------------
# HTTP Trigger
# URL:
# http://localhost:7071/api/media?id=1
# ------------------------------------------------------------------
@app.route(route="media", auth_level=func.AuthLevel.ANONYMOUS)
def media_endpoint(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Media API request received")

    # --------------------------------------------------------------
    # STEP 1: Get the ID from the query string
    #
    # Power Automate equivalent:
    # Trigger -> Get value from request
    # --------------------------------------------------------------
    media_id = req.params.get("id")

    # --------------------------------------------------------------
    # STEP 2: Validation
    #
    # Power Automate equivalent:
    # Condition -> Is ID empty?
    # --------------------------------------------------------------
    if not media_id:
        return func.HttpResponse(
            "Media ID is required.",
            status_code=400
        )

    # --------------------------------------------------------------
    # STEP 3: Lookup media item
    #
    # Power Automate equivalent:
    # Get item from SharePoint / Dataverse / SQL
    # --------------------------------------------------------------
    item = media.get(media_id)

    # --------------------------------------------------------------
    # STEP 4: Validation
    #
    # Power Automate equivalent:
    # Condition -> Was item found?
    # --------------------------------------------------------------
    if not item:
        return func.HttpResponse(
            "Media item not found.",
            status_code=404
        )

    # --------------------------------------------------------------
    # STEP 5: Return successful response
    #
    # Power Automate equivalent:
    # Respond to HTTP request
    # --------------------------------------------------------------
    return func.HttpResponse(
        json.dumps(item),
        mimetype="application/json",
        status_code=200
        )


# HTTP Request
#     ↓
# Get id from query string
#     ↓
# Is id empty?
#  ├─ Yes → Return 400
#  └─ No
#       ↓
# Look up item in media dictionary
#       ↓
# Was item found?
#  ├─ No → Return 404
#  └─ Yes
#       ↓
# Return media details (200)