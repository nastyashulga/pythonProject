from flask import Flask
from functions import load_candidates, get_all, get_by_pk, get_by_skill

FILENAME = 'candidates.json'
candidates = get_all(load_candidates(FILENAME))
app = Flask(__name__)

@app.route('/')
def main_page():
    str = '<pre>'
    for i in candidates:
        str += f'{i}\n \n'
    str += '<pre>'
    return str

@app.route('/candidstes/<int:pk>')
def get_user(pk):
    user = get_by_pk(pk, candidates)
    if user:
        str = f'<img src= "{user.picture}">'
        str += f'<pre> {user} </pre>'
    else:
        str = 'NOT FOUND'
    return str

@app.route('/skills/<x>')
def get_users(x):
    users = get_by_skill(x, candidates)
    if users:
        str = '<pre>'
        for i in candidates:
            str += f'<{i}\n \n>'
        str += '</pre>'
    else:
        str = 'NOT FOUND'
    return str

if __name__ == '__main__':
    app.run(port=5012)

