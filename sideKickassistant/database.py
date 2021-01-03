# Copied off of Ed May
import sqlite3 as sq

class DatabaseManager:
    def __init__(self, database_filename):
        self.conn = sq.connect(database_filename)
    
    def __del__(self):
        self.conn.close()
    
    def _execute(self, statement, values=None):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(statement, values or [])
            return cur
    
    def create_table(self, table_name, cols):
        cols_with_types = [
            f'{col_name} {data_type}'
            for col_name, data_type in cols.items()
        ]

        statement = f'''
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(cols_with_types)});
            '''
        self._execute(statement)

    def add(self, table_name, data):
        placeholders = ', '.join('?' * len(data))
        col_names = ', '.join(data.keys())
        col_vals = tuple(data.values())

        self._execute(
            f'''
            INSERT INTO {table_name}
            ({col_names})
            VALUES ({placeholders});
            ''',
            col_vals,
        )
    
    def delete(self, table_name, criteria):
        placeholders = [ f'{col} = ?' for col in criteria.keys() ]
        delete_criteria = ' AND '.join(placeholders)
        self._execute(
            f'''
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            ''',
            tuple(criteria.values()),
        )
    
    def select(self, table_name, criteria=None, order_by=None):
        criteria = criteria or {}
        query = f'SELECT * FROM {table_name}'

        if criteria:
            placeholders = [ f'{col} = ?' for col in criteria.keys() ]
            select_criteria = ' AND '.join(placeholders)
            query += f' WHERE {select_criteria}'
        
        if order_by:
            query += f' ORDER BY {order_by}'
        
        return self._execute(
            query,
            tuple(criteria.values())
        )