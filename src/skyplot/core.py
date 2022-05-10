"""
Plot the sky coverage and discoveries of the GHRSS survey.

`skyplot` allows the user to plot the sky coverage of the GMRT High Resolution
Southern Sky (GHRSS) survey, in either equatorial and galactic coordinates. It
then adds the objects discovered in Phases I and II of the survey to the same
plot, classified by type, and saves it to the desired image format. It can also
create interactive versions of the same plot, which can be used to display it on
the web.
"""

import matplotlib.pyplot as plt

from typing import List
from attrs import define
from pathlib import Path
from astropy.coordinates import Angle
from astropy.coordinates import SkyCoord
from astropy.units import degree, hourangle


here = Path(__file__)
here = here.resolve()
here = here.parent
data = here / "data"


def extract_beams(fname: str):

    """
    Extract the center coordinates of beams in the GHRSS survey.
    """

    centers: List[str] = []
    with open(data / f"{fname}", "r") as lines:
        for line in lines:
            line = line.strip()
            suffix = line.replace("HR_", "")
            ra, dec = suffix.split("-")
            ra = ":".join([ra[:2], ra[2:]])
            dec = ":".join([dec, "00"])
            dec = "".join(["-", dec])
            centers.append(" ".join([ra, dec]))
    return centers


def get_galactic(coords: SkyCoord):

    """
    Return galactic coordinates from a given SkyCoord object.
    """

    return zip(
        *[
            (l, b)
            for (l, b) in zip(
                coords.galactic.l.wrap_at(180 * degree).radian,
                coords.galactic.b.wrap_at(180 * degree).radian,
            )
            if (b < Angle(-5 * degree).radian) or (b > Angle(5 * degree).radian)
        ]
    )


@define
class Sky:

    """
    Class that plots the sky coverage and discoveries of the GHRSS survey.
    """

    beams: SkyCoord
    observed: SkyCoord
    unobserved: SkyCoord

    @classmethod
    def create(cls):

        """
        Create an instance of the `Sky` class.
        """

        beams = extract_beams("GHRSS.list")
        observed = extract_beams("GHRSS.list.obsvd")
        unobserved = [beam for beam in beams if beam not in observed]

        return cls(
            *[
                SkyCoord(
                    coord,
                    frame="icrs",
                    unit=(hourangle, degree),
                )
                for coord in [beams, observed, unobserved]
            ]
        )

    def plot(self):

        """
        Plot the sky coverage for the GHRSS survey.
        """

        ax = plt.subplot(projection="aitoff")
        ax.scatter(*get_galactic(self.observed))
        ax.scatter(*get_galactic(self.unobserved))
        ax.set_title("The GHRSS Survey")
        ax.set_ylabel("Galactic Latitude, b")
        ax.set_xlabel("Galactic Longitude, l")
        plt.tight_layout()
        plt.show()
