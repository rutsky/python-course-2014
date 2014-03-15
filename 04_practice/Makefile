all:
	rst2html.py practice03.rst > practice03.html
	rst2xetex.py practice03.rst | xelatex -jobname=practice03

clean:
	rm -f practice03.html
	rm -f practice03.pdf
	rm -f *.aux *.log *.out
