"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # Constructor accepts parsed NEO fields directly.
    def __init__(self, designation, name=None, diameter=float('nan'), hazardous=False):
        """Create a new NearEarthObject.

        :param designation: The primary designation for this NEO.
        :param name: The optional IAU name for this NEO.
        :param diameter: The optional diameter, in kilometers, for this NEO.
        :param hazardous: Whether this NEO is potentially hazardous.
        """
        # Normalize incoming raw values to stable internal types.
        self.designation = str(designation)
        self.name = str(name).strip() if name not in (None, '') else None
        self.diameter = float(diameter) if diameter not in (None, '') else float('nan')
        if isinstance(hazardous, str):
            self.hazardous = hazardous.upper() == 'Y'
        else:
            self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        
        # Build "{designation} ({name})" when name exists, otherwise designation.
        if self.name:
            return f"{self.designation} ({self.name})"
        return self.designation

    def __str__(self):
        """Return `str(self)`."""
        
        # Human-readable NEO summary.
        hazard_text = "is" if self.hazardous else "is not"
        return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and {hazard_text} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # Constructor accepts parsed close-approach fields directly.
    def __init__(self, des='', cd=None, dist=0.0, v_rel=0.0):
        """Create a new `CloseApproach`.

        :param des: The primary designation of the associated NEO.
        :param cd: The close-approach date/time string from NASA data.
        :param dist: The nominal approach distance in astronomical units.
        :param v_rel: The relative approach velocity in km/s.
        """
        self._designation = str(des)
        self.time = cd_to_datetime(cd) if cd else None
        self.distance = float(dist) if dist not in (None, '') else 0.0
        self.velocity = float(v_rel) if v_rel not in (None, '') else 0.0

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        if self.time is None:
            return ''
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        
        # Human-readable close-approach summary.
        fullname = self.neo.fullname if self.neo is not None else self._designation
        return (
            f"On {self.time_str}, '{fullname}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."
        )

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
