import code

import numpy as np

import matplotlib.pyplot as plt


def create_3d_scatter(num_points=50):
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    z = np.random.rand(num_points)

    fig = plt.figure(figsize=(10, 8))

    ax = fig.add_subplot(111, projection=("3d"))

    scatter = ax.scatter(x, y, z, c=z, cmap="viridis")

    ax.set_xlabel("️X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("️Z-axis")

    ax.set_title("Arush Singh's 3D Scatter Plot ‼️")

    plt.colorbar(scatter, label="Z Value")
    plt.show()


def main():
    print("🔥 Welcome to the 3-D Graphing Project!")
    print("")
    print("This project will help you create a ⭐️ RANDOM 3-D Scatterplot ⭐️\n")

    while True:
        try:
            num_points = int(input("(5-500) Enter the Datapoints in the graph: "))

            if 5 <= num_points <= 500:
                create_3d_scatter(num_points)
                break

            else:
                print("⚠️ Enter a number in the range 5-500")

        except ValueError:
            print("\n⚠️ ERROR Code 69: No Numerical Value entered!")
            quit(code)

        except KeyboardInterrupt:
            print("\n⚠️ ERROR Code 420: Program manually stopped!")
            quit(code)

    print("\n🥶🔥 Thank you for your time!")


if __name__ == "__main__":
    main()
