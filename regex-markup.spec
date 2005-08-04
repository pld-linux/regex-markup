Summary:	Regex-markup performs regular expression-based text markup
Summary(pl):	Narzêdzie do kolorowania wyników dowolnych poleceñ
Name:		regex-markup
Version:	0.10.0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://savannah.nongnu.org/download/regex-markup/%{name}-%{version}.tar.gz
# Source0-md5:	47f9df1cd3865d20aecd6d73e7a7518d
URL:		http://www.nongnu.org/regex-markup/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regex-markup performs regular expression-based text markup according
to used-defined rules. This can be used to color syslog files as well
as the output of programs such as ping, traceroute, gcc, etc. The
hierarchal rules-format is simple to understand, yet very powerful.
Regex-markup is written entirely in C, and uses POSIX regular
expressions to do much of its work.

%description -l pl
Regex-markup koloruje tekst bazuj±c na zasadach zdefiniowanych przez
u¿ytkownika. Regex-markup mo¿e byæ u¿yty do kolorowania logów
systemowych, jak i do kolorowania danych wyj¶ciowych takich programów
jak ping, traceroute czy gcc. Hierarchiczny format regu³ jest ³atwy do
zrozumienia, a zarazem posiadaj±cy du¿e mo¿liwo¶ci. Regex-markup jest
napisany w C i w du¿ym stopniu dzia³a w oparciu o wyra¿enia regularne
POSIX.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/regex-markup
%{_datadir}/regex-markup/*
%{_mandir}/man1/*
