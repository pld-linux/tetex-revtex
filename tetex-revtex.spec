%define _short_name 	revtex
Summary:	Set of LaTeX macros for physicists.
Name:		tetex-revtex
Version:	3.1
Release:	3
Copyright:	nocommercial	
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.dante.de/tex-archive/macros/latex209/contrib/revtex/%{_short_name}%{version}.tar.gz
Patch0:		tetex-revtex-array.patch
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	tetex-latex
Prereq:		tetex
Prereq:		/usr/bin/mktexlsr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Set of LaTeX macros for physicists.

%prep
%setup -q -c -n %{_short_name}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name} \
	$RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{_short_name} 

install *.cls *.sty *.bst $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name} 
	
install *.sty *.bst $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name} 

gzip -9nf README *.tex

%post 
/usr/bin/mktexlsr

%postun
/usr/bin/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/texmf/tex/latex/%{_short_name}/*
