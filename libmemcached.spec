Summary:	memcached client library
Summary(pl.UTF-8):	blblioteka kliencka memcached
Name:		libmemcached
Version:	0.30
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.tangent.org/%{name}-%{version}.tar.gz
# Source0-md5:	a67c5a9062325ff4a09db56e2426e104
URL:		http://tangent.org/553/default.html
BuildRequires:	autoconf
BuildRequires:	automake
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libmemcached
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
