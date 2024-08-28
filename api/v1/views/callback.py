from api.v1.views import app_views
from flask import request
from models import storage
from models.payments import Payment

@app_views.route("/callback", methods=['POST'], strict_slashes=False)
def callback():
    """get data and store
    """
    """
    get the data in varibales
    make payment object
    new 
    save
    """
    print("recieving data")
    data = request.get_json()
    # Extract relevant data
    callback_metadata = data['Body']['stkCallback']['CallbackMetadata']['Item']
    payment_info = {item['Name']: item['Value'] for item in callback_metadata}
    # Create Payment object
    payment = Payment(
            phone_number=str(payment_info.get("PhoneNumber")),
            transaction_id=payment_info.get("MpesaReceiptNumber"),
            initiation_id=data['Body']['stkCallback']['CheckoutRequestID'],
            amount=int(payment_info.get("Amount")),
            time_received=datetime.fromtimestamp(payment_info.get("TransactionDate") / 1000.0)
            )
    storage.new(payment)
    storage.save()
    return "ok"
