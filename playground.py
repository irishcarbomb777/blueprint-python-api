import json




try:
    print(len(a))
except Exception as inst:
    print(inst)
    x = inst.args
    print(type(x[0]))
    body = json.dumps(x)
    print(body)

print( {
    body
})
