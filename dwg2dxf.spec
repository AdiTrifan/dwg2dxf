Summary:	Command line converter for *.dwg files into *.dxf
Summary(pl):	Program konwertuj�cy pliki z *.dwg do *.dxf
Name:		dwg2dxf
Version:	2.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://nchc.dl.sourceforge.net/sourceforge/lx-viewer/%{name}-%{version}.tar.gz
# Source0-md5:	c1ba5f874d23746360cd73986830a249
Patch0:		%{name}-%{version}-shared-files.patch
URL:		http://sourceforge.net/projects/lx-viewer/
#BuildRequires:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A command line program to convert AutoCad drawing files (*.dwg) 
into Drawing Interchange Format (*.dxf) files.
%description -l pl
Konsolowy program konwertuj�cy pliki AutoCad'a (*.dwf) do 
Drawing Interchange Format (*.dxf), potem taki plik *.dxf mo�na
otworzy� za pomoc� QCAD'a.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}
install %{name}/adinit.dat $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install %{name}/docs/en/index*.html $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/%{name}/adinit.dat
%doc %{_defaultdocdir}/%{name}-%{version}/*.html
