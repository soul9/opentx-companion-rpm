
Summary: OpenTX Companion
Name: opentx-companion

%global commit0 b55b68f191cfa22dee396ee2842e9fb836d9664f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Version: 2.2.1
Release: git_%{shortcommit0}.1%{?dist}
License: GPLv2
URL: http://www.open-tx.org
Source0: https://github.com/opentx/opentx/archive/%{commit0}.tar.gz#/opentx-%{shortcommit0}.tar.gz
Patch1: opentx-cmake-2.2.1.patch
Patch2: opentx-desktop-2.2.0.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-devel
BuildRequires: fox-devel
BuildRequires: SDL-devel
BuildRequires: arm-none-eabi-gcc-cs-c++
BuildRequires: arm-none-eabi-newlib
BuildRequires: python3-qt5
Requires: dfu-util

%description
OpenTX Companion transmitter support software is used for many different
tasks like loading OpenTX firmware to the radio, backing up model
settings, editing settings and running radio simulators.

%prep
%setup -n opentx-%{commit0}
%patch1 -p1
%patch2 -p1

%build
rm -rf build-taranis-debug
mkdir build-taranis-debug
cd build-taranis-debug
%cmake -DPCB=X9D+ -DGVARS=YES -DLUA=YES -DDEBUG=YES -DCMAKE_BUILD_TYPE=Debug -DBUILD_SHARED_LIBS:BOOL=OFF ../
make %{?_smp_mflags} opentx-companion
make %{?_smp_mflags} opentx-simulator

%install
make -C build-taranis-debug install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/opentx-companion
%{_bindir}/opentx-simulator
%{_libdir}/opentx-companion-22/
%{_prefix}/lib/udev/rules.d/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Tue Mar 20 2018 J <j@roxor.me> - 2.2.1-3
- update to upstream 2.2.1 tag

* Sun Aug 20 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.1-2
- Rebase to 2.2 master.

* Sat Aug 19 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.2.0-1
- Rebase to 2.2.0.

* Sat Jul 15 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.1.9-4
- Drive the build and installation by cmake and macros more.

* Fri Jul 14 2017 Jan Pazdziora <jpx-opentx@adelton.com> - 2.1.9-2
- Rebase to 2.1.9.

* Fri Jun 27 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 2.0.5-1
- Use 2.0.2.

* Fri Jun 13 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 2.0.2-0.1
- Use 2.0.2.

* Fri Jun 06 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 2.0.1-0.1
- Use 2.0.1.

* Sun Jun 01 2014 Jan Pazdziora <jpx-opentx@adelton.com> - 1.99.7-0.1
- Initial attempt to build on Fedora 20.

