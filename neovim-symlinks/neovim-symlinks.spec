Name:           neovim-symlinks
Version: 1.0.1
Release:        1%{?dist}
Summary:        System-wide: Runs neovim if vi or vim is invoked
License:        MIT
Url:            https://github.com/mkrawiec/copr-project-neovim

BuildArch:      noarch
Requires:       neovim
Conflicts:      otherproviders(vim)
Conflicts:      otherproviders(vi)
Provides:       vim
Provides:       vi

%description
System-wide: Runs neovim if vi or vim is invoked

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin

_link_names=(edit ex rview rvim vedit vi view vim)
for link in "${_link_names[@]}"; do
    ln -s nvim "$RPM_BUILD_ROOT/usr/bin/$link"
done

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/edit
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/rvim
%{_bindir}/vedit
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/vim
