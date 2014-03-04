all:
	for f in *.py; do pygmentize -l pycon -f html -O full,style=pastie,encoding=utf-8 -o $${f%.*}.html $$f; done

clean:
	for f in *.py; do rm -f $${f%.*}.html; done
