#!/usr/bin/env python3

import adapters

print(dir(adapters.AdapterInterface))
print(adapters.AdapterInterface.get_adapters())
# print(adapters.get_adapters())
for key, value in adapters.AdapterInterface.get_adapters().items():
    print(key, value)
    print(value.is_available())
    print(value())
