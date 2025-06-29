from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Monte Carlo API is live"

@app.route('/simulate', methods=['POST'])
def simulate():
    # Example dummy MC simulation output
    data = request.get_json()
    home_team = data.get("home_team", "TBD")
    away_team = data.get("away_team", "TBD")

    # Simulate 1000 outcomes (replace with your real logic)
    import random
    home_wins = sum([1 for _ in range(1000) if random.random() > 0.5])
    away_wins = 1000 - home_wins

    return jsonify({
        "home_team": home_team,
        "away_team": away_team,
        "home_wins": home_wins,
        "away_wins": away_wins,
        "home_win_pct": round(home_wins / 1000, 3)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
