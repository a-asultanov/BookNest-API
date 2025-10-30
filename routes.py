from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from extensions import db
from models import Book, User
from schemas import BookSchema

bp = Blueprint('api', __name__, url_prefix='/api')
bp_auth = Blueprint('auth', __name__, url_prefix='/auth')
book_schema = BookSchema()
books_schema = BookSchema(many=True)


@bp.route('/status')
def status():
    return jsonify({"status": "API is running"}), 200


@bp_auth.route('/register', methods=['POST'])
def register(): 
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@bp_auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify(access_token=access_token), 200    


@bp.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        is_read=data.get('is_read', False)
    )
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), 201

@bp.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result), 200 


@bp.route('/books', methods=['PUT'])
@jwt_required()
def update_book():
    data = request.get_json()
    book = Book.query.get(data['id'])
    if not book:
        return jsonify({"message": "Book not found"}), 404

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)
    book.is_read = data.get('is_read', book.is_read)

    db.session.commit()
    return book_schema.jsonify(book), 200   

@bp.route('/books/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"}), 200