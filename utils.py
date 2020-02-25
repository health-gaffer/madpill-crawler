import pymysql
import os
from tqdm import tqdm

from config import mysql_config

_drug_file = 'drugs.txt'


def _build_insert_sql(drug_info):
    sql = 'INSERT INTO `mp_warehouse` '
    sql += '({})'.format(', '.join(['`{}`'.format(field) for field in drug_info.keys()]))
    sql += ' VALUES '
    sql += '({})'.format(', '.join(['\"{}\"'.format(value) for value in drug_info.values()]))
    sql += ';'
    return sql


def save_drugs_to_file(drug_infos, file_path=_drug_file):
    with open(file_path, 'w+') as f:
        for drug_info in drug_infos:
            for k, v in drug_info.items():
                f.write('{}: {}\n'.format(k, v))
            f.write('=' * 100)
            f.write('\n')


def load_drugs_from_file(file_path=_drug_file):
    if not os.path.exists(file_path):
        return []
    drug_infos = []
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        drug_info = {}
        for line in lines:
            if line:
                items = [item.strip() for item in line.split(':')]
                field = items[0]
                content = ':'.join(items[1:])
                content = content.replace('\"', '\\"').replace('\'', "\\'")
                drug_info[field] = content
            else:
                drug_infos.append(dict(drug_info))
                drug_info = {}
    return drug_infos


def save_drugs_to_mysql(drug_infos):
    with open('add_drugs.sql', 'w+') as f:
        for drug_info in drug_infos:
            f.write(_build_insert_sql(drug_info))
            f.write('\n')
    # connection = pymysql.connect(
    #     host=mysql_config['host'],
    #     user=mysql_config['user'],
    #     password=mysql_config['password'],
    #     db=mysql_config['database'],
    #     charset='utf8mb4'
    # )
    # try:
    #     with connection.cursor() as cursor:
    #         for drug_info in tqdm(drug_infos):
    #             sql = _build_insert_sql(drug_info)
    #             cursor.execute(sql)
    #     connection.commit()
    # finally:
    #     connection.close()


if __name__ == '__main__':
    drug_infos = load_drugs_from_file()
    save_drugs_to_mysql(drug_infos)
