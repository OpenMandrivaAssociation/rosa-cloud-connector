Name:		rosa-cloud-connector
Version:	0.3.1
Release:	2
Summary:	Connect to different cloud storage services
License:	BSD
Group:		Networking/File transfer
Url:		https://abf.rosalinux.ru/soft/rosa-cloud-connector
Source0:	https://abf.rosalinux.ru/soft/rosa-cloud-connector/archive/%{name}-%{version}.tar.gz
BuildRequires:	qmake5
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist-tools

%description
A simple tool to connect to different cloud storage services.

%prep
%setup -q

%build
%qmake_qt5
%make
%{_libdir}/qt5/bin/lrelease app/rosa_cloud_ru.ts

%install
mkdir -p %{buildroot}/%{_bindir}
cp app/rosa-cloud %{buildroot}/%{_bindir}

mkdir -p %{buildroot}%{_datadir}/%{name}/data/lang/
cp app/*qm %{buildroot}%{_datadir}/%{name}/data/lang/
cp app/*ts %{buildroot}%{_datadir}/%{name}/data/lang/

%files
%{_bindir}/*
%{_datadir}/%{name}
