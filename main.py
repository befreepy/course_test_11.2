from flask import Flask, render_template
import utils


app = Flask(__name__)

@app.route("/")
def index():
    candidates = utils.get_all()
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_id(pk)
    return render_template('card.html', candidate=candidate)

@app.route("/candidate/<candidate_name>")
def get_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_by_skills(skill):
    candidates = utils.get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))

if __name__ == "__main__":
    app.run(debug = True)
