"""
Flask Backend Server for Granica × IIT Guwahati Hackathon
AI-Augmented Triage Layer (IPM).
Supports Multimodal Image Analysis, Minimalist Light Theme, and Parquet/CSV exports.
"""

import os
import sys
import json
import base64
import urllib.parse
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file

# Add root directory to sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from pipeline.schema import IPMTicketAnalysis
from pipeline.demo_data import get_all_demos, get_demo_by_id
from pipeline.triage_engine import analyze_ticket

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024  # 32 MB max

@app.route("/")
def index():
    demos = get_all_demos()
    is_blank = request.args.get("blank", "false").lower() in ["true", "1"]
    return render_template("index.html", demos=demos, is_blank=is_blank)

@app.route("/new")
def new_ticket():
    demos = get_all_demos()
    return render_template("index.html", demos=demos, is_blank=True)

@app.route("/api/demos", methods=["GET"])
def api_get_demos():
    return jsonify({"status": "success", "demos": get_all_demos()})

@app.route("/api/demos/<ticket_id>", methods=["GET"])
def api_get_demo_ticket(ticket_id):
    ticket = get_demo_by_id(ticket_id)
    return jsonify({"status": "success", "ticket": ticket})

@app.route("/api/triage", methods=["POST"])
def api_triage():
    try:
        image_path = None
        
        if request.is_json:
            data = request.get_json() or {}
            raw_text = data.get("raw_text", "").strip()
            hostel = data.get("hostel", "Lohit Hostel")
            room = data.get("room", "A233")
            original_category = data.get("original_category", "Electricity")
            api_key = data.get("api_key", None)
            force_offline = bool(data.get("force_offline", False))
            image_url = data.get("image_url", None)
            image_base64 = data.get("image_base64", None)
            
            # If client uploaded base64 data
            if image_base64 and len(image_base64) > 50:
                header, encoded = image_base64.split(",", 1) if "," in image_base64 else ("", image_base64)
                img_data = base64.b64decode(encoded)
                upload_dir = BASE_DIR / "static" / "uploads"
                upload_dir.mkdir(parents=True, exist_ok=True)
                dest = upload_dir / "client_uploaded_evidence.jpg"
                with open(dest, "wb") as f:
                    f.write(img_data)
                image_path = str(dest)

            # If image_url is a static path
            elif image_url and image_url.startswith("/static/"):
                rel_path = urllib.parse.unquote(image_url[len("/static/"):])
                local_img = BASE_DIR / "static" / rel_path
                if local_img.exists():
                    image_path = str(local_img)

        else:
            raw_text = request.form.get("raw_text", "").strip()
            hostel = request.form.get("hostel", "Lohit Hostel")
            room = request.form.get("room", "A233")
            original_category = request.form.get("original_category", "Electricity")
            api_key = request.form.get("api_key", None)
            force_offline = request.form.get("force_offline", "false").lower() == "true"
            
            # Handle uploaded image file
            if "image_file" in request.files:
                uploaded_file = request.files["image_file"]
                if uploaded_file.filename:
                    upload_dir = BASE_DIR / "static" / "uploads"
                    upload_dir.mkdir(parents=True, exist_ok=True)
                    dest = upload_dir / uploaded_file.filename
                    uploaded_file.save(dest)
                    image_path = str(dest)

        if not raw_text:
            return jsonify({"status": "error", "message": "Raw complaint text cannot be empty."}), 400

        # Run multimodal triage analysis
        result: IPMTicketAnalysis = analyze_ticket(
            raw_text=raw_text,
            hostel=hostel,
            room=room,
            original_category=original_category,
            image_path=image_path,
            api_key=api_key,
            force_offline=force_offline
        )

        return jsonify({
            "status": "success",
            "data": result.model_dump()
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/export/parquet", methods=["GET"])
def export_parquet():
    parquet_path = BASE_DIR / "data" / "ipm_triaged_tickets.parquet"
    if not parquet_path.exists():
        return jsonify({"status": "error", "message": "Parquet file not generated."}), 404
    return send_file(
        str(parquet_path),
        as_attachment=True,
        download_name="ipm_triaged_tickets.parquet",
        mimetype="application/octet-stream"
    )

@app.route("/api/export/csv", methods=["GET"])
def export_csv():
    csv_path = BASE_DIR / "data" / "ipm_triaged_tickets.csv"
    if not csv_path.exists():
        return jsonify({"status": "error", "message": "CSV file not generated."}), 404
    return send_file(
        str(csv_path),
        as_attachment=True,
        download_name="ipm_triaged_tickets.csv",
        mimetype="text/csv"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"\n=======================================================")
    print(f"🚀 Granica × IIT Guwahati Hackathon - IPM Triage Server")
    print(f"📡 Minimalist Light Mode Serving on http://127.0.0.1:{port}")
    print(f"=======================================================\n")
    app.run(host="0.0.0.0", port=port, debug=True)
