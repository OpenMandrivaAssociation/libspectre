# libspectre is used by cairo, cairo is used by gtk-3.0,
# gtk-3.0 is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major	1
%define libname %mklibname spectre %{major}
%define devname %mklibname -d spectre
%define lib32name %mklib32name spectre %{major}
%define dev32name %mklib32name -d spectre

Summary:	Postscript rendering library
Name:		libspectre
Version:	0.2.12
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://libspectre.freedesktop.org/wiki/
Source0:	http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	ghostscript-devel
%if %{with compat32}
BUildRequires:	devel(libgs)
BuildRequires:	devel(libtiff)
BuildRequires:	devel(libcups)
BuildRequires:	devel(libpng16)
BuildRequires:	devel(libjbig2dec)
BuildRequires:	devel(libjpeg)
BuildRequires:	devel(libz)
BuildRequires:	devel(libfreetype)
BuildRequires:	devel(libopenjp2)
BuildRequires:	devel(libzstd)
BuildRequires:	devel(liblzma)
BuildRequires:	devel(libkrb5)
BuildRequires:	devel(libk5crypto)
BuildRequires:	devel(libcom_err)
BuildRequires:	devel(libgnutls)
BuildRequires:	devel(libbz2)
BuildRequires:	devel(libidn2)
BuildRequires:	devel(libunistring)
BuildRequires:	devel(libtasn1)
BuildRequires:	devel(libnettle)
BuildRequires:	devel(libhogweed)
BuildRequires:	devel(libgmp)
BuildRequires:	libcrypt-devel
%endif

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

%description -n %{devname}
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%if %{with compat32}
%package -n %{lib32name}
Group:		System/Libraries
Summary:	Postscript rendering library (32-bit)

%description -n %{lib32name}
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package -n %{dev32name}
Summary:	Postscript rendering library (32-bit)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.
%endif

%prep
%setup -q
export CONFIGURE_TOP="$(pwd)"
export CFLAGS="%{optflags} -I$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libspectre.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README TODO
%{_libdir}/libspectre.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libspectre.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libspectre.so
%{_prefix}/lib/pkgconfig/*
%endif
