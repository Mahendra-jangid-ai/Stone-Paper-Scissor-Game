from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']

def play_round(user, machine):
    if user == machine:
        return "It's a tie!"
    elif (user == 'rock' and machine == 'scissors') or \
         (user == 'paper' and machine == 'rock') or \
         (user == 'scissors' and machine == 'paper'):
        return "You win!"
    else:
        return "Machine wins!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start', methods=['POST'])
def start():
    try:
        total = int(request.form.get('rounds', 1))
    except ValueError:
        total = 1

    if total < 1:
        total = 1

    state = {
        "total_rounds": total,
        "current_round": 0,
        "results": [] 
    }

    return render_template("round.html",
                           total_rounds=state["total_rounds"],
                           current_round=state["current_round"],
                           results_json=json.dumps(state["results"]))

@app.route('/round', methods=['POST'])
def round_play():
    try:
        total_rounds = int(request.form.get('total_rounds', 1))
    except ValueError:
        total_rounds = 1

    try:
        current_round = int(request.form.get('current_round', 0))
    except ValueError:
        current_round = 0

    results = request.form.get('results_json', '[]')
    try:
        results_list = json.loads(results)
    except json.JSONDecodeError:
        results_list = []

    user_choice = request.form.get('choice')
    if user_choice:
        user_choice = user_choice.lower()
        if user_choice not in choices:
            message = "Invalid choice selected. Please pick rock/paper/scissors."
            return render_template("round.html",
                                   total_rounds=total_rounds,
                                   current_round=current_round,
                                   results_json=json.dumps(results_list),
                                   message=message)

        machine_choice = random.choice(choices)
        result = play_round(user_choice, machine_choice)

        results_list.append({
            "round": current_round + 1,
            "user": user_choice,
            "machine": machine_choice,
            "result": result
        })

        current_round += 1

    if current_round < total_rounds:
        return render_template("round.html",
                               total_rounds=total_rounds,
                               current_round=current_round,
                               results_json=json.dumps(results_list))
    else:
        you_wins = sum(1 for r in results_list if r["result"] == "You win!")
        machine_wins = sum(1 for r in results_list if r["result"] == "Machine wins!")
        ties = sum(1 for r in results_list if r["result"] == "It's a tie!")

        if you_wins > machine_wins:
            final_winner = "You are the final winner! "
        elif machine_wins > you_wins:
            final_winner = "Machine is the final winner! "
        else:
            final_winner = "It's an overall tie!"

        return render_template("result.html",
                               results=results_list,
                               you_wins=you_wins,
                               machine_wins=machine_wins,
                               ties=ties,
                               final_winner=final_winner)

if __name__ == "__main__":
    app.run(debug=True)
