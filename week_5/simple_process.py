import os

if os.fork() == 0:
    foo = 'baz'
    print('Child: ', foo)
else:
    print('parant: ', foo)
    os.wait()
