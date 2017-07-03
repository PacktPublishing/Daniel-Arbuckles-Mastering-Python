import sqlite3

def database(connclass):
    fname = getattr(connclass, 'database', 'default.sqlite')
    connection = sqlite3.connect(fname, detect_types=sqlite3.PARSE_DECLTYPES)

    for tablename in dir(connclass):
        if tablename.startswith('_'):
            continue

        tabledata = getattr(connclass, tablename, None)

        if not isinstance(tabledata, type):
            continue

        columns = []

        for colname in dir(tabledata):
            if colname.startswith('_'):
                continue
            coldata = getattr(tabledata, colname, None)
            if coldata in ('INTEGER', 'TEXT'):
                columns.append('{} {}'.format(colname, coldata))

        sql = 'CREATE TABLE IF NOT EXISTS {} ({});'
        sql = sql.format(tablename, ', '.join(columns))

        connection.execute(sql)

    return connection
