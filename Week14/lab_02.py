import matplotlib.pyplot as plt
from math import sin, pi

def drawing_sin():
    step=0.1
    d=0
    y,x=[],[]
    fh=open("sin_data.dat","w")
    while d<=2*pi:
        x.append(d)
        y.append(sin(d))
        d=d+step
        fh.write("%f , %f\n" % (x[-1],y[-1]))
    fh.close()
    # show_img(x,y)

def  read_data():
    fh=open("sin_data.dat","r")
    file_text=fh.readlines()
    fh.close()

    data=[[],[]]
    for s in file_text:
        data[0].append(float(s.split(',')[0]))
        data[1].append(float(s.split(',')[1]))
    return data

def show_img(x,y):
    plt.plot(x,y)
    plt.title('123')
    plt.ylabel('sin')
    plt.xlabel('degree')
    plt.show()

def main():
    drawing_sin()
    show_img(read_data()[0],read_data()[1])



if __name__ == '__main__':
    main()