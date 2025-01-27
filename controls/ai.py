import numpy as np
def control(data,p):
    if p==2: #flip the data
        data[1]=800-data[1]
        data[3]=-data[3]
        tmp=data[5]
        data[5]=data[6]
        data[6]=tmp
    dd=np.array(data)
    w=np.array([[ 3.9119e-03, -6.1827e-03,  2.2695e-03],
        [ 6.9741e-03, -1.4600e-02,  7.6245e-03],
        [-4.7968e-02,  1.0869e-04,  4.7869e-02],
        [-9.4286e-03,  5.7871e-05,  9.4022e-03],
        [ 4.2871e-04, -2.1062e-06, -4.2524e-04],
        [ 3.5001e-03, -9.6078e-03,  6.1072e-03],
        [ 3.7573e-03, -6.5067e-03,  2.7486e-03]])
    b=np.array([4.3872e-11])
    z=dd@w+b
    return(z.argmax()-1)