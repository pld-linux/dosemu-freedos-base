Summary:	FreeDOS Ripcord base part
Summary(pl):	Czê¶æ 'base' FreeDosa
Name:		dosemu-freedos-base
Version:	beta7h01
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/beta7h01/EN/full/disksets/base1.zip
URL:		http://www.freedos.org/
BuildRequires:	unzip
Obsoletes:	dosemu-freedos
Requires:	dosemu
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In this package there is base part of FreeDOS Ripcord.

%description -l pl
W tym pakiecie jest czê¶æ 'base' FreeDOSa.

%prep
%setup -c %{name} -q

%build
rm -rf freedos
mkdir freedos
for i in *.ZIP ; do
	unzip -L -o $i -d freedos
done
rm -f freedos/copying

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/dosemu/bootdir
cp -fR freedos $RPM_BUILD_ROOT/var/lib/dosemu/bootdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/var/lib/dosemu/bootdir/freedos/*
