%global tl_name tex-overview
%global tl_revision 41403

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	An overview of the development of TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tex-overview
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-overview.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document gives a short overview of TeX and its children, as well as
the macro packages LaTeX and ConTeXt.

