#
# TODO:
# m4 macros from pandora-build (http://code.launchpad.net/pandora-build)
#
# Conditional build
%bcond_without  static_libs	# don't build static library
#
Summary:	memcached client library
Summary(pl.UTF-8):	Blblioteka kliencka memcached
Name:		libmemcached
Version:	1.0.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://launchpad.net/libmemcached/1.0/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	6eded403ce736f6ac3c42c8f54dc88ae
URL:		http://libmemcached.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cyrus-sasl-devel
BuildRequires:	libevent-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmemcached is a C and C++ client library to the memcached server
(http://danga.com/memcached). It has been designed to be light on
memory usage, thread safe, and provide full access to server side
methods.

%description -l pl.UTF-8
libmemcached to biblioteka kliencka serwera memcached
(http://danga.com/memcached) dla języków C/C++. Została zaprojektowana
z myślą o niewielkim zużyciu pamięci, bezpieczeństwe i pełnym dostępie
do metod po stronie serwera.

%package devel
Summary:	Header files for memcached library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki memcached
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cyrus-sasl-devel

%description devel
Header files for memcached library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki memcached.

%package static
Summary:	Static memcached library
Summary(pl.UTF-8):	Statyczna biblioteka memcached
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static memcached library.

%description static -l pl.UTF-8
Statyczna biblioteka memcached.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LIBS="-lrt -lsasl -lpthread" \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules \
	--with-memcached=no # disable memcached detection, we're not doing tests
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/memcapable
%attr(755,root,root) %{_bindir}/memcat
%attr(755,root,root) %{_bindir}/memcp
%attr(755,root,root) %{_bindir}/memdump
%attr(755,root,root) %{_bindir}/memerror
%attr(755,root,root) %{_bindir}/memexist
%attr(755,root,root) %{_bindir}/memflush
%attr(755,root,root) %{_bindir}/memparse
%attr(755,root,root) %{_bindir}/memping
%attr(755,root,root) %{_bindir}/memrm
%attr(755,root,root) %{_bindir}/memslap
%attr(755,root,root) %{_bindir}/memstat
%attr(755,root,root) %{_bindir}/memtouch
%attr(755,root,root) %{_libdir}/libhashkit.so.*.*.*
%attr(755,root,root) %{_libdir}/libmemcached.so.*.*.*
%attr(755,root,root) %{_libdir}/libmemcachedprotocol.so.*.*.*
%attr(755,root,root) %{_libdir}/libmemcachedutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhashkit.so.?
%attr(755,root,root) %ghost %{_libdir}/libmemcached.so.?
%attr(755,root,root) %ghost %{_libdir}/libmemcachedprotocol.so.?
%attr(755,root,root) %ghost %{_libdir}/libmemcachedutil.so.?
%{_mandir}/man1/mem*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhashkit.so
%attr(755,root,root) %{_libdir}/libmemcached.so
%attr(755,root,root) %{_libdir}/libmemcachedprotocol.so
%attr(755,root,root) %{_libdir}/libmemcachedutil.so
%{_libdir}/libhashkit.la
%{_libdir}/libmemcached.la
%{_libdir}/libmemcachedprotocol.la
%{_libdir}/libmemcachedutil.la
%{_includedir}/libhashkit
%{_includedir}/libhashkit-*.*
%{_includedir}/libmemcached
%{_includedir}/libmemcached-*.*
%{_includedir}/libmemcachedprotocol-*.*
%{_includedir}/libmemcachedutil-*.*
%{_pkgconfigdir}/libmemcached.pc
%{_mandir}/man3/*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libhashkit.a
%{_libdir}/libmemcached.a
%{_libdir}/libmemcachedprotocol.a
%{_libdir}/libmemcachedutil.a
%endif
