%define major 1
%define libname %mklibname spectre %{major}
%define develname %mklibname -d spectre

Summary:	Postscript rendering library
Name:		libspectre
Version:	0.2.6
Release:	6
License:	GPLv2+
Group:		System/Libraries
Url:		http://libspectre.freedesktop.org/wiki/
Source0:	http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.bz2
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

%package -n %{develname}
Summary:	Postscript rendering library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libspectre-devel = %{version}-%{release}

%description -n %{develname}
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS NEWS README TODO
%{_libdir}/libspectre.so.%{major}*

%files -n %{develname}
%{_libdir}/libspectre.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.6-3mdv2011.0
+ Revision: 662416
- mass rebuild

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 0.2.6-2
+ Revision: 637001
- reuild for new gs

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.2.6-1mdv2011.0
+ Revision: 550778
- update to new version 0.2.6

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.2.5-2mdv2010.1
+ Revision: 540036
- rebuild so that shared libraries are properly stripped again

* Sun Apr 18 2010 Götz Waschk <waschk@mandriva.org> 0.2.5-1mdv2010.1
+ Revision: 536485
- new version
- update file list

* Sun Feb 21 2010 Götz Waschk <waschk@mandriva.org> 0.2.4-1mdv2010.1
+ Revision: 509277
- update to new version 0.2.4

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.2.3-1mdv2010.1
+ Revision: 461015
- update to new version 0.2.3

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2.2-2mdv2010.0
+ Revision: 425751
- rebuild

* Wed Nov 26 2008 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 306912
- update to new version 0.2.2

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2009.0
+ Revision: 271720
- new version

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdv2009.0
+ Revision: 229846
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2008.1
+ Revision: 159757
- import libspectre


* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2008.1
- initial package
