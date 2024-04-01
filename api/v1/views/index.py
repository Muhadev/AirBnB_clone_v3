from api.v1.views import app_views
from flask import jsonify

# Define a route /status on the app_views Blueprint
@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
