all:
	pygmentize -l pycon -f html -O full,style=pastie,encoding=utf-8 -o practice01_1_answer.html practice01_1_answer.pycon
	pygmentize -l pycon -f html -O full,style=pastie,encoding=utf-8 -o practice01_2_answer.html practice01_2_answer.pycon
	rst2html.py practice01.rst > practice01.html
	rst2xetex.py practice01.rst | xelatex -jobname=practice01
	rst2xetex.py practice01_1_answer.pycon | xelatex -jobname=practice01_1_answer
	rst2xetex.py practice01_2_answer.pycon | xelatex -jobname=practice01_2_answer

clean:
	rm -f practice01.html practice01_1_answer.html practice01_2_answer.html
	rm -f practice01.pdf practice01_1_answer.pdf practice01_2_answer.pdf
	rm -f *.aux *.log *.out
