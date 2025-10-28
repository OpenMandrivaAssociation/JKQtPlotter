%define major 5
%define libname %mklibname JKQtPlotter
%define devname %mklibname JKQtPlotter -d

Name:		JKQtPlotter
Version:	5.0.0~20251028
Release:	1
Source0:	https://github.com/jkriege2/JKQtPlotter/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz
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
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(OpenCV)
BuildRequires:	cmake(VulkanHeaders)
# The build system seems to prefer Qt 5.x unconditionally, so
# let's just conflict with it to make sure we use 6.x. 5.x is
# going away soon anyway
BuildConflicts:	cmake(Qt5Core)
BuildSystem:	cmake
BuildOption:	-DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF

%patchlist

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

%files
%{_bindir}/*
%doc %{_docdir}/JKQTPlotter

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
