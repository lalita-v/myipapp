from flask import Flask, request, jsonify, render_template
# Flask lets you turn a Python script into a web server that can handle HTTP requests (like GET, POST).
# Jsonify is a function in Flask that converts Python data (like dictionaries) into JSON format so it can be used in web applications and APIs.

app = Flask(__name__)

@app.route("/")  # Homepage Route
def home():
    print("Loading index.html...")  # Debugging message
    return render_template("index.html")  # Load the UI

@app.route("/myip", methods=["GET"])  # API Route
# Flask defaults to GET only, but we specific methods 'Get' to disallow other http method from client
def get_my_ip():
    print(request.headers)
    #user_ip = request.remote_addr
    user_ip = request.headers.get("X-Real-IP", request.headers.get("X-Forwarded-For", request.remote_addr))
    #user_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return jsonify({"ip": user_ip})

if __name__ == "__main__":
    # Run the app and allow connections from other computers and define listing port
    # Use debug mode to see the detailed error messages
    app.run(host="0.0.0.0", port=8080, debug=True)
