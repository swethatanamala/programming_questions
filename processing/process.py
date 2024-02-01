from multiprocessing import Process

def f(name):
	print("hello ", name)

if __name__ == "__main__":
	p1 = Process(target=f, args=('bob', ))
	p1.start()
	p1.join()
	p2 = Process(target=f, args=('swetha', ))
	p2.start()
	p2.join()
