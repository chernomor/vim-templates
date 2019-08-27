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

%if 0%{?rhel}  == 7
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


%files
#install -D -m 755 %FILE %{buildroot}%{_bindir}/%DEST
#%{_bindir}/file
#%exclude %{_libdir}/lib*.la
#%doc LICENSE
#%doc README
#%doc path/to/sample.cfg

%files doc
# include content of directory "docs" as %{_docdir}/%{_name}-%{_version}/
%doc docs/*

%changelog
* Wed Nov 07 2018 NAME <EMAIL> - 0.0.0
- initial
