from flask import Flask, render_template
from models  import storage
from api.v1.views.dashboard import get_stats  # Make sure to replace 'your_module' with the actual module name

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    stats = get_stats()
    sales_list = storage.getthetwo()
    return render_template('dashboard.html', stats=stats, sales_list=sales_list)

if __name__ == '__main__':
    app.run(debug=True)

