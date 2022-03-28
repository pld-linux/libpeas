#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	luajit		# LuaJIT implementation of lua 5.1
%bcond_without	static_libs	# static libraries
%bcond_without	glade		# glade catalog file packaging
%bcond_without	lua		# Lua (5.1) loader
%bcond_without	python2		# Python 2.x loader
%bcond_without	python3		# Python 3.x loader

# luajit is not supported on x32
%ifarch x32
%undefine	with_luajit
%endif

Summary:	GObject Plugin System
Summary(pl.UTF-8):	System wtyczek GObject
Name:		libpeas
Version:	1.32.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libpeas/1.32/%{name}-%{version}.tar.xz
# Source0-md5:	ea067e520d1b19606dbe47d20c625b8f
URL:		https://wiki.gnome.org/Libpeas
BuildRequires:	gettext-tools >= 0.19.7
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.7}
%{?with_glade:BuildRequires:	glade-devel >= 2.0}
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gobject-introspection-devel >= 1.40.0
BuildRequires:	gtk+3-devel >= 3.0.0
%if %{with lua}
BuildRequires:	lua-lgi >= 0.9.0
%{!?with_luajit:BuildRequires:	lua51-devel >= 5.1.0}
%{?with_luajit:BuildRequires:	luajit-devel >= 2.0}
%endif
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5.2
BuildRequires:	python-pygobject3-devel >= 3.2.0
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2.0
BuildRequires:	python3-pygobject3-devel >= 3.2.0
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
%{!?with_luajit:BuildConflicts:	luajit-devel}
Requires:	glib2 >= 1:2.38.0
Requires:	gobject-introspection >= 1.40.0
Obsoletes:	libpeas-loader-gjs < 1.10.0
Obsoletes:	libpeas-loader-seed < 1.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpeas is a gobject-based plugins engine, and is targetted at giving
every application the chance to assume its own extensibility. It also
has a set of features including, but not limited to:
 - multiple extension points
 - on demand (lazy) programming language support for C, Python and Lua
 - simplicity of the API

%description -l pl.UTF-8
libpeas to silnik wtyczek oparty na bibliotece GObject; jego celem
jest zapewnienie każdej aplikacji własnej rozszerzalności. Ma także
pewien zbiór możliwości, w tym:
 - wiele punktów rozszerzeń
 - wsparcie dla leniwego programowania dla języków C, Python i Lua
 - prostota API

%package loader-lua
Summary:	Lua loader for libpeas library
Summary(pl.UTF-8):	Moduł ładujący dla języka Lua do biblioteki libpeas
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lua-lgi >= 0.9.0

%description loader-lua
Lua loader for libpeas library.

%description loader-lua -l pl.UTF-8
Moduł ładujący dla języka Lua do biblioteki libpeas.

%package loader-python
Summary:	Python 2.x loader for libpeas library
Summary(pl.UTF-8):	Moduł ładujący dla Pythona 2.x do biblioteki libpeas
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-libs >= 1:2.5.2

%description loader-python
Python 2.x loader for libpeas library.

%description loader-python -l pl.UTF-8
Moduł ładujący dla Pythona 2.x do biblioteki libpeas.

%package loader-python3
Summary:	Python 3.x loader for libpeas library
Summary(pl.UTF-8):	Moduł ładujący dla Pythona 3.x do biblioteki libpeas
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-python3
Python 3.x loader for libpeas library.

%description loader-python3 -l pl.UTF-8
Moduł ładujący dla Pythona 3.x do biblioteki libpeas.

%package devel
Summary:	Header files for libpeas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpeas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.38.0
Requires:	gobject-introspection-devel >= 1.40.0

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
Summary:	GObject Plugin System - GTK+ widgets
Summary(pl.UTF-8):	System wtyczek GObject - widgety GTK+
Group:		X11/Libraries
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.0.0
Requires:	hicolor-icon-theme

%description gtk
libpeas is a gobject-based plugins engine, and is targetted at giving
every application the chance to assume its own extensibility. It also
has a set of features including, but not limited to:
 - multiple extension points
 - on demand (lazy) programming language support for C, Python and Lua
 - simplicity of the API

This package contains GTK+ widgets library.

%description gtk -l pl.UTF-8
libpeas to silnik wtyczek oparty na bibliotece GObject; jego celem
jest zapewnienie każdej aplikacji własnej rozszerzalności. Ma także
pewien zbiór możliwości, w tym:
 - wiele punktów rozszerzeń
 - wsparcie dla leniwego programowania dla języków C, Python i Lua
 - prostota API

Ten pakiet zawiera bibliotekę widgetów GTK+.

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

%package gtk-glade
Summary:	libpeas-gtk catalog file for Glade
Summary(pl.UTF-8):	Plik katalogu libpeas-gtk dla Glade
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}
Requires:	glade >= 2.0

%description gtk-glade
libpeas-gtk catalog file for Glade.

%description gtk-glade -l pl.UTF-8
Plik katalogu libpeas-gtk dla Glade.

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
BuildArch:	noarch

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
%if %{with lua}
Requires:	%{name}-loader-lua = %{version}-%{release}
%endif
%if %{with python3}
Requires:	%{name}-loader-python3 = %{version}-%{release}
%endif

%description demo
Demo application for libpeas.

%description demo -l pl.UTF-8
Aplikacja demonstracyjna libpeas.

%prep
%setup -q

%if %{with lua}
# meson buildsystem expects .pc file for lua-lgi detection
install -d fake-pkgconfig
cat >fake-pkgconfig/lua5.1-lgi.pc <<'EOF'
Name: lua-lgi
Description: Lua LGI
Version: %(rpm -q --qf '%%{V}\n' lua-lgi)
EOF
%endif

%build
export PKG_CONFIG_PATH=$(pwd)/fake-pkgconfig
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	%{!?with_glade:-Dglade_catalog=false} \
	%{?with_apidocs:-Dgtk_doc=true} \
	%{!?with_lua:-Dlua51=false} \
	%{?with_python2:-Dpython2=true} \
	%{!?with_python3:-Dpython3=false} \
	-Dvapi=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%py3_comp $RPM_BUILD_ROOT%{_libdir}/peas-demo/plugins/pythonhello
%py3_ocomp $RPM_BUILD_ROOT%{_libdir}/peas-demo/plugins/pythonhello

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/doc/libpeas-* $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%find_lang libpeas-1.0

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

%files -f libpeas-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libpeas-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpeas-1.0.so.0
%dir %{_libdir}/libpeas-1.0
%dir %{_libdir}/libpeas-1.0/loaders
%{_libdir}/girepository-1.0/Peas-1.0.typelib

%if %{with lua}
%files loader-lua
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-1.0/loaders/liblua51loader.so
%endif

%if %{with python2}
%files loader-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-1.0/loaders/libpythonloader.so
%endif

%if %{with python3}
%files loader-python3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-1.0/loaders/libpython3loader.so
%endif

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
%{_iconsdir}/hicolor/*x*/actions/libpeas-plugin.png
%{_iconsdir}/hicolor/scalable/actions/libpeas-plugin.svg

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpeas-gtk-1.0.so
%{_pkgconfigdir}/libpeas-gtk-1.0.pc
%{_datadir}/gir-1.0/PeasGtk-1.0.gir

%if %{with glade}
%files gtk-glade
%defattr(644,root,root,755)
%{_datadir}/glade/catalogs/libpeas-gtk.xml
%endif

%if %{with static_libs}
%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libpeas-gtk-1.0.a
%endif

%files demo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/peas-demo
%dir %{_libdir}/peas-demo
%dir %{_libdir}/peas-demo/plugins
%dir %{_libdir}/peas-demo/plugins/helloworld
%attr(755,root,root) %{_libdir}/peas-demo/plugins/helloworld/libhelloworld.so
%{_libdir}/peas-demo/plugins/helloworld/helloworld.plugin
%if %{with lua}
%dir %{_libdir}/peas-demo/plugins/luahello
%{_libdir}/peas-demo/plugins/luahello/luahello.lua
%{_libdir}/peas-demo/plugins/luahello/luahello.plugin
%endif
%if %{with python3}
%dir %{_libdir}/peas-demo/plugins/pythonhello
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.plugin
%{_libdir}/peas-demo/plugins/pythonhello/pythonhello.py
%{_libdir}/peas-demo/plugins/pythonhello/__pycache__
%endif
%dir %{_libdir}/peas-demo/plugins/secondtime
%attr(755,root,root) %{_libdir}/peas-demo/plugins/secondtime/libsecondtime.so
%{_libdir}/peas-demo/plugins/secondtime/secondtime.plugin

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libpeas-1.0
%{_gtkdocdir}/libpeas-gtk-1.0
%endif
