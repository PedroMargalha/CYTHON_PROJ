build:
	easycython fib_cy.py
	easycython *.pyx
	python setup.py build_ext -if


clean:
	@echo "Passando a vassoura no pó"
	rm -rf __pycache__
	rm -r *.so
	rm -r f*.c
	rm -rf build 
	rm -rf *.html
	rm -rf prof*