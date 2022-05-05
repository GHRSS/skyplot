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
from astropy.coordinates import SkyCoord
from astropy.units import degree, hourangle


here = Path(__file__)
here = here.resolve()
here = here.parent
data = here / "data"


def beams():
    centers: List[str] = []
    with open(data / "GHRSS.list.obsvd", "r") as lines:
        for line in lines:
            line = line.strip()
            suffix = line.replace("HR_", "")
            ra, dec = suffix.split("-")
            ra = ":".join([ra[:2], ra[2:]])
            dec = ":".join([dec, "00"])
            dec = "".join(["-", dec])
            centers.append(" ".join([ra, dec]))
    return SkyCoord(centers, frame="icrs", unit=(hourangle, degree))


@define
class SkyPlot:

    """
    Class that plots the sky coverage and discoveries of the GHRSS survey.
    """

    beams: SkyCoord

    @classmethod
    def create(cls):
        return cls(beams=beams())

    def plot(self):

        gl = self.beams.galactic.l.wrap_at(180 * degree).radian
        gb = self.beams.galactic.b.wrap_at(180 * degree).radian

        ax = plt.subplot(111, projection="aitoff")
        ax.scatter(gl, gb)
        ax.grid(True)
        plt.tight_layout()
        plt.show()
