import astropy.coordinates as coord
from astropy import units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy
from ghrss import utility
import pickle


class GHRSS:
    def __init__(self):
        self.RA_source = {}
        self.Dec_source = {}
        self.RA_objects = {}
        self.Dec_objects = {}
        self.file_names_sources = []
        self.file_names_objects = []
        self.colors1 = []
        self.colors2 = []
        # colors can changed as per output requirement
        self.colors_init = ["r", "g", "y", "k", "violet"]
        self.coordinates = 0
        self.coord_ra = []
        self.coord_dec = []
        self.coord_l = []
        self.coord_b = []
        self.label_RaDec = []
        self.label_lb = []
        self.color_count = 0

    def write_colors(self, color_new):
        """
        ###Description
        writes the colors existing in list colors1 and colors 2.
        (color map can be changed according to output requirement)

        ###Args:
        color_new: the updated list of of the colors

        """
        self.colors2 = iter(cm.Blues(numpy.linspace(0, 1, 6)))
        with open("../colors.txt", "w") as f:
            for c in color_new:
                f.write("%s\n" % c)
        f.close()
        x = str(self.color_count)
        with open("../colors2.txt", "w") as f1:
            f1.write("%s" % x)
        f1.close()

    def read_colors(self):
        """
        Reads the colors from the files colors.txt and colors2.txt and stores in the variables
        """
        color1 = []
        with open("../colors.txt", "r") as file:
            temp = file.readlines()
        for i in temp:
            temp2 = i.split("\n")
            color1.append(temp2[0])
        self.colors1 = color1
        # color map can be changed
        self.colors2 = iter(cm.Blues(numpy.linspace(0, 1, 6)))
        with open("../colors2.txt", "r") as file:
            temp = file.readlines()
        temp2 = int(temp[0])
        while temp2:
            c = next(self.colors2)
            temp2 = temp2 - 1
            self.color_count = self.color_count + 1

    def set_coordinates(self, file_names, data, header, split_char):
        """
        ###Description:
        Takes the data read from files and obtains the coordinates from the names of the pulsar/source in the form RA and Dec
        ###Args:
        file_names: list of the file names

        data: table consisting of the data read from files

        header: header of each file

        split_char: the character indicating where to split the name of source('_') or pulsar('J')
        """
        c = []
        q = {}
        s = {}

        for i in range(0, len(file_names)):
            if split_char == "J":
                header_index = header[0]
            else:
                header_index = header[i]
            s[i] = data[file_names[i]][header_index]
            k = 0
            ra = []
            dec = []
            for j in s[i]:
                q[k] = s[i][k].split(split_char)
                c = q[k][1]
                ra.append(c[0] + c[1] + ":" + c[2] + c[3])
                if len(c) == 7:
                    dec.append(c[4] + c[5] + c[6])
                else:
                    dec.append(c[4] + c[5] + c[6] + ":" + c[7] + c[8])
                k = k + 1
            if split_char == "J":
                self.RA_objects[i] = ra
                self.Dec_objects[i] = dec
            else:
                self.RA_source[i] = ra
                self.Dec_source[i] = dec

    def plot_area(self, files, n1, ax):
        """
        ###Description:
        Converts the RA-Declination of sources to galactic coordinates and plots these coordinates on the galactic coordinate system using the figure object ax.
        The points with latitutude within the range of -5 and +5 are not plotted, because this region is avoided in the survey.
        ###Args:
        files: list of names of the files

        ax: plot object
        """
        c = next(self.colors2)

        lat = []
        lon = []
        for i in range(0, len(files)):
            lat = []
            lon = []
            coord1 = SkyCoord(
                self.RA_source[i], self.Dec_source[i], unit=(u.hourangle, u.deg)
            )
            coord1 = coord1.galactic
            L = coord1.l.wrap_at(180 * u.degree).radian
            B = coord1.b.wrap_at(180 * u.degree).radian
            c = next(self.colors2)
            for j, k in zip(B, L):
                if (
                    j < coord.Angle(-5, u.degree).radian
                    or j > coord.Angle(5, u.degree).radian
                ):
                    lat.append(j)
                    lon.append(k)
            ax.scatter(lon, lat, color=c, label=files[i])
            self.color_count = self.color_count + 1

    def plot_discovered(self, file_d, data, n2, ax):
        """
        ###Description:
        Converts the RA-declination of pulsars and RRATs to galactic coordinates.
        Using the periods of the pulsars, they are divided into different types (normal and MSPs), RRATs are given periods as '-' in the files.
        These are then plotted using different symbols, same color for a given file.
        ###Args:
        file_d: list of the file names (discovery data)

        data: table consisting of data read from files

        ax: plot object
        """
        for i in range(0, len(file_d)):
            coord1 = SkyCoord(
                self.RA_objects[i], self.Dec_objects[i], unit=(u.hourangle, u.deg)
            )
            coord1 = coord1.galactic
            L = coord1.l.wrap_at(180 * u.degree).radian
            B = coord1.b.wrap_at(90 * u.degree).radian
            k = 0
            lat_rrat = []
            lat_msp = []
            lat_normalpulsar = []
            lon_rrat = []
            lon_msp = []
            lon_normalpulsar = []
            for x in L:
                p = data[file_d[i]]["Period"][k]
                if float(p) < 0:
                    lat_rrat.append(L[k])
                    lon_rrat.append(B[k])
                elif float(p) < 30:
                    lat_msp.append(L[k])
                    lon_msp.append(B[k])
                else:
                    lat_normalpulsar.append(L[k])
                    lon_normalpulsar.append(B[k])
                k = k + 1
            if len(lat_rrat) != 0:
                ax.scatter(
                    lat_rrat,
                    lon_rrat,
                    color=self.colors1[0],
                    marker="^",
                    s=80,
                    label="RRATs discovered in " + file_d[i],
                )
            if len(lat_normalpulsar) != 0:
                ax.scatter(
                    lat_normalpulsar,
                    lon_normalpulsar,
                    color=self.colors1[0],
                    label="Pulsars discovered in " + file_d[i],
                )
            if len(lat_msp) != 0:
                ax.scatter(
                    lat_msp,
                    lon_msp,
                    color=self.colors1[0],
                    marker="*",
                    s=80,
                    label="MSPs discovered in " + file_d[i],
                )
            self.colors1.pop(0)

    def read_and_plot_sources(self, file_names, ax):
        """
        ###Description:
        Calls the function to read data files containing the list of sources
        then subsequently calls the function to obtain coordinates and the function to plot the same.
        ###Args:
        file_names: list of file names

        ax: plot object
        """
        data_table, n1, header = utility.read_data(file_names, header=True)
        if n1 != 0:
            self.set_coordinates(file_names, data_table, header, split_char="_")
            self.plot_area(file_names, n1, ax)

    def read_and_plot_objects(self, file_d, ax):
        """
        ###Description:
        Calls the function to read data files containing the list of pulsar names and period (.csv files)
        then subsequently calls the function to obtain coordinates and the function to plot the same.
        ###Args:
        file_d: list of files names

        ax: plot object
        """
        data_table, n2, header = utility.read_data(file_d, header=False)
        if data_table:
            self.set_coordinates(file_d, data_table, header, split_char="J")
            self.plot_discovered(file_d, data_table, n2, ax)

    def show_plot(self, ax):
        """
        ###Description:
        calls the function to plot given data files and saves the plot object by pickling it.
        It shows the final plot after the program is terminated.
        ###Args:
        ax: plot object
        """
        if len(self.file_names_sources) != 0:
            self.read_and_plot_sources(self.file_names_sources, ax)
        if len(self.file_names_objects) != 0:
            self.read_and_plot_objects(self.file_names_objects, ax)
        if self.coordinates == 1:
            self.plot_using_coordinate(ax)
        ax.legend(
            loc="upper right", bbox_to_anchor=(1, 1.15), ncol=2, prop={"size": 10}
        )
        utility.save_ax(ax)
        plt.savefig("GHRSS.png", format="png", dpi=300)
        plt.show()

    def accept_coord(self):
        """Accepts the coordinates (Either RA-Dec or Latitude-Longitude) from the user"""
        n = input("Enter 1.RA/Dec or 2.Latitude-longitude: ")
        if n == "1":
            self.label_RaDec.append(input("enter the name: "))
            self.coord_ra.append(float(input("Enter RA")))
            self.coord_dec.append(float(input("Enter declination")))
        elif n == "2":
            self.label_lb.append(input("enter the name: "))
            self.coord_l.append(float(input("Enter longitude")))
            self.coord_b.append(float(input("Enter latitude")))

    def plot_using_coordinate(self, ax):
        """Plots the coordinates accepted by function accept_coord()"""
        j = 0
        for i in self.label_RaDec:
            coord1 = SkyCoord(
                self.coord_ra[j], self.coord_dec[j], unit=(u.hourangle, u.deg)
            )
            coord1 = coord1.galactic
            L = coord1.l.wrap_at(180 * u.degree).radian
            B = coord1.b.wrap_at(180 * u.degree).radian
            ax.scatter(L, B, color=self.colors1[0], s=80, label=self.label_RaDec[j])
            j = j + 1
            self.colors1.pop(0)
        j = 0
        for i in self.label_lb:
            L = coord.Angle(self.coord_l[j], u.degree)
            B = coord.Angle(self.coord_b[j], u.degree)
            L = L.wrap_at(180 * u.degree).radian
            B = B.wrap_at(180 * u.degree).radian
            ax.scatter(L, B, color=self.colors1[0], s=80, label=self.label_lb[j])
            j = j + 1
            self.colors1.pop(0)

    def accept_choice(self):
        """accepts the user's choice and depending on it, either calls the function to create new figure and plot object 'ax'
        and initialises the colors or use the pickeled object and existing colors."""
        ch = input(
            "1.Plot with all the option\n2.Plot on the existing graph\nEnter 1 or 2: "
        )
        if ch == "1":
            ax = self.create_ax()
            self.write_colors(self.colors_init)
            self.read_colors()
            self.user_choice()
            self.show_plot(ax)
            self.write_colors(self.colors1)
        elif ch == "2":
            self.read_colors()
            with open("../plot.pkl", "rb") as fid:
                ax1 = pickle.load(fid)
            self.user_choice()
            self.show_plot(ax1)
            self.write_colors(self.colors1)
        else:
            print("invalid input")

    def user_choice(self):
        """Accepts user choice to plot various datafiles from the user."""
        plot_choice = "0"
        while plot_choice != "4":
            plot_choice = input(
                "Plot\n1.Targeted sky area\n2.Observed sources\n3.Discovered object\n4.end"
            )
            if plot_choice == "4":
                return 0
            elif plot_choice == "1":
                x = int(input("Enter the number of files to plot targeted file: "))
                for i in range(x):
                    self.file_names_sources.append(input("Enter the file names: "))
                    # file with extension .list, having values of ra-dec starting with 'HR_'
            elif plot_choice == "2":
                print(
                    "Observed sources:\n1.Plot all observed\n2.Plot different data files"
                )
                co = input("enter 1 or 2: ")
                if co == "1":
                    if input("append more to existing data?(y/n): ") == "y":
                        y = input("Enter the file name: ")
                        x = y + ".list"
                        # file with extension .list, having values of ra-dec starting with 'HR_'
                        utility.append_file("GHRSS observed sources.list", x)
                        self.file_names_sources.append("GHRSS observed sources")
                    else:
                        self.file_names_sources.append("GHRSS observed sources")
                elif co == "2":
                    n = int(input("Enter the number of files to plot: "))
                    for i in range(n):
                        self.file_names_sources.append(input("Enter the file name: "))
                        # file with extension .list, having values of ra-dec starting with 'HR_'
                else:
                    print("invalid input")

                print("\n")
            elif plot_choice == "3":
                dp = input(
                    "Plot\n1.Pulsars dicovered in phase-1\n2.Pulsars discovered in phase-2\n3.data files containing coordinates\n4.by giving coordiantes"
                )
                if dp == "1":
                    if input("append new phase1 data?(y/n)") == "y":
                        y = input("Enter the file name: ")
                        x = y + ".csv"
                        # .csv file with pulsar_name and period values(no header)
                        utility.append_file("phase1.csv", x)
                        self.file_names_objects.append("phase1")
                    else:
                        self.file_names_objects.append("phase1")
                elif dp == "2":
                    if input("append new phase2 data?(y/n)") == "y":
                        y = input("Enter the file name: ")
                        x = y + ".csv"
                        # .csv file with pulsar_name and period values(no header)
                        utility.append_file("phase2.csv", x)
                        self.file_names_objects.append("phase2")
                    else:
                        self.file_names_objects.append("phase2")
                elif dp == "3":
                    file_name = input("enter the name of the file: ")
                    # .csv file with pulsar_name and period values(header:'Pulsar_name,Period')
                    self.file_names_objects.append(file_name)
                elif dp == "4":
                    self.coordinates = 1
                    self.accept_coord()
                else:
                    print("Invalid input.")
            else:
                print("invalid input")

    def create_ax(self):
        """
        ###Description:
        Creates and returns the figure and the plot object 'ax' which will be used to plot all the coordinates
        ###Returns:
        The plot object 'ax'
        """
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, projection="aitoff")
        ax.grid()
        ax.set_ylabel("Galactic latitude, b", fontsize=15)
        ax.set_xlabel("Galactic longitude, l", fontsize=15)
        return ax
