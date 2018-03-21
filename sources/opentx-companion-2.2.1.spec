Summary: OpenTX Companion
Name: opentx-companion

%global commit0 b55b68f191cfa22dee396ee2842e9fb836d9664f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global CMAKE_OPTS -DSIMULATOR_INSTALL_PREFIX=/usr -DFIRMWARE_TARGET=NO -DGVARS=YES -DHELI=YES -DALLOW_NIGHTLY_BUILDS=NO -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 -DVERSION_SUFFIX= -DDEBUG=YES -DCMAKE_BUILD_TYPE=Debug -DBUILD_SHARED_LIBS:BOOL=OFF

Version: 2.2.1
Release: git_%{shortcommit0}.5%{?dist}
License: GPLv2
URL: http://www.open-tx.org
Source0: https://github.com/opentx/opentx/archive/%{commit0}.tar.gz#/opentx-%{shortcommit0}.tar.gz
Patch1: opentx-companion_qtlibs_link.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-devel
BuildRequires: fox-devel
BuildRequires: SDL-devel
BuildRequires: python3-qt5
Requires: dfu-util

%description
OpenTX Companion transmitter support software is used for many different
tasks like loading OpenTX firmware to the radio, backing up model
settings, editing settings and running radio simulators.

%prep
%setup -n opentx-%{commit0}
%patch1 -p1

%build
rm -rf build
mkdir build
cd build
for tgt in 9X GRUVIN9X MEGA2560 SKY9X 9XRPRO; do
  %cmake -DPCB=$tgt %CMAKE_OPTS ../
  %make_build libsimulator
done
for stmtgt in X7 X9D X9D+ X9E X12S; do
  %cmake -DPCB=$stmtgt -DLUA=YES %CMAKE_OPTS ../
  %make_build libsimulator
done
%make_build companion22 simulator22

%install
cd build
%cmake %CMAKE_OPTS ../
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/companion22
%{_bindir}/simulator22
%{_libdir}/companion22/
%{_prefix}/lib/udev/rules.d/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Tue Mar 21 2018 J <j@roxor.me> - 2.2.1-4
- remove dependency on arm toolchain

* Tue Mar 20 2018 J <j@roxor.me> - 2.2.1-4
- do not use custom cmake macro, just override BUILD_SHARED_LIBS:BOOL=OFF

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

