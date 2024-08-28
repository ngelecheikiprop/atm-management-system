import os
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1*":{"origins":"*"}})

@app.teardown_appcontext
def teardown_appcontext(code):
    """when its all said and done
    """
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"error":"Not found"}), 404)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
