Name:
Version: 0.0.0
Release: 1%{?dist}
Summary:

Group:
License:
URL:
Source:
#Source1:   %{name}-README
#BuildArch: 	noarch

BuildRequires:
Requires:

%if 0%{?rhel}  >= 7
Requires: systemd
BuildRequires: systemd
%endif


%description

%package doc
Summary: Docs for %{name}

%description doc
Docs for %{name}


%prep
%setup -q
#%setup -q -n some-%{version}-thing


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

#install -D %{SOURCE1} %{buildroot}/%{_docdir}/%{name}-%{version}/README
#install -D %{SOURCE2} %{buildroot}/%{_unitdir}/%{name}.service

#%post
getent group %{name} > /dev/null || groupadd --system %{name}
getent passwd %{name} > /dev/null || \
    useradd --system -g %{name} -d /var/lib/%{name} -s /sbin/nologin %{name}

#install -d -o %{name} /var/log/%{name}
#install -d -o %{name} /var/lib/%{name}

#%if 0%{?rhel} >= 7
#systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf
#%systemd_post %{name}.service
#%else
#/sbin/chkconfig --add %{name} || :
#%endif

#%preun
#/sbin/service %{name} stop || :

#%if 0%{?rhel} >= 7
#systemd-tmpfiles --remove %{_tmpfilesdir}/%{name}.conf || :
#%systemd_preun %{name}.service || :
#%else
#/sbin/chkconfig --del %{name} || :
#%endif

%files
#%config(noreplace) %{_sysconfdir}/%{name}/conf
#%{_bindir}/file
#%exclude %{_libdir}/lib*.la

#%doc LICENSE
#%doc README
#%doc path/to/sample.cfg

#%if 0%{?rhel} >= 7
#%{_unitdir}/%{name}.service
#%{_tmpfilesdir}/%{name}.conf
#%else
#%{_sysconfdir}/init.d/%{name}
#%endif


%files doc
# include content of directory "docs" as %{_docdir}/%{_name}-%{_version}/
%doc docs/*

%changelog
* Wed Nov 07 2018 NAME <EMAIL> - 0.0.0
- initial
