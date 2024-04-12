#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v8
# autospec commit: 658bd0d
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmines
Version  : 24.02.2
Release  : 65
URL      : https://download.kde.org/stable/release-service/24.02.2/src/kmines-24.02.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.2/src/kmines-24.02.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.2/src/kmines-24.02.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-SA-4.0 CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kmines-bin = %{version}-%{release}
Requires: kmines-data = %{version}-%{release}
Requires: kmines-license = %{version}-%{release}
Requires: kmines-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep '^\[GNUPG:\] GOODSIG BB463350D6EF31EF' gpg.status
%setup -q -n kmines-24.02.2
cd %{_builddir}/kmines-24.02.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712882506
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1712882506
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmines
cp %{_builddir}/kmines-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmines/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kmines-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmines/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmines-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/kmines/f26cccd93362d640ef2c05d1c52b5efe1620a9b2 || :
cp %{_builddir}/kmines-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmines/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmines-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kmines/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kmines-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmines/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
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
/usr/share/kmines/themes/clean_blue.desktop
/usr/share/kmines/themes/clean_blue_dark.desktop
/usr/share/kmines/themes/clean_blue_dark_preview.png
/usr/share/kmines/themes/clean_blue_preview.png
/usr/share/kmines/themes/default.desktop
/usr/share/kmines/themes/default_preview.png
/usr/share/kmines/themes/graveyard-mayhem-preview.png
/usr/share/kmines/themes/graveyard-mayhem.desktop
/usr/share/kmines/themes/graveyard-mayhem.svgz
/usr/share/kmines/themes/green.desktop
/usr/share/kmines/themes/green.png
/usr/share/kmines/themes/kmines_classic.svgz
/usr/share/kmines/themes/kmines_clean_blue.svg
/usr/share/kmines/themes/kmines_clean_blue_dark.svg
/usr/share/kmines/themes/kmines_green.svgz
/usr/share/kmines/themes/kmines_oxygen.svgz
/usr/share/metainfo/org.kde.kmines.appdata.xml
/usr/share/qlogging-categories6/kmines.categories

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
/usr/share/package-licenses/kmines/f26cccd93362d640ef2c05d1c52b5efe1620a9b2

%files locales -f kmines.lang
%defattr(-,root,root,-)

