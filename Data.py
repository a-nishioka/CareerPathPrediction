import DB


class Data:
    db = DB.DB()

    def __init__(self):
        self.db.open()
        return

    def __del__(self):
        self.db.close()
        return
