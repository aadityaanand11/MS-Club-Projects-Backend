from flask import Flask, request, jsonify
from models import db, Note
import os

def create_app():
    app = Flask(__name__)

    # Database setup - SQLite file stored locally
    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "notes.sqlite3")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()   # creates the table if not already present

    # --- CRUD routes ---

    @app.route("/notes", methods=["GET"])
    def list_notes():
        notes = Note.query.all()
        return jsonify([n.to_dict() for n in notes])

    @app.route("/notes/<int:note_id>", methods=["GET"])
    def get_note(note_id):
        note = Note.query.get_or_404(note_id)
        return jsonify(note.to_dict())

    @app.route("/notes", methods=["POST"])
    def create_note():
        data = request.get_json() or {}
        title = data.get("title")
        content = data.get("content", "")
        if not title:
            return jsonify({"error": "title is required"}), 400
        note = Note(title=title, content=content)
        db.session.add(note)
        db.session.commit()
        return jsonify(note.to_dict()), 201

    @app.route("/notes/<int:note_id>", methods=["PUT"])
    def update_note(note_id):
        note = Note.query.get_or_404(note_id)
        data = request.get_json() or {}
        if "title" in data:
            note.title = data["title"]
        if "content" in data:
            note.content = data["content"]
        db.session.commit()
        return jsonify(note.to_dict())

    @app.route("/notes/<int:note_id>", methods=["DELETE"])
    def delete_note(note_id):
        note = Note.query.get_or_404(note_id)
        db.session.delete(note)
        db.session.commit()
        return jsonify({"message": "deleted"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
