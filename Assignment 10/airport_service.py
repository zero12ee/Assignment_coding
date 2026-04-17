from flask import Flask, Response
import json

app = Flask(__name__)

airports = {
    "LFLL": {"name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
    "KJFK": {"name": "John F. Kennedy International Airport", "city": "New York", "country": "US"}
}

@app.route("/airport/<icao>")
def airport_info(icao):
    airport = airports.get(icao.upper())
    if airport:
        result = {"icao": icao.upper(), **airport}
        return json.dumps(result)
    else:
        error = {"error": "Airport not found"}
        return json.dumps(error), 404

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
