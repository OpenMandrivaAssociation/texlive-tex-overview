# revision 27724
# category Package
# catalog-ctan /info/tex-overview
# catalog-date 2012-09-16 19:39:43 +0200
# catalog-license lppl1.3
# catalog-version 0.1f
Name:		texlive-tex-overview
Version:	0.1f
Release:	4
Summary:	An overview of the development of TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/tex-overview
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document gives a short overview of TeX and its children, as
well as the macro packages LaTeX and ConTeXt.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/tex-overview/README
%doc %{_texmfdistdir}/doc/latex/tex-overview/tex-overview-aux.tex
%doc %{_texmfdistdir}/doc/latex/tex-overview/tex-overview.pdf
%doc %{_texmfdistdir}/doc/latex/tex-overview/tex-overview.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
