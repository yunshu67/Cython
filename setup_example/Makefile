
all:setup
cfile =impl_in_C
newModule=newModule
setup:setup.py $(newModule).pyx $(cfile).c 
	python3 setup.py build_ext --inplace && rm -rf $(newModule).c build $(cfile).o && mv *.so $(newModule).so

.PHONY: clean

clean:
	rm -rf $(newModule).so

