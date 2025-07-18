%define		short_name 	revtex
Summary:	Set of LaTeX macros for physicists
Summary(pl.UTF-8):	Zestaw makr LaTeXa dla fizyków
Name:		tetex-revtex
# NOTE: this is _not_ intended to be upgraded to v4 (or any newer)
Version:	3.1
Release:	5
License:	non-commercial
Group:		Applications/Publishing/TeX
Source0:	http://ftp.agh.edu.pl/pub/tex/macros/latex209/contrib/revtex/%{short_name}%{version}.tar.gz
# Source0-md5:	70de3a42b831a26bfa3f1521944d7a56
Patch0:		%{name}-array.patch
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of LaTeX macros for physicists.

%description -l pl.UTF-8
Zestaw makr LaTeXa dla fizyków.

%prep
%setup -q -c -n %{short_name}
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.cls *.sty *.bst $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.tex
%{_datadir}/texmf/tex/latex/%{short_name}
