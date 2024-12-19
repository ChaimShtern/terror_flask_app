from flask import Blueprint, jsonify, request, render_template
from app.db.database import session_maker
from app.repository.stats_repo import most_deadly_attacks, most_attacked_groups, attacks_by_region, \
    attacks_percentage_change_by_region, most_active_groups_by_region
from app.serices.json_to_map import attacks_by_region_to_map, attacks_percentage_to_map, most_active_groups_to_map
from app.serices.models_to_json import deadly_attacks_to_json

sql_queries_bluprint = Blueprint("sql_queries", __name__)


@sql_queries_bluprint.route("/most_deadly_attacks", methods=["GET"])
def get_most_deadly_attacks():
    try:
        most_deadly = most_deadly_attacks(session_maker)
        return deadly_attacks_to_json(most_deadly), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404


@sql_queries_bluprint.route("/most_attacked_groups", methods=["GET"])
def get_most_attacked_groups():
    try:
        most_attacked_group = most_attacked_groups(session_maker)
        return jsonify(most_attacked_group), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404


@sql_queries_bluprint.route("/attacks_by_region", methods=["GET"])
def get_attacks_by_region():
    attacks_by_regions = attacks_by_region(session_maker)
    attacks_by_region_to_map(attacks_by_regions)
    return render_template('attacks_by_region.html')


@sql_queries_bluprint.route("/attacks_percentage/from/<int:start>/to/<int:end>", methods=["GET"])
def get_attacks_percentage_change_by_region(start, end):
    attacks_percentages = attacks_percentage_change_by_region(session_maker, start, end)
    attacks_percentage_to_map(attacks_percentages)
    return render_template('attacks_percentage.html')


@sql_queries_bluprint.route("/most_active_groups", methods=["GET"])
def get_most_active_groups_by_region():
    most_active_groups = most_active_groups_by_region(session_maker)
    most_active_groups_to_map(most_active_groups)
    return render_template('most_active_groups.html')
