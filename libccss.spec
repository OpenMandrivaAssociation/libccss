%define major 4
%define libname %mklibname ccss %major
%define develname %mklibname -d ccss

Name: libccss
Version: 0.4.0
Release: %mkrel 3
Summary: A simple api for CSS Stylesheets
Group: System/Libraries
License: LGPLv2+
URL: http://people.freedesktop.org/~robsta/libccss/
Source0: http://people.freedesktop.org/~robsta/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cairo-devel >= 1.4
BuildRequires: gtk+2-devel >= 2.10
BuildRequires: libcroco0.6-devel
BuildRequires: librsvg2-devel >= 2.22.4
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
%setup -q

%build
%configure2_5x --disable-examples

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#Remove libtool archives.
rm -rf %{buildroot}/%{_libdir}/*.la

%clean
rm -rf %{buildroot}

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
%{_includedir}/libccss-1
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/ccss
%{_datadir}/gtk-doc/html/ccss-cairo
