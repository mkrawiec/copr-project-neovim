Name:           unibilium
Summary:        A terminfo parsing library
Version: 1.2.0
Release:        1%{?dist}
License:        GPLv3 or LGPLv3
Group:          System Environment/Libraries
URL:            https://github.com/mauke/unibilium/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  libtool

%description
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%__make %{?_smp_flags} \
    CFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    LIBDIR="%{_libdir}" \
    INCDIR="%{_includedir}" \
    MANDIR="%{_mandir}"


%install
%__make \
    CFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    LIBDIR="%{_libdir}" \
    INCDIR="%{_includedir}" \
    MANDIR="%{_mandir}" \
    DESTDIR="%{buildroot}" \
    install

rm $RPM_BUILD_ROOT%{_libdir}/*.la


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc GPLv3 LGPLv3 LICENSE README
%{_libdir}/libunibilium.so.*


%files devel
%defattr(-,root,root)
%{_includedir}/unibilium.h
%{_libdir}/libunibilium.so
%{_libdir}/libunibilium.a
%{_libdir}/pkgconfig/unibilium.pc
%{_mandir}/man3/unibi*.3*


%changelog
