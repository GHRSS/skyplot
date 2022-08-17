import astropy.coordinates as coord
from astropy import units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import math


class SurveyPlot:
    def type1(self, dec1, d, a, ax):
        c1 = []
        L1 = []
        B1 = []
        L = []
        B = []
        s = 0
        e = 0
        index = 0
        for i in range(0, 360):
            c1.append(SkyCoord(ra=i * u.degree, dec=dec1 * u.degree, frame="icrs"))
            c1[i] = c1[i].galactic
            L1.append(c1[i].l.wrap_at(180 * u.degree))
            B1.append(c1[i].b.wrap_at(180 * u.degree))
        for i in range(0, 360):
            if L1[i] < 0:
                s = math.floor(math.degrees(B1[i].radian))
                e = math.floor(math.degrees(B1[i + 1].radian))
                break
            index = i
        index = index + 1
        for j in range(index + 1, 360):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        for j in range(0, index):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        for i in range(s, 90):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        j = 90
        for i in range(0, 90 - e):
            L.append(coord.Angle(-180, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(j, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 1
        ax.fill(L, B, color=d, alpha=a)

    def type2(self, dec1, d, a, ax):
        c1 = []
        L1 = []
        B1 = []
        L = []
        B = []
        e = 0
        s = 0
        index1 = 0
        index2 = 0
        for i in range(0, 360):
            c1.append(SkyCoord(ra=i * u.degree, dec=dec1 * u.degree, frame="icrs"))
            c1[i] = c1[i].galactic
            L1.append(c1[i].l.wrap_at(180 * u.degree))
            B1.append(c1[i].b.wrap_at(180 * u.degree))
        for i in range(0, 360):
            if L1[i] < 0:
                e = math.floor(math.degrees(B1[i].radian))
                index1 = i
                break

        for i in range(index1, 360):
            if L1[i] > 0:
                s = math.floor(math.degrees(B1[i + 1].radian))
                index2 = i
                break
        for j in range(index1 + 1, index2 - 1):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        i = s
        for j in range(0, s - e):
            L.append(coord.Angle(-180, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
            i = i - 1
        ax.fill(L, B, color=d, alpha=a)
        L = []
        B = []
        for j in range(index2, 360):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        for j in range(0, index1 - 1):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        for i in range(e, s):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        ax.fill(L, B, color=d, alpha=a)

    def type3(self, dec1, d, a, ax):
        x = []
        y = []

        for i in range(0, 360):
            c1 = SkyCoord(ra=i * u.degree, dec=dec1 * u.degree, frame="icrs")
            c1 = c1.galactic
            x.append(c1.l.wrap_at(180 * u.degree).radian)
            y.append(c1.b.wrap_at(180 * u.degree).radian)
        ax.fill(x, y, color=d, alpha=a)

    def type4(self, dec1, d, a, ax):
        c1 = []
        L1 = []
        B1 = []
        L = []
        B = []
        e = 0
        s = 0
        index = 0
        for i in range(0, 360):
            c1.append(SkyCoord(ra=i * u.degree, dec=dec1 * u.degree, frame="icrs"))
            c1[i] = c1[i].galactic
            L1.append(c1[i].l.wrap_at(180 * u.degree))
            B1.append(c1[i].b.wrap_at(180 * u.degree))
        for i in range(0, 360):
            if L1[i] < 0:
                s = math.floor(math.degrees(B1[i].radian))
                e = math.floor(math.degrees(B1[i + 1].radian))
                index = i
                break
        for j in range(index + 1, 360):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        for j in range(0, index):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        j = s
        for i in range(-90, s):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(j, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 1
        for i in range(-90, -90 - e):
            L.append(coord.Angle(-180, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        ax.fill(L, B, color=d, alpha=a)

    def type5(self, dec1, d, a, ax):
        c1 = []
        L1 = []
        B1 = []
        L = []
        B = []
        for i in range(0, 360):
            c1.append(SkyCoord(ra=i * u.degree, dec=dec1 * u.degree, frame="icrs"))
            c1[i] = c1[i].galactic
            L1.append(c1[i].l.wrap_at(180 * u.degree))
            B1.append(c1[i].b.wrap_at(180 * u.degree))
        lat = math.floor(math.degrees(B1[0].radian))
        lon = math.floor(math.degrees(L1[0].radian))
        for i in range(0, 360):
            L.append(L1[i].radian)
            B.append(B1[i].radian)
        for i in range(lon, 179):
            L.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(lat, u.degree).wrap_at(180 * u.degree).radian)
        for i in range(lat, 90):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        j = 90
        for i in range(0, 180):
            L.append(coord.Angle(-180, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(j, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 1
        for i in range(-90, lat + 1):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        j = 179.99
        for i in range(lon, 179):
            L.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(lat - 0.1, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 0.5
        ax.fill(L, B, color=d, alpha=a)

    def type6(self, dec1, d, a, ax):
        c1 = []
        L1 = []
        B1 = []
        L = []
        B = []
        for i in range(0, 360):
            c1.append(SkyCoord(ra=i * u.degree, dec=dec1 * u.degree, frame="icrs"))
            c1[i] = c1[i].galactic
            L1.append(c1[i].l.wrap_at(180 * u.degree))
            B1.append(c1[i].b.wrap_at(180 * u.degree))
        lat = math.floor(math.degrees(B1[0].radian))
        lon = math.floor(math.degrees(L1[0].radian))
        for i in range(0, 360):
            L.append(L1[i].radian)
            B.append(B1[i].radian)
        j = lat
        for i in range(-90, lat):
            L.append(coord.Angle(lon, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(j, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 1
        for i in range(-90, 90):
            L.append(coord.Angle(-180, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        j = 90
        for i in range(-90, 89):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(j, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 1
        for i in range(-89, lat):
            L.append(coord.Angle(lon, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        ax.fill(L, B, color=d, alpha=a)

    def type7(self, dec1, d, a, ax):
        c1 = []
        L1 = []
        B1 = []
        L = []
        B = []
        e = 0
        s = 0
        index1 = 0
        index2 = 0
        for i in range(0, 360):
            c1.append(SkyCoord(ra=i * u.degree, dec=dec1 * u.degree, frame="icrs"))
            c1[i] = c1[i].galactic
            L1.append(c1[i].l.wrap_at(180 * u.degree))
            B1.append(c1[i].b.wrap_at(180 * u.degree))
        for i in range(0, 360):
            if L1[i] < 0:
                e = math.floor(math.degrees(B1[i].radian))
                index1 = i
                break
        for i in range(index1, 360):
            if L1[i] > 0:
                s = math.floor(math.degrees(B1[i + 1].radian))
                index2 = i
                break
        for j in range(index1 + 1, i2 - 1):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        # i = s
        for i in range(s, 90):
            L.append(coord.Angle(-180, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
            # i = i - 1
        j = 90
        for i in range(s, 90):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(j, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 1
        for j in range(index2, 360):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        for j in range(0, index1 - 1):
            L.append(L1[j].radian)
            B.append(B1[j].radian)
        j = e
        for i in range(-90, e):
            L.append(coord.Angle(179.99, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(j, u.degree).wrap_at(180 * u.degree).radian)
            j = j - 1
        for i in range(-90, e):
            L.append(coord.Angle(180, u.degree).wrap_at(180 * u.degree).radian)
            B.append(coord.Angle(i, u.degree).wrap_at(180 * u.degree).radian)
        ax.fill(L, B, color=d, alpha=a)

    def create_ax(self):
        data = plt.imread("./haslam408.png")

        fig = plt.figure(figsize=(15, 15))
        ax0 = fig.add_subplot(111)
        ax0.imshow(data)
        ax0.axis("off")
        ax = fig.add_subplot(111, projection="aitoff", label="polar")
        ax.set_facecolor("None")
        ax.grid()
        ax.set_ylabel("Galactic latitude, b", fontsize=15)
        ax.set_xlabel("Galactic longitude, l", fontsize=15)
        return ax

    def shade_dec(self, c, ax):
        # sur = input('Enter survey name:')
        dec1 = int(input("enter the minimum declination:"))
        dec2 = int(input("enter the maximum declination:"))
        if dec1 > dec2 or dec1 > 90 or dec1 < -90 or dec2 > 90 or dec2 < -90:
            print("Invalid values")
        else:
            if dec2 == 90:
                if dec1 > -26 and dec1 < 28:
                    self.type4(dec1, c, 1, ax)
                elif dec1 > 27 and dec1 < 41:
                    self.type7(dec1, c, 1, ax)
                    # print('a')
                elif dec1 <= -26:
                    # ax.fill_between([coord.Angle(-180,u.degree).radian,coord.Angle(180,u.degree).radian],coord.Angle(-90,u.degree).radian,coord.Angle(90,u.degree).radian, facecolor=c, alpha = 0.5)
                    self.type3(dec1, "w", 1, ax)
                else:
                    self.type6(dec1, c, 1, ax)
            if dec1 == -90:
                if dec2 > -26 and dec2 < 28:
                    # ax.fill_between([coord.Angle(-180,u.degree).radian,coord.Angle(180,u.degree).radian],coord.Angle(-90,u.degree).radian,coord.Angle(90,u.degree).radian, facecolor=c, alpha = 0.5)
                    self.type1(dec2, "w", 1, ax)
                elif dec2 > 27 and dec2 <= 41:
                    # ax.fill_between([coord.Angle(-180,u.degree).radian,coord.Angle(180,u.degree).radian],coord.Angle(-90,u.degree).radian,coord.Angle(90,u.degree).radian, facecolor=c, alpha = 0.5)
                    self.type2(dec2, "w", 1, ax)
                elif dec2 > 41:
                    # ax.fill_between([coord.Angle(-180,u.degree).radian,coord.Angle(180,u.degree).radian],coord.Angle(-90,u.degree).radian,coord.Angle(90,u.degree).radian, facecolor=c, alpha = 0.5)
                    self.type3(dec1, "w", 1, ax)

            if dec1 != 90 and dec2 != 90:
                if dec1 > -26 and dec1 < 28:
                    if dec2 > 27 and dec2 <= 41:
                        self.type4(dec1, "w", 1, ax)
                        self.type2(dec2, "w", 1, ax)
                    elif dec2 > -26 and dec2 < 28:
                        self.type4(dec1, c, 1, ax)
                        self.type1(dec2, "w", 1, ax)
                    else:
                        self.type4(dec1, c, 1, ax)
                        self.type3(dec2, "w", 1, ax)
                elif dec1 > 27 and dec1 <= 41:
                    if dec2 > 27 and dec2 <= 41:
                        self.type7(dec1, c, 1, ax)
                        self.type2(dec2, "w", 1, ax)
                    else:
                        self.type7(dec1, c, 1, ax)
                        self.type3(dec2, "w", 1, ax)
                elif dec1 < -25:
                    if dec2 > 27 and dec2 <= 41:
                        # ax.fill_between([coord.Angle(-180,u.degree).radian,coord.Angle(180,u.degree).radian],coord.Angle(-90,u.degree).radian,coord.Angle(90,u.degree).radian, facecolor=c, alpha = 0.5)
                        self.type2(dec2, "w", 1, ax)
                        self.type3(dec1, "w", 1, ax)
                    elif dec2 > -26 and dec2 < 28:
                        # ax.fill_between([coord.Angle(-180,u.degree).radian,coord.Angle(180,u.degree).radian],coord.Angle(-90,u.degree).radian,coord.Angle(90,u.degree).radian, facecolor=c, alpha = 0.5)
                        self.type1(dec2, "w", 1, ax)
                        self.type3(dec1, "w", 1, ax)
                    elif dec2 < -25:
                        self.type5(dec2, c, 1, ax)
                        self.type3(dec1, "w", 1, ax)
                    else:
                        # ax.fill_between([coord.Angle(-180,u.degree).radian,coord.Angle(180,u.degree).radian],coord.Angle(-90,u.degree).radian,coord.Angle(90,u.degree).radian, facecolor=c, alpha = 0.5)
                        self.type3(dec2, "w", 1, ax)
                        self.type3(dec1, "w", 1, ax)
                else:
                    self.type6(dec1, c, 1, ax)
                    self.type3(dec2, "w", 1, ax)

    def shade_range(self, c, ax):
        # sur = input('Enter survey name:')
        L1 = float(input("Enter minimun longitude:"))
        L2 = float(input("Enter maximum longitude:"))
        B1 = float(input("Enter minimun latitude:"))
        B2 = float(input("Enter maximum latitude:"))
        ax.fill_between(
            [coord.Angle(-180, u.degree).radian, coord.Angle(179.99, u.degree).radian],
            coord.Angle(-90, u.degree).radian,
            coord.Angle(B1, u.degree).radian,
            color=c,
        )
        ax.fill_between(
            [coord.Angle(-180, u.degree).radian, coord.Angle(L1, u.degree).radian],
            coord.Angle(-90, u.degree).radian,
            coord.Angle(90, u.degree).radian,
            color=c,
        )
        ax.fill_between(
            [coord.Angle(L2, u.degree).radian, coord.Angle(179.99, u.degree).radian],
            coord.Angle(-90, u.degree).radian,
            coord.Angle(90, u.degree).radian,
            color=c,
        )
        ax.fill_between(
            [coord.Angle(-180, u.degree).radian, coord.Angle(179, u.degree).radian],
            coord.Angle(B2, u.degree).radian,
            coord.Angle(90, u.degree).radian,
            color=c,
        )

    def accept_choice(self):
        plot_obj = self.create_ax()
        print("Shade the survey region")
        print("1.give the range declnation")
        print("2.give the range of latitude and longitude")
        x = input("enter 1 or 2:")
        if x == "1":
            self.shade_dec("w", plot_obj)
        elif x == "2":
            self.shade_range("w", plot_obj)
        else:
            print("invalid input")
        plt.show()
