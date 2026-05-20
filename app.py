from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style="font-family: 'Segoe UI', Arial, sans-serif; background-color: #f8f9fa; margin: 0; padding: 30px; color: #333;">
        <div style="border-bottom: 2px solid #e9ecef; padding-bottom: 15px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center;">
            <h1 style="margin: 0; color: #212529; font-size: 24px;">📊 Data Pipeline Monitoring Dashboard</h1>
            <span style="background-color: #d1e7dd; color: #0f5132; padding: 6px 12px; border-radius: 4px; font-weight: 600; font-size: 14px;">● Pipeline Active</span>
        </div>

        <div style="display: flex; gap: 20px; margin-bottom: 30px;">
            <div style="background: white; padding: 20px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); flex: 1; border-top: 4px solid #0d6efd;">
                <h3 style="margin: 0 0 10px 0; color: #6c757d; font-size: 14px; text-transform: uppercase;">Records Ingested</h3>
                <p style="margin: 0; font-size: 28px; font-weight: bold; color: #212529;">1,420,850</p>
            </div>
            <div style="background: white; padding: 20px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); flex: 1; border-top: 4px solid #198754;">
                <h3 style="margin: 0 0 10px 0; color: #6c757d; font-size: 14px; text-transform: uppercase;">Data Quality</h3>
                <p style="margin: 0; font-size: 28px; font-weight: bold; color: #198754;">99.92%</p>
            </div>
            <div style="background: white; padding: 20px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); flex: 1; border-top: 4px solid #ffc107;">
                <h3 style="margin: 0 0 10px 0; color: #6c757d; font-size: 14px; text-transform: uppercase;">Execution Time</h3>
                <p style="margin: 0; font-size: 28px; font-weight: bold; color: #212529;">4.2s</p>
            </div>
        </div>

        <div style="background: #e9ecef; padding: 15px; border-radius: 6px; font-size: 14px; color: #495057;">
            <strong>Environment Details:</strong> Jenkins CI/CD Containerized Deployment via Docker.
        </div>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)