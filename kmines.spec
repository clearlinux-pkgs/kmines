#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmines
Version  : 19.12.2
Release  : 16
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kmines-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kmines-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kmines-19.12.2.tar.xz.sig
Summary  : The classic Minesweeper game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kmines-bin = %{version}-%{release}
Requires: kmines-data = %{version}-%{release}
Requires: kmines-license = %{version}-%{release}
Requires: kmines-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kmines-19.12.2
cd %{_builddir}/kmines-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581026387
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581026387
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmines
cp %{_builddir}/kmines-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/kmines/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kmines-19.12.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kmines/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/kmines-19.12.2/LICENSE %{buildroot}/usr/share/package-licenses/kmines/2169315544493c7e4a5dd8bac41b70ab63ec417e
pushd clr-build
%make_install
popd
%find_lang kmines

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/package-licenses/kmines/2169315544493c7e4a5dd8bac41b70ab63ec417e
/usr/share/package-licenses/kmines/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kmines/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kmines.lang
%defattr(-,root,root,-)

