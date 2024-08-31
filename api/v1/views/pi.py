"""recieves what is sent from the pi and stores in db
"""
from api.v1.views import app_views
from flask import request, jsonify
from models import storage
from models.dispensed import Dispensed
from models.deposit import Deposit

@app_views.route("/dispensed", methods=['POST'], strict_slashes=False)
def record_dispensed():
    """Records the milk dispensed by the machine into the database."""
    data = request.get_json()
    dispensed = Dispensed(
        initiation_id=data.get("initiation_id"),
        litres_dispensed=data.get("litres_dispensed"),
        status=data.get("status")
    )
    storage.new(dispensed)
    storage.save()
    return jsonify("dispensed recorded"), 201

@app_views.route("/deposited", methods=['POST'], strict_slashes=False)
def record_deposited():
    """Records the milk deposited into the machine into the database."""
    data = request.get_json()
    deposit = Deposit(
        litres_deposited=data.get("litres_deposited")
    )
    storage.new(deposit)
    storage.save()
    return jsonify("deposited recorded"), 201
