%define major	1
%define libname %mklibname spectre %{major}
%define devname %mklibname -d spectre

Summary:	Postscript rendering library
Name:		libspectre
Version:	0.2.9
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://libspectre.freedesktop.org/wiki/
Source0:	http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	libgs-devel

%description
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package -n %{libname}
Group:		System/Libraries
Summary:	Postscript rendering library

%description -n %{libname}
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package -n %{devname}
Summary:	Postscript rendering library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%prep
%setup -q

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libspectre.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README TODO
%{_libdir}/libspectre.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

