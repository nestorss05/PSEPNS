from Clases import *

def main():
	p1 = Producto("Tacos de caca", 20)
	p2 = Perecedero("Tacos de caca oxidados", 10, 2)
	p3 = NoPerecedero("Tacos de cada pro", 30, "Esquizofrenico")
	print(p1)
	print(p2)
	print(p3)

if __name__ == "__main__":
	main()