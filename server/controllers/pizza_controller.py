from flask import Blueprint, jsonify
from ..models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas]), 200
