EXPORT_DIR = ../rutsky.github.io/python-course-2014/

DIRS = 01_introduction 02_modules_scopes 03_unicode_io_exceptions 04_bindings_pygame 05_oop_classes 06_iterators_decorators 07_network 08_web 09_interoperability 10_math

rebuild:
	$(foreach DIR,$(DIRS),make -C $(DIR) clean slides;)

copy-presentations:
	$(foreach DIR,$(DIRS),rm -rf $(EXPORT_DIR)/$(DIR); cp -r $(DIR)/_build/slides/ $(EXPORT_DIR)/$(DIR);)

zip-presentations:
	$(foreach DIR,$(DIRS),cd $(EXPORT_DIR); zip -r $(DIR).zip $(DIR);)
