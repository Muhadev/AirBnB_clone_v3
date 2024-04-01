from flask import Flask
from models import storage
from api.v1.views import app_views

# Create a Flask instance
app = Flask(__name__)

# Register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)
# Declare a method to handle @app.teardown_appcontext storage.close()


@app.teardown_appcontext
def teardown_appcontext(error):
    storage.close()


if __name__ == "__main__":
    import os
    # Define host and port
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))

    app.run(host=host, port=port, threaded=True)
