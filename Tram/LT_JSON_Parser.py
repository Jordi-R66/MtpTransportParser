from Tram_Classes import *

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

	Lignes: list[Ligne] = []

	for f in features:
		L: Ligne = Ligne()

		geometry: dict | None = f.get("geometry")
		properties: dict | None = f.get("properties")

		if (type(geometry) == dict):
			track: list[list[float, float]] | None = geometry.get("coordinates")

			if (track != None):
				track: list[tuple[float, float]] = [tuple(coords) for coords in track]
				L.track += track
			else:
				raise Exception("Error : Couldn't find \"geometry.coordinates\"")

		else:
			raise Exception("Error : Couldn't find \"geometry\"")

		L.ComputeDistance()

		if (type(properties) == dict):
			nom_ligne: str | None = properties.get("nom_ligne")
			num_exploit: int | None = properties.get("num_exploitation")
			ligne_id: str | None = properties.get("id_lignes_sens")

			if (type(nom_ligne) == str):
				L.NomLigne = nom_ligne

			if (type(num_exploit) == int):
				L.NumExploit = num_exploit
			
			if (type(ligne_id) == str):
				L.LigneID = int(ligne_id.replace("IDLTRAM", ""))

		else:
			raise Exception("Error : Couldn't find \"properties\"")

		Lignes.append(L)

	return Lignes

fichier = OpenJson("Datasets/MMM_MMM_LigneTram.json")
GetListLignes(fichier)