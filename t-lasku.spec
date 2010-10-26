%define name	t-lasku
%define version	1.1.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Free Finnish invoicing software
Group:		Office
License:	GPLv3+
URL:		http://helineva.net/%{name}/
Source0:	http://helineva.net/%{name}/%{name}-%{version}-i386.tar.gz
Source1:	http://helineva.net/%{name}/%{name}-%{version}-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel
Requires:	qt4-database-plugin-sqlite

%description
T-lasku is a free Finnish invoicing software for Linux.

%prep
%ifarch x86_64
%setup -q -T -b1
%else
%setup -q -T -b0
%endif

%build 
g++ %{optflags} %{ldflags} -o t-lasku t-lasku-relocatable -lQtScript -lQtSql -lQtGui -lQtCore -lpthread

%install
rm -rf %{buildroot}

#binary
install -Dpm755 %{name} %{buildroot}%{_bindir}/%{name}

#desktop file
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=T-lasku
GenericName=Invoicing software
Comment=Free Finnish invoicing software
Terminal=false
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Qt;Office;Finance;
EOF

# Install hicolor icons
for i in 16x16 24x24 32x32 48x48
do
	install -Dpm 644 images/%{name}-$i.png %{buildroot}%{_datadir}/icons/hicolor/$i/apps/%{name}.png
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsbasedir}/*/apps/%{name}.png
