install:
	pip3 install -e .

solve-bfs:
	python3 -m solver.solver bfs

solve-dfs: 
ifdef max_depth
	python3 -m solver.solver dfs --max_depth $(max_depth)
else
	python3 -m solver.solver dfs
endif

solve-idfs:
	python3 -m solver.solver idfs
