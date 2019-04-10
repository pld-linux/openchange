# TODO
# - nagios plugin (see it's files section for details)
#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_with	mapiproxy	# mapiproxy suite (disabled with Samba 4.4+)
%bcond_with	mapitest	# mapitest utility (disabled with Samba 4.4+)
%bcond_with	python		# build python package (requires disabled mapiproxy)

%define	cname	VULCAN
Summary:	OpenChange - portable implementation of MS Exchange Server and Exchange protocols
Summary(pl.UTF-8):	OpenChange - przenośna implementacja serwera oraz protokołów MS Exchange
Name:		openchange
Version:	2.3
Release:	39
License:	GPL v3+
Group:		Libraries
Source0:	https://github.com/openchange/openchange/archive/%{name}-%{version}-%{cname}.tar.gz
# Source0-md5:	96c13c78c2bcbd7040f7848746284b9f
Patch0:		disable-mapiproxy.patch
Patch1:		%{name}-link.patch
Patch2:		flex2.6.patch
Patch3:		samba-4.2.patch
Patch4:		fix-connection-args.patch
Patch5:		samba-4.4.patch
Patch6:		%{name}-covscan.patch
Patch7:		%{name}-samba-4.10-macros.patch
URL:		https://github.com/openchange
BuildRequires:	QtCore-devel >= 4.3.0
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	check-devel
BuildRequires:	doxygen
BuildRequires:	ldb-devel
BuildRequires:	libical-devel >= 0.46
BuildRequires:	libmagic-devel
BuildRequires:	libmemcached-devel >= 1.0.18
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mysql-devel
BuildRequires:	nanomsg-devel >= 0.5
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	popt-devel
%if %{with python}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-samba >= 4.2.2
%endif
BuildRequires:	rpmbuild(macros) >= 1.219
# with DCERCP multiplex and pending call support (upstream 4.1.18+ or 4.2.2+)
# samba-4.10-macros patch requires samba-pidl 4.10+
BuildRequires:	samba-devel >= 4.10
BuildRequires:	samba-pidl >= 4.10
BuildRequires:	sed >= 4.0
BuildRequires:	subunit-devel
BuildRequires:	talloc-devel
BuildRequires:	tdb-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
%{?with_python:Requires:	python-openchange = %{version}-%{release}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenChange is a portable Open Source implementation of Microsoft
Exchange server and Exchange protocols. It provides a complete
solution to interoperate with Microsoft Outlook clients or Microsoft
Exchange servers.

OpenChange client-side library is used in existing messaging clients
and is the solution in new projects to communicate natively with
Microsoft Exchange and Exchange-compatible servers. OpenChange server
is a transparent Microsoft Exchange server replacement using native
Exchange protocols and does not require any plugin installation in
Outlook.

%description -l pl.UTF-8
OpenChange to przenośna, mająca otwarte źródła implementacja serwera
oraz protokołów Microsoft Exchange. Dostarcza kompletne rozwiązanie
pozwalające współpracować z klientami Microsoft Outlook oraz serwerami
Microsoft Exchange.

Biblioteka kliencka OpenChange jest używana przez istniejących
klientów pocztowych i pozwalają na natywną komunikację z serwerami
Microsoft Exchange oraz zgodnymi. Serwer OpenChange to przezroczysty
zamiennik serwera Microsoft Exchange wykorzystujący natywne protokoły
Exchange, nie wymagający instalowania żadnych wtyczek w Outlooku.

%package libs
Summary:	OpenChange client libraries
Summary(pl.UTF-8):	Biblioteki klienckie OpenChange
Group:		Libraries

%description libs
OpenChange client libraries.

%description libs -l pl.UTF-8
Biblioteki klienckie OpenChange.

%package devel
Summary:	Header files for OpenChange libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek OpenChange
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ldb-devel
Requires:	samba-devel >= 4.2.2
Requires:	talloc-devel
Requires:	tevent-devel
Requires:	zlib-devel

%description devel
Header files for OpenChange libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OpenChange.

%package c++
Summary:	C++ interface to OpenChange MAPI library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki OpenChange MAPI
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description c++
C++ interface to OpenChange MAPI library.

%description c++ -l pl.UTF-8
Interfejs C++ do biblioteki OpenChange MAPI.

%package c++-devel
Summary:	Header files of C++ interface to OpenChange MAPI library
Summary(pl.UTF-8):	Pliki nagłówkowe interfejsu C++ do biblioteki OpenChange MAPI
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files of C++ interface to OpenChange MAPI library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe interfejsu C++ do biblioteki OpenChange MAPI.

%package qt
Summary:	Qt interface to OpenChange MAPI library
Summary(pl.UTF-8):	Interfejs Qt do biblioteki OpenChange MAPI
Group:		Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	QtCore >= 4.3.0
Requires:	QtGui >= 4.3.0

%description qt
Qt interface to OpenChange MAPI library.

%description qt -l pl.UTF-8
Interfejs Qt do biblioteki OpenChange MAPI.

%package qt-devel
Summary:	Header files of Qt interface to OpenChange MAPI library
Summary(pl.UTF-8):	Pliki nagłówkowe interfejsu Qt do biblioteki OpenChange MAPI
Group:		Development/Libraries
Requires:	%{name}-qt = %{version}-%{release}
Requires:	QtGui-devel >= 4.3.0

%description qt-devel
Header files of Qt interface to OpenChange MAPI library.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe interfejsu Qt do biblioteki OpenChange MAPI.

%package apidocs
Summary:	API documentation for OpenChange libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek OpenChange
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for OpenChange libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek OpenChange.

%package -n python-openchange
Summary:	Python interface to OpenChange libraries
Summary(pl.UTF-8):	Interfejs Pythona do bibliotek OpenChange
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-openchange
Python interface to OpenChange libraries.

%description -n python-openchange -l pl.UTF-8
Interfejs Pythona do bibliotek OpenChange.

%package -n nagios-plugin-openchange
Summary:	Nagios plugin to check Exchange/OpenChange services
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania usług Exchange/OpenChange
Group:		Networking
Requires:	%{name} = %{version}-%{release}
Requires:	nagios

%description -n nagios-plugin-openchange
Nagios plugin to check Exchange/OpenChange services.

%description -n nagios-plugin-openchange -l pl.UTF-8
Wtyczka Nagiosa do sprawdzania usług Exchange/OpenChange.

%prep
%setup -q -n %{name}-%{name}-%{version}-%{cname}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# no switch for verbose mode, enable manually :/
%{__sed} -i -e 's/^	@\(\$(\(PIDL\|CC\|CXX\|MOC\)\)/	\1/' Makefile

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--datadir=%{_datadir}/openchange \
	--enable-openchange-qt4 \
	%{?with_python:--enable-pyopenchange} \
	--with-modulesdir=%{_libdir}/openchange/modules
%{__make}

%if %{with apidocs}
%{__make} doxygen
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# doxygen generated man pages are messy; use HTML docs and install man1 pages manually
%if 0
%{__make} installman \
	DESTDIR=$RPM_BUILD_ROOT
%else
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp doc/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
%endif

# missing from make install
install -d $RPM_BUILD_ROOT%{_includedir}/libqtmapi
cp -p qt/lib/*.h $RPM_BUILD_ROOT%{_includedir}/libqtmapi
cp -a libqtmapi.so.*.* libqtmapi.so $RPM_BUILD_ROOT%{_libdir}

# tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/test_asyncnotif
%if %{without mapitest}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/mapitest.1
%endif

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.md IDL_LICENSE.txt README.md README.smbconf.md doc/howto.txt
%attr(755,root,root) %{_bindir}/exchange2ical
%attr(755,root,root) %{_bindir}/exchange2mbox
%attr(755,root,root) %{_bindir}/mapiprofile
%attr(755,root,root) %{_bindir}/mapipropsdump
%attr(755,root,root) %{_bindir}/openchangeclient
%attr(755,root,root) %{_bindir}/openchangemapidump
%attr(755,root,root) %{_bindir}/openchangepfadmin
%attr(755,root,root) %{_bindir}/rpcextract
%attr(755,root,root) %{_bindir}/schemaIDGUID
%dir %{_datadir}/openchange
%dir %{_datadir}/openchange/setup
%{_datadir}/openchange/setup/profiles
%{_mandir}/man1/exchange2ical.1*
%{_mandir}/man1/exchange2mbox.1*
%{_mandir}/man1/mapiprofile.1*
%{_mandir}/man1/openchangeclient.1*
%{_mandir}/man1/openchangepfadmin.1*
%if %{with mapiproxy}
%attr(755,root,root) %{_bindir}/ocnotify
%attr(755,root,root) %{_sbindir}/openchange_group
%attr(755,root,root) %{_sbindir}/openchange_migrate
%attr(755,root,root) %{_sbindir}/openchange_neworganization
%attr(755,root,root) %{_sbindir}/openchange_newuser
%attr(755,root,root) %{_sbindir}/openchange_provision
# XXX: dir specified by dcerpc_server.pc file, should belong to samba or samba-libs
%dir %{_libdir}/samba/dcerpc_server
%attr(755,root,root) %{_libdir}/samba/dcerpc_server/dcesrv_asyncemsmdb.so
%attr(755,root,root) %{_libdir}/samba/dcerpc_server/dcesrv_mapiproxy.so
%dir %{_libdir}/openchange
%dir %{_libdir}/openchange/modules
%dir %{_libdir}/openchange/modules/dcerpc_mapiproxy
%attr(755,root,root) %{_libdir}/openchange/modules/dcerpc_mapiproxy/mpm_cache.so
%attr(755,root,root) %{_libdir}/openchange/modules/dcerpc_mapiproxy/mpm_downgrade.so
%attr(755,root,root) %{_libdir}/openchange/modules/dcerpc_mapiproxy/mpm_dummy.so
%attr(755,root,root) %{_libdir}/openchange/modules/dcerpc_mapiproxy/mpm_pack.so
%dir %{_libdir}/openchange/modules/dcerpc_mapiproxy_server
%attr(755,root,root) %{_libdir}/openchange/modules/dcerpc_mapiproxy_server/exchange_ds_rfr.so
%attr(755,root,root) %{_libdir}/openchange/modules/dcerpc_mapiproxy_server/exchange_emsmdb.so
%attr(755,root,root) %{_libdir}/openchange/modules/dcerpc_mapiproxy_server/exchange_nsp.so
%{_datadir}/openchange/setup/mapistore
%{_datadir}/openchange/setup/openchangedb
%dir %{_datadir}/samba/setup/AD
%{_datadir}/samba/setup/AD/oc_provision_*.ldif
%{_datadir}/samba/setup/AD/provision_schema_basedn_modify.ldif
%{_datadir}/samba/setup/AD/update_now.ldif
%{_datadir}/samba/setup/AD/prefixMap.txt
%endif
%if %{with mapitest}
%attr(755,root,root) %{_bindir}/mapitest
%{_datadir}/openchange/mapitest
%{_mandir}/man1/mapitest.1*
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmapi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmapi.so.0
%attr(755,root,root) %{_libdir}/libmapiadmin.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmapiadmin.so.0
%attr(755,root,root) %{_libdir}/libocpf.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libocpf.so.0
%if %{with mapiproxy}
%attr(755,root,root) %{_libdir}/libmapiproxy.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmapiproxy.so.0
%attr(755,root,root) %{_libdir}/libmapiserver.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmapiserver.so.0
%attr(755,root,root) %{_libdir}/libmapistore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmapistore.so.0
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmapi.so
%attr(755,root,root) %{_libdir}/libmapiadmin.so
%attr(755,root,root) %{_libdir}/libocpf.so
%{_includedir}/gen_ndr
%{_includedir}/libmapi
%{_includedir}/libmapiadmin
%{_includedir}/libocpf
%{_pkgconfigdir}/libmapi.pc
%{_pkgconfigdir}/libmapiadmin.pc
%{_pkgconfigdir}/libocpf.pc
%if %{with mapiproxy}
%attr(755,root,root) %{_libdir}/libmapiproxy.so
%attr(755,root,root) %{_libdir}/libmapiserver.so
%attr(755,root,root) %{_libdir}/libmapistore.so
%{_includedir}/mapistore
%{_includedir}/libmapiproxy.h
%{_includedir}/libmapiserver.h
%{_pkgconfigdir}/libmapiproxy.pc
%{_pkgconfigdir}/libmapiserver.pc
%{_pkgconfigdir}/libmapistore.pc
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmapipp.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmapipp.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmapipp.so
%{_includedir}/libmapi++
%{_pkgconfigdir}/libmapi++.pc

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtmapi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libqtmapi.so.0

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtmapi.so
%{_includedir}/libqtmapi

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc apidocs/html/*
%endif

%if %{with python}
%files -n python-openchange
%defattr(644,root,root,755)
%dir %{py_sitedir}/openchange
%attr(755,root,root) %{py_sitedir}/openchange/mapi.so
%attr(755,root,root) %{py_sitedir}/openchange/mapistore.so
%if %{with mapiproxy}
%{py_sitedir}/openchange/*.py[co]
%{py_sitedir}/openchange/migration
%{py_sitedir}/openchange/tests
%{py_sitedir}/openchange/utils
%{py_sitedir}/openchange/web
%endif
%endif

%files -n nagios-plugin-openchange
%defattr(644,root,root,755)
# R: perl, openchangeclient
# FIXME: use /usr/lib/nagios/plugins dir and make package noarch
%attr(755,root,root) %{_libdir}/nagios/check_exchange
# default profile database - should be /etc/...
#%config(noreplace) %verify(not md5 mtime size) %{_libdir}/nagios/plugins/check_exchange.ldb
