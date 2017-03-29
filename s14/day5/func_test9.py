__author__ = "Steven Lee"

DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "d:\project\python\s14\day5/"
}


def file_db_handle(conn_params):
    print('file db:', conn_params)
    # db_path ='%s/%s' %(conn_params['path'],conn_params['name'])
    return file_execute


def db_handler():
    conn_params = DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
        pass


def file_execute(sql, **kwargs):  # "select * from accounts where account=%s" % account
    conn_params = DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

    print(sql, db_path)
    sql_list = sql.split("where")
    print("sql_list is", sql_list)

db_api = db_handler()
data = db_api("select * from accounts where account=1234")
