# TODO:	- provide subpackages with cgi and fastcgi demos
#
# Conditional build:
%bcond_without	static_libs # don't build static libraries

Summary:	A C++ library for CGI programming
Summary(pl.UTF-8):	Biblioteka C++ do programowania CGI
Name:		cgicc
Version:	3.2.20
Release:	1
License:	LGPL v3+ (library), FDL v1.1+ (documentation)
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/cgicc/%{name}-%{version}.tar.gz
# Source0-md5:	5b56a513c697fb019e253a565ffd06f2
Patch0:		%{name}-link.patch
URL:		http://www.gnu.org/software/cgicc/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU cgicc is a C++ class library that greatly simplifies the creation
of CGI applications for the World Wide Web. cgicc performs the
following functions:
- Parses both GET and POST form data transparently.
- Provides string, integer, floating-point and single- and
  multiple-choice retrieval methods for form data.
- Provides methods for saving and restoring CGI environments to aid in
  application debugging.
- Provides full on-the-fly HTML generation capabilities, with support
  for cookies.
- Supports HTTP file upload.
- Compatible with FastCGI.

%description -l pl.UTF-8
GNU cgicc to biblioteka klas C++ znacznie upraszczająca tworzenie
aplikacji CGI dla WWW. cgicc wykonuje następujące funkcje:
- w sposób przezroczysty analizuje dane z formularzy GET i POST
- udostępnia metody uzyskiwania łańcuchów znaków, liczb całkowitych i
  zmiennoprzecinkowych oraz opcji jednokrotnego i wielokrotnego wyboru z
  danych formularzy
- udostępnia metody do zapisu i odtwarzania środowiska CGI pomagające
  przy śledzeniu aplikacji
- udostępnia pełne możliwości generowania HTML-a w locie, z obsługą
  ciasteczek
- obsługuje wysyłanie plików po HTTP
- jest kompatybilna z FastCGI.

%package devel
Summary:	A C++ library for CGI programming - header files
Summary(pl.UTF-8):	Biblioteka C++ do programowania CGI - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for cgicc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cgicc.

%package static
Summary:	A C++ library for CGI programming - static version
Summary(pl.UTF-8):	Biblioteka C++ do programowania CGI - wersja statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of cgicc library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki cgicc.

%package apidocs
Summary:	API documentation for cgicc library
Summary(pl.UTF-8):	Dokumentacja API biblioteki cgicc
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for cgicc library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki cgicc.

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
	--disable-demos \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcgicc.la

# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS doc/html/*
%attr(755,root,root) %{_libdir}/libcgicc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcgicc.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cgicc-config
%attr(755,root,root) %{_libdir}/libcgicc.so
%{_includedir}/cgicc
%{_pkgconfigdir}/cgicc.pc
%{_aclocaldir}/cgicc.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcgicc.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
