#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmines
Version  : 23.08.1
Release  : 57
URL      : https://download.kde.org/stable/release-service/23.08.1/src/kmines-23.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.1/src/kmines-23.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.1/src/kmines-23.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kmines-bin = %{version}-%{release}
Requires: kmines-data = %{version}-%{release}
Requires: kmines-license = %{version}-%{release}
Requires: kmines-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KMINES : the KDE minesweeper
----------------------------
Distributed under the GNU General Public License

%package bin
Summary: bin components for the kmines package.
Group: Binaries
Requires: kmines-data = %{version}-%{release}
Requires: kmines-license = %{version}-%{release}

%description bin
bin components for the kmines package.


%package data
Summary: data components for the kmines package.
Group: Data

%description data
data components for the kmines package.


%package doc
Summary: doc components for the kmines package.
Group: Documentation

%description doc
doc components for the kmines package.


%package license
Summary: license components for the kmines package.
Group: Default

%description license
license components for the kmines package.


%package locales
Summary: locales components for the kmines package.
Group: Default

%description locales
locales components for the kmines package.


%prep
%setup -q -n kmines-23.08.1
cd %{_builddir}/kmines-23.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695076499
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1695076499
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmines
cp %{_builddir}/kmines-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmines/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kmines-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmines/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmines-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmines/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmines-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kmines/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kmines-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmines/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kmines
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kmines
/usr/bin/kmines

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmines.desktop
/usr/share/icons/hicolor/128x128/apps/kmines.png
/usr/share/icons/hicolor/16x16/apps/kmines.png
/usr/share/icons/hicolor/22x22/apps/kmines.png
/usr/share/icons/hicolor/32x32/apps/kmines.png
/usr/share/icons/hicolor/48x48/apps/kmines.png
/usr/share/icons/hicolor/64x64/apps/kmines.png
/usr/share/kmines/themes/classic.desktop
/usr/share/kmines/themes/classic_preview.png
/usr/share/kmines/themes/default.desktop
/usr/share/kmines/themes/default_preview.png
/usr/share/kmines/themes/graveyard-mayhem-preview.png
/usr/share/kmines/themes/graveyard-mayhem.desktop
/usr/share/kmines/themes/graveyard-mayhem.svgz
/usr/share/kmines/themes/green.desktop
/usr/share/kmines/themes/green.png
/usr/share/kmines/themes/kmines_classic.svgz
/usr/share/kmines/themes/kmines_green.svgz
/usr/share/kmines/themes/kmines_oxygen.svgz
/usr/share/metainfo/org.kde.kmines.appdata.xml
/usr/share/qlogging-categories5/kmines.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmines/gameboard.png
/usr/share/doc/HTML/ca/kmines/index.cache.bz2
/usr/share/doc/HTML/ca/kmines/index.docbook
/usr/share/doc/HTML/de/kmines/index.cache.bz2
/usr/share/doc/HTML/de/kmines/index.docbook
/usr/share/doc/HTML/en/kmines/gameboard.png
/usr/share/doc/HTML/en/kmines/index.cache.bz2
/usr/share/doc/HTML/en/kmines/index.docbook
/usr/share/doc/HTML/es/kmines/index.cache.bz2
/usr/share/doc/HTML/es/kmines/index.docbook
/usr/share/doc/HTML/es/kmines/kmines1.png
/usr/share/doc/HTML/es/kmines/kmines2.png
/usr/share/doc/HTML/et/kmines/index.cache.bz2
/usr/share/doc/HTML/et/kmines/index.docbook
/usr/share/doc/HTML/fr/kmines/index.cache.bz2
/usr/share/doc/HTML/fr/kmines/index.docbook
/usr/share/doc/HTML/fr/kmines/kmines1.png
/usr/share/doc/HTML/fr/kmines/kmines2.png
/usr/share/doc/HTML/gl/kmines/index.cache.bz2
/usr/share/doc/HTML/gl/kmines/index.docbook
/usr/share/doc/HTML/it/kmines/index.cache.bz2
/usr/share/doc/HTML/it/kmines/index.docbook
/usr/share/doc/HTML/nl/kmines/index.cache.bz2
/usr/share/doc/HTML/nl/kmines/index.docbook
/usr/share/doc/HTML/pl/kmines/index.cache.bz2
/usr/share/doc/HTML/pl/kmines/index.docbook
/usr/share/doc/HTML/pt/kmines/index.cache.bz2
/usr/share/doc/HTML/pt/kmines/index.docbook
/usr/share/doc/HTML/pt_BR/kmines/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmines/index.docbook
/usr/share/doc/HTML/ru/kmines/index.cache.bz2
/usr/share/doc/HTML/ru/kmines/index.docbook
/usr/share/doc/HTML/sv/kmines/index.cache.bz2
/usr/share/doc/HTML/sv/kmines/index.docbook
/usr/share/doc/HTML/sv/kmines/kmines1.png
/usr/share/doc/HTML/sv/kmines/kmines2.png
/usr/share/doc/HTML/uk/kmines/gameboard.png
/usr/share/doc/HTML/uk/kmines/index.cache.bz2
/usr/share/doc/HTML/uk/kmines/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmines/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmines/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kmines/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kmines/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmines/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kmines.lang
%defattr(-,root,root,-)

