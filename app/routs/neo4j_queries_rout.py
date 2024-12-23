from flask import Blueprint, jsonify, request, render_template

from app.repository.neo4j_repo import groups_with_same_target, groups_with_same_strartegy, groups_with_same_perpes, \
    high_groups, groups_with_wide_influence
from app.services.json_to_map import groups_with_same_target_to_mup, high_groups_to_mup, same_strartegy_to_mup, \
    groups_with_wide_influence_to_mup

neo4j_queries_bluprint = Blueprint("neo4j_queries", __name__)


# 11
@neo4j_queries_bluprint.route("/same_target", methods=["GET"])
def get_groups_with_same_target():
    same_target = groups_with_same_target()
    groups_with_same_target_to_mup(same_target)
    return render_template('same_target.html')


# 14

@neo4j_queries_bluprint.route("/same_strartegy", methods=["GET"])
def get_groups_with_same_strartegy():
    same_strartegy = groups_with_same_strartegy()
    same_strartegy_to_mup(same_strartegy)
    return render_template('same_strartegy.html')



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
    high_group = high_groups()
    high_groups_to_mup(high_group)
    return render_template('high_groups.html')


# 18
@neo4j_queries_bluprint.route("/wide_influence", methods=["GET"])
def get_groups_with_wide_influence():
    wide_influence = groups_with_wide_influence()
    groups_with_wide_influence_to_mup(wide_influence)

    return render_template('wide_influence.html')

