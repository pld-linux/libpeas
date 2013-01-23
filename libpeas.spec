#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	GObject Plugin System
Summary(pl.UTF-8):	System wtyczek GObject
Name:		libpeas
Version:	1.6.2
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libpeas/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	183db6b32051a73c3b7bfbfccdc88e4c
URL:		http://live.gnome.org/Libpeas
BuildRequires:	autoconf >= 2.63.2
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gjs-devel >= 1.32.0
BuildRequires:	glade-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	python >= 2.5.2
BuildRequires:	python-pygobject3-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	seed-devel >= 3.0.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Summary:	JavaScript (seed) loader for libpeas library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-seed
JavaScript (seed) loader for libpeas library.

%package loader-gjs
Summary:	JavaScript (GJS) loader for libpeas library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-gjs
JavaScript (GJS) loader for libpeas library.

%package devel
Summary:	Header files for libpeas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpeas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	gobject-introspection-devel >= 0.10.1

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
Group:		X11/Libraries
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	hicolor-icon-theme

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
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0.0

%description gtk-devel
Header files for libpeas-gtk library.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpeas-gtk.

%package gtk-static
Summary:	Static libpeas-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka libpeas-gtk
Group:		X11/Development/Libraries
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
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for libpeas library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libpeas.

%package demo
Summary:	Demo application for libpeas
Summary(pl.UTF-8):	Aplikacja demonstracyjna libpeas
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	%{name}-loader-gjs = %{version}-%{release}
Requires:	%{name}-loader-python = %{version}-%{release}
Requires:	%{name}-loader-seed = %{version}-%{release}

%description demo
Demo application for libpeas.

%description demo -l pl.UTF-8
Aplikacja demonstracyjna libpeas.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable static_libs static} \
	%{__enable_disable apidocs gtk-doc} \
	--with-html-dir=%{_gtkdocdir}
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

%post gtk
/sbin/ldconfig
%update_icon_cache hicolor

%postun	gtk
/sbin/ldconfig
%update_icon_cache hicolor

%files -f libpeas.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libpeas-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpeas-1.0.so.0
%dir %{_libdir}/libpeas-1.0
%dir %{_libdir}/libpeas-1.0/loaders
%{_libdir}/girepository-1.0/Peas-1.0.typelib

%files loader-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-1.0/loaders/libpythonloader.so

%files loader-seed
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-1.0/loaders/libseedloader.so

%files loader-gjs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-1.0/loaders/libgjsloader.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-1.0.so
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
%attr(755,root,root) %{_libdir}/libpeas-gtk-1.0.so
%{_pkgconfigdir}/libpeas-gtk-1.0.pc
%{_datadir}/gir-1.0/PeasGtk-1.0.gir
%{_datadir}/glade/catalogs/libpeas-gtk.xml

%if %{with static_libs}
%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libpeas-gtk-1.0.a
%endif

%files demo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/peas-demo
%dir %{_libdir}/peas-demo/plugins
%dir %{_libdir}/peas-demo/plugins/helloworld
%attr(755,root,root) %{_libdir}/peas-demo/plugins/helloworld/libhelloworld.so
%{_libdir}/peas-demo/plugins/helloworld/helloworld.plugin
%dir %{_libdir}/peas-demo/plugins/pythonhello
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.plugin
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.py*
%dir %{_libdir}/peas-demo/plugins/secondtime
%attr(755,root,root) %{_libdir}/peas-demo/plugins/secondtime/libsecondtime.so
%{_libdir}/peas-demo/plugins/secondtime/secondtime.plugin
%dir %{_libdir}/peas-demo/plugins/seedhello
%{_libdir}/peas-demo/plugins/seedhello/seedhello.js
%{_libdir}/peas-demo/plugins/seedhello/seedhello.plugin
%dir %{_libdir}/peas-demo/plugins/gjshello
%{_libdir}/peas-demo/plugins/gjshello/gjshello.js
%{_libdir}/peas-demo/plugins/gjshello/gjshello.plugin

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libpeas
%endif
