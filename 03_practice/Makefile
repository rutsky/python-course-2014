all:
	rst2html.py practice02.rst > practice02.html
	rst2xetex.py practice02.rst | xelatex -jobname=practice02

clean:
	rm -f practice02.html
	rm -f practice02.pdf
	rm -f *.aux *.log *.out
