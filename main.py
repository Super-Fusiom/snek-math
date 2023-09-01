import matplotlib
import matplotlib.pyplot
import numpy


def main():
    x = numpy.linspace(0, 2 * numpy.pi, 200)
    y = numpy.sin(x)
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(x, y)
    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()
