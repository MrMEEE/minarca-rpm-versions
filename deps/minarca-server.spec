%global python3_pkgversion 3.11

%define _unpackaged_files_terminate_build 0
%define  debug_package %{nil}
%define _prefix /opt/eda-rpm
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user minarca
%define service_group minarca
%define service_homedir /opt/minarca/server
%define service_logdir /var/log/minarca
%define service_configdir /etc/micarca

Summary: Minarca Backup Server
Name: minarca-server
Version: 6.0.0b3
Release: 22%{dist}
Source0: minarca-server-6.0.0b3.tar.gz
#Patch0: awx-patch.patch-%{version}
License: GPLv3
Group: Backup
URL: https://github.com/ikus060/minarca
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: Minarca
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: python%{python3_pkgversion} python%{python3_pkgversion}-devel 
#BuildRequires: python3.11-backports-tarfile = 1.2.0
BuildRequires: python3.11-build = 1.2.1
BuildRequires: python3.11-cachecontrol = 0.14.0
BuildRequires: python3.11-cachecontrol+filecache = 0.14.0
BuildRequires: python3.11-calver = 2022.6.26
BuildRequires: python3.11-cleo = 2.1.0
BuildRequires: python3.11-cmake = 3.29.6
BuildRequires: python3.11-crashtest = 0.4.1
BuildRequires: python3.11-cython = 3.0.10
BuildRequires: python3.11-distlib = 0.3.8
BuildRequires: python3.11-distro = 1.9.0
BuildRequires: python3.11-dulwich = 0.21.7
BuildRequires: python3.11-fastjsonschema = 2.20.0
BuildRequires: python3.11-filelock = 3.15.4
BuildRequires: python3.11-hatch-fancy-pypi-readme = 24.1.0
BuildRequires: python3.11-hatchling = 1.25.0
BuildRequires: python3.11-hatch-vcs = 0.4.0
BuildRequires: python3.11-importlib-metadata = 8.0.0
BuildRequires: python3.11-installer = 0.7.0
BuildRequires: python3.11-jaraco-classes = 3.4.0
BuildRequires: python3.11-jaraco-context = 5.3.0
BuildRequires: python3.11-jaraco-functools = 4.0.1
BuildRequires: python3.11-jeepney = 0.8.0
BuildRequires: python3.11-keyring = 24.3.1
BuildRequires: python3.11-more-itertools = 10.3.0
BuildRequires: python3.11-msgpack = 1.0.8
BuildRequires: python3.11-packaging = 24.1
BuildRequires: python3.11-pathspec = 0.12.1
BuildRequires: python3.11-pexpect = 4.9.0
BuildRequires: python3.11-pkginfo = 1.11.1
BuildRequires: python3.11-platformdirs = 4.2.2
BuildRequires: python3.11-ptyprocess = 0.7.0
BuildRequires: python3.11-pyproject-hooks = 1.1.0
BuildRequires: python3.11-rapidfuzz = 3.9.3
BuildRequires: python3.11-rapidfuzz+full = 3.9.3
BuildRequires: python3.11-requests-toolbelt = 1.0.0
BuildRequires: python3.11-scikit-build = 0.17.6
BuildRequires: python3.11-scikit-build-core = 0.9.7
BuildRequires: python3.11-secretstorage = 3.3.3
BuildRequires: python3.11-setuptools-scm = 8.1.0
BuildRequires: python3.11-setuptools-scm+toml = 8.1.0
BuildRequires: python3.11-shellingham = 1.5.4
BuildRequires: python3.11-tomlkit = 0.12.5
BuildRequires: python3.11-trove-classifiers = 2024.5.22
BuildRequires: python3.11-virtualenv = 20.26.3
BuildRequires: python3.11-zipp = 3.19.2
BuildRequires: python3.11-poetry


#Requires: python%{python3_pkgversion} nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 
#Requires: python3.11-backports-tarfile = 1.2.0
Requires: python3.11-build = 1.2.1
Requires: python3.11-cachecontrol = 0.14.0
Requires: python3.11-cachecontrol+filecache = 0.14.0
Requires: python3.11-calver = 2022.6.26
Requires: python3.11-cleo = 2.1.0
Requires: python3.11-cmake = 3.29.6
Requires: python3.11-crashtest = 0.4.1
Requires: python3.11-cython = 3.0.10
Requires: python3.11-distlib = 0.3.8
Requires: python3.11-distro = 1.9.0
Requires: python3.11-dulwich = 0.21.7
Requires: python3.11-fastjsonschema = 2.20.0
Requires: python3.11-filelock = 3.15.4
Requires: python3.11-hatch-fancy-pypi-readme = 24.1.0
Requires: python3.11-hatchling = 1.25.0
Requires: python3.11-hatch-vcs = 0.4.0
Requires: python3.11-importlib-metadata = 8.0.0
Requires: python3.11-installer = 0.7.0
Requires: python3.11-jaraco-classes = 3.4.0
Requires: python3.11-jaraco-context = 5.3.0
Requires: python3.11-jaraco-functools = 4.0.1
Requires: python3.11-jeepney = 0.8.0
Requires: python3.11-keyring = 24.3.1
Requires: python3.11-more-itertools = 10.3.0
Requires: python3.11-msgpack = 1.0.8
Requires: python3.11-packaging = 24.1
Requires: python3.11-pathspec = 0.12.1
Requires: python3.11-pexpect = 4.9.0
Requires: python3.11-pkginfo = 1.11.1
Requires: python3.11-platformdirs = 4.2.2
Requires: python3.11-ptyprocess = 0.7.0
Requires: python3.11-pyproject-hooks = 1.1.0
Requires: python3.11-rapidfuzz = 3.9.3
Requires: python3.11-rapidfuzz+full = 3.9.3
Requires: python3.11-requests-toolbelt = 1.0.0
Requires: python3.11-scikit-build = 0.17.6
Requires: python3.11-scikit-build-core = 0.9.7
Requires: python3.11-secretstorage = 3.3.3
Requires: python3.11-setuptools-scm = 8.1.0
Requires: python3.11-setuptools-scm+toml = 8.1.0
Requires: python3.11-shellingham = 1.5.4
Requires: python3.11-tomlkit = 0.12.5
Requires: python3.11-trove-classifiers = 2024.5.22
Requires: python3.11-virtualenv = 20.26.3
Requires: python3.11-zipp = 3.19.2


%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n minarca-server
#%patch0 -p0

%build

%install
poetry install -E all --only-root

mkdir -p /var/log/minarca

#pip%{python3_pkgversion} install --root=%{buildroot}/ .

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}
#/usr/bin/gpasswd -a  %{service_user} redis

%post
#if [ ! -f /etc/nginx/nginx.crt ];then
#sscg -q --cert-file /etc/nginx/nginx.crt --cert-key-file /etc/nginx/nginx.key --ca-file /etc/nginx/ca.crt --lifetime 3650 --hostname $HOSTNAME --email root@$HOSTNAME
#fi

%preun

%postun

%clean

%files
%defattr(0644, eda, eda, 0755)
%attr(0755, root, root) /usr/bin/aap-eda-manage
/usr/lib/python3.11/site-packages/aap_eda*


%changelog
* Fri Jun 28 2024 08:39:08 PM CEST +0200 Martin Juhl <m@rtinjuhl.dk> 6.0.0b3
- New version build: 6.0.0b3

