# {key:value}

capital = {"USA": "Washington D.C.",
           "India": "New Delhi",
           "China": "Beijing",
           "Russia": "Moscow"}

capital.get("USA")
capital.update({"Germany": "Berlin"})
capital.update({"USA": "Detroit"})
capital.pop("China")
capital.popitem()
capital.clear()

keys = capital.keys()
for key in capital.keys():
    print(key)

values = capital.values()
for value in capital.values():
    print(value)

items = capital.items()
for key, value in capital.items():
    print(f"{key}:{value}")