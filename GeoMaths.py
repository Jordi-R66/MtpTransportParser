from math import cos, sin, acos, pi

# ----------------------------------------------------------------------

DEGREES: float = 180 / (2 * pi)
RADIANS: float = 2 * pi / 180

# ----------------------------------------------------------------------

R_POLE: float = 6_356_752.314245179497563967
R_EQUA: float = 6_378_137.0

R_TERRE: float = (2*R_EQUA + R_POLE) / 3

# ----------------------------------------------------------------------

MTP_CENTER: tuple[float, float] = 43.61081089705258, 3.8766503042297473

# ----------------------------------------------------------------------

def Haversine(latA: float, lngA: float, latB: float = MTP_CENTER[0], lngB: float = MTP_CENTER[1]) -> float:
	"""
		latA, lngA : latitude & longitude of point A (floats)
		latB, lngB : latitude & longitude of point B (floats)
		Output : Great Circle Distance (Haversine) between these two points (float)
	"""

	delta_lng: float = lngB - lngA

	latA *= RADIANS
	latB *= RADIANS

	lngA *= RADIANS
	lngB *= RADIANS

	S_AB: float = acos(sin(latA) * sin(latB) + cos(latA) * cos(latB) * cos(delta_lng))

	D: float = R_TERRE * S_AB

	return D

if __name__ == "__main__":
	pass
