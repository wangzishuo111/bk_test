import test
import numpy as np
import base64
import matplotlib.pyplot as plt
from io import BytesIO

def create_image():
    
    a = 20
    b = 30
    c = 60
    x = 0
    width = 1
    
    plt.bar(x, a,  width=0.5, label='a')
    plt.bar(x + width, b, width=0.5, label='b')
    plt.bar(x + 2 * width, c, width=0.5, label='c')
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    context = {
            'info': imd,
        }
    return render(request, 'home_application/chart.html', context)

dic = test.group_hosts()
dic = test.overview()
print (dic)
