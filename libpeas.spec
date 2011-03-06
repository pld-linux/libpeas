# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	GObject Plugin System
Summary(pl.UTF-8):	System wtyczek GObject
Name:		libpeas
Version:	0.7.3
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libpeas/0.7/%{name}-%{version}.tar.gz
# Source0-md5:	58456ddf05c3dc5b8a8dc68a68f88356
Patch0:		gir.patch
URL:		http://live.gnome.org/Libpeas
BuildRequires:	autoconf >= 2.63.2
BuildRequires:	automake >= 1.11
BuildRequires:	libtool >= 2.2.6
BuildRequires:	intltool >= 0.40.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	seed-devel >= 2.31.91
BuildRequires:	python >= 2.5.2
BuildRequires:	python-pygobject-devel >= 2.20.0
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	gnome-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpeas is a gobject-based plugins engine, and is targetted at giving 
every application the chance to assume its own extensibility. It also 
has a set of features including, but not limited to:

 - multiple extension points
 - on demand (lazy) programming language support for C, Python and JS
 - simplicity of the API 

%package loader-python
Summary:	Python loader for libpeas library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-python
Python loader for libpeas library.

%package loader-seed
Summary:	JavaScript loader for libpeas library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-seed
JavaScript loader for libpeas library.

%package devel
Summary:	Header files for libpeas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpeas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpeas library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpeas.

%package static
Summary:	Static libpeas library
Summary(pl.UTF-8):	Statyczna biblioteka libpeas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpeas library.

%description static -l pl.UTF-8
Statyczna biblioteka libpeas.

%package gtk
Summary:	GObject Plugin System
Summary(pl.UTF-8):	System wtyczek GObject
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
libpeas is a gobject-based plugins engine, and is targetted at giving 
every application the chance to assume its own extensibility. It also 
has a set of features including, but not limited to:

 - multiple extension points
 - on demand (lazy) programming language support for C, Python and JS
 - simplicity of the API 

%package gtk-devel
Summary:	Header files for libpeas-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpeas-gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}

%description gtk-devel
Header files for libpeas-gtk library.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpeas-gtk.

%package gtk-static
Summary:	Static libpeas-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka libpeas-gtk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Static libpeas library.

%description gtk-static -l pl.UTF-8
Statyczna biblioteka libpeas.

%package apidocs
Summary:	libpeas API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libpeas
Group:		Documentation

%description apidocs
API and internal documentation for libpeas library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libpeas.

%package demo
Summary:	Demo application for libpeas
Summary(pl.UTF-8): Aplikacja demonstracyjna libpeas
Group:		Application
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	%{name}-loader-python = %{version}-%{release}
Requires:	%{name}-loader-seed = %{version}-%{release}

%description demo
Demo application for libpeas.

%description demo -l pl.UTF-8
Aplikacja demonstracyjna libpeas.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable static_libs static} \
	%{__enable_disable apidocs gtk-doc} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/peas-demo/plugins/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/libpeas-1.0/loaders/*.la

%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/peas-demo/plugins/*/*.a \
	$RPM_BUILD_ROOT%{_libdir}/libpeas-1.0/loaders/*.a
%endif

%find_lang libpeas

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files -f libpeas.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libpeas-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpeas-1.0.so.0
%dir %{_libdir}/libpeas-1.0
%dir %{_libdir}/libpeas-1.0/loaders
%{_libdir}/libpeas-1.0/loaders/libcloader.so
%{_libdir}/girepository-1.0/Peas-1.0.typelib

%files loader-python
%defattr(644,root,root,755)
%{_libdir}/libpeas-1.0/loaders/libpythonloader.so

%files loader-seed
%defattr(644,root,root,755)
%{_libdir}/libpeas-1.0/loaders/libseedloader.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpeas-1.0.so
%{_includedir}/libpeas-1.0
%{_pkgconfigdir}/libpeas-1.0.pc
%{_datadir}/gir-1.0/Peas-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpeas-1.0.a
%endif

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-gtk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpeas-gtk-1.0.so.0
%{_libdir}/girepository-1.0/PeasGtk-1.0.typelib
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg

%files gtk-devel
%defattr(644,root,root,755)
%{_libdir}/libpeas-gtk-1.0.so
%{_pkgconfigdir}/libpeas-gtk-1.0.pc
%{_datadir}/gir-1.0/PeasGtk-1.0.gir

%if %{with static_libs}
%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libpeas-gtk-1.0.a
%endif

%files demo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/peas-demo/plugins/helloworld/helloworld.plugin
%attr(755,root,root) %{_libdir}/peas-demo/plugins/helloworld/libhelloworld.so
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.plugin
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.py
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.pyc
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.pyo
%attr(755,root,root) %{_libdir}/peas-demo/plugins/secondtime/libsecondtime.so
%{_libdir}/peas-demo/plugins/secondtime/secondtime.plugin
%{_libdir}/peas-demo/plugins/seedhello/seedhello.js
%{_libdir}/peas-demo/plugins/seedhello/seedhello.plugin

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_datadir}/gtk-doc/html/libpeas
%endif
