from flask import Flask, render_template, request, redirect, url_for, session
import qrcode
import io
import base64

app = Flask(__name__)
app.secret_key = "supersecretkey" 

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        url = request.form.get("input-link").strip()
        
        qr = qrcode.QRCode()
        qr.add_data(url)
        img = qr.make_image()

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        session["qr_code"] = qr_base64

        return redirect(url_for("home")) 
    qr_base64 = session.pop("qr_code", None)

    return render_template("index.html", qr_base64=qr_base64)


if __name__ == "__main__":
    app.run(debug=True)