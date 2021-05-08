install:
	pip3 install -e .

solve: install
	python3 -m solver.solver
