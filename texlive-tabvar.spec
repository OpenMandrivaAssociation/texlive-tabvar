%global tl_name tabvar
%global tl_revision 63921

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Typesetting tables showing variations of functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabvar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package is meant to ease the typesetting of tables showing
variations of functions as they are used in France.

