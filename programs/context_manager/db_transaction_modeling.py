import contextlib


class Connection:

    def __init__(self):
        self.xid = 0
    
    def start_transaction(self):
        print("starting transaction", self.xid)
        res = self.xid
        self.xid += 1
        return res
    
    def _commit_transaction(self, xid):
        print("committing transaction", xid)
    
    def _rollback_transaction(self, xid):
        print("rolling back transaction", xid)


class Transaction:

    def __init__(self, conn):
        self.conn = conn
        self.xid = conn.start_transaction()
    
    def commit(self):
        self.conn._commit_transaction(self.xid)
    
    def rollback(self):
        self.conn._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield
    except:
        tx.rollback()
        raise

    tx.commit()


if __name__ == "__main__":
    conn = Connection()
    try:
        with start_transaction(conn):
            raise ValueError()
    except ValueError:
        print("Oops! Operation Failed")