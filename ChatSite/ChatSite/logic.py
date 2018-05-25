from .client_2 import send

def measure():
    x=send('GET','192.168.43.102',8000)
    x=eval(x)
    per=x/100
    y=per*415
    print(int(y))
    return int(y)