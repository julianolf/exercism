import json
from enum import Enum, auto


class HTTPMethod(Enum):
    GET = auto()
    POST = auto()


class Database:
    def __init__(self, data=None):
        self.data = data or []

    def add(self, data):
        self.data.append(data)
        return len(self.data) - 1

    def put(self, data):
        for index, user in enumerate(self.data):
            if user["name"] == data["name"]:
                self.data[index].update(data)
                return index

        self.data.append(data)
        return len(self.data) - 1

    def get(self, index):
        return self.data[index]

    def list(self, names=None):
        if names is None:
            return self.data

        return [user for user in self.data if user["name"] in names]

    def find(self, name):
        for user in self.data:
            if user["name"] == name:
                return user


class User:
    def __init__(self, name, owes=None, owed_by=None, balance=0.0):
        self.name = name
        self.owes = owes or {}
        self.owed_by = owed_by or {}
        self.balance = balance

    def to_dict(self):
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance,
        }

    def borrow_from(self, lender, amount):
        if self.name in lender.owes:
            balance = lender.owes[self.name] - amount

            if balance > 0:
                lender.owes[self.name] -= amount
                lender.balance += amount

                self.owed_by[lender.name] -= amount
                self.balance -= amount
            elif balance < 0:
                owed_by_value = self.owed_by.get(self.name, 0.0)
                lender.owed_by[self.name] = owed_by_value + abs(balance)
                lender.owes.pop(self.name, None)
                lender.balance += amount

                owes_value = self.owes.get(lender.name, 0.0)
                self.owes[lender.name] = owes_value + abs(balance)
                self.owed_by.pop(lender.name, None)
                self.balance -= amount
            else:
                lender.owes.pop(self.name, None)
                lender.balance += amount

                self.owed_by.pop(lender.name, None)
                self.balance -= amount
        else:
            owed_by_value = lender.owed_by.get(self.name, 0.0)
            lender.owed_by[self.name] = owed_by_value + amount
            lender.balance += amount

            owes_value = self.owes.get(lender.name, 0.0)
            self.owes[lender.name] = owes_value + amount
            self.balance -= amount


class RestAPI:
    def __init__(self, database=None):
        data = database["users"] if database else []
        self.database = Database(data)
        self.routes = {
            "/users": {HTTPMethod.GET: self.users},
            "/add": {HTTPMethod.POST: self.add},
            "/iou": {HTTPMethod.POST: self.iou},
        }

    def handle(self, method, url, payload=None):
        resource = self.routes[url][method]

        try:
            response = resource(payload)
        except Exception as error:
            return json.dumps({"error": str(error)})
        else:
            return response

    def get(self, url, payload=None):
        return self.handle(HTTPMethod.GET, url, payload)

    def post(self, url, payload=None):
        return self.handle(HTTPMethod.POST, url, payload)

    def add(self, payload=None):
        if payload is None:
            return json.dumps({"error": "missing required payload"})

        data = json.loads(payload)
        user = User(name=data["user"])
        index = self.database.add(user.to_dict())

        return json.dumps(self.database.get(index))

    def users(self, payload=None):
        names = None

        if payload is not None:
            data = json.loads(payload)
            names = data.get("users")

        users = self.database.list(names)

        return json.dumps({"users": users})

    def iou(self, payload=None):
        if payload is None:
            return json.dumps({"error": "missing required payload"})

        data = json.loads(payload)
        amount = data["amount"]

        lender = User(name=data["lender"])
        lender_data = self.database.find(lender.name)

        if lender_data is not None:
            lender = User(**lender_data)

        borrower = User(name=data["borrower"])
        borrower_data = self.database.find(borrower.name)

        if borrower_data is not None:
            borrower = User(**borrower_data)

        borrower.borrow_from(lender, amount)

        self.database.put(lender.to_dict())
        self.database.put(borrower.to_dict())

        users = [lender.to_dict(), borrower.to_dict()]
        users = sorted(users, key=lambda usr: usr["name"])

        return json.dumps({"users": users})
