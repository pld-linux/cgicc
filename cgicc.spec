Summary:	A C++ library for CGI programming
Summary(pl):	Biblioteka C++ do programowania CGI
Name:		cgicc
Version:	3.2.3
Release:	0.1
License:	GPL v2
Group:		Libraries
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
Source0:	ftp://ftp.cgicc.org/%{name}-%{version}.tar.bz2
# Source0-md5:	cd7a7a5a1fd186bd8f481c4e17354a0b
URL:		http://www.cgicc.org/
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

%package devel
Summary:	A C++ library for CGI programming - header files
Summary(pl):	Biblioteka C++ do programowania CGI - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cgicc library.

%description devel -l pl
Pliki nag³ówkowe biblioteki cgicc.

%package static
Summary:	A C++ library for CGI programming - static version
Summary(pl):	Biblioteka C++ do programowania CGI - wersja statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of cgicc library.

%description static -l pl
Statyczna wersja biblioteki cgicc.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
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
%doc doc/html/*
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/cgicc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
