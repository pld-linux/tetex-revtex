%define _short_name 	revtex
Summary:	Set of LaTeX macros for prepering slides.
Name:		tetex-revtex
Version:	3.1
Release:	1
Copyright:	nocommercial	
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.dante.de/tex-archive/macros/latex209/contrib/revtex/%{_short_name}%{version}.tar.gz
Requires:	tetex
Requires:	tetex-latex
BuildRequires:	tetex-latex
Prereq:		tetex
Prereq:		/usr/bin/mktexlsr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
%prep
%setup -q -c   -n %{_short_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name} 
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{_short_name} 

install *.sty *.bst $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name} 
	
install README manintro.tex manend.tex manaip.tex manaps.tex segman.tex josaa.tex josab.tex aplop.tex manosa.tex sample.tex template.tex template.aps reftest.tex apssamp.tex sample.tex $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{_short_name}

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{_short_name}/*.tex
gzip -9nf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{_short_name}/README
%post 
/usr/bin/mktexlsr

%postun
/usr/bin/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc
%{_datadir}/texmf/tex/latex/%{_short_name}/*
%doc %{_datadir}/texmf/doc/latex/%{_short_name}/*
