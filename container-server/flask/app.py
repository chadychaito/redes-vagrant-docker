from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/container', methods=['POST'])
def container():
    content = request.json
    file = open('containers.txt', 'w')

    keys = content.keys()
    for key in keys:
        aux = key + '->' + content[key] + ' '
        file.write(aux)
    file.write('\n')

    data = {'message': 'Dados do container armazenados com sucesso!'}
    return jsonify(data), 201


@app.route('/containers', methods=['GET'])
def containers():
    file = open('containers.txt')
    return file.read(), 200


if __name__ == '__main__':
    app.run()

