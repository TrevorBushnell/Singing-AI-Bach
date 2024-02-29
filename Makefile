publish:
	jb build paper/ && ghp-import -n -p -f ./paper/_build/html
