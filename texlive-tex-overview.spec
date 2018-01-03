Name:		texlive-tex-overview
Version:	0.2
Release:	1
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
%doc %{_texmfdistdir}/doc/latex/tex-overview

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
