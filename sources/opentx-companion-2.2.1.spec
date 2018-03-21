Summary: OpenTX Companion
Name: opentx-companion

%global commit0 b55b68f191cfa22dee396ee2842e9fb836d9664f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global CMAKE_OPTS -DSIMULATOR_INSTALL_PREFIX=/usr -DFIRMWARE_TARGET=NO -DGVARS=YES -DHELI=YES -DALLOW_NIGHTLY_BUILDS=NO -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 -DVERSION_SUFFIX= -DDEBUG=YES -DCMAKE_BUILD_TYPE=Debug
%global mycmake \
  CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
  CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
  FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
  FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
  %{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \
  %__cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \\\
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \\\
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
%if "%{?_lib}" == "lib64" \
        %{?_cmake_lib_suffix64} \\\
%endif \
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir}

Version: 2.2.1
Release: git_%{shortcommit0}.3%{?dist}
License: GPLv2
URL: http://www.open-tx.org
Source0: https://github.com/opentx/opentx/archive/%{commit0}.tar.gz#/opentx-%{shortcommit0}.tar.gz
Patch1: opentx-companion_qtlibs_link.patch

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

%build
rm -rf build
mkdir build
cd build
for tgt in 9X GRUVIN9X MEGA2560 SKY9X 9XRPRO; do
  %mycmake -DPCB=$tgt %CMAKE_OPTS ../
  %make_build libsimulator
done
for stmtgt in X7 X9D X9D+ X9E X12S; do
  %mycmake -DPCB=$stmtgt -DLUA=YES %CMAKE_OPTS ../
  %make_build libsimulator
done
%make_build companion22 simulator22

%install
cd build
%mycmake %CMAKE_OPTS ../
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

