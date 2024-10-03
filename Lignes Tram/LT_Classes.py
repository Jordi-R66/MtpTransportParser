class Ligne:
	def __init__(self) -> None:
		self.track: list[tuple[float, float]] = []
		self.NumExploit: int = 0
		self.LigneID: int = 0
		self.NomLigne: str = ""
		self.direction: int = 0

		self.totalDistance: float = 0.0
