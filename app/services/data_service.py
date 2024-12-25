class DataService:
    def get_data(self):
        return {"name": "test", "score": 100}
    def post_data(self, data):
        print(f"input = {data}")
        return data