all:
	rst2html.py practice03.rst > practice03.html
	rst2xetex.py practice03.rst | xelatex -jobname=practice03
	for f in *.py; do pygmentize -l py3 -f html -O full,style=pastie,encoding=utf-8 -o $${f%.*}.html $$f; done

clean:
	rm -f practice03.html
	rm -f practice03.pdf
	rm -f *.aux *.log *.out
	for f in *.py; do rm -f $${f%.*}.html; done
