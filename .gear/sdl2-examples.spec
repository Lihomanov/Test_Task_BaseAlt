%define _unpackaged_files_terminate_build 1

Name: sdl2-examples
Version: 1.0
Release: alt3
Summary: sdl2-examples
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/xyproto/sdl2-examples.git
VCS: https://github.com/xyproto/sdl2-examples.git
Source0: %name-%version.tar
Patch1: 0001-fix_c18_img_path.patch
Patch2: 0002-fix_c11_img_path.patch
Patch3: 0003-fix_python_img_path.patch

BuildRequires: gcc, python3-module-sdl2, rpm-build-python3
BuildRequires: libSDL2-devel

%description
sdl2-examples.

%package c18
Group: Development/Other
Summary: c18
Requires: sdl2-examples-images

%package c11
Group: Development/Other
Summary: c11
Requires: sdl2-examples-images

%package images
Group: Development/Other
Summary: sdl2-examples-images

%package python
Group: Development/Other
Summary: python
Requires: sdl2-examples-images

%description c18
c18.

%description c11
c11.

%description python
python.

%description images
sdl2-examples-images.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make -C c18
%make -C c11

%install
mkdir -p %buildroot/usr/share/sdl2-examples/
cp img/grumpy-cat.bmp %buildroot/usr/share/sdl2-examples/grumpy-cat.bmp
cp img/grumpy-cat.png %buildroot/usr/share/sdl2-examples/grumpy-cat.png

mkdir -p %buildroot/usr/bin
cp c18/main %buildroot/usr/bin/sdl2-examples-c18
cp c11/main %buildroot/usr/bin/sdl2-examples-c11
cp python/main.py  %buildroot/usr/bin/sdl2-examples-python

%files images
%_usr/share/sdl2-examples/grumpy-cat.bmp
%_usr/share/sdl2-examples/grumpy-cat.png

%files c18
%_bindir/sdl2-examples-c18

%files c11
%_bindir/sdl2-examples-c11

%files python
%_bindir/sdl2-examples-python

%changelog
* Sun Dec 01 2024 Andrew Lihomanov <lihomanov0202@inbox.ru> 1.0-alt3
- Add build for python changing image's path.

* Sun Dec 01 2024 Andrew Lihomanov <lihomanov0202@inbox.ru> 1.0-alt2
- Add build for c11 changing image's path.

* Wed Nov 27 2024 Andrew Lihomanov <lihomanov0202@inbox.ru> 1.0-alt1
- Initial build.
