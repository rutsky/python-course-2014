EXPORT_DIR = ../rutsky.github.io/python-course-2014/

DIRS = 01_introduction 02_modules_scopes 03_unicode_io_exceptions 04_bindings_pygame

rebuild:
	$(foreach DIR,$(DIRS),make -C $(DIR) clean slides;)

copy-presentations:
	$(foreach DIR,$(DIRS),rm -rf $(EXPORT_DIR)/$(DIR); cp -r $(DIR)/_build/slides/ $(EXPORT_DIR)/$(DIR);)

zip-presentations:
	$(foreach DIR,$(DIRS),cd $(EXPORT_DIR); zip -r $(DIR).zip $(DIR);)
