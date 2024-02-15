from src import Updog, HTTPGetBuilder

b = HTTPGetBuilder(url="http://localhost:5000")
print(b.to_dict())
