from flask import Blueprint, jsonify, request, render_template

from app.repository.neo4j_repo import groups_with_same_target, groups_with_same_strartegy, groups_with_same_perpes, \
    high_groups, groups_with_wide_influence

neo4j_queries_bluprint = Blueprint("neo4j_queries", __name__)


# 11
@neo4j_queries_bluprint.route("/same_target", methods=["GET"])
def get_groups_with_same_target():
    try:
        same_target = groups_with_same_target()
        return jsonify(same_target), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404


# 14

@neo4j_queries_bluprint.route("/same_strartegy", methods=["GET"])
def get_groups_with_same_strartegy():
    try:
        same_strartegy = groups_with_same_strartegy()
        return jsonify(same_strartegy), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404


# 15
@neo4j_queries_bluprint.route("/same_perpes", methods=["GET"])
def get_groups_with_same_perpes():
    try:
        same_perpes = groups_with_same_perpes()
        return jsonify(same_perpes), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404


# 16
@neo4j_queries_bluprint.route("/high_groups", methods=["GET"])
def get_high_groups():
    try:
        high_group = high_groups()
        return jsonify(high_group), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404


# 18
@neo4j_queries_bluprint.route("/wide_influence", methods=["GET"])
def get_groups_with_wide_influence():
    try:
        wide_influence = groups_with_wide_influence()
        return jsonify(wide_influence), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404
