from db.run_sql import run_sql
from models.zombie_type import ZombieType
from models.human import *
from models.biting import Biting
from models.zombie import *

import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository
import repositories.zombie_type_repository as zombie_type_repository


def save(biting):
    sql = " INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    print(biting.human)
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    biting.id = id

def select_all():
    bitings = []
    sql = "SELECT * from bitings"
    results = run_sql(sql)

    for row in results:
        human = human_repository.select(row['human_id'])
        zombie = zombie_repository.select(row['zombie_id'])
        biting = Biting(human,zombie,row['id'])
        bitings.append(biting)
    return bitings

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def select(id):
    sql = "SELECT * FROM bitings WHERE id =%s"
    values = [id]
    result = run_sql(sql,values)[0]
    human = human_repository.select(['human_id'])
    zombie = zombie_repository.select(['zombie_id'])
    biting = Biting(human,zombie,result['id'])
    return biting

def update(biting):
    sql = "UPDATE bitings SET (zombie_id, human_id) = (%s, %s) WHERE id = %s"
    values = [biting.zombie_id, biting.human_id]
    run_sql(sql, values)




# save
# select_all
# select
# delete
# delete_all
# update