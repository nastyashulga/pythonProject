from utils import get_candidate, get_all, get_candidates_by_name, get_candidates_by_skill, load_candidates_from_json
from flask import Flask, render_template


FILENAME = 'candidates.json'
candidates = get_all(load_candidates_from_json(FILENAME))

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:x>')
def candidates_page(x):
    item = get_candidate(x, candidates)
    if item:
        return render_template('single.html', item=item)
    return "Not Found"

@app.route('/search/<candidate_name>')
def get_one_user(candidate_name):
    items = get_candidates_by_name(candidate_name, candidates)
    if items:
        return render_template('search.html', candidates=items)
    return "Not Found"

@app.route('/skill/<skill_name>')
def user_by_skill(skill_name):
    skills = get_candidates_by_skill(skill_name, candidates)
    if skills:
        return render_template('skill.html', skill=skill_name, candidates=skills)
    return "Not Found"


if __name__ == '__main__':
    app.run(port=5013)
