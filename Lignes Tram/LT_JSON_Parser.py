from LT_Classes import *

from pprint import pprint
from json import dumps, loads

def OpenJson(filename: str) -> dict:
	fp = open(filename, "r", encoding="utf8")

	RawJson: str = fp.read()
	fp.close()

	DictJson: dict = loads(RawJson)

	return DictJson

def GetListLignes(TramJson: dict) -> list[Ligne]:
	features: list[dict] = TramJson.get("features")

	for f in features:
		L: Ligne = Ligne()
		geometry: dict | None = f.get("geometry")

		if (geometry != None):
			track: list[list[float, float]] | None = None

			if (track != None):
				track: list[tuple[float, float]] = [tuple(coords) for coords in track]
				L.track += track
			else:
				raise Exception("Error : Couldn't find \"geometry.coordinates\"")

		else:
			raise Exception("Error : Couldn't find \"geometry\"")

FICHIER = OpenJson("Datasets/MMM_MMM_LigneTram.json")
GetListLignes(FICHIER)