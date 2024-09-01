from api.v1.views import app_views
from flask import request
from models import storage
from models.payments import Payment
from datetime import datetime
@app_views.route("/callback", methods=['POST'], strict_slashes=False)
def callback():
    """get payment data and store it in database
    """
    print("recieving data")
    data = request.get_json()
    # Extract relevant data
    callback_metadata = data['Body']['stkCallback']['CallbackMetadata']['Item']
    payment_info = {item.get('Name'): item.get('Value') for item in callback_metadata}
    # Create Payment object
    time_received_str = str(payment_info.get("TransactionDate"))
    time_format = "%Y%m%d%H%M%S"
    time_recieved = datetime.strptime(time_received_str, time_format)
    payment = Payment(
            phone_number=str(payment_info.get("PhoneNumber")),
            transaction_id=payment_info.get("MpesaReceiptNumber"),
            initiation_id=data['Body']['stkCallback']['CheckoutRequestID'],
            amount=int(payment_info.get("Amount")),
            time_received=time_recieved
            )
    storage.new(payment)
    storage.save()
    return "ok"


@app_views.route("/status", strict_slashes=False)
def get_status():
    return "ok"
