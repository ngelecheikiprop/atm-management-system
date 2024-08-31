"""gets the stats for her honour the dashboard
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def get_stats():
    """Fetches the aggregated statistics for the dashboard."""
    total_sales = storage.get_sum_of('Payment.amount')
    total_litres_dispensed = storage.get_sum_of('Dispensed.litres_dispensed')
    total_litres_deposited = storage.get_sum_of('Deposit.litres_deposited')
    litres_remaining = total_litres_deposited - total_litres_dispensed
    stats = {
        "total_sales": total_sales,
        "total_litres_dispensed": total_litres_dispensed,
        "total_litres_deposited": total_litres_deposited,
        "litres_remaining":litres_remaining
    }

    return jsonify(stats)

@app_views.route("/sales", methods=['GET'], strict_slashes=False)
def get_sales():
    """Fetches the sales data for the dashboard."""
    return jsonify(storage.getthetwo())

