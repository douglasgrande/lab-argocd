from flask import Flask, jsonify # type: ignore
from prometheus_flask_exporter import PrometheusMetrics # type: ignore

app = Flask(__name__)

# Configura o exportador de métricas
metrics = PrometheusMetrics(app)

# Métricas estáticas (opcional)
metrics.info('app_info', 'Informações da API', version='1.0.0')

@app.route('/', methods=['GET'])
def root():
    return jsonify({"status": "ok"})

@app.route('/health', methods=['GET'])
def health():
    # Aqui você poderia testar conexão com banco de dados, etc.
    return jsonify({
        "status": "healthy",
        "uptime": "up",
        "services": {"database": "online"}
    })

# O endpoint /metrics é criado automaticamente pelo PrometheusMetrics

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)