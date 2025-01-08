#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : ksystemstats
Version  : 6.2.5
Release  : 61
URL      : https://download.kde.org/stable/plasma/6.2.5/ksystemstats-6.2.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.2.5/ksystemstats-6.2.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.2.5/ksystemstats-6.2.5.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0
Requires: ksystemstats-bin = %{version}-%{release}
Requires: ksystemstats-data = %{version}-%{release}
Requires: ksystemstats-lib = %{version}-%{release}
Requires: ksystemstats-license = %{version}-%{release}
Requires: ksystemstats-locales = %{version}-%{release}
Requires: ksystemstats-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : libksysguard-dev
BuildRequires : lm-sensors-dev
BuildRequires : networkmanager-qt-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-route-3.0)
BuildRequires : qt6base-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KSystemStats
============
KSystemStats is a daemon that collects statistics about the running system.

%package bin
Summary: bin components for the ksystemstats package.
Group: Binaries
Requires: ksystemstats-data = %{version}-%{release}
Requires: ksystemstats-license = %{version}-%{release}
Requires: ksystemstats-services = %{version}-%{release}

%description bin
bin components for the ksystemstats package.


%package data
Summary: data components for the ksystemstats package.
Group: Data

%description data
data components for the ksystemstats package.


%package lib
Summary: lib components for the ksystemstats package.
Group: Libraries
Requires: ksystemstats-data = %{version}-%{release}
Requires: ksystemstats-license = %{version}-%{release}

%description lib
lib components for the ksystemstats package.


%package license
Summary: license components for the ksystemstats package.
Group: Default

%description license
license components for the ksystemstats package.


%package locales
Summary: locales components for the ksystemstats package.
Group: Default

%description locales
locales components for the ksystemstats package.


%package services
Summary: services components for the ksystemstats package.
Group: Systemd services
Requires: systemd

%description services
services components for the ksystemstats package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n ksystemstats-6.2.5
cd %{_builddir}/ksystemstats-6.2.5
pushd ..
cp -a ksystemstats-6.2.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736201687
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
%cmake .. -DBUILD_TESTING=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
%cmake .. -DBUILD_TESTING=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1736201687
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksystemstats
cp %{_builddir}/ksystemstats-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/ksystemstats/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/ksystemstats-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksystemstats/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/ksystemstats-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksystemstats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ksystemstats-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/ksystemstats/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/ksystemstats-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ksystemstats/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/ksystemstats-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/ksystemstats/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/ksystemstats-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/ksystemstats/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/cpu/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/disks/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/gpu/autotests/fixtures/520.txt.license %{buildroot}/usr/share/package-licenses/ksystemstats/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/gpu/autotests/fixtures/525.txt.license %{buildroot}/usr/share/package-licenses/ksystemstats/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/gpu/autotests/fixtures/530.txt.license %{buildroot}/usr/share/package-licenses/ksystemstats/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/gpu/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/lmsensors/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/memory/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/network/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/osinfo/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/power/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
cp %{_builddir}/ksystemstats-%{version}/plugins/pressure/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang ksystemstats_plugins
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kstatsviewer
/V3/usr/bin/ksystemstats
/usr/bin/kstatsviewer
/usr/bin/ksystemstats

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.kde.ksystemstats1.service

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_cpu.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_disk.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_gpu.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_lmsensors.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_memory.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_network.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_osinfo.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_power.so
/V3/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_pressure.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_cpu.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_disk.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_gpu.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_lmsensors.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_memory.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_network.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_osinfo.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_power.so
/usr/lib64/qt6/plugins/ksystemstats/ksystemstats_plugin_pressure.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksystemstats/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
/usr/share/package-licenses/ksystemstats/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/ksystemstats/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/ksystemstats/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/ksystemstats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ksystemstats/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/ksystemstats/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/ksystemstats/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-ksystemstats.service

%files locales -f ksystemstats_plugins.lang
%defattr(-,root,root,-)

