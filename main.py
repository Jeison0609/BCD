import ssl
import socket
import hashlib
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/huella", methods=["GET"])
def obtener_huella():
    hostname = "bcdme.qondor.com"
    port = 443
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert_der = ssock.getpeercert(binary_form=True)
            fingerprint = hashlib.sha256(cert_der).hexdigest().upper()

    return jsonify({"Certificado": fingerprint})

# No incluyas app.run() aquí, Render usará Gunicorn



