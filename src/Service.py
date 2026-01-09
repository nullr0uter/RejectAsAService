import random, json
from argparse import ArgumentParser, Namespace
from typing import List, Literal

from flask import Flask, Response

app = Flask(__name__)

def parse_args() -> Namespace:
    p = ArgumentParser(description='API which rejects every request with a random message')
    p.add_argument('--host', type=str, default='127.0.0.1')
    p.add_argument('--port', type=int, default=5000)
    p.add_argument('--debug', action='store_true')
    return p.parse_args()

def get_random_rejection(culture: Literal['de','en']) -> str:
    with open(f'rejections_{culture}.txt', 'r', encoding='utf-8') as f:
        lines: List[str] = [l.rstrip('\n') for l in f if l.strip()]
    return random.choice(lines)

@app.route('/')
def root() -> Response:
    return Response(
        json.dumps({'culture':'Please choose /de or /en'}, ensure_ascii=False), mimetype='application/json; charset=utf-8')

@app.route('/de')
def german_reject() -> Response:
    return Response(json.dumps({'reason':get_random_rejection('de')}, ensure_ascii=False), mimetype='application/json; charset=utf-8')

@app.route('/en')
def english_reject() -> Response:
    return Response(json.dumps({'reason':get_random_rejection('en')}, ensure_ascii=False), mimetype='application/json; charset=utf-8')

if __name__ == '__main__':
    try:
        args = parse_args()
        app.run(host=args.host, port=args.port, debug=args.debug)
    except KeyboardInterrupt: print("Stopped!")