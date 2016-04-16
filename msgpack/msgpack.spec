Name:		msgpack
Version: 1.4.1
Release:	1%{?dist}
Summary:	Binary-based efficient object serialization library
Group:		System Environment/Libraries

License:	ASL 2.0
URL:		http://msgpack.org
Source0:	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++
BuildRequires:	libtool
BuildRequires:	gtest-devel
BuildRequires:	zlib-devel

%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.


%package devel
Summary:	Libraries and header files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for %{name}


%prep
%setup -q


%build
./bootstrap
%configure --disable-static
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc CHANGELOG.md COPYING NOTICE README.md
%license LICENSE_1_0.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/msgpack.pc


%changelog
