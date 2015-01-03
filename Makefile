#PDFS = 01_introduction 02_modules_scopes 03_unicode_io_exceptions 04_bindings_pygame 05_oop_classes 06_iterators_decorators 07_network 08_web 10_math
PDFS = 10_math

cut:
	$(foreach PDF,$(PDFS),gs -o $(PDF).pdf -sDEVICE=pdfwrite -c "[/CropBox [59 416 536 782] /PAGES pdfmark" -f $(PDF)_orig.pdf;)
