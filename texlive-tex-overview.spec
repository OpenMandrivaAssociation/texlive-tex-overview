Name:		texlive-tex-overview
Version:	41403
Release:	2
Summary:	An overview of the development of TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tex-overview
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
