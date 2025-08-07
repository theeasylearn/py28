a = 100 
b = 1000

result = a is b 
print(f"{result} ",id(a),id(b))

result = a is not b 
print(f"{result} ",id(a),id(b))

