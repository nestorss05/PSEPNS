class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        frase = "(" + str(self.x) + "," + str(self.y) + ")"
        return frase

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def desplaza(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distancia(self, punto):
        difx = self.x - punto.x
        dify = self.y - punto.y
        res = difx + dify
        return res