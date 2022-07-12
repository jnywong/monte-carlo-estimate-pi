import argparse
import random
import matplotlib.pyplot as plt
 
def main(INTERVAL):
    INTERVAL = 100
    
    circle_points = 0
    square_points = 0

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)

    # Total Random numbers generated= possible x
    # values* possible y values
    for i in range(INTERVAL**2):
    
        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is -1 to 1
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
    
        # Distance between (x, y) from the origin
        origin_dist = rand_x**2 + rand_y**2
    
        # Checking if (x, y) lies inside the circle
        if origin_dist <= 1:
            circle_points += 1
            ax.plot(rand_x, rand_y, color = "#ff79c6", marker = 'o')
        else:
            ax.plot(rand_x, rand_y, color = "#6272a4", marker = 's')
        square_points += 1

    # Estimating value of pi,
    # pi= 4*(no. of points generated inside the
    # circle)/ (no. of points generated inside the square)
    pi = 4 * circle_points / square_points
    print("Final Estimation of Pi=", pi)

    circle = plt.Circle((0, 0), 1, linewidth=2, edgecolor='k', fill=False, zorder=2)
    square = plt.Rectangle((-1, -1), 2, 2, linewidth=2, edgecolor='k', fill=False, zorder=2)
    ax.add_patch(circle)
    ax.add_patch(square)
    ax.set_aspect(1)
    ax.axis("off")
    plt.title(r"Estimation of $\pi$ using Monte Carlo method")
    plt.text(-1,
            -1.1,
            r"Number of points in circle, $N_c=$ {:d},"
            "\n"
            r"Number of points in square, $N_s=$ {:d},"
            "\n"
            r"$\pi \approx 4N_c/N_s=${:.5f}".format(circle_points, square_points, pi),
            va="top")

    plt.savefig("estimate-pi.png", dpi=300, format="png", bbox_inches="tight", )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Estimate pi using Monte Carlo method.')
    parser.add_argument('num_points', metavar='num_points', type=str, nargs=1,
                        help='specify number of points used for the estimation')
    args = parser.parse_args()
    main(args.num_points)