%define name libspectre
%define version 0.2.4
%define release %mkrel 1
%define major 1
%define libname %mklibname spectre %major
%define develname %mklibname -d spectre

Summary: Postscript rendering library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
License: GPLv2+
Group: System/Libraries
Url: http://libspectre.freedesktop.org/wiki/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgs-devel
BuildRequires: cairo-devel

%description
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package -n %libname
Group: System/Libraries
Summary: Postscript rendering library

%description -n %libname
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package -n %develname
Summary: Postscript rendering library
Group: Development/C
Requires: %libname = %version
Provides: libspectre-devel = %version-%release

%description -n %develname
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.



%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%_libdir/libspectre.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog 
%_libdir/libspectre.so
%_libdir/libspectre*a
%_libdir/pkgconfig/*
%_includedir/*


