%define _unpackaged_files_terminate_build 1

Name: sdl2-examples
Version: 1.0
Release: alt1
Summary: sdl2-examples
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/xyproto/sdl2-examples.git
VCS: https://github.com/xyproto/sdl2-examples.git
Source0: %name-%version.tar
Patch1: 0001-fix_c18_img_path.patch

BuildRequires: gcc
BuildRequires: libSDL2-devel

%description
sdl2-examples.

%package c18
Group: Development/Other
Summary: c18

%description c18
c18.

%prep
%setup -n %name-%version
%patch1 -p1

%build
%make -C c18

%install
mkdir -p %buildroot/usr/share/sdl2-examples/
cp img/grumpy-cat.bmp %buildroot/usr/share/sdl2-examples/grumpy-cat.bmp
cp img/grumpy-cat.png %buildroot/usr/share/sdl2-examples/grumpy-cat.png

mkdir -p %buildroot/usr/bin
cp c18/main %buildroot/usr/bin/sdl2-examples-c18

%files c18
%_usr/share/sdl2-examples/grumpy-cat.bmp
%_usr/share/sdl2-examples/grumpy-cat.png
%_bindir/sdl2-examples-c18

%changelog
* Wed Nov 27 2024 Andrew Lihomanov <lihomanov0202@inbox.ru> 1.0-alt1
-Initial build.
