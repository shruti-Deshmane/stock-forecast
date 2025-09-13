from flask import Flask, render_template, request
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load forecasted prices from CSV
future_df = pd.read_csv("future_prices.csv")
future_df.reset_index(drop=True, inplace=True)

@app.route("/", methods=["GET", "POST"])
def index():
    forecast_value = None
    forecast_day = None
    
    if request.method == "POST":
        try:
            # Get user input
            n_days = int(request.form["n_days"])
            
            # Fetch forecasted value from last column of CSV
            forecast_value = future_df.iloc[n_days-1, -1]
            forecast_day = n_days
        except Exception as e:
            forecast_value = f"Error: {e}"
    
    return render_template("index.html", forecast=forecast_value, day=forecast_day)

if __name__ == "__main__":
    app.run(debug=True)
