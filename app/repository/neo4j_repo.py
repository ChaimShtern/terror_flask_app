from app.db.neo4j_connaction import driver
import toolz as t


# 11
def groups_with_same_target():
    with driver.session() as session:
        query = """ 
                match  (g:Group) -[rel:ATTACKED]- (c:Country)
                return rel.type as type, collect(DISTINCT g.name) as groups, c.name as country
                """
        res = session.run(query).data()
        return t.pipe(
            res,
            list
        )


# 14
def groups_with_same_strartegy():
    with driver.session() as session:
        query = """ 
                match  (g:Group) -[rel:ATTACKED]- (c:Country)
                return rel.target as target, collect(DISTINCT g.name) as groups, c.name as country
                """
        res = session.run(query).data()
        print(res)
        return t.pipe(
            res,
            list
        )


# 15
def groups_with_same_perpes():
    with driver.session() as session:
        query = """
              match  (g:Group) -[rel:ATTACKED]- (c:Country)
              return rel.target as target, collect(g.name) as groups, count(g.name) as count
              """
        res = session.run(query).data()
        return t.pipe(
            res,
            list
        )


# 16
def high_groups():
    with driver.session() as session:
        query = """match  (g:Group) -[rel:ATTACKED]- (c:Country) return  g.name as group, count(DISTINCT c) as country_count, 
        count(DISTINCT rel.target) as target_count, count(DISTINCT rel.type) as type_count, collect(DISTINCT c) as countries"""

        res = session.run(query).data()
        return t.pipe(
            res,
            list
        )


# 18
def groups_with_wide_influence():
    with driver.session() as session:
        query = """
                 match  (g:Group) -[rel:ATTACKED]- (c:Country)
                return  count(DISTINCT g.name) as group_count, collect(DISTINCT g.name) as groups, c.name as country
                """
        res = session.run(query).data()
        return t.pipe(
            res,
            list
        )
