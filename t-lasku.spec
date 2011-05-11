%define name	t-lasku
%define version	1.9.4
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Finnish invoicing software
Group:		Office
License:	BSD
URL:		http://helineva.net/%{name}/
Source0:	http://helineva.net/%{name}/%{name}-%{version}-i386.tar.gz
Source1:	http://helineva.net/%{name}/%{name}-%{version}-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel >= 4:4.6
Requires:	qt4-database-plugin-sqlite

%description
T-lasku is a Finnish invoicing software for Linux.

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
Comment=Finnish invoicing software
Terminal=false
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Qt;Office;Finance;X-MandrivaLinux-CrossDesktop;
EOF

# Install hicolor icons
for i in 16x16 24x24 32x32 48x48
do
	install -Dpm 644 images/%{name}-$i.png %{buildroot}%{_datadir}/icons/hicolor/$i/apps/%{name}.png
done

#translations
mkdir -p %{buildroot}%{_datadir}/%{name}/translations/
cp translations/* %{buildroot}%{_datadir}/%{name}/translations/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
