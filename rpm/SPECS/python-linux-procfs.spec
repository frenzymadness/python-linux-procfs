%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: python-linux-procfs
Version: 0.2
Release: 1%{?dist}
License: GPLv2
Summary: Linux /proc abstraction classes
Group: Application/System
Source: http://userweb.kernel.org/~acme/python-linux-procfs/%{name}-%{version}.tar.bz2
BuildArch: noarch
BuildRequires: python-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Abstractions to extract information from the Linux kernel /proc files.

%prep
%setup -q -c -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{python_sitelib}/procfs/
%{python_sitelib}/*.egg-info

%changelog
* Mon Feb 25 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-1
- package created