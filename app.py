from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 50px; padding: 20px; border-left: 5px solid #238636; background-color: #f6f8fa;">
        <h1 style="color: #24292f;">👋 Hello from Flask CI/CD Pipeline!</h1>
        <p style="color: #57606a; font-size: 18px;">Automated Build, Test, and Deployment executed flawlessly.</p>
        <span style="background-color: #238636; color: white; padding: 5px 10px; border-radius: 15px; font-weight: bold; font-size: 14px;">Build successful 🚀</span>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)