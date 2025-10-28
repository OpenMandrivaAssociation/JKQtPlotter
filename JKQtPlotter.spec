%define major 4
%define libname %mklibname JKQtPlotter
%define devname %mklibname JKQtPlotter -d

Name:		JKQtPlotter
Version:	4.0.3
Release:	1
Source0:	https://github.com/jkriege2/JKQtPlotter/archive/refs/tags/v%{version}.tar.gz
Summary:	Extensive C++ library for data visualization, plotting and charting for Qt
URL:		https://github.com/jkriege2/JKQtPlotter
License:	LGPL-2.1
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(OpenCV)
# The build system seems to prefer Qt 5.x unconditionally, so
# let's just conflict with it to make sure we use 6.x. 5.x is
# going away soon anyway
BuildConflicts:	cmake(Qt5Core)
BuildSystem:	cmake
BuildOption:	-DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF

%patchlist
jkqtplotter-4.0.3-qt-6.10.patch

%description
Extensive C++ library for data visualization, plotting and charting for Qt

%package -n %{libname}
Summary:	Extensive C++ library for data visualization, plotting and charting for Qt
Group:		System/Libraries

%description -n %{libname}

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}, an extensive C++
library for data visualization, plotting and charting for Qt

%prep -a
# Fix FS layout hardcodes
sed -i -e 's,DESTINATION lib/cmake,DESTINATION %{_lib}/cmake/%{name},g' lib/*/CMakeLists.txt
sed -i -e 's,DESTINATION doc,DESTINATION share/doc,g' lib/*/CMakeLists.txt

# We don't need a "SharedLib" suffix on a .so.* file (what else would it be?)
# But we do need a "6" suffix because avogadrolibs assumes it's there, even if
# we don't ship Qt5 libs anymore
sed -i -e 's,SharedLib,6,g' lib/*/CMakeLists.txt examples/*/CMakeLists.txt

%files
%{_bindir}/*
%doc %{_docdir}/JKQtPlotter

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
