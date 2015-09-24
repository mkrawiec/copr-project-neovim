%global luaver 5.3

Name:           lua-msgpack
Version: 0.3.3
Release:        1%{?dist}
Summary:        Lua binary-based efficient object serialization library

License:        MIT
URL:            http://fperrad.github.io/lua-MessagePack/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  lua
Requires:       lua >= %{luaver}

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Lua MessagePack.

%prep
%setup -q
echo '#!/bin/sh' > ./configure
chmod +x ./configure

%build
%configure
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p" PREFIX="%{_prefix}" LUAVER="%{luaver}"

%files
%doc
%{_datadir}/lua/%{luaver}/MessagePack.lua

%changelog
