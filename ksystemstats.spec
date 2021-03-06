#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : ksystemstats
Version  : 5.25.3
Release  : 19
URL      : https://download.kde.org/stable/plasma/5.25.3/ksystemstats-5.25.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.3/ksystemstats-5.25.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.3/ksystemstats-5.25.3.tar.xz.sig
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
BuildRequires : ki18n-dev
BuildRequires : libksysguard-dev
BuildRequires : lm-sensors-dev
BuildRequires : networkmanager-qt-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-route-3.0)
BuildRequires : systemd-dev

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

%description services
services components for the ksystemstats package.


%prep
%setup -q -n ksystemstats-5.25.3
cd %{_builddir}/ksystemstats-5.25.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657649618
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DBUILD_TESTING=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657649618
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksystemstats
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/ksystemstats/ea97eb88ae53ec41e26f8542176ab986d7bc943a
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksystemstats/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksystemstats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/ksystemstats/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksystemstats/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ksystemstats/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/ksystemstats/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/ksystemstats-5.25.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/ksystemstats/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/ksystemstats-5.25.3/plugins/cpu/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
cp %{_builddir}/ksystemstats-5.25.3/plugins/disks/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
cp %{_builddir}/ksystemstats-5.25.3/plugins/gpu/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
cp %{_builddir}/ksystemstats-5.25.3/plugins/lmsensors/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
cp %{_builddir}/ksystemstats-5.25.3/plugins/memory/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
cp %{_builddir}/ksystemstats-5.25.3/plugins/network/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
cp %{_builddir}/ksystemstats-5.25.3/plugins/osinfo/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
cp %{_builddir}/ksystemstats-5.25.3/plugins/power/metadata.json.license %{buildroot}/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
pushd clr-build
%make_install
popd
%find_lang ksystemstats_plugins

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kstatsviewer
/usr/bin/ksystemstats

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.kde.ksystemstats.service

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_cpu.so
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_disk.so
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_gpu.so
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_lmsensors.so
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_memory.so
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_network.so
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_osinfo.so
/usr/lib64/qt5/plugins/ksystemstats/ksystemstats_plugin_power.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksystemstats/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/ksystemstats/4eaf911568a0c644a8b15fc8b348e89eae0a50f5
/usr/share/package-licenses/ksystemstats/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/ksystemstats/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/ksystemstats/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/ksystemstats/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ksystemstats/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/ksystemstats/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/ksystemstats/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-ksystemstats.service

%files locales -f ksystemstats_plugins.lang
%defattr(-,root,root,-)

