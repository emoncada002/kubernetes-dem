import os

from flask import Flask  # type: ignore[import-not-found]

app = Flask(__name__)


@app.route("/")
def hello():
    # Obtiene el nombre del Pod desde la variable de entorno HOSTNAME
    # (por defecto en Kubernetes)
    # o utiliza "localhost" si se ejecuta fuera de un entorno K8s.
    pod_name = os.environ.get("HOSTNAME", "localhost")
    return f"Hola desde Kubernetes - Atendido por el Pod: {pod_name}"


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
