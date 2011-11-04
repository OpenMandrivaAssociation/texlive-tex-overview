# revision 23730
# category Package
# catalog-ctan /info/tex-overview
# catalog-date 2011-08-27 22:03:02 +0200
# catalog-license lppl1.3
# catalog-version 0.1e
Name:		texlive-tex-overview
Version:	0.1e
Release:	1
Summary:	An overview of the development of TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/tex-overview
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The document gives a short overview of TeX and its children, as
well as the macro packages LaTeX and ConTeXt.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/tex-overview/README
%doc %{_texmfdistdir}/doc/latex/tex-overview/tex-overview-aux.tex
%doc %{_texmfdistdir}/doc/latex/tex-overview/tex-overview.pdf
%doc %{_texmfdistdir}/doc/latex/tex-overview/tex-overview.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
