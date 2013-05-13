%define major 5
%define libname %mklibname ccss %major
%define develname %mklibname -d ccss
%define oname ccss
Name: libccss
Version: 0.5.0
Release: 2
Summary: A simple api for CSS Stylesheets
Group: System/Libraries
License: LGPLv2+
URL: http://people.freedesktop.org/~robsta/ccss/
Source0: http://people.freedesktop.org/~robsta/%{oname}/%{oname}-%{version}.tar.gz
BuildRequires: pkgconfig(cairo) >= 1.4
BuildRequires: pkgconfig(gtk+-2.0) >= 2.10
BuildRequires: libcroco0.6-devel
BuildRequires: pkgconfig(librsvg-2.0) >= 2.22.4
BuildRequires: libsoup-devel

%description
Libccss offers a simple API to

    * Parse CSS stylesheets.
    * Query for style configurations on a user-provided document
      representation.
    * Draw query results onto cairo surfaces.

%package -n %libname
Summary: Library files for %{name}
Group: System/Libraries

%description -n %libname
Library files for %{name}.

%package -n %develname
Summary: Development package for %{name}
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: gtk-css-engine < 0.3.0

%description -n %develname
Files for development with %{name}.

%prep
%setup -q -n %oname-%version

%build
export LIBS="-lgmodule-2.0"
%configure2_5x --disable-examples

%make

%install
%makeinstall_std

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS TODO
%{_bindir}/ccss-stylesheet-to-gtkrc

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %develname
%defattr(-,root,root,-)
%{_includedir}/ccss-1
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/ccss
%{_datadir}/gtk-doc/html/ccss-cairo
%{_datadir}/gtk-doc/html/ccss-gtk


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-2mdv2011.0
+ Revision: 620086
- the mass rebuild of 2010.0 packages

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 415489
- new version
- new major
- update URL
- update file list

* Sat Aug 01 2009 Funda Wang <fwang@mandriva.org> 0.4.0-3mdv2010.0
+ Revision: 405355
+ rebuild (emptylog)

* Sat Aug 01 2009 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2010.0
+ Revision: 405352
- fix conflicts with older gtk-css-engine

* Sat Aug 01 2009 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 405340
- add build root
- import libccss

