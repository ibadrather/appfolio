import datetime
import os


class RequestLimiter:
    def __init__(self, requests_per_day=200, counter_file="requests_counter.txt"):
        self.requests_per_day = requests_per_day
        self.counter_file = counter_file
        self.requests_per_day_counter = 0
        self.last_request_date = datetime.datetime.now().date()

        self.load_counter()

    def load_counter(self):
        if os.path.exists(self.counter_file):
            with open(self.counter_file, "r") as f:
                data = f.read().splitlines()
                self.last_request_date = datetime.datetime.strptime(
                    data[0], "%Y-%m-%d"
                ).date()
                self.requests_per_day_counter = int(data[1])

    def save_counter(self):
        with open(self.counter_file, "w") as f:
            f.write(f"{self.last_request_date}\n{self.requests_per_day_counter}")

    def check_request_limit(self):
        if self.requests_per_day_counter >= self.requests_per_day:
            if self.last_request_date == datetime.datetime.now().date():
                raise Exception(
                    "You have reached the limit of requests per day. Please try again tomorrow."
                )
            else:
                self.requests_per_day_counter = 0
                self.last_request_date = datetime.datetime.now().date()

        self.requests_per_day_counter += 1
        self.save_counter()
