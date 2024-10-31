from __future__ import annotations
from GeoMaths import *

class Ligne:
	def __init__(self) -> None:
		self.track: list[tuple[float, float]] = []
		self.NumExploit: int = 0
		self.LigneID: int = 0
		self.NomLigne: str = ""
		self.direction: int = 0

		self.totalLength: float = 0.0

	def ComputeDistance(self) -> float:
		distance: float = 0.0

		for i in range(len(self.track[:-1])):
			j: int = i + 1

			coordsA: tuple[float, float] = self.track[i][::-1]
			coordsB: tuple[float, float] = self.track[j][::-1]

			distance += Haversine(*coordsA, *coordsB)

		self.totalLength = distance

	def AddArretToLigne(self, arret: Arret) -> int:
		"""Ajoute un arrêt au tracé de la ligne et retourne l'index de ces coordonnées dans la liste"""

		return 0

	def __str__(self) -> str:
		output: str = f"Ligne(\n\tNomLigne={self.NomLigne}\n\ttrack size: {len(self.track)} points\n\tNumExploit={self.NumExploit}\n\tLigneID={self.LigneID}\n\tDirection={self.direction}\n\ttotalLength={self.totalLength}\n)"

		return output

	def __repr__(self) -> str:
		return self.__str__()

class Arret:
	def __init__(self) -> None:
		self.nom = ""
		self.GeoCoords: tuple[float, float] = ()
		self.MtpCoords: tuple[float, float] = ()
		self.id = 0