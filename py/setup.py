r"""Setup."""
import platform
import shutil
import pathlib
import subprocess
from setuptools import setup, Extension

LIBSDARWIN = ("libgfortran.5", "libquadmath.0", "libgcc_s.1.1")
LIBSWINDOWS = ("libgfortran-5", "libquadmath-0", "libgcc_s_seh-1", "libwinpthread-1")
LIBSLINUX = []
ROOTLINUX = "/usr/lib/"
ROOTDARWIN = "/usr/local/opt/gcc/lib/gcc/current"
ROOTWINDOWS = "C:/msys64/mingw64/bin"
ROOT = ROOTLINUX
LIBS = LIBSLINUX

name = "ecx"
libraries = None
library_dirs = None
runtime_library_dirs = None
extra_objects = None
ext = [".so"]


if platform.system() == "Linux":
    libraries = [name]
    library_dirs = [f"./src/py{name:s}"]
    runtime_library_dirs = ["$ORIGIN"]
    ext = [".so"]
    ROOT = ROOTLINUX
    LIBS = LIBSLINUX
if platform.system() == "Windows":
    extra_objects = [f"./src/py{name:s}/lib{name:s}.dll.a"]
    ext = [".dll", ".dll.a"]
    ROOT = ROOTWINDOWS
    LIBS = LIBSWINDOWS
if platform.system() == "Darwin":
    libraries = [name]
    library_dirs = [f"./src/py{name:s}"]
    runtime_library_dirs = ["@loader_path"]
    ext = [".dylib"]
    ROOT = ROOTDARWIN
    LIBS = LIBSDARWIN


## Headers
#root_src = pathlib.Path(f"./src/py{name:s}/include/")
#root_dest = pathlib.Path(f"./src/py{name:s}/")
#files = [f"{name:s}.h"]
#for file in files:
#    src = root_src / file
#    dest = root_dest / file
#    if not src.exists():
#        raise ValueError(f"The library {name:s} was not installed. Run in the root folder: make install prefix=./py/src/py{name:s}")
#    try:
#        print(f"copying {str(src):s} -> {str(dest.parent):s}.")
#        shutil.copy(src, dest)
#    except:
#        print(f"{file:s} was not copied.")
#
## Libs
#root_src = pathlib.Path(f"./src/py{name:s}/lib/")
#root_dest = pathlib.Path(f"./src/py{name:s}/")
#files = list(map(lambda s: f"lib{name:s}"+s, ext))
#for file in files:
#    src = root_src / file
#    dest = root_dest / file
#    if not src.exists():
#        raise ValueError(f"The library {name:s} was not installed. Run in the root folder: make install prefix=./py/src/py{name:s}")
#    try:
#        print(f"copying {str(src):s} -> {str(dest.parent):s}.")
#        shutil.copy(src, dest)
#    except:
#        print(f"{file:s} was not copied.")
#
## gfortran libs
#root_src = pathlib.Path(ROOT)
#root_dest = pathlib.Path(f"./src/py{name:s}/")
#files = LIBS
#for file in files:
#    src = root_src / (file + ext[0])
#    dest = root_dest / (file + ext[0])
#    cmd = ["install_name_tool", "-change", f"{str(src):s}", f"@loader_path/{src.name}", f"./src/py{name:s}/lib{name:s}{ext[0]:s}"]
#    try:
#        print(f"copying {str(src):s} -> {str(dest.parent):s}.")
#        shutil.copy(src, dest)
#        if platform.system() == "Darwin":
#            print(f"changing rpath for {str(file):s}")
#            subprocess.check_call(cmd)
#    except subprocess.CalledProcessError:
#        print(" ".join(cmd) + " was not successful.")
#    except:
#        print(f"{file:s} was not copied.")
#
## check rpaths for Darwin
#if platform.system() == "Darwin":
#    cmd = ["otool", "-L", f"./src/py{name:s}/lib{name:s}{ext[0]:s}"]
#    try:
#        print(f"checking rpaths")
#        subprocess.check_call(cmd)
#    except subprocess.CalledProcessError:
#        print(" ".join(cmd) + " was not successful.")

version = None
with open("./VERSION", "r") as f:
    version = f.read().strip()


if __name__ == "__main__":
    
    mod_version = Extension(name="pyecx.version",
                         sources=["./src/pyecx/cpy_version.c"],
                         libraries=libraries,
                         library_dirs=library_dirs,
                         runtime_library_dirs=runtime_library_dirs,
                         extra_objects=extra_objects)
    mod_eis = Extension(name="pyecx.eis",
                        sources=["./src/pyecx/cpy_eis.c", "./src/pyecx/cpy_common.c"],
                        libraries=libraries,
                        library_dirs=library_dirs,
                        runtime_library_dirs=runtime_library_dirs,
                        extra_objects=extra_objects)
    mod_core = Extension(name="pyecx.core",
                         sources=["./src/pyecx/cpy_core.c", "./src/pyecx/cpy_common.c"],
                         libraries=libraries,
                         library_dirs=library_dirs,
                         runtime_library_dirs=runtime_library_dirs,
                         extra_objects=extra_objects)

    setup(version=version,
          ext_modules=[mod_version, mod_core, mod_eis])

