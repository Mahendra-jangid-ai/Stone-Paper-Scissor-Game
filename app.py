from flask import Flask, render_template, request, redirect, url_for, session
import random
import os

app = Flask(__name__)
app.secret_key = "change_this_to_a_random_secret_for_prod"

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
    session.pop('state', None)
    return render_template("index.html")

@app.route('/start', methods=['POST'])
def start():
    try:
        total = int(request.form.get('rounds', 1))
    except ValueError:
        total = 1
    if total < 1:
        total = 1

    session['state'] = {
        "total_rounds": total,
        "current_round": 0,
        "results": []
    }
    return redirect(url_for('round_play'))

@app.route('/round', methods=['GET', 'POST'])
def round_play():
    state = session.get('state')
    if not state:
        return redirect(url_for('index'))

    total_rounds = state['total_rounds']
    current_round = state['current_round']

    if request.method == 'POST':
        user_choice = request.form.get('choice')
        if not user_choice or user_choice.lower() not in choices:
            return render_template("round.html",
                                   total_rounds=total_rounds,
                                   current_round=current_round,
                                   message="Invalid choice. Choose rock/paper/scissors.")
        user_choice = user_choice.lower()
        machine_choice = random.choice(choices)
        result = play_round(user_choice, machine_choice)

        state['results'].append({
            "round": current_round + 1,
            "user": user_choice,
            "machine": machine_choice,
            "result": result
        })
        state['current_round'] = current_round + 1

        session['state'] = state

        if state['current_round'] >= state['total_rounds']:
            return redirect(url_for('result'))

        return redirect(url_for('round_play'))

    return render_template("round.html",
                           total_rounds=total_rounds,
                           current_round=current_round,
                           message=None)

@app.route('/result')
def result():
    state = session.get('state')
    if not state:
        return redirect(url_for('index'))

    results_list = state['results']
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
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
