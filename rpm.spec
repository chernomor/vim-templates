# https://docs.fedoraproject.org/en-US/packaging-guidelines/
# https://docs.fedoraproject.org/en-US/packaging-guidelines/RPMMacros/
#   Macros for paths set 
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/
# 
#            install upgrade uninstall
# %pretrans  $1 == 0 $1 == 0  (N/A) 
# %pre       $1 == 1 $1 == 2  (N/A) 
# %post      $1 == 1 $1 == 2  (N/A) 
# %preun      (N/A)  $1 == 1 $1 == 0 
# %postun     (N/A)  $1 == 1 $1 == 0 
# %posttrans $1 == 0 $1 == 0  (N/A) 

#  Order
# The scriptlets in %pre and %post are respectively run before and after a package is installed. The scriptlets %preun and %postun are run before and after a package is uninstalled. The scriptlets %pretrans and %posttrans are run at start and end of a transaction. On upgrade, the scripts are run in the following order:

#    %pretrans of new package
#    %pre of new package
#    (package install)
#    %post of new package
#    %triggerin of other packages (set off by installing new package)
#    %triggerin of new package (if any are true)
#    %triggerun of old package (if it’s set off by uninstalling the old package)
#    %triggerun of other packages (set off by uninstalling old package)
#    %preun of old package
#    (removal of old package)
#    %postun of old package
#    %triggerpostun of old package (if it’s set off by uninstalling the old package)
#    %triggerpostun of other packages (if they’re set off by uninstalling the old package)
#    %posttrans of new package

# The %pretrans Scriptlet
# Note that the %pretrans scriptlet will, in the particular case of system installation, run before anything at all has been installed. This implies that it cannot have any dependencies at all. For this reason, %pretrans is best avoided, but if used it MUST (by necessity) be written in Lua. See http://rpm.org/user_doc/lua.html for more information.

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
