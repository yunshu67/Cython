from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from os import system as sys

cfile='impl_in_C'
newmodule='newModule'
shared_obj=f'gcc {cfile}.c -fPIC -c -o {cfile}.o'
print(shared_obj)
sys(shared_obj)

# extension module setup
ext_modules=[Extension(name=f"{newmodule}",
                         sources=[f"{newmodule}.pyx"],
                       extra_compile_args=["-fPIC","-O3"],
                         extra_link_args=[f"{cfile}.o"]
                         )]

# calling setup
setup(name=f'{newmodule}',cmdclass={'build_ext':build_ext},ext_modules=ext_modules)