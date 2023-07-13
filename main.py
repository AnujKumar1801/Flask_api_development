from flask import Flask, jsonify, request
import ipl
import jugad

app = Flask(__name__)


@app.route('/')
def home():
  return 'hello world'


@app.route('/api/teams')
def teams():
  return jsonify(ipl.allteams())


@app.route('/api/teamencountrs')
def teamencountrs():
  team1 = request.args.get('team1')
  team2 = request.args.get('team2')
  response = ipl.teamvsteam(team1, team2)
  return response


@app.route('/api/teamrecord')
def teamrecord():
  team = request.args.get('teamname')
  response = jugad.team_record(team)
  return jsonify(response)


@app.route('/api/allrecords')
def allrecord():
  team = request.args.get('teamname')
  response = jugad.allRecord(team)
  return jsonify(response)


if __name__ == '__main__':
  app.run("0.0.0.0", debug=True)
