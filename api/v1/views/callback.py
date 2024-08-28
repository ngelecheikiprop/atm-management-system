from api.v1.views import app_views
from flask import request

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
    print(data)
    return "ok"
